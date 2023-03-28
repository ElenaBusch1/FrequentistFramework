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



def spuriousSignal(sigmeans, sigwidths, infile, infilePD, outfile, rangelow, rangehigh, channelNames, cdir, atlasLabel="Simulation Internal", bkgOnlyFitFile = None, fitName = "", crange = 30000, isNInjected=False, outputdir="", signalName = "Z'", labels = [], delta = 50, deltaMassAboveFit = 0):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    meansCentered = []
    meansCentered.append(sigmeans[0] - (sigmeans[1]-sigmeans[0])/2.)
    for i in range(len(sigmeans)-1):
      meansCentered.append((sigmeans[i] + sigmeans[i+1])/2.)
    nbins = len(sigmeans)
    meansCentered.append(sigmeans[nbins-1] + (sigmeans[nbins-1] - sigmeans[nbins-2])/2.)

    minMean = min(sigmeans)
    maxMean = max(sigmeans)

    c = df.setup_canvas("test1")
    c2 = df.setup_canvas("test2")
    # This is a hacky way of getting all of the fit parameters, and the ranges that they are allowed to span, just to make some plots of this
    configName = config.cdir + "/" + config.fitFunctions[fitName]["Config"]

    with open(configName) as f:
      lines = f.readlines()
      configFile = lines[2]

    h_pars = []
    h_parList = []
    parNum = 1
    while configFile.find("p%d"%(parNum)) >= 0:
      index1 = configFile.find("p%d_CATEGORY["%(parNum))
      substr1 = configFile[index1:-1]
      substr2 = substr1[3:substr1.find("]")]
      substr3 = substr2[substr2.find(",")+1:]
      substr4 = substr3[0:substr3.find(",")]
      substr5 = substr3[substr3.find(",")+1:]
      #print (configFile[index1:-1])
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

    h_spurious = {}


    for i,sigwidth in enumerate(sigwidths):
        h_myPoints = []
        sigmeansExists = []
        for j,sigmean in enumerate(sigmeans):
          massIndex = 0
          h_pars = []
          h_parList = []
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

          h_allPoints_list = []

          for index, channelName in enumerate(channelNames):

            #h_allPoints = TH1F("spuriousSignal_%d_%d"%(sigmean, sigwidth), ";N_{extracted signal};No. of toys", 21, -crange[j], crange[j])
            #h_allPoints = TH1F("spuriousSignal_%d_%d"%(sigmean, sigwidth), ";S_{spur};No. of toys", 21, -crange[j], crange[j])
            h_allPoints = TH1F("spuriousSignal_%d_%d"%(sigmean, sigwidth), ";S_{spur};No. of toys", 63, -crange[j], crange[j])
            h_allPoints.SetDirectory(0)

            rangelow = config.samples[channelName]["rangelow"]
            if sigmean < (rangelow + deltaMassAboveFit) :
              h_allPoints_list.append(h_allPoints)
              #print "fails mass"
              continue

            path = config.getFileName(infile, cdir, channelName, outputdir + channelName, sigmean, sigwidth, 0) + ".root"
            tmp_path_fitresults = glob(path)

            if len(tmp_path_fitresults) == 0:
                # Depending on how the code is run, we might be missing some inputs
                print "No fit results for ", sigmean, sigwidth, path
                #h_allPoints.Fill(0)
                h_allPoints_list.append(h_allPoints)
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
                  #nBkg = fpe.GetNbkg()
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
              #if nBkg == 0:
              #    continue

              h_allPoints.Fill(nsig)
              for index in range(len(h_pars)):
                # The first 2 parameters are the number of background and number of signal, and the indexing starts at 1 --> 3+index
                h_parList[index][massIndex].Fill(params.GetBinContent(3+index))
            massIndex += 1

            h_allPoints_list.append(h_allPoints)
            h_spurious["%d_%d_%s"%(sigmean,sigwidth,channelName)] = h_allPoints



          legendNamesMasses = []
          for k, channelName in enumerate(channelNames):
            legendNamesMasses.append(config.samples[channelName]["varLabel"])
          #labels = []
          labels.append("m_{Y} = %d GeV, #sigma_{m} = %d %%"%(sigmean, sigwidth))

          if(len(h_allPoints_list)==0):
            h_allPoints_list.append(0)
            continue
          # Plotting:
          #outfileName = config.getFileName("SpuriousSignal"+outfile, cdir, "all", outputdir) + "_mean_%d"%(sigmean) + ".pdf"
          outfileName = config.getFileName("SpuriousSignal"+outfile, cdir, "all", outputdir, sigmean, sigwidth,0) + ".pdf"
          #df.SetRange(h_allPoints_list, myMin=0)
          df.SetRange(h_allPoints_list)
          leg = df.DrawHists(c, h_allPoints_list, legendNamesMasses, labels, sampleName = "", drawOptions = ["HIST", "HIST"], styleOptions=df.get_rainbow_style_opt, isLogX=0)
          c.Print(outfileName)
          labels.pop()

          h_myPoints.append(h_allPoints_list)



        graphs = []
        sigmas = []
        h_sigmas = []
        ratios = []
        legendNames = []
        meanSpurs = []
        sigSpurs = []
        for k, channelName in enumerate(channelNames):
          g_sigma = TGraphErrors()
          g_sigma.SetTitle(config.samples[channelName]["varLabel"])
          h_sigma = TH1D("%s_sigma"%(channelName), ";m_{Y} [GeV]",len(sigmeans), array('d', meansCentered))

          g_avg = TGraphErrors()
          #g_avg.SetTitle("#sigma / m = %.2d"%sigwidth)
          g_avg.SetTitle(config.samples[channelName]["varLabel"])
          g_avg.GetXaxis().SetTitle("m_{%s}"%(signalName))
          g_avg.GetYaxis().SetTitle("<N_{sig}>")
          g_ratio = TGraphErrors()
          g_ratio.GetYaxis().SetTitle("S_{spur} / #sigma_{fit}")
          g_ratio.GetXaxis().SetTitle("m_{%s}"%(signalName))
          for j,sigmean in enumerate(sigmeans):
            n = g_avg.GetN()
            myMean =  h_myPoints[j][k].GetMean()
            
            quantiles = array('d', [0.] )
            xq = array('d', [0.5])
            h_myPoints[j][k].GetQuantiles(1, quantiles, xq);
            myMedian = quantiles[0]
            stdDev = h_myPoints[j][k].GetStdDev()
            #print sigmean, myMean, myMedian,  h_myPoints[j][k].GetStdDev()
            if h_myPoints[j][k].GetEntries()>0:
              print( sigmean, stdDev)
              g_sigma.SetPoint(n, sigmean+delta*k, stdDev)
              h_sigma.Fill(sigmean, stdDev)
              g_avg.SetPoint(n, sigmean+delta*k, myMedian)
              g_avg.SetPoint(n, 0.001, stdDev)
            if  stdDev > 0:
              g_ratio.SetPoint(n, sigmean+delta*k, myMedian / stdDev)
              #print len(h_myPoints[j][k])
            if  stdDev ==0 and h_myPoints[j][k].GetEntries()>0:
              #print len(h_myPoints[j][k])
              g_ratio.SetPoint(n, sigmean+delta*k, myMedian )
          meanSpurs.append(myMedian)
          sigSpurs.append( stdDev)
          g_avg.GetXaxis().SetLimits(minMean-50, maxMean+delta*(len(channelNames)+2))
          g_ratio.GetXaxis().SetLimits(minMean-50, maxMean+delta*(len(channelNames)+2))

          graphs.append(g_avg)
          sigmas.append(g_sigma)
          h_sigmas.append(h_sigma)
          ratios.append(g_ratio)
          legendNames.append(config.samples[channelName]["varLabel"])


        graphs[0].GetYaxis().SetTitle("S_{spur}")
        ratios[0].GetYaxis().SetRangeUser(-0.8,0.8)
        ratios[0].GetYaxis().SetTitle("S_{spur} / #sigma_{fit}")
        graphs[0].GetYaxis().SetRangeUser(-max(crange), max(crange))
        outfileName = config.getFileName("SpuriousSignal_PD_" + outfile + "Ratio", cdir, "all", outputdir) + "Width_%d"%sigwidth + ".pdf"
        leg, upperPad, lowerPad = df.DrawRatioHists(c2, graphs, ratios, legendNames, ["#sigma / m = %.2f"%(sigwidth/100.)], sampleName = "", drawOptions = ["AP", "P"], styleOptions=df.get_rainbow_style_opt, isLogX=0, isLogY=0, ratioDrawOptions = ["AP", "P"], ratioHeight = 0.45)
        upperPad.cd()
        line = ROOT.TLine(minMean-50, 0.0, maxMean+delta*(len(channelNames)+2), 0.0)
        line.Draw()
        lowerPad.cd()
        line0 = ROOT.TLine(minMean-50, 0.0, maxMean+delta*(len(channelNames)+2), 0.0)
        line1 = ROOT.TLine(minMean-50, 0.5, maxMean+delta*(len(channelNames)+2), 0.5)
        line2 = ROOT.TLine(minMean-50, -0.5, maxMean+delta*(len(channelNames)+2), -0.5)
        line3 = ROOT.TLine(minMean-50, 0.3, maxMean+delta*(len(channelNames)+2), 0.3)
        line4 = ROOT.TLine(minMean-50, -0.3, maxMean+delta*(len(channelNames)+2), -0.3)
        line1.SetLineStyle(2)
        line2.SetLineStyle(2)
        line3.SetLineStyle(3)
        line4.SetLineStyle(3)
        line0.Draw()
        line1.Draw()
        line2.Draw()
        line3.Draw()
        line4.Draw()
        c2.Print(outfileName)

        leg = df.DrawHists(c,h_sigmas, legendNames, [], drawOptions = ["HIST"], styleOptions=df.get_rainbow_style_opt, isLogX=0)
        path = config.getFileName("Sigma", cdir, "", outputdir) + "Width_%d.pdf"%sigwidth 
        c.Print(path)
        for channelName, h_sigma in zip(channelNames, h_sigmas):
          biasFileName = config.getFileName("bias_%s"%(signalName), cdir, channelName, outputdir) +".root"
          fout = TFile(biasFileName, "RECREATE")
          print biasFileName
          
          h_sigma.Write()
          fout.Close()
           


        # Plot the fit parameters for the different toys
        for h_par, i in zip(h_parList, range(len(h_parList))):
          leg = df.DrawHists(c, h_par, legendNamesMasses, ["#sigma / m = %.2f"%(sigwidth/100.)], drawOptions = ["hist"], styleOptions=df.get_rainbow_style_opt, isLogX=0)
          path = config.getFileName("Spurious_" + h_pars[i].GetTitle(), cdir, channelName, outputdir) + "Width_%d"%sigwidth + ".pdf"
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

