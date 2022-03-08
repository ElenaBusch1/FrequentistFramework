#!/usr/bin/env python

import ROOT
import array
import glob, argparse

#patternMatch = "PostFit_NotRebinned_fivePar_J100yStar_bOnly_ibin*.root"
#resolutionBinsFileName = "/home/mariana/Nube/TLA/FrequentistFramework/Input/data/dijetTLAnlo/data_J100yStar06_range171_3217.root"
#resolutionBinsHistoName = "data"

def computeResiduals(data, fit, histoName="residuals"):
    h = fit.Clone(histoName)
    h.SetDirectory(0)
    h.Reset("M")
    
    for ibin in range(1, fit.GetNbinsX()+1):
        valueErrorData = data.GetBinError(ibin)
        valueData = data.GetBinContent(ibin)
        valueFit = fit.GetBinContent(ibin)

        binSig = 0.
        if valueErrorData > 0. and valueFit > 0.:
            binSig = (valueData - valueFit)/ valueErrorData
            h.SetBinContent(ibin, binSig)
            h.SetBinError(ibin, 0)
    
    return h

def StitchSwiftResults( patternMatch, outputFileName, resolutionBinsFileName = "Input/data/dijetTLAnlo/binning2021/data_J100yStar06_range171_3217.root", resolutionBinsHistoName = "data"):

  resfile = ROOT.TFile(resolutionBinsFileName, 'read')
  #resHisto = ROOT.TH1D()
  #resfile.GetObject(resolutionBinsHistoName, resHisto)
  resHisto = resfile.Get(resolutionBinsHistoName)
  binEdges = [ resHisto.GetBinLowEdge(i) for i in range(1, resHisto.GetNbinsX()+2) ]
  resolutionBins = array.array('d', binEdges)
  resolutionFrame = ROOT.TH1D("resolutionFrame", "", len(resolutionBins)-1, resolutionBins)

  collectFiles = glob.glob(patternMatch)

  #print "Found files:"
  #print collectFiles

  isFirst = True

  for f in collectFiles:
      # print "Opening file", f
      postfitFile = ROOT.TFile(f, 'read')
      h_fit  = postfitFile.Get("postfit")
      h_res  = postfitFile.Get("residuals")
      if isFirst:
	  h_data = postfitFile.Get("data")
	  h_data.SetDirectory(0)
	  # Store results in 1GeV Bins here:
	  h_swiftFit = h_data.Clone("swiftFit")
	  h_swiftFit.SetDirectory(0)
	  h_swiftFit.Reset()
	  h_swiftResiduals = h_data.Clone("swiftResiduals")
	  h_swiftResiduals.SetDirectory(0)
	  h_swiftResiduals.Reset()
	  isFirst = False

      # va a estar en el otro codigo
      i = int(f.split("ibin")[1].split("_")[0])
      low = resolutionFrame.GetXaxis().GetBinLowEdge(i)
      high = resolutionFrame.GetXaxis().GetBinUpEdge(i)
      for j in range(1,h_fit.GetNbinsX()+1):
	if h_fit.GetXaxis().GetBinLowEdge(j)>= low and h_fit.GetXaxis().GetBinUpEdge(j)<= high:
	  h_swiftFit.SetBinContent( h_swiftFit.FindBin( h_fit.GetBinCenter(j)) , h_fit.GetBinContent(j))
	  h_swiftResiduals.SetBinContent( h_swiftResiduals.FindBin( h_res.GetBinCenter(j) ), h_res.GetBinContent(j))
      
      postfitFile.Close()

  h_swiftFit.SetLineColor(ROOT.kRed)
  h_swiftFit.SetLineWidth(2)
  # We also want to include stuff rebinned in resolution bins:
  firstBin = h_swiftFit.FindFirstBinAbove(0)
  # print "First non-zero bin is", firstBin

  rebinBins = [ binEdge for binEdge in binEdges if binEdge >= h_swiftFit.GetBinLowEdge(firstBin) ]
  # print rebinBins
  h_rebinFit = h_swiftFit.Clone()
  h_rebinFit = h_rebinFit.Rebin( len(rebinBins)-1, "swiftFit_rebinned", array.array('d', rebinBins))
  h_rebinFit.SetNameTitle("swiftFit_rebinned","swiftFit_rebinned")
  h_rebinData = h_data.Clone()
  h_rebinData = h_rebinData.Rebin( len(rebinBins)-1, "data_rebinned", array.array('d', rebinBins))
  h_rebinData.SetNameTitle("data_rebinned", "data_rebinned")
  # Recompute residuals in new binning:
  h_rebinResiduals = computeResiduals( h_rebinData, h_rebinFit, "swiftResiduals_rebinned")

  outputfile = ROOT.TFile(outputFileName,'recreate')
  outputfile.cd()
  h_swiftFit.Write()
  h_data.Write("data")
  h_swiftResiduals.Write()
  h_rebinFit.Write()
  h_rebinData.Write()
  h_rebinResiduals.Write()
  outputfile.Close()

  return

