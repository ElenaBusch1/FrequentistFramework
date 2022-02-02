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
import config as config

ROOT.gROOT.SetBatch(ROOT.kTRUE)


def spuriousSignal(sigmeans, sigwidths, infile, infilePD, outfile, rangelow, rangehigh, channelName, cdir, atlasLabel="Simulation Internal"):

    h_allPoints_list = []
    sigmeansExists = []

    for j,sigmean in enumerate(sigmeans):
        for i,sigwidth in enumerate(sigwidths):
            h_allPoints = TH1F("spuriousSignal_%d_%d"%(sigmean, sigwidth), ";nsig;No. of toys", 80, -20000, 20000)
            h_allPoints.SetDirectory(0)

            tmp_path_fitresult = config.getFileName(infile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
            tmp_path_fitresults = glob(tmp_path_fitresult)

            if len(tmp_path_fitresults) == 0:
                print "No fit results for ", sigmean, sigwidth, tmp_path_fitresult
                continue
            sigmeansExists.append(sigmean)

            for path in tmp_path_fitresults:
              fpe = efp.FitParameterExtractor(path)
              for toy in range(config.nToys):
                try:
                    fpe.suffix = "_%d"%(toy)
                    fpe.ExtractFromFile( "_%d"%(toy))
                    nsig = fpe.GetNsig()
                except:
                    print "Couldn't read nsig from", path
                    continue

                if nsig == None or  math.isnan(nsig):
                    continue

                h_allPoints.Fill(nsig)

            h_allPoints_list.append(h_allPoints)


    # Plotting:
    c = df.setup_canvas()


    graphs = []
    legendNames = []
    for sigwidth in sigwidths:
       g_avg = TGraphErrors()
       g_avg.SetTitle("#sigma / m = %.2d"%sigwidth)
       g_avg.GetXaxis().SetTitle("m_{jj}")
       g_avg.GetYaxis().SetTitle("<N_{sig}>")
       for sigmean, i in zip(sigmeansExists, range(len(sigmeansExists))):
         n = g_avg.GetN()
         g_avg.SetPoint(n, sigmean, h_allPoints_list[i].GetMean())
         g_avg.SetPointError(n, 0.001, h_allPoints_list[i].GetStdDev())
       graphs.append(g_avg)
       legendNames.append("#sigma / m = %.2d"%sigwidth)

         

    outfileName = config.getFileName(outfile + "Test", cdir, channelName, rangelow, rangehigh) + ".pdf"
    leg = df.DrawHists(c, graphs, legendNames, [], sampleName = "", drawOptions = ["AP", "P"], styleOptions=df.get_finalist_style_opt, isLogX=0)
    c.Print(outfileName)


    legendNames = []
    for mean in sigmeansExists:
      legendNames.append("m_{Z'} = %d"%mean)
 
    outfileName = config.getFileName("SpuriousSignal", cdir, channelName, rangelow, rangehigh) + ".pdf"
    df.SetRange(h_allPoints_list, myMin=0)
    df.SetStyleOptions(h_allPoints_list, df.get_finalist_style_opt)
    leg = df.DrawHists(c, h_allPoints_list, legendNames, [], sampleName = "", drawOptions = ["HIST", "HIST"], styleOptions=df.get_finalist_style_opt, isLogX=0)
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


    createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=args.infile, infilePD=args.infilePD, outfile=args.outfile)

    
if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   

