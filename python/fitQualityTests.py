# This code tests the variation in the fits of the pseudodata.

#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from ROOT import *
import math
import config as config
import DrawingFunctions as df
import ExtractFitParameters as efp




def fitQualityTests(pdfile, nominalname, fitFunction1File, fitFunction2File, outfile, ntoys, rangelow, rangehigh, lumi, sigmean, sigwidth, sigamp, cdir, channelName, fitName = ""):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    nominalFileName = config.getFileName(nominalname, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
    nominalFile = ROOT.TFile(nominalFileName, "READ")

    nominalFit = nominalFile.Get("postfit_0")
    nominalFit.SetDirectory(0)

    tmpError = nominalFit.Clone("tmpError")
    relError = nominalFit.Clone("RelError")
    relError.SetDirectory(0)
    relError.GetXaxis().SetTitle("m_{jj}")


    #toyName = config.getFileName(pdfile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
    h_pars = []
    configName = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/" + config.fitFunctions[fitName]["Config"]

    with open(configName) as f:
      lines = f.readlines()
      configFile = lines[2]

    parNum = 1 
    while configFile.find("p%d"%(parNum)) >= 0:
      index1 = configFile.find("p%d["%(parNum))
      substr1 = configFile[index1:-1]
      substr2 = substr1[3:substr1.find("]")]
      substr3 = substr2[substr2.find(",")+1:]
      substr4 = substr3[0:substr3.find(",")]
      substr5 = substr3[substr3.find(",")+1:]
      pMin = float(substr4)
      pMax = float(substr5)
      if pMin < pMax:
        h_p = TH1F("p%d_%d_%d"%(parNum, sigmean, sigwidth), "p%d;p%d;No. of toys"%(parNum,parNum), 80, pMin, pMax)
        h_p.SetDirectory(0)
        h_pars.append(h_p)

      parNum += 1



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

       efpName = pdfile.replace("PostFit", "FitParameters")
       tmp_path_fitBkg = config.getFileName(efpName, cdir, channelName, rangelow, rangehigh, 0) + ".root"
       fpeBkg = efp.FitParameterExtractor(tmp_path_fitBkg)
       try:
         fpeBkg.suffix = "_%d"%(toy)
         fpeBkg.ExtractFromFile( "_%d"%(toy))
         params = fpeBkg.GetH1Params()
       except:
         continue

       for parIndex in range(len(h_pars)):
         h_pars[parIndex].Fill(params.GetBinContent(2+parIndex))



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


    c = df.setup_canvas("canvas")
    relError.GetYaxis().SetRangeUser(-0.03, 0.03)
    leg = df.DrawHists(c, [relError, relErrorFit], ["Stat uncertainty on fit", "Function choice"], [], drawOptions = ["ex0"], styleOptions=df.get_extraction_style_opt, isLogX=0)
    path = config.getFileName(outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"
    c.Print(path)

    for h_par in h_pars:
      leg = df.DrawHists(c, [h_par], ["Bkg-only fits"], [], drawOptions = ["hist"], styleOptions=df.get_extraction_style_opt, isLogX=0)
      path = config.getFileName(h_par.GetTitle(), cdir, channelName, rangelow, rangehigh) + ".pdf"
      c.Print(path)





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
