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
import FittingFunctions as ff



#def spuriousSignal(sigmeans, sigwidths, infile, infilePD, outfile, rangelow, rangehigh, channelName, cdir, atlasLabel="Simulation Internal", bkgOnlyFitFile = None, fitName = "", crange = 30000, isNInjected=False, outputdir=""):
def spuriousSignal(sigmeans, sigwidths, infile, infilePD, outfile, rangelow, rangehigh, channelNames, cdir, atlasLabel="Simulation Internal", bkgOnlyFitFile = None, fitName = "", crange = 30000, isNInjected=False, outputdir=""):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    h_allPoints_list = []
    sigmeansExists = []

    minMean = min(sigmeans)
    maxMean = max(sigmeans)

    # This is a hacky way of getting all of the fit parameters, and the ranges that they are allowed to span, just to make some plots of this
    h_pars = []
    h_parList = []
    configName = config.cdir + "/" + config.fitFunctions[fitName]["Config"]

    with open(configName) as f:
      lines = f.readlines()
      configFile = lines[2]

    parNum = 1
    while configFile.find("p%d"%(parNum)) >= 0:
      index1 = configFile.find("p%d_CATEGORY["%(parNum))
      substr1 = configFile[index1:-1]
      substr2 = substr1[3:substr1.find("]")]
      substr3 = substr2[substr2.find(",")+1:]
      substr4 = substr3[0:substr3.find(",")]
      substr5 = substr3[substr3.find(",")+1:]
      pMin = float(substr4)
      pMax = float(substr5)
      # When pMin == pMax, the fit parameter is fixed, and it won't show up in this plot
      if pMin < pMax:
        h_p = TH1F("p%d"%(parNum), "p%d;p%d;No. of toys"%(parNum,parNum), 500, pMin, pMax)
        h_p.SetDirectory(0)
        h_pars.append(h_p)
        clist = []
        h_parList.append(clist)
      parNum += 1


    massIndex = 0
    for j,sigmean in enumerate(sigmeans):
        for i,sigwidth in enumerate(sigwidths):
          for channelName in channelNames:
            h_allPoints = TH1F("spuriousSignal_%d_%d"%(sigmean, sigwidth), ";N_{extracted signal};No. of toys", 120, -crange, crange)
            h_allPoints.SetDirectory(0)

            path = config.getFileName(infile, cdir, channelName, outputdir, sigmean, sigwidth, 0) + ".root"
            tmp_path_fitresults = glob(path)

            if len(tmp_path_fitresults) == 0:
                # Depending on how the code is run, we might be missing some inputs
                print "No fit results for ", sigmean, sigwidth, path
                continue
            sigmeansExists.append(sigmean)

            for hpar, index in zip(h_pars, range(len(h_pars))):
              h_parMass = hpar.Clone("%s_%d_%d"%(hpar.GetTitle(), sigmean, sigwidth))
              h_parMass.SetDirectory(0)
              h_parList[index].append(h_parMass)

            fpe = efp.FitParameterExtractor(path)
            
            isBroken=True;
            for toy in range(config.nToys):
              try:
                  fpe.suffix = "%s__%d"%(channelName,toy)
                  fpe.ExtractFromFile( "%s__%d"%(channelName,toy), channelName)
                  nsig = fpe.GetNsig()
                  params = fpe.GetH1Params()
                  isBroken=False
              except:
                  # Note: not writing an error message, because this makes it cleaner 
                  #       if we haven't finished running all of the toys
                  if isBroken:
                    isBroken=False
                    print(fpe.suffix, path)
                  continue

              if nsig == None or  math.isnan(nsig):
                  continue

              h_allPoints.Fill(nsig)
              for index in range(len(h_pars)):
                # The first 2 parameters are the number of background and number of signal, and the indexing starts at 1 --> 3+index
                h_parList[index][massIndex].Fill(params.GetBinContent(3+index))
            massIndex += 1

          h_allPoints_list.append(h_allPoints)


    graphs = []
    ratios = []
    legendNames = []
    meanSpurs = []
    sigSpurs = []
    for sigwidth in sigwidths:
       g_avg = TGraphErrors()
       g_avg.SetTitle("#sigma / m = %.2d"%sigwidth)
       g_avg.GetXaxis().SetTitle("m_{Z'}")
       g_avg.GetYaxis().SetTitle("<N_{sig}>")
       g_ratio = TGraphErrors()
       g_ratio.GetYaxis().SetTitle("S_{spur} / #sigma_{fit}")
       g_ratio.GetXaxis().SetTitle("m_{Z'}")
       for sigmean, i in zip(sigmeansExists, range(len(sigmeansExists))):
         n = g_avg.GetN()
         g_avg.SetPoint(n, sigmean, h_allPoints_list[i].GetMean())
         g_avg.SetPointError(n, 0.001, h_allPoints_list[i].GetStdDev())
         if h_allPoints_list[i].GetStdDev() > 0:
           g_ratio.SetPoint(n, sigmean, h_allPoints_list[i].GetMean() / h_allPoints_list[i].GetStdDev())
         meanSpurs.append(h_allPoints_list[i].GetMean())
         sigSpurs.append(h_allPoints_list[i].GetStdDev())
       g_avg.GetXaxis().SetLimits(minMean-50, maxMean+50)
       g_ratio.GetXaxis().SetLimits(minMean-50, maxMean+50)

       graphs.append(g_avg)
       ratios.append(g_ratio)
       legendNames.append("#sigma / m = %d%%"%sigwidth)

    c2 = df.setup_canvas()
    graphs[0].GetYaxis().SetTitle("N_{extracted signal}")
    ratios[0].GetYaxis().SetRangeUser(-1.2,1.2)
    ratios[0].GetYaxis().SetTitle("S_{spur} / #sigma_{fit}")
    outfileName = config.getFileName("SpuriousSignal_PD_" + outfile + "Ratio", cdir, channelName, outputdir) + ".pdf"
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
    for mean, meanSpur, sigSpur in zip(sigmeansExists, meanSpurs, sigSpurs):
      legendNamesMasses.append("m_{Z'} = %d, n_{spur}=%.2f, #sigma_{fit}=%.2f"%(mean, meanSpur, sigSpur))
 
    # Plotting:
    c = df.setup_canvas()
    outfileName = config.getFileName("SpuriousSignal"+outfile, cdir, channelName, outputdir) + ".pdf"
    df.SetRange(h_allPoints_list, myMin=0)
    leg = df.DrawHists(c, h_allPoints_list, legendNamesMasses, [], sampleName = "", drawOptions = ["HIST", "HIST"], styleOptions=df.get_extraction_style_opt, isLogX=0)
    c.Print(outfileName)

    # Plot the fit parameters for the different toys
    for h_par, i in zip(h_parList, range(len(h_parList))):
      leg = df.DrawHists(c, h_par, legendNamesMasses, [], drawOptions = ["hist"], styleOptions=df.get_extraction_style_opt, isLogX=0)
      path = config.getFileName("Spurious_" + h_pars[i].GetTitle(), cdir, channelName, outputdir) + ".pdf"
      c.Print(path)




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

