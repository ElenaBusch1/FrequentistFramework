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
             fithistName="postfit", suffix="", fitNames = None, sigamp=0, sigmean=0, sigwidth=0, toy=None, indir=""):

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
      dataHistTmp = lf.read_histogram(path, datahistName + channelName + "_" +suffix)
      fitHist = lf.read_histogram(path, fithistName +channelName + "_" + suffix)
      residualHist = lf.read_histogram(path, residualhistName +channelName + "_" + suffix)
      dataHistTmp.SetName("data_%s_%s_%s"%(dataHistTmp.GetName(), infileName, suffix))
      fitHist.SetName("%s_%s_%s"%(fitHist.GetName(), infileName, suffix))
      residualHist.SetName("%s_%s_%s"%(residualHist.GetName(), infileName, suffix))

      try:
        postFit = path.replace("FitParameters", "PostFit")
        chi2Hist = lf.read_histogram(postFit, "chi2"+channelName+"_"+suffix)
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
        if toy!=None:
          fpe.suffix = "%s__%d"%(channelName,toy)
          #fpe.ExtractFromFile( "%s"%(channelName))
          fpe.ExtractFromFile( "%s__%d"%(channelName,toy))
          params = fpe.GetH1Params()
        else:
          fpe.suffix = channelName
          fpe.ExtractFromFile( channelName)
        nsig = fpe.GetNsig()
        nbkg = fpe.GetNbkg()
        #labels.append("N_{sig, extracted} = %.3f"%nsig)
        #labels.append("N_{bkg} = %.3f"%nbkg)
      except:
        print "Unable to find fit parameters,", fitPath
        x1230123=1



      if not dataHistTmp or not fitHist or not residualHist:
        continue
      dataHist = fitHist.Clone("data_%s"%(dataHistTmp.GetName()))
      dataHist.SetDirectory(0)
      dataHist.Reset()
      for cbin in range(dataHist.GetNbinsX()):
         dataHist.SetBinContent(cbin+1, dataHistTmp.GetBinContent(dataHistTmp.FindBin(dataHist.GetBinCenter(cbin+1))))
         dataHist.SetBinError(cbin+1, dataHistTmp.GetBinError(dataHistTmp.FindBin(dataHist.GetBinCenter(cbin+1))))

      
      dataHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
      dataHist.SetTitle(config.samples[channelName]["legend"])
      fitHist.GetXaxis().SetRangeUser(minMjj, maxMjj)
      residualHist.GetXaxis().SetRangeUser(minMjj, maxMjj)



      #fitNoSignal = ROOT.TF1("testFit", "[0]*TMath::Power(1-x/[1],[2])/TMath::Power(x/[1], [3] + [4]*TMath::Log(x/[1]) )", 0, 2000)
      #fitNoSignal = ROOT.TF1("testFit", "[0]*TMath::Power(1-x/[1],[2])/TMath::Power(x/[1], [3] + [4]*TMath::Log(x/[1]) + [5]*TMath::Power(TMath::Log(x/[1]), 2) )", 0, 2000)
      fitNoSignal = ROOT.TF1("testFit", "[0]*TMath::Power(1-x/[1],[2])/TMath::Power(x/[1], [3] + [4]*TMath::Log(x/[1]) )", minMjj, maxMjj)
      fitNoSignal.SetNpx(maxMjj-minMjj)
      fitNoSignal.GetXaxis().SetRangeUser(minMjj, maxMjj)

      par5 = 0
      par1 = 13000
      # The first 2 parameters are the number of background and number of signal, and the indexing starts at 1 --> 3+index
      for cbin in range(params.GetNbinsX()):
          if params.GetXaxis().GetBinLabel(cbin+1).find("p2") >= 0:
            par2 = params.GetBinContent(cbin+1)
          if params.GetXaxis().GetBinLabel(cbin+1).find("p3") >= 0:
            par3 = params.GetBinContent(cbin+1)
          if params.GetXaxis().GetBinLabel(cbin+1).find("p4") >= 0:
            par4 = params.GetBinContent(cbin+1)
          if params.GetXaxis().GetBinLabel(cbin+1).find("p5") >= 0:
            par5 = params.GetBinContent(cbin+1)


      #par0 = params.GetBinContent(1) / fitNoSignal.Integral(minMjj, maxMjj)
      par0 = dataHistTmp.Integral(minMjj, maxMjj) / (maxMjj - minMjj) / 1000000
      print par0
      #par0 = dataHist.Integral(minMjj, maxMjj) 
      fitNoSignal.SetParameter(0, par0)
      fitNoSignal.SetParameter(1, par1)
      fitNoSignal.SetParameter(2, par2)
      fitNoSignal.SetParameter(3, par3)
      fitNoSignal.SetParameter(4, par4)
      #fitNoSignal.SetParameter(5, par5)
      #labels.append("p2 = %.2f, p3=%.2f, p4=%.2f, p5=%.2f"%(par2, par3, par4, par5))
      #labels.append("BkgOnly: p2 = %.2f#pm%.2f, p3=%.2f#pm%.2f, p4=%.2f#pm%.2f, p5=%.2f#pm%.2f"%(par2BkgOnly, par2ErrBkgOnly, par3BkgOnly, par3ErrBkgOnly, par4BkgOnly, par4ErrBkgOnly, par5BkgOnly, par5ErrBkgOnly))


      histNoSignal = fitNoSignal.GetHistogram()
      histNoSignal.SetDirectory(0)
      print histNoSignal, fitNoSignal

      histNoSignal.Scale(fitHist.Integral() / histNoSignal.Integral())
    
      # This allows us to rebin the histograms using resolution binning, if we want
      if rebinedges:
        dataHist = dataHist.Rebin(len(rebinedges)-1, "dataHist_%s"%(infileName), array.array('d', rebinedges))
        fitHist = fitHist.Rebin(len(rebinedges)-1, "fitHist_%s"%(infileName), array.array('d', rebinedges))
        residualHist = residualHist.Rebin(len(rebinedges)-1, "residual_%s"%(infileName), array.array('d', rebinedges))
        histNoSignal = histNoSignal.Rebin(len(rebinedges)-1, "residual_%s"%(infileName), array.array('d', rebinedges))
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

      if index == 0:
        dataRes = residualHist.Clone("Residuals_zero")
        dataRes.Reset()
        dataRes.GetYaxis().SetRangeUser(-1.6, 1.6)
        dataRes.SetDirectory(0)
        residualHists.append(dataRes)
        dataHist.SetTitle(config.samples[channelName]["legend"])
        plotHists.append(dataHist)
        legNames.append(config.samples[channelName]["legend"])

      plotHists.append(fitHist)
      try:
        tmpName = config.fitFunctions[fitName]["Name"]
      except:
        tmpName = fitName
      legNames.append("#splitline{%s, S+B }{#chi^{2} / ndof = %.2f, p-val = %.2f}"%(tmpName, chi2, pval))


      print histNoSignal
      plotHists.append(histNoSignal)
      dataRes = histNoSignal.Clone("Residuals_zero2")
      #dataRes.Reset()
      dataRes.Add(dataHist,-1)
      dataRes.GetYaxis().SetRangeUser(-1.6, 1.6)
      dataRes.SetDirectory(0)
      residualHists.append(dataRes)
      legNames.append("#splitline{%s, S only }{#chi^{2} / ndof = %.2f, p-val = %.2f}"%(tmpName, chi2, pval))

      dataHists.append(dataHist)
      fitHists.append(fitHist)
      residualHists.append(residualHist)


    c.SetLogx()
    #df.SetRange(plotHists, minMin=1, maxMax=1e8, isLog=True)
    df.SetRange(plotHists, myMin=1e-5, myMax=1e5, isLog=True)
    outname = outfile.replace(".root", "")

    # Note: do not try to use Logx with this version of root (6.20.04), because it will fail.
    # For now, leave in linear, and if we can update the root version, we can also fix this
    #
    leg = df.DrawRatioHists(c, plotHists, residualHists, legNames, labels, "", drawOptions = ["e", "HIST", "HIST", "HIST", "HIST", "HIST"], outName=outname, isLogX = False, styleOptions = df.get_fit_style_opt, lumi=lumi, atlasLabel=atlasLabel, ratioDrawOptions = ["HIST", "HIST", "HIST", "HIST", "HIST"])
    #fitNoSignal.Draw("SAME")
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
