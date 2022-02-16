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
from color import getColorSteps
import DrawingFunctions as df
import AtlasStyle as AS



def createExtractionGraphs(sigmeans, sigwidths, sigamps, infile, infilePD, outfile, rangelow, rangehigh, channelName, cdir, lumi, atlasLabel="Simulation Internal"):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    profile_list = []
    allPoints_list = []
    c = df.setup_canvas()

    for j,sigmean in enumerate(sigmeans):
        for i,sigwidth in enumerate(sigwidths):
            g_allPoints = TGraph()
            g_profile   = TGraphErrors()

            sqrtB = None

            h_nsigs = []
            legs = []
            for k,sigamp in enumerate(sigamps):
                h_nsig = ROOT.TH1D("nsig_%d_%d_%d"%(sigmean, sigwidth, sigamp), ";N_{sig, extracted};# toys, normalised", 50,  0, 10)
                h_nsig.SetDirectory(0)
                chi2s = []
                pvals = []

                #find number of injected events:

                if sigamp > 0:
                    tmp_path_injection = infilePD
                    tmp_path_injection = config.getFileName(infilePD, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"

                    checkPath = glob(tmp_path_injection)
                    if len(checkPath) == 0:
                        continue

                    f = TFile(tmp_path_injection)
                    try:
                      h = f.Get("pseudodata_0_injection")
                      n_injected = h.Integral(0, h.GetNbinsX()+1)
                    except:
                      f.Close()
                      continue
                    f.Close()
                else:
                    n_injected = 0


                tmp_path_fitresult = config.getFileName(infile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"

                inj_extr = []
                pvals = []
                nans = 0

                for toy in range(config.nToys):
                    try:
                      path2 = tmp_path_fitresult.replace("FitParameters", "PostFit")
                      checkPath = glob(path2)
                      if len(checkPath) == 0:
                        continue

                      f2 = TFile(path2)
                      chi2Hist = f2.Get("chi2_%d"%(toy))
                      chi2 = chi2Hist.GetBinContent(2)
                    except:
                      continue
                    pval = chi2Hist.GetBinContent(6)
                    f2.Close()
                    chi2s.append(chi2)
                    if(pval < 0.01):
                      continue
                   
                    fpe = efp.FitParameterExtractor(tmp_path_fitresult)
                    fpe.suffix = "_%d"%(toy)
                    fpe.ExtractFromFile( "_%d"%(toy))
                    try:
                        nsig = fpe.GetNsig()
                    except:
                        #print "Couldn't read nsig from", tmp_path_fitresult
                        continue

                    if nsig == None or  math.isnan(nsig):
                        nans += 1
                    if nsig == None:
                        continue

                    inj_extr.append((n_injected, nsig))
                    pvals.append(pval)

                print "n_injected: %d,   NaNs: %d" % (n_injected, nans)
                
                if len(inj_extr) > 0 and  float(nans) / len(inj_extr) < 0.02:
                    for t in inj_extr:
                        g_allPoints.SetPoint(g_allPoints.GetN(), t[0], t[1])

                arr = numpy.array([x[1] for x in inj_extr])
                nFit = numpy.mean(arr)
                nFitErr = numpy.std(arr, ddof=1) #1/N-1 corrected

                if sqrtB == None:
                    sqrtB = (n_injected / sigamp) if sigamp != 0 else 1

                for i in range(len(inj_extr)):
                  h_nsig.Fill(inj_extr[i][1]/sqrtB)

                g_profile.SetPoint(g_profile.GetN(), sigamp, nFit / sqrtB)
                g_profile.SetPointError(g_profile.GetN()-1, 0, nFitErr / sqrtB)
                h_nsigs.append(h_nsig)
                legs.append("Signal amplitude = %d, average = %.2f"%(sigamp, nFit/sqrtB))


            leg = df.DrawHists(c, h_nsigs, legs, [], sampleName = "", drawOptions = ["HIST"], styleOptions=df.get_extraction_style_opt, isLogX=0, lumi=lumi, atlasLabel=atlasLabel)
            outfileNameTmp = config.getFileName("NsigDistributions_" + outfile, cdir, channelName, rangelow, rangehigh) 
            c.Print("%s.pdf"%(outfileNameTmp))

            g_allPoints.SetTitle("%d GeV Gauss (%d%%)" % (sigmean, sigwidth))

            g_profile.SetTitle("%d GeV Gauss (%d%%)" % (sigmean, sigwidth))
            g_profile.GetXaxis().SetTitle("Injected N_{sig} / #sqrt{N_{bkg}}")
            g_profile.GetYaxis().SetTitle("Extracted N_{sig} / #sqrt{N_{bkg}}")
            g_profile.GetXaxis().SetLimits(-0.5, max(sigamps)+0.5)
            g_profile.SetMinimum(-0.5)
            g_profile.SetMaximum(max(sigamps)+4)

            allPoints_list.append(g_allPoints)
            profile_list.append(g_profile)


    text1 = "Pseudodata"
    labels = [text1]
    outfileName = config.getFileName(outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"
    legendNames = []
    for i in profile_list:
      legendNames.append(i.GetTitle())
    leg = df.DrawHists(c, profile_list, legendNames, labels, sampleName = "", drawOptions = ["ALP", "LP", "LP", "LP", "LP"], styleOptions=df.get_extraction_style_opt, isLogX=0, atlasLabel=atlasLabel, lumi=lumi)

    l = TLine(-0.5,-0.5,max(sigamps)+0.5, max(sigamps)+0.5)
    l.SetLineColor(kGray+2)
    l.SetLineStyle(7)
    l.Draw()

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

