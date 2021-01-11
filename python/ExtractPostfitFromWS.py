#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from ROOT import *

#This scripts sometimes crashes with errors like "Error in `python': corrupted size vs. prev_size"
#It must be related to the way ROOT closes the file containing the RooWorkspace. Fortunately, the
#output is fine nevertheless.


def main(args):

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--datafile', dest='datafile', type=str, default='../Input/data/dijetTLAnlo/data_J75yStar03_range400_2079.root', help='original data file name (to get binning from)')
    parser.add_argument('--datahist', dest='datahist', type=str, default='data', help='original data hist name (to get binning from)')
    parser.add_argument('--datafirstbin', dest='datafirstbin', type=int, default=0, help='First bin in data histogram considered in fit. 0 for first non-underflow bin')
    parser.add_argument('--wsfile', dest='wsfile', type=str, default='', help='Workspace file name')
    parser.add_argument('--wsname', dest='wsname', type=str, default='combWS', help='Name of workspace')
    parser.add_argument('--modelname', dest='modelname', type=str, default='ModelConfig', help='Name of model in workspace')
    parser.add_argument('--outfile', dest='outfile', type=str, default='', help='Output file name')

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

        h_postfit = h_data.Clone()
        h_postfit.Reset("M")

        for ibin in range(1, hpdf.GetNbinsX()+1):
            h_postfit.SetBinContent(ibin + args.datafirstbin, hpdf.GetBinContent(ibin))
            h_postfit.SetBinError(ibin + args.datafirstbin, 0)

        # h_postfit.Draw()

        h_residuals = h_data.Clone()
        h_residuals.Reset("M")

        for ibin in range(1, h_residuals.GetNbinsX()+1):
            valueErrorData = h_data.GetBinError(ibin)
            valueData = h_data.GetBinContent(ibin)
            postFitValue = h_postfit.GetBinContent(ibin)

            binSig = 0.0  
            if valueErrorData > 0.0:
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
        fout.Close()

    # w.Delete()
    fd.Close()
    f.Close()

    print "Finished ExtractPostfitFromWS"

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
