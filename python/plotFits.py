#!/usr/bin/env python

# This script does some checks of the pulls of the fit

import ROOT
import sys, re, os, math, argparse
import python.LocalFunctions as lf
import python.DrawingFunctions as df
import python.AtlasStyle as AS
import array
import config as config
import python.ExtractFitParameters as efp



def plotFits(infiles, outfile, minMjj, maxMjj, lumi, cdir, channelName, rebinedges=None, 
             atlasLabel="Simulation Internal", residualhistName="residuals", datahistName="data", 
             fithistName="postfit", suffix="", fitNames = None, sigamp=0, sigmean=0, sigwidth=0, toy=None, indir="", cutoffSpectrum = False):

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
    labels.append(config.samples[channelName]["varLabel"])

    for index, infileName, fitName in zip(range(len(infiles)), infiles, fitNames):
      path = config.getFileName(infileName, cdir, channelName, indir, sigmean, sigwidth, sigamp) + ".root"
      csuffix = suffix
      if toy != None:
        csuffix = "%s_%d"%(suffix, toy)
      dataHistTmp = lf.read_histogram(path, datahistName + channelName + "_" +csuffix)
      print path, datahistName + channelName + "_" +csuffix
      fitHist = lf.read_histogram(path, fithistName +channelName + "_" + csuffix)
      residualHist = lf.read_histogram(path, residualhistName +channelName + "_" + csuffix)
      #print path, datahistName + channelName+suffix
      dataHistTmp.SetName("data_%s_%s_%s"%(dataHistTmp.GetName(), infileName, csuffix))
      fitHist.SetName("%s_%s_%s"%(fitHist.GetName(), infileName, csuffix))
      residualHist.SetName("%s_%s_%s"%(residualHist.GetName(), infileName, csuffix))

      try:
        postFit = path.replace("FitParameters", "PostFit")
        chi2Hist = lf.read_histogram(postFit, "chi2"+channelName+"_"+csuffix)
        chi2 = chi2Hist.GetBinContent(2)
        pval = chi2Hist.GetBinContent(6)
      except:
        #print "Did not find the chi2 or pval", postFit, suffix, "chi2"+suffix
        chi2 = -1
        pval = -1

      fitPath = path
      fitPath = fitPath.replace("PostFit","FitParameters")
      nsig=0
      try:
        fpe = efp.FitParameterExtractor(fitPath)
        if toy:
          fpe.suffix = "%s__%d"%(channelName,toy)
          #fpe.ExtractFromFile( "%s"%(channelName))
          fpe.ExtractFromFile( "%s__%d"%(channelName,toy))
        else:
          fpe.suffix = channelName
          fpe.ExtractFromFile( channelName)
        nsig = fpe.GetNsig()
        nbkg = fpe.GetNbkg()
        labels.append("N_{sig, extracted} = %.3f"%nsig)
        labels.append("N_{bkg} = %.3f"%nbkg)
      except:
        #print "Unable to find fit parameters,", fitPath
        x1230123=1

      if not dataHistTmp or not fitHist or not residualHist:
        continue
      dataHist = fitHist.Clone("data_%s"%(dataHistTmp.GetName()))
      dataHist.SetDirectory(0)
      dataHist.Reset()
      maxData = 0
      for cbin in range(dataHist.GetNbinsX()):
         dataHist.SetBinContent(cbin+1, dataHistTmp.GetBinContent(dataHistTmp.FindBin(dataHist.GetBinCenter(cbin+1))))
         dataHist.SetBinError(cbin+1, dataHistTmp.GetBinError(dataHistTmp.FindBin(dataHist.GetBinCenter(cbin+1))))

      
      if(cutoffSpectrum):
        maxMjj = maxData
      dataHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
      dataHist.SetTitle(config.samples[channelName]["legend"])
      fitHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
      residualHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
    
      # This allows us to rebin the histograms using resolution binning, if we want
      if rebinedges:
        dataHist = dataHist.Rebin(len(rebinedges)-1, "dataHist_%s"%(infileName), array.array('d', rebinedges))
        fitHist = fitHist.Rebin(len(rebinedges)-1, "fitHist_%s"%(infileName), array.array('d', rebinedges))
        residualHist = residualHist.Rebin(len(rebinedges)-1, "residual_%s"%(infileName), array.array('d', rebinedges))
        dataHist.SetDirectory(0)
        fitHist.SetDirectory(0)
        residualHist.SetDirectory(0)

        for ibin in range(1, dataHist.GetNbinsX()+1):
          valueErrorData = dataHist.GetBinError(ibin)
          valueData = dataHist.GetBinContent(ibin)
          postFitValue = fitHist.GetBinContent(ibin)

          binSig = 0.
          if valueErrorData > 0. and postFitValue > 0.:
            binSig = (valueData - postFitValue)/valueErrorData

            residualHist.SetBinContent(ibin, binSig)
            residualHist.SetBinError(ibin, 0)
            residualHist.GetXaxis().SetTitle(config.samples[channelName]["varAxis"])
            residualHist.GetYaxis().SetTitle("Residuals (#sigma)")


      dataHist.GetXaxis().SetTitle(config.samples[channelName]["varAxis"])
      dataHist.GetYaxis().SetTitle("N_{events}")

      if cutoffSpectrum:
         for cbin in range(dataHist.GetNbinsX()):
           if dataHist.GetBinContent(cbin+1) > 0:
             maxData = dataHist.GetBinLowEdge(cbin+4)
      if(cutoffSpectrum):
        maxMjj = maxData
      dataHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
      fitHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
      residualHist.GetXaxis().SetRangeUser(minMjj, maxMjj)

      if index == 0:
        dataRes = residualHist.Clone("Residuals_zero")
        dataRes.Reset()
        dataRes.GetYaxis().SetRangeUser(-3, 3)
        dataRes.GetXaxis().SetRangeUser(minMjj, maxMjj)
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
      legNames.append("#splitline{%s, }{#chi^{2} / ndof = %.2f, p-val = %.2f}"%(tmpName, chi2, pval))


    #c.SetLogx()
    df.SetRange(plotHists, minMin=1e-5, maxMax=1e8, isLog=True, minMjj=minMjj, maxMjj = maxMjj)
    outname = outfile.replace(".root", "")

    # Note: do not try to use Logx with this version of root (6.20.04), because it will fail.
    # For now, leave in linear, and if we can update the root version, we can also fix this
    plotHists[0].SetFillStyle(1001)
    plotHists[0].SetFillColorAlpha(ROOT.kBlack, 0.25);
    leg = df.DrawRatioHists(c, plotHists, residualHists, legNames, labels, "", drawOptions = ["e2", "HIST", "HIST", "HIST", "HIST", "HIST"], outName=outname, isLogX = False, styleOptions = df.get_fit_style_opt, lumi=lumi, atlasLabel=atlasLabel, ratioDrawOptions = ["HIST", "HIST", "HIST", "HIST", "HIST"])

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
