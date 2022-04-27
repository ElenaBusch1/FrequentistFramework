#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from ROOT import *
import array
import json

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

class PostfitExtractor:
    def __init__(self, 
                 wsfile, 
                 datafile, 
                 datahist, 
                 wsname="combWS", 
                 modelname="ModelConfig", 
                 datafirstbin=0, 
                 rebinfile=None, 
                 rebinhist=None, 
                 externalchi2file=None, 
                 externalchi2fct=None, 
                 externalchi2bins=40, 
                 maskmin=-1, 
                 maskmax=-1):

        self.wsfile = wsfile
        self.datafile = datafile
        self.datahist = datahist
        self.wsname = wsname
        self.modelname = modelname
        self.datafirstbin = datafirstbin
        self.rebinfile = rebinfile
        self.rebinhist = rebinhist
        self.externalchi2file = externalchi2file
        self.externalchi2fct = externalchi2fct
        self.externalchi2bins = externalchi2bins
        self.maskmin = maskmin
        self.maskmax = maskmax
        self.h_data = None
        self.channel_chi2 = {}
        self.channel_nbins = {}
        self.channel_npars = {}
        self.channel_ndof = {}
        self.channel_pval = {}
        self.channel_hpostfit = {}
        self.channel_hchi2 = {}
        self.channel_hresiduals = {}
 
    
    def Extract(self):
        
        f = ROOT.TFile(self.wsfile, "READ")
        w = f.Get(self.wsname)

        fd =  ROOT.TFile(self.datafile, "READ")
        self.h_data = fd.Get(self.datahist)
        self.h_data.SetDirectory(0)

        model = w.obj(self.modelname)
        pdf = model.GetPdf()
        cat = pdf.indexCat()
        nChan = cat.numBins("")

        print "There are %d channels" % nChan

        obs = pdf.getObservables(model.GetObservables())
        obs.Print()

        data = w.data("combData")
        dataList = data.split( cat, True )

        for i in range(nChan):
            datai = dataList.At( i )
            channelname = cat.getLabel()
            pdfi = pdf.getPdf(channelname)
            x = pdfi.getObservables(datai).first()
            
            print "Channel %s:" % channelname
            print "Expected:"
            expectedEvents = pdfi.expectedEvents(RooArgSet(x))

            print expectedEvents

            hpdf = pdfi.createHistogram("hpdf", x)
            hpdf.Scale(expectedEvents/hpdf.Integral())


            binEdges = []
            nBins = hpdf.GetNbinsX()
            for i in range(1, nBins+2):
                binEdges.append(self.h_data.GetBinLowEdge(i+self.datafirstbin))

            h_postfit = TH1D("postfit", "postfit", nBins, array.array('d', binEdges))
            h_postfit.SetDirectory(0)

            for ibin in range(1, nBins+1):
                h_postfit.SetBinContent(ibin, hpdf.GetBinContent(ibin))
                h_postfit.SetBinError(ibin, 0)

            chi2 = 0.
            chi2bins = 0
            maskedchi2bins = 0

            for ibin in range(1, nBins+1):
                binCenter = self.h_data.GetBinCenter(self.datafirstbin+ibin)

                valueErrorData = self.h_data.GetBinError(self.datafirstbin+ibin)
                valueData = self.h_data.GetBinContent(self.datafirstbin+ibin)
                postFitValue = h_postfit.GetBinContent(ibin)

                binSig = 0.
                if valueErrorData > 0. and postFitValue > 0.:
                    #binSig = (valueData - postFitValue)/valueErrorData
		    # low stats: (e.g.: J100, above 2.5 TeV, less than 10 entries per 1GeV bin)
		    binSig = (valueData - postFitValue)/math.sqrt(postFitValue) 

                    if binCenter < self.maskmin or binCenter > self.maskmax:
                        chi2bins += 1
                        chi2 += binSig*binSig
                    else:
                        maskedchi2bins += 1

            npars = getNPars(pdfi, x, exclSyst=True)

            if self.externalchi2file and self.externalchi2fct:
                f_chi2 = TFile(self.externalchi2file)
                tf1_chi2 = f_chi2.Get(self.externalchi2fct)
                ndof = chi2bins - self.externalchi2bins + tf1_chi2.GetParameter(0)
                ndoferr = tf1_chi2.GetParError(0)
                f_chi2.Close()
            else:
                ndof = chi2bins - npars
                ndoferr = 0.

            pval = ROOT.Math.chisquared_cdf_c(chi2, ndof)

            h_chi2 = TH1D("chi2", "chi2", 6, 0, 6)
            h_chi2.SetDirectory(0)
            h_chi2.SetBinContent(1, chi2)
            h_chi2.SetBinContent(2, chi2/ndof)
            h_chi2.SetBinContent(3, chi2bins)
            h_chi2.SetBinContent(4, npars)
            h_chi2.SetBinContent(5, ndof)
            h_chi2.SetBinError(5, ndoferr)
            h_chi2.SetBinContent(6, pval)

            h_chi2.GetXaxis().SetBinLabel(1, "chi2")
            h_chi2.GetXaxis().SetBinLabel(2, "chi2/ndof")
            h_chi2.GetXaxis().SetBinLabel(3, "nbins")
            h_chi2.GetXaxis().SetBinLabel(4, "npars")
            h_chi2.GetXaxis().SetBinLabel(5, "ndof")
            h_chi2.GetXaxis().SetBinLabel(6, "pval")

            binEdges = None
            if self.rebinfile and self.rebinhist:
                f_rebin = ROOT.TFile(self.rebinfile, "READ")
                h_rebin = f_rebin.Get(self.rebinhist)

                binEdges = []
                nBins = h_rebin.GetNbinsX()
                for i in range(1, nBins+2):
                    edge = h_rebin.GetBinLowEdge(i)
                    if edge < h_postfit.GetBinLowEdge(1) or edge > h_postfit.GetBinLowEdge(h_postfit.GetNbinsX()+2):
                        continue
                    binEdges.append(edge)
                    
                f_rebin.Close()
            
            if binEdges:
                h_postfit = h_postfit.Rebin(len(binEdges)-1, "postfit", array.array('d', binEdges))
                self.h_data = self.h_data.Rebin(len(binEdges)-1, self.datahist, array.array('d', binEdges))
                self.datafirstbin = self.h_data.FindBin(self.datafirstbin) - 1

            h_residuals = h_postfit.Clone("residuals")
            h_residuals.SetDirectory(0)
            h_residuals.Reset("M")

            for ibin in range(1, h_residuals.GetNbinsX()+1):
                valueErrorData = self.h_data.GetBinError(ibin+self.datafirstbin)
                valueData = self.h_data.GetBinContent(ibin+self.datafirstbin)
                postFitValue = h_postfit.GetBinContent(ibin)

                binSig = 0.
                if valueErrorData > 0. and postFitValue > 0.:
                    binSig = (valueData - postFitValue)/valueErrorData

                    h_residuals.SetBinContent(ibin, binSig)
                    h_residuals.SetBinError(ibin, 0)

            self.channel_chi2[channelname] = chi2
            self.channel_nbins[channelname] = chi2bins
            self.channel_npars[channelname] = npars
            self.channel_ndof[channelname] = ndof
            self.channel_pval[channelname] = pval

            self.channel_hpostfit[channelname] = h_postfit
            self.channel_hresiduals[channelname] = h_residuals
            self.channel_hchi2[channelname] = h_chi2

        fd.Close()
        f.Close()

    def WriteRoot(self, outfile, dirPerCategory=False):
        if not self.h_data:
            self.Extract()

        fout = ROOT.TFile(outfile, "RECREATE")

        if dirPerCategory:
            for channelname in self.channel_chi2:
                d = fout.mkdir(channelname)
                d.cd()

                self.h_data.Write("data")
                self.channel_hpostfit[channelname].Write("postfit")
                self.channel_hresiduals[channelname].Write("residuals")
                # self.channel_hresiduals[channelname].Write("postFitSigma")
                self.channel_hchi2[channelname].Write("chi2")
        else:
            # just take first (and hopefully only) channel
            self.h_data.Write("data")
            next(iter(self.channel_hpostfit.values())).Write("postfit")
            next(iter(self.channel_hresiduals.values())).Write("residuals")
            # next(iter(self.channel_hresiduals.values())).Write("postFitSigma")
            next(iter(self.channel_hchi2.values())).Write("chi2")

        fout.Close()

    def GetChi2(self, channelname=None):
        if not self.channel_chi2:
            self.Extract()
        if channelname:
            return self.channel_chi2[channelname]
        else:
            return next(iter(self.channel_chi2.values()))

    def GetNbins(self, channelname=None):
        if not self.channel_nbins:
            self.Extract()
        if channelname:
            return self.channel_nbins[channelname]
        else:
            return next(iter(self.channel_nbins))

    def GetNpars(self, channelname=None):
        if not self.channel_npars:
            self.Extract()
        if channelname:
            return self.channel_npars[channelname]
        else:
            return next(iter(self.channel_npars))

    def GetNdof(self, channelname=None):
        if not self.channel_ndof:
            self.Extract()
        if channelname:
            return self.channel_ndof[channelname]
        else:
            return next(iter(self.channel_ndof))
        
    def GetPval(self, channelname=None):
        if not self.channel_pval:
            self.Extract()
        if channelname:
            return self.channel_pval[channelname]
        else:
            return next(iter(self.channel_pval.values()))

    def GetH1Chi2(self, channelname=None):
        if not self.channel_hchi2:
            self.Extract()
        if channelname:
            return self.channel_hchi2[channelname]
        else:
            return next(iter(self.channel_hchi2))

    def GetH1Postfit(self, channelname=None):
        if not self.channel_hpostfit:
            self.Extract()
        if channelname:
            return self.channel_hpostfit[channelname]
        else:
            return next(iter(self.channel_hpostfit))

    def GetH1Residuals(self, channelname=None):
        if not self.channel_hresiduals:
            self.Extract()
        if channelname:
            return self.channel_hresiduals[channelname]
        else:
            return next(iter(self.channel_hresiduals))

    def GetCategories(self):
        if not self.channel_chi2:
            self.Extract()
        return self.channel_chi2.keys()


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
    parser.add_argument('--externalchi2bins', dest='externalchi2bins', type=int, default=40, help='Number of bins for external chi2 TF1')
    parser.add_argument('--maskmin', dest='maskmin', type=int, default=-1, help='Masked range to exclude from chi2 calculation')
    parser.add_argument('--maskmax', dest='maskmax', type=int, default=-1, help='Masked range to exclude from chi2 calculation')

    args = parser.parse_args(args)

    pfe = PostfitExtractor(
        wsfile=args.wsfile,
        datafile=args.datafile,
        datahist=args.datahist,
        datafirstbin=args.datafirstbin,
        wsname=args.wsname,
        modelname=args.modelname,
        rebinfile=args.rebinfile,
        rebinhist=args.rebinhist,
        externalchi2file=args.externalchi2file,
        externalchi2fct=args.externalchi2fct,
        externalchi2bins=args.externalchi2bins,
        maskmin=args.maskmin,
        maskmax=args.maskmax
    )
    pfe.Extract()
    pfe.WriteRoot(args.outfile)
    
    print "Finished ExtractPostfitFromWS"

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
