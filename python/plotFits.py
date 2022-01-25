#!/usr/bin/env python

# This script does some checks of the pulls of the fit

import ROOT
import sys, re, os, math, argparse
import DrawingFunctions as df

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")

def main(args):
    ROOT.SetAtlasStyle()

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--infiles', dest='infiles', type=str, nargs="*", default=None, help='Input file names')
    #parser.add_argument('--inResidualHist', dest='residualhist', type=str, default='residuals', help='Input residual hist name')
    #parser.add_argument('--inDataName', dest='datahist', type=str, default='data', help='Data hist name')
    parser.add_argument('--outfile', dest='outfile', type=str, default='fits.root', help='Output file name')
    parser.add_argument('--minMjj', dest='minMjj', type=int, default=300, help='Minimum fit range')
    parser.add_argument('--maxMjj', dest='maxMjj', type=int, default=300, help='Maximum fit range')
    parser.add_argument('--rebinedges', dest='rebinedges', type=int, nargs="*", default=None, help='Name of template hist')
    args = parser.parse_args(args)


    c = ROOT.TCanvas("c1", "c1", 800, 600)
    c.SetRightMargin(0.10)
    c.SetLeftMargin(0.10)
    c.SetLogy()

    dataHists = []
    fitHists = []
    residualHists = []

   
    for index, infileName in zip(range(len(args.infiles)), args.infiles):
      inFile = ROOT.TFile(infileName, "READ")
        
      dataHist = inFile.Get("data")
      fitHist = inFile.Get("postfit")
      residualHist = inFile.Get("residuals")

      dataHist.SetDirectory(0)
      fitHist.SetDirectory(0)
      residualHist.SetDirectory(0)

      dataHist.SetName("%s_%s"%(dataHist.GetName(), infileName))
      fitHist.SetName("%s_%s"%(fitHist.GetName(), infileName))
      residualHist.SetName("%s_%s"%(residualHist.GetName(), infileName))

      dataHists.append(dataHist)
      fitHists.append(fitHist)
      residualHists.append(residualHist)

      dataHist.GetXaxis().SetRangeUser(args.minMjj, args.maxMjj)
      fitHist.GetXaxis().SetRangeUser(args.minMjj, args.maxMjj)
      residualHist.GetXaxis().SetRangeUser(args.minMjj, args.maxMjj)


    # TODO fix these labels
    leg = df.DrawRatioHists(c, dataHists, residualHists, args.infiles, [], "", drawOptions = "HIST", outName="Test", isLogX = False)
    c.Print(args.outfile.replace(".root", ".pdf"))

    inFile.Close()


if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
