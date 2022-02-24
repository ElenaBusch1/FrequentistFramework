#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
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



def spuriousSignal(sigmeans, sigwidths, infile, infilePD, outfile, rangelow, rangehigh, channelName, cdir, atlasLabel="Simulation Internal", bkgOnlyFitFile = None):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    h_allPoints_list = []
    h_p1_list = []
    h_p2_list = []
    h_p3_list = []
    h_p4_list = []
    h_p5_list = []
    sigmeansExists = []

    minMean = min(sigmeans)
    maxMean = max(sigmeans)

    for j,sigmean in enumerate(sigmeans):
        for i,sigwidth in enumerate(sigwidths):
            h_allPoints = TH1F("spuriousSignal_%d_%d"%(sigmean, sigwidth), ";N_{extracted signal};No. of toys", 50, -30000, 30000)
            h_p1 = TH1F("p1_%d_%d"%(sigmean, sigwidth), ";p1;No. of toys", 80, 12000, 15000)
            h_p2 = TH1F("p2_%d_%d"%(sigmean, sigwidth), ";p2;No. of toys", 80, 0, 100)
            h_p3 = TH1F("p3_%d_%d"%(sigmean, sigwidth), ";p3;No. of toys", 80, -5, 10)
            h_p4 = TH1F("p4_%d_%d"%(sigmean, sigwidth), ";p4;No. of toys", 80, -1, 3)
            h_p5 = TH1F("p5_%d_%d"%(sigmean, sigwidth), ";p5;No. of toys", 80, -0.5, 1)
            h_allPoints.SetDirectory(0)
            h_p1.SetDirectory(0)
            h_p2.SetDirectory(0)
            h_p3.SetDirectory(0)
            h_p4.SetDirectory(0)
            h_p5.SetDirectory(0)

            tmp_path_fitresult = config.getFileName(infile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
            tmp_path_fitresults = glob(tmp_path_fitresult)

            if len(tmp_path_fitresults) == 0:
                print "No fit results for ", sigmean, sigwidth, tmp_path_fitresult
                continue
            sigmeansExists.append(sigmean)

            tmp_path_fitpar = config.getFileName(infile.replace("FitParameters", "PostFit"), cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
            tmp_path_fitpars = glob(tmp_path_fitpar)

            if len(tmp_path_fitresults) == 0:
                print "No fit results for ", sigmean, sigwidth, tmp_path_fitresult
                continue

            for path in tmp_path_fitresults:
              fpe = efp.FitParameterExtractor(path)
              test = ROOT.TFile(tmp_path_fitpar)
              
              for toy in range(config.nToys):
                h_in = test.Get("chi2_%d"%(toy))
                if not h_in:
                  continue

                chi2 = (h_in.GetBinContent(1))
                chi2ndof = (h_in.GetBinContent(2))
                pval = (h_in.GetBinContent(6))
                #if chi2ndof > 1.1:
                #  continue
                #if pval < 0.05:
                ##if pval < 0.01:
                #   continue

                try:
                    fpe.suffix = "_%d"%(toy)
                    fpe.ExtractFromFile( "_%d"%(toy))
                    nsig = fpe.GetNsig()
                    params = fpe.GetH1Params()
                except:
                    #print "Couldn't read nsig from", path
                    continue

                if nsig == None or  math.isnan(nsig):
                    continue

                h_allPoints.Fill(nsig)
                h_p1.Fill(params.GetBinContent(3))
                h_p2.Fill(params.GetBinContent(4))
                h_p3.Fill(params.GetBinContent(5))
                h_p4.Fill(params.GetBinContent(6))
                h_p5.Fill(params.GetBinContent(7))
                #print nsig, chi2, params.GetBinContent(3), params.GetBinContent(4), params.GetBinContent(5), params.GetBinContent(6)

            h_allPoints_list.append(h_allPoints)
            h_p1_list.append(h_p1)
            h_p2_list.append(h_p2)
            h_p3_list.append(h_p3)
            h_p4_list.append(h_p4)
            h_p5_list.append(h_p5)


    if bkgOnlyFitFile:
      h_p1 = h_p1_list[0].Clone("p1")
      h_p2 = h_p2_list[0].Clone("p2")
      h_p3 = h_p3_list[0].Clone("p3")
      h_p4 = h_p4_list[0].Clone("p4")
      h_p5 = h_p5_list[0].Clone("p5")
      h_p1.Reset()
      h_p2.Reset()
      h_p3.Reset()
      h_p4.Reset()
      h_p5.Reset()
      h_p1.SetDirectory(0)
      h_p2.SetDirectory(0)
      h_p3.SetDirectory(0)
      h_p4.SetDirectory(0)
      h_p5.SetDirectory(0)

      tmp_path_fitBkg = config.getFileName(bkgOnlyFitFile, cdir, channelName, rangelow, rangehigh, 0, 0, 0) + ".root"
      fpeBkg = efp.FitParameterExtractor(tmp_path_fitBkg)
      for toy in range(config.nToys):
          try:
             fpeBkg.suffix = "_%d"%(toy)
             fpeBkg.ExtractFromFile( "_%d"%(toy))
             params = fpeBkg.GetH1Params()
          except:
             #print "Couldn't read nsig from", path
             continue
  
          #print params.GetBinContent(2), params.GetBinContent(3), params.GetBinContent(4), params.GetBinContent(5), params.GetBinContent(6)
  
          h_p1.Fill(params.GetBinContent(2))
          h_p2.Fill(params.GetBinContent(3))
          h_p3.Fill(params.GetBinContent(4))
          h_p4.Fill(params.GetBinContent(5))
          h_p5.Fill(params.GetBinContent(6))
  
      h_p1_list.append(h_p1)
      h_p2_list.append(h_p2)
      h_p3_list.append(h_p3)
      h_p4_list.append(h_p4)
      h_p5_list.append(h_p5)




    graphs = []
    ratios = []
    legendNames = []
    for sigwidth in sigwidths:
       g_avg = TGraphErrors()
       g_avg.SetTitle("#sigma / m = %.2d"%sigwidth)
       g_avg.GetXaxis().SetTitle("m_{jj}")
       g_avg.GetYaxis().SetTitle("<N_{sig}>")
       g_ratio = TGraphErrors()
       g_ratio.GetYaxis().SetTitle("S_{spur} / #sigma_{fit}")
       g_ratio.GetXaxis().SetTitle("m_{jj}")
       for sigmean, i in zip(sigmeansExists, range(len(sigmeansExists))):
         n = g_avg.GetN()
         g_avg.SetPoint(n, sigmean, h_allPoints_list[i].GetMean())
         g_avg.SetPointError(n, 0.001, h_allPoints_list[i].GetStdDev())
         if h_allPoints_list[i].GetStdDev() > 0:
           g_ratio.SetPoint(n, sigmean, h_allPoints_list[i].GetMean() / h_allPoints_list[i].GetStdDev())
       g_avg.GetXaxis().SetLimits(minMean-50, maxMean+50)
       g_ratio.GetXaxis().SetLimits(minMean-50, maxMean+50)

       graphs.append(g_avg)
       ratios.append(g_ratio)
       legendNames.append("#sigma / m = %d%%"%sigwidth)

    c2 = df.setup_canvas()
    graphs[0].GetYaxis().SetTitle("N_{extracted signal}")
    ratios[0].GetYaxis().SetRangeUser(-1,1)
    ratios[0].GetYaxis().SetTitle("S_{spur} / #sigma_{fit}")
    outfileName = config.getFileName("SpuriousSignal_PD_" + outfile + "Ratio", cdir, channelName, rangelow, rangehigh) + ".pdf"
    leg, upperPad, lowerPad = df.DrawRatioHists(c2, graphs, ratios, legendNames, [], sampleName = "", drawOptions = ["AP", "P"], styleOptions=df.get_extraction_style_opt, isLogX=0, isLogY=0, ratioDrawOptions = ["AP", "P"])
    upperPad.cd()
    line = ROOT.TLine(minMean-50, 0.0, maxMean+50, 0.0)
    line.Draw()
    lowerPad.cd()
    line0 = ROOT.TLine(minMean-50, 0.0, maxMean+50, 0.0)
    line1 = ROOT.TLine(minMean-50, 0.5, maxMean+50, 0.5)
    line2 = ROOT.TLine(minMean-50, -0.5, maxMean+50, -0.5)
    line1.SetLineStyle(2)
    line2.SetLineStyle(2)
    line0.Draw()
    line1.Draw()
    line2.Draw()

    c2.Print(outfileName)


         

    legendNamesMasses = []
    for mean in sigmeansExists:
      legendNamesMasses.append("m_{Z'} = %d"%mean)
 
    # Plotting:
    c = df.setup_canvas()
    outfileName = config.getFileName("SpuriousSignal"+outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"
    df.SetRange(h_allPoints_list, myMin=0)
    df.SetStyleOptions(h_allPoints_list, df.get_finalist_style_opt)
    leg = df.DrawHists(c, h_allPoints_list, legendNamesMasses, [], sampleName = "", drawOptions = ["HIST", "HIST"], styleOptions=df.get_extraction_style_opt, isLogX=0)
    c.Print(outfileName)

    if bkgOnlyFitFile:
      legendNamesMasses.append("Bkg only fit")

    outfileName = config.getFileName("Spuriour_p1" + outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"
    df.SetRange(h_p1_list, myMin=0)
    df.SetStyleOptions(h_p1_list, df.get_finalist_style_opt)
    leg = df.DrawHists(c, h_p1_list, legendNamesMasses, [], sampleName = "", drawOptions = ["HIST", "HIST"], styleOptions=df.get_extraction_style_opt, isLogX=0)
    c.Print(outfileName)

    outfileName = config.getFileName("Spuriour_p2" + outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"
    df.SetRange(h_p2_list, myMin=0)
    df.SetStyleOptions(h_p2_list, df.get_finalist_style_opt)
    leg = df.DrawHists(c, h_p2_list, legendNamesMasses, [], sampleName = "", drawOptions = ["HIST", "HIST"], styleOptions=df.get_extraction_style_opt, isLogX=0)
    c.Print(outfileName)

    outfileName = config.getFileName("Spuriour_p3" + outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"
    df.SetRange(h_p3_list, myMin=0)
    df.SetStyleOptions(h_p3_list, df.get_finalist_style_opt)
    leg = df.DrawHists(c, h_p3_list, legendNamesMasses, [], sampleName = "", drawOptions = ["HIST", "HIST"], styleOptions=df.get_extraction_style_opt, isLogX=0)
    c.Print(outfileName)


    outfileName = config.getFileName("Spuriour_p4" + outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"
    df.SetRange(h_p4_list, myMin=0)
    df.SetStyleOptions(h_p4_list, df.get_finalist_style_opt)
    leg = df.DrawHists(c, h_p4_list, legendNamesMasses, [], sampleName = "", drawOptions = ["HIST", "HIST"], styleOptions=df.get_extraction_style_opt, isLogX=0)
    c.Print(outfileName)

    outfileName = config.getFileName("Spuriour_p5" + outfile, cdir, channelName, rangelow, rangehigh) + ".pdf"
    df.SetRange(h_p5_list, myMin=0)
    df.SetStyleOptions(h_p5_list, df.get_finalist_style_opt)
    leg = df.DrawHists(c, h_p5_list, legendNamesMasses, [], sampleName = "", drawOptions = ["HIST", "HIST"], styleOptions=df.get_extraction_style_opt, isLogX=0)
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

