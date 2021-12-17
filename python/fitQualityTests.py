# This code tests the variation in the fits of the pseudodata.

#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from ROOT import *
import math

ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")


def main(args):
    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--wsfile', dest='wsfile', type=str, default='../run/FitResult.root', help='Input workspace file name')
    parser.add_argument('--outfile', dest='outfile', type=str, default='plots/fitStability.root', help='Output file name')
    parser.add_argument('--nToys', dest='nToys', type=int, default=50, help='Number of toys to run')
    
    args = parser.parse_args(args)

    nominalName = "ajj/PostFit_ajj_simpleTrig_yStar0p825_1GeVBin_GlobalFit300to1000_0.root"
    nominalFile = ROOT.TFile(nominalName, "READ")
    nominalFit = nominalFile.Get("postfit")
    nominalFit.SetDirectory(0)
    tmpError = nominalFit.Clone("tmpError")
    relError = nominalFit.Clone("RelError")
    relError.SetDirectory(0)

    for toy in range(args.nToys):
       #toyName = "plots/BkgFitTest_pd_%d.root"%(toy)
       toyName = "ajj/PostFitPD_ajj_simpleTrig_yStar0p825_1GeVBin_GlobalFit300to1000_%d.root"%(toy)
       toyFile = ROOT.TFile(toyName, "READ")
       toyFit = toyFile.Get("postfit")
       toyFit.SetDirectory(0)

       toyFit.Add(nominalFit, -1)
       toyFit.Multiply(toyFit)

       tmpError.Add(toyFit)
    
    for xbin in range(nominalFit.GetNbinsX()):
       nominalFit.SetBinError(xbin+1, math.sqrt(tmpError.GetBinContent(xbin+1)))
       relError.SetBinError(xbin+1, math.sqrt(tmpError.GetBinContent(xbin+1)) / nominalFit.GetBinContent(xbin+1) )
       relError.SetBinContent(xbin+1, 1 )
       #print(xbin+1, nominalFit.GetBinContent(xbin+1), nominalFit.GetBinError(xbin+1))
      
    outFile = ROOT.TFile(args.outfile, "RECREATE")
    nominalFit.Write("FitWithError")
    outFile.Close()



    c = ROOT.TCanvas("c1", "c1", 800, 600)
    c.SetRightMargin(0.10)
    c.SetLeftMargin(0.10)
    relError.Draw("ex0")
    c.Print("plots/fit.pdf")

    

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
