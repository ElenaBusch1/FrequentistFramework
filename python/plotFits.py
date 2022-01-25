#!/usr/bin/env python

# This script does some checks of the pulls of the fit

import ROOT
import sys, re, os, math, argparse
import DrawingFunctions as df
import python.AtlasStyle as AS
import array

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")

def plotFits(infiles, outfile, minMjj, maxMjj, rebinedges=None, atlasLabel="Simulation Internal", residualhistName="residuals", datahistName="data", fithistName="postfit"):
    AS.SetAtlasStyle()

    c = df.setup_canvas()
    c.SetLogy()

    dataHists = []
    fitHists = []
    residualHists = []
    plotHists = []
    legNames = []

    labels = []

    for index, infileName in zip(range(len(infiles)), infiles):
      inFile = ROOT.TFile(infileName, "READ")

      dataHist = inFile.Get(datahistName)
      fitHist = inFile.Get(fithistName)
      residualHist = inFile.Get(residualhistName)
      chi2Hist = inFile.Get("chi2")
      chi2 = chi2Hist.GetBinContent(2)
      pval = chi2Hist.GetBinContent(6)

      dataHist.SetDirectory(0)
      fitHist.SetDirectory(0)
      residualHist.SetDirectory(0)

      dataHist.SetName("%s_%s"%(dataHist.GetName(), infileName))
      fitHist.SetName("%s_%s"%(fitHist.GetName(), infileName))
      residualHist.SetName("%s_%s"%(residualHist.GetName(), infileName))


      dataHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
      fitHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
      residualHist.GetXaxis().SetRangeUser(minMjj, maxMjj)

    
      if rebinedges:
        print("Rebinning histogram based on list of bins")
        dataHist = dataHist.Rebin(len(rebinedges)-1, "postfit", array.array('d', rebinedges))
        fitHist = fitHist.Rebin(len(rebinedges)-1, "postfit", array.array('d', rebinedges))
        residualHist = residualHist.Rebin(len(rebinedges)-1, "postfit", array.array('d', rebinedges))

      dataHists.append(dataHist)
      fitHists.append(fitHist)
      residualHists.append(residualHist)
      plotHists.append(dataHist)
      plotHists.append(fitHist)
      legNames.append("data")
      legNames.append("fit")


      label = "#chi^2 / ndof = %.2f, p-value = %.1f %%"%(chi2, pval)
      labels.append(label)


    # TODO fix these labels
    outname = outfile.replace(".root", "")
    leg = df.DrawRatioHists(c, plotHists, residualHists, legNames, labels, "", drawOptions = "HIST", outName=outname, isLogX = False)

    inFile.Close()



def main(args):
    ROOT.SetAtlasStyle()

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--infiles', dest='infiles', type=str, nargs="*", default=None, help='Input file names')
    parser.add_argument('--inResidualHist', dest='residualhist', type=str, default='residuals', help='Input residual hist name')
    parser.add_argument('--inDataName', dest='datahist', type=str, default='data', help='Data hist name')
    parser.add_argument('--outfile', dest='outfile', type=str, default='fits.root', help='Output file name')
    parser.add_argument('--minMjj', dest='minMjj', type=int, default=300, help='Minimum fit range')
    parser.add_argument('--maxMjj', dest='maxMjj', type=int, default=300, help='Maximum fit range')
    parser.add_argument('--rebinedges', dest='rebinedges', type=int, nargs="*", default=None, help='Name of template hist')
    args = parser.parse_args(args)

    plotFits(infiles=args.infiles, outfile=args.outfile, minMjj=args.minMjj, maxMjj=args.maxMjj, rebinedges=args.rebinedges, residualhistName=args.residualhist, datahistName=args.datahist)




if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
