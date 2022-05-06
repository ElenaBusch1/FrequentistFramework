#!/usr/bin/env python

# This script does some checks of the pulls of the fit

import ROOT
import sys, re, os, math, argparse
import DrawingFunctions as df
import python.AtlasStyle as AS
import array
import config as config


def stitchSwift(infiles, outfile, minMjj, maxMjj, lumi, cdir, channelName, rebinedges=None, atlasLabel="Simulation Internal", minMasses = [], maxMasses = [], fithistName="postfit", suffix=""):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    print minMjj, maxMjj
    for index, infileName in zip(range(len(infiles)), infiles):
      hFull = ROOT.TH1F("hFull", "", (maxMjj-minMjj), minMjj, maxMjj)
      hData = ROOT.TH1F("hData", "", (maxMjj-minMjj), minMjj, maxMjj)
      hFull.SetDirectory(0)
      hData.SetDirectory(0)

      for minMass, maxMass, massIndex in zip(minMasses, maxMasses, range(len(maxMasses))):
        path = config.getFileName(infileName, cdir, channelName, minMass, maxMass) + ".root"

        inFile = ROOT.TFile(path, "READ")
        if not inFile:
          print "Did not find file ", path
  
        inFile.Print()
        fitHist = inFile.Get(fithistName + suffix)
        dataHist = inFile.Get("data" + suffix)


        deltaMass = 10
        cRange = deltaMass 
        for i in range(cRange):
          cMass = minMass + int((maxMass - minMass)/2) + i  - cRange + 0.5
          print cMass, (i*1.0/cRange)
          cBin = fitHist.FindBin(cMass)
          cBinFull = hFull.FindBin(cMass)
          cBinData = dataHist.FindBin(cMass)
          hFull.Fill(cMass, fitHist.GetBinContent(cBin)*(i*1.0/cRange))
          hData.SetBinContent(cBinFull, dataHist.GetBinContent(cBinData))
          hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))

        for i in range(cRange):
          cMass = minMass + int((maxMass - minMass)/2) + i  + 0.5
          cBin = fitHist.FindBin(cMass)
          cBinFull = hFull.FindBin(cMass)
          cBinData = dataHist.FindBin(cMass)
          print cMass, (1.-i*1.0/cRange)
          hFull.Fill(cMass, fitHist.GetBinContent(cBin)*(1.-i*1.0/cRange))
          hData.SetBinContent(cBinFull, dataHist.GetBinContent(cBinData))
          hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))

        #if massIndex == 0:
        #  for i in range(int((maxMass - minMass)/2)):
        #    cMass = minMass + i + 0.5
        #    cBin = fitHist.FindBin(cMass)
        #    cBinData = dataHist.FindBin(cMass)
        #    hFull.SetBinContent(i+1, fitHist.GetBinContent(cBin))
        #    hData.SetBinContent(i+1, dataHist.GetBinContent(cBinData))
        #    hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))

        #if massIndex == len(minMasses)-1:
        #  for i in range(int((maxMass - minMass)/2)):
        #    cMass = minMass + (maxMass - minMass)/2 + i + 0.5
        #    cBin = fitHist.FindBin(cMass)
        #    cBinFull = hFull.FindBin(cMass)
        #    cBinData = dataHist.FindBin(cMass)
        #    hFull.SetBinContent(cBinFull, fitHist.GetBinContent(cBin))
        #    hData.SetBinContent(cBinFull, dataHist.GetBinContent(cBinData))
        #    hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))






        '''
        cRange = int((maxMass - minMass)/2)
        for i in range(int((maxMass - minMass)/2)):
          cMass = minMass + i + 0.5
          cBin = fitHist.FindBin(cMass)
          cBinFull = hFull.FindBin(cMass)
          cBinData = dataHist.FindBin(cMass)
          hFull.SetBinContent(cBinFull, fitHist.GetBinContent(cBin))
          hData.SetBinContent(cBinFull, dataHist.GetBinContent(cBinData))
          hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))

        if massIndex == 0:
          for i in range(int((maxMass - minMass)/2)):
            cMass = minMass + i + 0.5
            cBin = fitHist.FindBin(cMass)
            cBinData = dataHist.FindBin(cMass)
            hFull.SetBinContent(i+1, fitHist.GetBinContent(cBin))
            hData.SetBinContent(i+1, dataHist.GetBinContent(cBinData))
            hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))

        if massIndex == len(minMasses)-1:
          for i in range(int((maxMass - minMass)/2)):
            cMass = minMass + (maxMass - minMass)/2 + i + 0.5
            cBin = fitHist.FindBin(cMass)
            cBinFull = hFull.FindBin(cMass)
            cBinData = dataHist.FindBin(cMass)
            hFull.SetBinContent(cBinFull, fitHist.GetBinContent(cBin))
            hData.SetBinContent(cBinFull, dataHist.GetBinContent(cBinData))
            hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))
        '''





        '''
 

        cRange = int((maxMass - minMass)/2)
        for i in range(int((maxMass - minMass)/2)):
          cMass = minMass + i + 0.5
          cBin = fitHist.FindBin(cMass)
          cBinFull = hFull.FindBin(cMass)
          cBinData = dataHist.FindBin(cMass)
          hFull.Fill(cMass, fitHist.GetBinContent(cBin)*(i*1.0/cRange))
          hData.SetBinContent(cBinFull, dataHist.GetBinContent(cBinData))
          hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))

        for i in range(int((maxMass - minMass)/2)):
          cMass = minMass + (maxMass - minMass)/2 + i + 0.5
          cBin = fitHist.FindBin(cMass)
          cBinFull = hFull.FindBin(cMass)
          cBinData = dataHist.FindBin(cMass)
          hFull.Fill(cMass, fitHist.GetBinContent(cBin)*((cRange-i)*1.0/cRange))
          hData.SetBinContent(cBinFull, dataHist.GetBinContent(cBinData))
          hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))


        if massIndex == 0:
          for i in range(int((maxMass - minMass)/2)):
            cMass = minMass + i + 0.5
            cBin = fitHist.FindBin(cMass)
            cBinData = dataHist.FindBin(cMass)
            hFull.SetBinContent(i+1, fitHist.GetBinContent(cBin))
            hData.SetBinContent(i+1, dataHist.GetBinContent(cBinData))
            hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))

        if massIndex == len(minMasses)-1:
          for i in range(int((maxMass - minMass)/2)):
            cMass = minMass + (maxMass - minMass)/2 + i + 0.5
            cBin = fitHist.FindBin(cMass)
            cBinFull = hFull.FindBin(cMass)
            cBinData = dataHist.FindBin(cMass)
            hFull.SetBinContent(cBinFull, fitHist.GetBinContent(cBin))
            hData.SetBinContent(cBinFull, dataHist.GetBinContent(cBinData))
            hData.SetBinError(cBinFull, dataHist.GetBinError(cBinData))


        '''

      chi2 = 0.
      chi2bins = 0

      for ibin in range(hData.GetNbinsX()):
          binCenter = hData.GetBinCenter(ibin+1)

          valueErrorData = hData.GetBinError(ibin+1)
          valueData = hData.GetBinContent(ibin+1)
          postFitValue = hFull.GetBinContent(ibin+1)

          binSig = 0.
          if valueErrorData > 0. and postFitValue > 0.:
              binSig = (valueData - postFitValue)/valueErrorData

              chi2bins += 1
              chi2 += binSig*binSig

      print chi2, chi2bins-3, chi2/(chi2bins-3), ROOT.Math.chisquared_cdf_c(chi2, chi2bins-3)

      #npars = getNPars(pdfi, x, exclSyst=True)

      #if self.externalchi2file and self.externalchi2fct:
      #    f_chi2 = TFile(self.externalchi2file)
      #    tf1_chi2 = f_chi2.Get(self.externalchi2fct)
      #    ndof = chi2bins - self.externalchi2bins + tf1_chi2.GetParameter(0)
      #    f_chi2.Close()
      #else:
      #    ndof = chi2bins - npars




    inFile.Close()
    outfileName = config.getFileName("PostFit_fullSwift_bkgonly", cdir, channelName, minMjj, maxMjj) + ".root"
    outfile = ROOT.TFile(outfileName, "RECREATE")
    outfile.cd()
    hFull.Write("postfit")
    hData.Write("data")
    hRes = hData.Clone("residuals")
    hErr = hData.Clone("err")
    hErr.Reset()
    for i in range(hData.GetNbinsX()):
       hErr.SetBinContent(i+1, hData.GetBinError(i+1))
  
    hRes.Add(hFull, -1)
    hRes.Divide(hErr)
    hRes.Write("residuals")
    outfile.Close()




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
