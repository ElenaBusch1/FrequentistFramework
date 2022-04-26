#!/usr/bin/env python

# This script does some checks of the pulls of the fit

import ROOT
import sys, re, os, math, argparse
import DrawingFunctions as df
import python.AtlasStyle as AS
import array
import config as config
import ExtractFitParameters as efp



def plotFits(infiles, outfile, minMjj, maxMjj, lumi, cdir, channelName, rebinedges=None, 
             atlasLabel="Simulation Internal", residualhistName="residuals", datahistName="data", 
             fithistName="postfit", suffix="", fitNames = None, sigamp=0, sigmean=0, sigwidth=0, toy=0):

    ROOT.gROOT.SetBatch(ROOT.kTRUE)
    AS.SetAtlasStyle()

    c = df.setup_canvas(outfile)
    c.SetLogy()

    dataHists = []
    fitHists = []
    residualHists = []
    plotHists = []
    legNames = []

    if not fitNames:
      fitNames = infiles

    labels = []

    for index, infileName, fitName in zip(range(len(infiles)), infiles, fitNames):
      path = config.getFileName(infileName, cdir, channelName, minMjj, maxMjj, sigmean, sigwidth, sigamp) + ".root"
      inFile = ROOT.TFile(path, "READ")
      if not inFile:
        print "Did not find file ", path

      dataHist = inFile.Get(datahistName + suffix)
      fitHist = inFile.Get(fithistName + suffix)
      residualHist = inFile.Get(residualhistName + suffix)
      try:
        chi2Hist = inFile.Get("chi2"+suffix)
        chi2 = chi2Hist.GetBinContent(2)
        pval = chi2Hist.GetBinContent(6)
      except:
        chi2 = -1
        pval = -1
      inFile.Close()

      fitPath = path
      fitPath = fitPath.replace("PostFit","FitParameters")
      nsig=0
      try:
        fpe = efp.FitParameterExtractor(fitPath)
        fpe.suffix = "_%d"%(toy)
        fpe.ExtractFromFile( "_%d"%(toy))
        nsig = fpe.GetNsig()
        labels.append("N_{sig, extracted} = %.3f"%nsig)
      except:
        print "no luck"

      dataHist.SetName("%s_%s_%s"%(dataHist.GetName(), infileName, suffix))
      fitHist.SetName("%s_%s_%s"%(fitHist.GetName(), infileName, suffix))
      residualHist.SetName("%s_%s_%s"%(residualHist.GetName(), infileName, suffix))

      dataHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
      dataHist.SetTitle(config.samples[channelName]["legend"])
      fitHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
      residualHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
    
      # This allows us to rebin the histograms using resolution binning, if we want
      if rebinedges:
        dataHist = dataHist.Rebin(len(rebinedges)-1, "postfit", array.array('d', rebinedges))
        fitHist = fitHist.Rebin(len(rebinedges)-1, "postfit", array.array('d', rebinedges))
        residualHist = residualHist.Rebin(len(rebinedges)-1, "postfit", array.array('d', rebinedges))

        for ibin in range(1, dataHist.GetNbinsX()+1):
          valueErrorData = dataHist.GetBinError(ibin)
          valueData = dataHist.GetBinContent(ibin)
          postFitValue = fitHist.GetBinContent(ibin)

          binSig = 0.
          if valueErrorData > 0. and postFitValue > 0.:
            binSig = (valueData - postFitValue)/valueErrorData

            residualHist.SetBinContent(ibin, binSig)
            residualHist.SetBinError(ibin, 0)
            residualHist.GetXaxis().SetTitle(config.samples[channelName]["varName"])
            residualHist.GetYaxis().SetTitle("Residuals (#sigma)")


      dataHist.SetDirectory(0)
      dataHist.GetXaxis().SetTitle(config.samples[channelName]["varName"])
      dataHist.GetYaxis().SetTitle("N_{events}")
      fitHist.SetDirectory(0)
      residualHist.SetDirectory(0)

      if index == 0:
        dataRes = residualHist.Clone("Residuals_zero")
        dataRes.Reset()
        dataRes.GetYaxis().SetRangeUser(-5.2,5.2)
        dataRes.SetDirectory(0)
        residualHists.append(dataRes)
        dataHist.SetTitle(config.samples[channelName]["legend"])
        plotHists.append(dataHist)
        legNames.append(config.samples[channelName]["legend"])

      dataHists.append(dataHist)
      fitHists.append(fitHist)
      residualHists.append(residualHist)

      plotHists.append(fitHist)
      try:
        tmpName = config.fitFunctions[fitName]["Name"]
      except:
        tmpName = fitName
      legNames.append("#splitline{%s, }{#chi^{2} / ndof = %.2f, p-value = %.2f %%}"%(tmpName, chi2, pval))


    df.SetRange(plotHists, minMin=1, maxMax=1e8, isLog=True)
    outname = outfile.replace(".root", "")

    leg = df.DrawRatioHists(c, plotHists, residualHists, legNames, labels, "", drawOptions = ["PX0", "HIST", "HIST", "HIST"], outName=outname, isLogX = False, styleOptions = df.get_fit_style_opt, lumi=lumi, atlasLabel=atlasLabel)
    c.Print(outname + ".pdf")




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
