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


def createExtractionGraphs(sigmeans, sigwidths, sigamps, infile, infilePD, outfile, rangelow, rangehigh, channelName, cdir, atlasLabel="Simulation Internal"):
    # # colors = [kBlue, kRed+1, kOrange-3]
    # colors = [kMagenta+3, kRed+1, kOrange-3, kSpring+5, kTeal+5, kCyan-1, kAzure-6]
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

                #find number of injected events:

                if sigamp > 0:
                    tmp_path_injection = infilePD
                    tmp_path_injection = config.getFileName(infilePD, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + "*.root"
                    #print tmp_path_injection
                    tmp_path_injection = glob(tmp_path_injection)

                    if len(tmp_path_injection) == 0:
                        print "No injection paths"
                        continue

                    f = TFile(tmp_path_injection[0])
                    #print tmp_path_injection[0]
                    h = f.Get("pseudodata_0_injection")
                    n_injected = h.Integral(0, h.GetNbinsX()+1)
                    f.Close()
                else:
                    n_injected = 0


                tmp_path_fitresult = infile
                tmp_path_fitresult = config.getFileName(infile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + "*.root"
                #print tmp_path_fitresult
                tmp_path_fitresult = glob(tmp_path_fitresult)
                if len(tmp_path_fitresult) == 0:
                    print "No fit results"
                    continue

                inj_extr = []
                nans = 0

                for path in tmp_path_fitresult:
                    fpe = efp.FitParameterExtractor(path)
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
                        continue

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


                #print (sigamp, nFit, sqrtB, nFit/sqrtB)
                g_profile.SetPoint(g_profile.GetN(), sigamp, nFit / sqrtB)
                g_profile.SetPointError(g_profile.GetN()-1, 0, nFitErr / sqrtB)

                # print "Setting point at", sigamp, nFit / sqrtB

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
    # mg.GetYaxis().SetLimits(-0.5, 15)
    mg.SetMinimum(-0.5)
    mg.SetMaximum(max(sigamps)+3)
    c.Update()

    c.BuildLegend(0.2,0.54,0.5,0.78)

    l = TLine(-0.5,-0.5,max(sigamps)+0.5, max(sigamps)+0.5)
    l.SetLineColor(kGray+2)
    l.SetLineStyle(7)
    l.Draw()

    lumi = 29
    if "lumi" in infile:
        try:
            lumi=int(infile.split("lumi")[-1].split("_")[0])
        except:
            pass
    text1 = "Pseudodata %d fb^{-1}" % lumi

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


    # raw_input("enter")

    outfileName = config.getFileName(outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"
    c.Print(outfileName)


def main(args):
    SetAtlasStyle()
 
    parser = argparse.ArgumentParser(description='%prog [options]')
    #parser.add_argument('--infile', dest='infile', type=str, default='/data/scratch/users/bartels/FarmOutput/TLA/quickFit_injections_globalFit_fivepar_lumi29_201202/quickFit_globalFit_J100_${MEAN}_${WIDTH}_${AMP}_sbFit/output.*/run/FitResult_*.root', help='Input FitResult paths')
    #parser.add_argument('--infilePD', dest='infilePD', type=str, default='/data/scratch/users/bartels/FarmOutput/TLA/quickFit_injections_globalFit_fivepar_lumi29_201202/quickFit_globalFit_J100_${MEAN}_${WIDTH}_${AMP}_sbFit/output.*/run/FitResult_*.root', help='Input FitResult paths')
    parser.add_argument('--infile', dest='infile', type=str, default='jjj/FitResult_sigPlusBkg_Fit_300_1200_Sig_MEAN_width_WIDTH_amp_AMP_*.root', help='Input FitResult paths')
    parser.add_argument('--infilePD', dest='infilePD', type=str, default='run/PD_swift_fivePar_bkgonly_range_300_1200_injected_meanMEAN_widthWIDTH_ampAMP.root', help='Input FitResult paths')
    parser.add_argument('--outfile', dest='outfile', type=str, default='extractionGraphs.root', help='Output file name')
    
    args = parser.parse_args(args)

    # sigmeans=[ 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1300, 1400, 1500, 1600, 1700, 1800, ]
    # sigwidths=[ 5, 7, 10, 12, 15, ]
    # sigmeans=[ 700, 800, 1000, 1200]
    #sigmeans=[ 700, 1000, 1400, 1800]
    sigmeans=[ 550]
    # sigmeans=[ 1000 ]
    sigwidths=[ 7 ]
    # sigamps=[ 0, 3, 5, 7, 10 ]
    # sigamps=[ 10, 7, 5, 3, 0 ]
    #sigamps=[ 5, 4, 3, 2, 1, 0 ]
    sigamps=[1, 5, 10 ]


    createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=args.infile, infilePD=args.infilePD, outfile=args.outfile)

    
if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   

