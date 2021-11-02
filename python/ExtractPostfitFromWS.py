#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from ROOT import *
import array

#This scripts sometimes crashes with errors like "Error in `python': corrupted size vs. prev_size"
#It must be related to the way ROOT closes the file containing the RooWorkspace. Fortunately, the
#output is fine nevertheless.

#adapted from xmlAnaWSBuilder::auxUtil::getNDOF()
def getNPars(pdf, obs, exclSyst):
    params = pdf.getVariables()
    nuispdf = RooStats.MakeNuisancePdf(pdf, RooArgSet(obs), "nuisancePdf")

    counter=0
    
    for var in params:
        if(not var.isConstant() and
           var.GetName() != obs.GetName() and
           not (exclSyst and nuispdf and nuispdf.dependsOn(RooArgSet(var)))):
            # if exclSyst, do not count nuisance parameters
            counter+=1
        
    return counter


def main(args):

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--datafile', dest='datafile', type=str, default='../Input/data/dijetTLAnlo/data_J75yStar03_range400_2079.root', help='original data file name (to get binning from)')
    parser.add_argument('--datahist', dest='datahist', type=str, default='data', help='original data hist name (to get binning from)')
    parser.add_argument('--datafirstbin', dest='datafirstbin', type=int, default=0, help='First bin in data histogram considered in fit. 0 for first non-underflow bin')
    parser.add_argument('--wsfile', dest='wsfile', type=str, help='Workspace file name')
    parser.add_argument('--wsname', dest='wsname', type=str, default='combWS', help='Name of workspace')
    parser.add_argument('--modelname', dest='modelname', type=str, default='ModelConfig', help='Name of model in workspace')
    parser.add_argument('--outfile', dest='outfile', type=str, default='', help='Output file name')
    parser.add_argument('--rebinfile', dest='rebinfile', type=str, help='Specify if rebinning to different template wanted')
    parser.add_argument('--rebinhist', dest='rebinhist', type=str, help='Specify if rebinning to different template wanted')
    parser.add_argument('--externalchi2file', dest='externalchi2file', type=str, help='File containing a TF1 chi2 pdf to calculate pval from')
    parser.add_argument('--externalchi2fct', dest='externalchi2fct', type=str, help='Name of chi2 pdf TF1 to calculate pval from')
    parser.add_argument('--maskmin', dest='maskmin', type=int, default=-1, help='Masked range to exclude from chi2 calculation')
    parser.add_argument('--maskmax', dest='maskmax', type=int, default=-1, help='Masked range to exclude from chi2 calculation')

    args = parser.parse_args(args)

    f = ROOT.TFile(args.wsfile, "READ")
    w = f.Get(args.wsname)

    # w.Print("all")

    fd =  ROOT.TFile(args.datafile, "READ")
    h_data = fd.Get(args.datahist)

    model = w.obj(args.modelname)
    pdf = model.GetPdf()
    cat = pdf.indexCat()
    nChan = cat.numBins("")

    print "There are %d channels" % nChan

    obs = pdf.getObservables(model.GetObservables())
    obs.Print()
    
    data = w.data("combData")
    dataList = data.split( cat, True )

    # asdata = w.data("asimovData_0")
    # asdata.Print("V")
    # asdata.get(0).Print("V")
    # asdata.get(1).Print("V")
    
    for i in range(nChan):
    
        datai = dataList.At( i )
        channelname = cat.getLabel()
        pdfi = pdf.getPdf(channelname)
        x = pdfi.getObservables(datai).first()
        
        print "Expected:"
        # print type(x)
        expectedEvents = pdfi.expectedEvents(RooArgSet(x))
    
        print expectedEvents

        hpdf = pdfi.createHistogram("hpdf", x)
        hpdf.Scale(expectedEvents/hpdf.Integral())

        h_postfit = h_data.Clone("postfit")
        h_postfit.Reset("M")

        for ibin in range(1, hpdf.GetNbinsX()+1):
            h_postfit.SetBinContent(ibin + args.datafirstbin, hpdf.GetBinContent(ibin))
            h_postfit.SetBinError(ibin + args.datafirstbin, 0)

        chi2 = 0.
        chi2bins = 0
        maskedchi2bins = 0

        for ibin in range(1, h_data.GetNbinsX()+1):
            binCenter = h_data.GetBinCenter(ibin)
                    
            valueErrorData = h_data.GetBinError(ibin)
            valueData = h_data.GetBinContent(ibin)
            postFitValue = h_postfit.GetBinContent(ibin)

            binSig = 0.
            if valueErrorData > 0. and postFitValue > 0.:
                binSig = (valueData - postFitValue)/valueErrorData

                if binCenter < args.maskmin or binCenter > args.maskmax:
                    chi2bins += 1
                    chi2 += binSig*binSig
                else:
                    maskedchi2bins += 1

        npars = getNPars(pdfi, x, exclSyst=True)

        if args.externalchi2file and args.externalchi2fct:
            f_chi2 = TFile(args.externalchi2file)
            tf1_chi2 = f_chi2.Get(args.externalchi2fct)
            ndof = tf1_chi2.GetParameter(0) - maskedchi2bins
            f_chi2.Close()
        else:
            ndof = chi2bins - npars
            
        pval = ROOT.Math.chisquared_cdf_c(chi2, ndof)

        h_chi2 = TH1D("chi2", "chi2", 6, 0, 6)
        h_chi2.SetBinContent(1, chi2)
        h_chi2.SetBinContent(2, chi2/ndof)
        h_chi2.SetBinContent(3, chi2bins)
        h_chi2.SetBinContent(4, npars)
        h_chi2.SetBinContent(5, ndof)
        h_chi2.SetBinContent(6, pval)
        
        h_chi2.GetXaxis().SetBinLabel(1, "chi2")
        h_chi2.GetXaxis().SetBinLabel(2, "chi2/ndof")
        h_chi2.GetXaxis().SetBinLabel(3, "nbins")
        h_chi2.GetXaxis().SetBinLabel(4, "npars")
        h_chi2.GetXaxis().SetBinLabel(5, "ndof")
        h_chi2.GetXaxis().SetBinLabel(6, "pval")

        binEdges = None
        if args.rebinfile and args.rebinhist:
            f_rebin = ROOT.TFile(args.rebinfile, "READ")
            h_rebin = f_rebin.Get(args.rebinhist)

            binEdges = []
            nBins = h_rebin.GetNbinsX()
            for i in range(1, nBins+2):
                binEdges.append(h_rebin.GetBinLowEdge(i))

            f_rebin.Close()

        if binEdges:
            h_postfit = h_postfit.Rebin(nBins, "postfit", array.array('d', binEdges))
            h_data = h_data.Rebin(nBins, args.datahist, array.array('d', binEdges))

        h_residuals = h_data.Clone("postFitSigma")
        h_residuals.Reset("M")

        for ibin in range(1, h_residuals.GetNbinsX()+1):
            valueErrorData = h_data.GetBinError(ibin)
            valueData = h_data.GetBinContent(ibin)
            postFitValue = h_postfit.GetBinContent(ibin)

            binSig = 0.
            if valueErrorData > 0. and postFitValue > 0.:
                binSig = (valueData - postFitValue)/valueErrorData

                h_residuals.SetBinContent(ibin, binSig)
                h_residuals.SetBinError(ibin, 0)



        outname = args.outfile
        if outname == "":
            outname = "postfit_" + os.path.basename(args.datafile).replace(".root", "_%s.root" % os.path.basename(args.datahist))
        fout = ROOT.TFile(outname, "RECREATE")

        h_postfit.Write("postfit")
        h_data.Write("data")
        h_residuals.Write("postFitSigma")
        h_chi2.Write("chi2")

        fout.Close()

    # w.Delete()
    fd.Close()
    f.Close()

    print "Finished ExtractPostfitFromWS"

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
