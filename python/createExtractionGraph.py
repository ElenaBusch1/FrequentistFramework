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

ROOT.gROOT.SetBatch(ROOT.kTRUE)

gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")


def createExtractionGraphs(sigmeans, sigwidths, sigamps, infile, infilePD, outfile, rangelow, rangehigh, channelName, cdir, lumi, atlasLabel="Simulation Internal"):
    colors = getColorSteps(len(sigmeans))
    fout = TFile(outfile, "RECREATE")

    profile_list = []
    allPoints_list = []

    for j,sigmean in enumerate(sigmeans):


        for i,sigwidth in enumerate(sigwidths):
            g_allPoints = TGraph()
            g_profile   = TGraphErrors()

            sqrtB = None
            for k,sigamp in enumerate(sigamps):
                chi2s = []
                pvals = []

                #find number of injected events:

                if sigamp > 0:
                    tmp_path_injection = infilePD
                    tmp_path_injection = config.getFileName(infilePD, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + "*.root"
                    tmp_path_injections = glob(tmp_path_injection)

                    if len(tmp_path_injections) == 0:
                        print "No injection paths for", tmp_path_injection, infilePD, sigmean, sigwidth, sigamp
                        continue

                    f = TFile(tmp_path_injections[0])
                    h = f.Get("pseudodata_0_injection")
                    n_injected = h.Integral(0, h.GetNbinsX()+1)
                    f.Close()
                else:
                    n_injected = 0


                tmp_path_fitresult = infile
                tmp_path_fitresult = config.getFileName(infile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + "*.root"
                tmp_path_fitresults = glob(tmp_path_fitresult)
                if len(tmp_path_fitresults) == 0:
                    print "No fit results for ", tmp_path_fitresult
                    continue

                inj_extr = []
                nans = 0

                for path in tmp_path_fitresults:
                  for toy in range(config.nToys):
                    try:
                      path2 = path.replace("FitParameters", "PostFit")
                      f2 = TFile(path2)
                      chi2Hist = f2.Get("chi2_%d"%(toy))
                      chi2 = chi2Hist.GetBinContent(2)
                    except:
                      continue
                    pval = chi2Hist.GetBinContent(6)
                    f2.Close()
                    chi2s.append(chi2)
                    pvals.append(pval)
                   
                    fpe = efp.FitParameterExtractor(path)
                    fpe.suffix = "_%d"%(toy)
                    fpe.ExtractFromFile( "_%d"%(toy))
                    try:
                        nsig = fpe.GetNsig()
                    except:
                        print "Couldn't read nsig from", path
                        continue

                    #print n_injected, nsig
                    if nsig == None or  math.isnan(nsig):
                        nans += 1
                    if nsig == None:
                        nsig = -1
                        #continue

                    inj_extr.append((n_injected, nsig))

                print "n_injected: %d,   NaNs: %d" % (n_injected, nans)
                if float(nans) / len(inj_extr) < 0.02:
                    for t in inj_extr:
                        g_allPoints.SetPoint(g_allPoints.GetN(), t[0], t[1])

                arr = numpy.array([x[1] for x in inj_extr])
                nFit = numpy.mean(arr)
                nFitErr = numpy.std(arr, ddof=1) #1/N-1 corrected

                if sqrtB == None:
                    sqrtB = (n_injected / sigamp) if sigamp != 0 else 1

                g_profile.SetPoint(g_profile.GetN(), sigamp, nFit / sqrtB)
                g_profile.SetPointError(g_profile.GetN()-1, 0, nFitErr / sqrtB)


            fout.cd()
            g_allPoints.SetTitle("%d GeV Gauss (%d%%)" % (sigmean, sigwidth))
            g_allPoints.Write("g1_extraction_gauss_%d_%d" % (sigmean, sigwidth))

            g_profile.SetTitle("%d GeV Gauss (%d%%)" % (sigmean, sigwidth))
            g_profile.Write("g1_profile_gauss_%d_%d" % (sigmean, sigwidth))

            allPoints_list.append(g_allPoints)
            profile_list.append(g_profile)

    fout.Close()

    # Plotting:
    c = df.setup_canvas()
    mg = TMultiGraph()

    for i,g in enumerate(profile_list):
        g.SetLineWidth(2)
        g.SetLineColor(colors[i])
        g.SetMarkerColor(colors[i])
        mg.Add(g, "")

    mg.Draw("APL")
    mg.GetXaxis().SetTitle("Injected N_{sig} / #sqrt{N_{bkg}}")
    mg.GetYaxis().SetTitle("Extracted N_{sig} / #sqrt{N_{bkg}}")
    mg.GetXaxis().SetLimits(-0.5, max(sigamps)+0.5)
    mg.SetMinimum(-0.5)
    mg.SetMaximum(max(sigamps)+4)
    c.Update()

    c.BuildLegend(0.2,0.54,0.5,0.78)

    l = TLine(-0.5,-0.5,max(sigamps)+0.5, max(sigamps)+0.5)
    l.SetLineColor(kGray+2)
    l.SetLineStyle(7)
    l.Draw()

    text1 = "Pseudodata %d fb^{-1}" % (lumi/1000.)

    text2 = "global fit"
    if "four" in  infile:
        text2 += " 4 par"
    if "five" in  infile:
        text2 += " 5 par"
    if "nloFit" in infile:
        text2 = "NLOFit"

    text = text1 + ", " + text2

    myText(0.2, 0.82, 1, text)
    AS.ATLASLabel(0.15, 0.9, 1, 0.15, 0.05, atlasLabel)

    outfileName = config.getFileName(outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"
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

