# This code tests the variation in the fits of the pseudodata.

#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from ROOT import *
import math
import config as config
import DrawingFunctions as df



def fitQualityTests(pdfile, nominalname, fitFunction1File, fitFunction2File, outfile, ntoys, rangelow, rangehigh, lumi, sigmean, sigwidth, sigamp, cdir, channelName):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    nominalFileName = config.getFileName(nominalname, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
    nominalFile = ROOT.TFile(nominalFileName, "READ")

    nominalFit = nominalFile.Get("postfit_0")
    nominalFit.SetDirectory(0)

    tmpError = nominalFit.Clone("tmpError")
    relError = nominalFit.Clone("RelError")
    relError.SetDirectory(0)
    relError.GetXaxis().SetTitle("m_{jj}")


    for toy in range(ntoys):
       toyName = config.getFileName(pdfile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
       toyFile = ROOT.TFile(toyName, "READ")
       try:
         toyFit = toyFile.Get("postfit_%d"%(toy))
         toyFit.SetDirectory(0)
       except:
         continue

       toyFit.Add(nominalFit, -1)
       toyFit.Multiply(toyFit)

       tmpError.Add(toyFit)

    for xbin in range(nominalFit.GetNbinsX()):
       nominalFit.SetBinError(xbin+1, math.sqrt(tmpError.GetBinContent(xbin+1)))
       relError.SetBinError(xbin+1, math.sqrt(tmpError.GetBinContent(xbin+1)) / nominalFit.GetBinContent(xbin+1) )
       relError.SetBinContent(xbin+1, 0 )

    fit1Name = config.getFileName(fitFunction1File, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
    fit1File = ROOT.TFile(fit1Name, "READ")
    Fit1 = fit1File.Get("postfit")
    Fit1.SetDirectory(0)

    fit2Name = config.getFileName(fitFunction2File, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
    fit2File = ROOT.TFile(fit2Name, "READ")
    Fit2 = fit2File.Get("postfit")
    Fit2.SetDirectory(0)

    relErrorFit = nominalFit.Clone("RelErrorFit")
    relErrorFit.SetDirectory(0)
    relErrorFit.GetXaxis().SetTitle("m_{jj}")
    for xbin in range(nominalFit.GetNbinsX()):
       relErrorFit.SetBinError(xbin+1, (Fit2.GetBinContent(xbin+1) - Fit1.GetBinContent(xbin+1)) / Fit1.GetBinContent(xbin+1) )
       relErrorFit.SetBinContent(xbin+1, 0 )


    c = ROOT.TCanvas("c1", "c1", 800, 600)
    leg = df.DrawHists(c, [relError, relErrorFit], ["Stat uncertainty on fit", "Function choice"], [], drawOptions = ["ex0"], styleOptions=df.get_extraction_style_opt, isLogX=0)
    path = config.getFileName(outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"





def main(args):
    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--pdfile', dest='pdfile', type=str, default='jjj/PD_swift_fivePar_bkgonly_range_300_1700.root', help='Input workspace file name')
    parser.add_argument('--nominalName', dest='nominalName', type=str, default='jjj/PostFit_swift_fivePar_bkgonly_range_300_1200.root', help='Input workspace file name')
    parser.add_argument('--outfile', dest='outfile', type=str, default='plots/fitStability.root', help='Output file name')
    parser.add_argument('--nToys', dest='nToys', type=int, default=50, help='Number of toys to run')
    
    args = parser.parse_args(args)

    fitQualityTests(args.pdfile, args.nominalname, args.outfile, args.ntoys, args.rangemin, args.rangemax, args.sigmean, args.sigwidth, args.sigamp, args.cdir, args.channelName)


    

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
