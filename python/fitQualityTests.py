# This code tests the variation in the fits of the pseudodata.

#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from ROOT import *
import math
import config as config

ROOT.gROOT.SetBatch(ROOT.kTRUE)

ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")


def fitQualityTests(pdfile, nominalname, outfile, ntoys, rangelow, rangehigh, lumi, sigmean, sigwidth, sigamp, cdir, channelName):

    nominalFileName = config.getFileName(nominalname, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
    nominalFile = ROOT.TFile(nominalFileName, "READ")

    nominalFit = nominalFile.Get("postfit_0")
    nominalFit.SetDirectory(0)
    tmpError = nominalFit.Clone("tmpError")
    relError = nominalFit.Clone("RelError")
    relError.SetDirectory(0)

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
       relError.SetBinContent(xbin+1, 1 )

    outFile = ROOT.TFile(outfile, "RECREATE")
    nominalFit.Write("FitWithError")
    outFile.Close()



    c = ROOT.TCanvas("c1", "c1", 800, 600)
    c.SetRightMargin(0.10)
    c.SetLeftMargin(0.10)
    relError.Draw("ex0")
    c.Print("plots/fit.pdf")




def main(args):
    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--pdfile', dest='pdfile', type=str, default='jjj/PD_swift_fivePar_bkgonly_range_300_1700.root', help='Input workspace file name')
    parser.add_argument('--nominalName', dest='nominalName', type=str, default='jjj/PostFit_swift_fivePar_bkgonly_range_300_1200.root', help='Input workspace file name')
    #parser.add_argument('--minMjj', dest='minMjj', type=str, default='300', help='Minimum value of mjj')
    #parser.add_argument('--maxMjj', dest='maxMjj', type=str, default='1000', help='Maximum value of mjj')
    parser.add_argument('--outfile', dest='outfile', type=str, default='plots/fitStability.root', help='Output file name')
    parser.add_argument('--nToys', dest='nToys', type=int, default=50, help='Number of toys to run')
    
    args = parser.parse_args(args)

    fitQualityTests(args.pdfile, args.nominalname, args.outfile, args.ntoys, args.rangemin, args.rangemax, args.sigmean, args.sigwidth, args.sigamp, args.cdir, args.channelName)


    

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
