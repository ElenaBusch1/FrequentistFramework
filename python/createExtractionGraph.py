#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
import config as config
from array import array
from ROOT import *
from math import sqrt
from glob import glob
import ExtractFitParameters as efp
import numpy
#from color import getColorSteps
import DrawingFunctions as df
import AtlasStyle as AS
import LocalFunctions as lf



def createExtractionGraphs(sigmeans, sigwidths, sigamps, infile, infilePD, outfile, rangelow, rangehigh, channelName, cdir, lumi, atlasLabel="Simulation Internal", isNInjected=False, pdFile = None, signalName = "Gaussian"):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)
    ROOT.gErrorIgnoreLevel = (ROOT.kInfo + 1)

    profile_list = []
    c = df.setup_canvas()

    for j,sigmean in enumerate(sigmeans):
      for i,sigwidth in enumerate(sigwidths):
        g_allPoints = TGraph()
        g_profile   = TGraphErrors()

        h_nsigs = []
        legs = []
        for k,sigamp in enumerate(sigamps):
          print sigmean, sigwidth, sigamp
          h_nsig = ROOT.TH1D("nsig_%d_%d_%d"%(sigmean, sigwidth, sigamp), ";N_{sig, extracted};# toys, normalised", 50,  0, 10)
          h_nsig.SetDirectory(0)


          inj_extr = []
          nans = 0

          tmp_path_fitresult = config.getFileName(infile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"

          for toy in range(config.nToys):
              if sigamp > 0:
                try:
                  fpe = efp.FitParameterExtractor(tmp_path_fitresult)
                  fpe.suffix = "%d"%(toy)
                  fpe.ExtractFromFile( "%d"%(toy))
                  #fpe.suffix = "_%d"%(toy)
                  #fpe.ExtractFromFile( "_%d"%(toy))
                  nsig = fpe.GetNsig()
                except:
                  #print "Couldn't read nsig from", tmp_path_fitresult, fpe.suffix
                  continue
              else:
                nsig = 0

              if nsig == None or  math.isnan(nsig):
                nans += 1
              if nsig == None:
                continue

              postFit = tmp_path_fitresult.replace("FitParameters", "PostFit")
              suffix = "%d"%(toy)
              chi2Hist = lf.read_histogram(postFit, "chi2"+suffix)
              pval = chi2Hist.GetBinContent(6)


              if pval < 0.10:
                continue
   
              if pdFile == None:
                #print "no file path given", 
                tmp_path_injection = config.getFileName(infilePD, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + "_Sig_%s.root"%(signalName)
              else: 
                tmp_path_injection = pdFile.replace("AMP","%d"%sigamp);
              checkPath = glob(tmp_path_injection)
              if len(checkPath) == 0:
                  print "Did not find ", tmp_path_injection
                  continue

              nBkg = fpe.GetNbkg()
              sqrtB = sqrt(nBkg)
              

              f = TFile(tmp_path_injection)
              h = f.Get("pseudodata_%d_injection"%(toy))
              #h = f.Get("h_pseudo%d_injection"%(toy))
              n_injected = h.Integral(0, h.GetNbinsX()+1)
              print n_injected, nsig, nBkg, pval
              #print n_injected*0.762, nsig*0.762, nBkg

              if sqrtB == 0:
                 sqrtB = 1

              #inj_extr.append((n_injected, nsig/0.762, sqrtB))
              inj_extr.append((n_injected, nsig*0.762, sqrtB))
              #inj_extr.append((n_injected, nsig, sqrtB))
              #inj_extr.append((n_injected, n_injected*0.762, sqrtB))

          if len(inj_extr)==0:
              print "Nothing found"
              continue
          
          if len(inj_extr) > 0:
              for t in inj_extr:
                  g_allPoints.SetPoint(g_allPoints.GetN(), t[0], t[1])

          arr = numpy.array([x[1] for x in inj_extr])
          nFit = numpy.mean(arr)
          nFitErr = numpy.std(arr, ddof=1) #1/N-1 corrected
          print nFit, len(arr)

          for i in range(len(inj_extr)):
            h_nsig.Fill(inj_extr[i][1] /  inj_extr[i][2])
          h_nsigs.append(h_nsig)

          g_profile.SetPoint(g_profile.GetN(), sigamp, nFit / sqrtB)
          g_profile.SetPointError(g_profile.GetN()-1, 0, nFitErr / sqrtB)
          legs.append("Signal amplitude = %d, average = %.2f"%(sigamp, nFit/sqrtB))


        df.SetRange(h_nsigs, myMin=0)
        leg = df.DrawHists(c, h_nsigs, legs, [], sampleName = "", drawOptions = ["HIST"], styleOptions=df.get_extraction_style_opt, isLogX=0, lumi=lumi, atlasLabel=atlasLabel)
        outfileNameTmp = config.getFileName("NsigDistributions_" + outfile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) 
        c.Print("%s.pdf"%(outfileNameTmp))

        g_allPoints.SetTitle("%d GeV Gauss (%d%%)" % (sigmean, sigwidth))

        g_profile.SetTitle("%d GeV Gauss (%d%%)" % (sigmean, sigwidth))
        g_profile.GetXaxis().SetTitle("Injected N_{sig} / #sqrt{N_{bkg}}")
        g_profile.GetYaxis().SetTitle("Extracted N_{sig} / #sqrt{N_{bkg}}")
        g_profile.GetXaxis().SetLimits(-0.5, max(sigamps)+0.5)
        g_profile.SetMinimum(-0.5)
        g_profile.SetMaximum(max(sigamps)+4)

        profile_list.append(g_profile)


    labels = ["Pseudodata"]
    outfileName = config.getFileName(outfile, cdir, channelName, rangelow, rangehigh) + "_sigwidth_%d"%sigwidth + ".pdf"
    legendNames = []
    for i in profile_list:
      legendNames.append(i.GetTitle())
    leg = df.DrawHists(c, profile_list, legendNames, labels, sampleName = "", drawOptions = ["ALP", "LP", "LP", "LP", "LP", "LP", "LP"], styleOptions=df.get_extraction_style_opt, isLogX=0, atlasLabel=atlasLabel, lumi=lumi)

    l = TLine(-0.5,-0.5,max(sigamps)+0.5, max(sigamps)+0.5)
    l.SetLineColor(kGray+2)
    l.SetLineStyle(7)
    l.Draw()
    print outfileName

    c.Print(outfileName)


def main(args):
    SetAtlasStyle()
 
    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--infile', dest='infile', type=str, default='jjj/FitResult_sigPlusBkg_Fit_300_1200_Sig_MEAN_width_WIDTH_amp_AMP_*.root', help='Input FitResult paths')
    parser.add_argument('--infilePD', dest='infilePD', type=str, default='run/PD_swift_fivePar_bkgonly_range_300_1200_injected_meanMEAN_widthWIDTH_ampAMP.root', help='Input FitResult paths')
    parser.add_argument('--outfile', dest='outfile', type=str, default='extractionGraphs.root', help='Output file name')
    
    args = parser.parse_args(args)

    sigmeans=[ 550]
    sigwidths=[ 7 ]
    sigamps=[1, 5, 10 ]


    createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=args.infile, infilePD=args.infilePD, outfile=args.outfile)

    
if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   

