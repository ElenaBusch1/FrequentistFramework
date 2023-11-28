#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from array import array
from ROOT import *
from math import sqrt
from glob import glob
import ExtractFitParameters as efp
#import ExtractPostFit as pfe
import numpy
from color import getColorSteps
import DrawingFunctions as df
import AtlasStyle as AS
import config as config
import LocalFunctions as lf
import FittingFunctions as ff



def spuriousSignal(sigmeans, sigwidths, infile, infilePD, outfile, rangelow, rangehigh, channelName, cdir, atlasLabel="Simulation Internal", bkgOnlyFitFile = None, fitName = "", crange = 30000, isNInjected=False, lumi = 0):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)
    labels = []
    labels.append("%s"%(config.samples[channelName]["label"]))


    meansCentered = []
    meansCentered.append(sigmeans[0] - (sigmeans[1]-sigmeans[0])/2.)
    for i in range(len(sigmeans)-1):
      meansCentered.append((sigmeans[i] + sigmeans[i+1])/2.)
    nbins = len(sigmeans)
    meansCentered.append(sigmeans[nbins-1] + (sigmeans[nbins-1] - sigmeans[nbins-2])/2.)

    minMean = min(sigmeans)
    maxMean = max(sigmeans)


    h_allPoints_list = []
    h_sigmas = []

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
      index1 = configFile.find("p%d["%(parNum))
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
            h_allPoints = TH1F("spuriousSignal_%d_%d"%(sigmean, sigwidth), ";N_{extracted signal};No. of toys", 20, -crange, crange)
            h_allPoints.SetDirectory(0)

            path = config.getFileName(infile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
            tmp_path_fitresults = glob(path)

            if len(tmp_path_fitresults) == 0:
                # Depending on how the code is run, we might be missing some inputs
                #print "No fit results for ", sigmean, sigwidth, path
                continue
            sigmeansExists.append(sigmean)

            for hpar, index in zip(h_pars, range(len(h_pars))):
              h_parMass = hpar.Clone("%s_%d_%d"%(hpar.GetTitle(), sigmean, sigwidth))
              h_parMass.SetDirectory(0)
              h_parList[index].append(h_parMass)

            fpe = efp.FitParameterExtractor(path)
            
            for toy in range(config.nToys):
              postFit = path.replace("FitParameters", "PostFit")
              #print postFit
              #suffix = "_%d"%(toy)
              suffix = "%d"%(toy)
              try:
                  chi2Hist = lf.read_histogram(postFit, "chi2"+suffix)
                  chi2 = chi2Hist.GetBinContent(2)
                  pval = chi2Hist.GetBinContent(6)
                  if pval < 0.05:
                     continue

                  fpe.suffix = "%d"%(toy)
                  fpe.ExtractFromFile( "%d"%(toy))
                  #fpe.suffix = "_%d"%(toy)
                  #fpe.ExtractFromFile( "_%d"%(toy))
                  nsig = fpe.GetNsig()
                  params = fpe.GetH1Params()
                  #print nsig
              except:
                  # Note: not writing an error message, because this makes it cleaner 
                  #       if we haven't finished running all of the toys
                  continue

              if nsig == None or  math.isnan(nsig):
                  continue
              if pval < 0.01:
                print "Failed p-val", pval, nsig
                continue
              if nsig > 20000:
                print pval, nsig

              h_allPoints.Fill(nsig)

              for index in range(len(h_pars)):
                # The first 2 parameters are the number of background and number of signal, and the indexing starts at 1 --> 3+index
                h_parList[index][massIndex].Fill(params.GetBinContent(3+index))
            massIndex += 1

        h_allPoints_list.append(h_allPoints)


    graphs = []
    ratios = []
    legendNames = []
    for i, sigwidth in enumerate(sigwidths):
       g_avg = TGraphErrors()
       g_avg.SetTitle("#sigma / m = %.2d"%sigwidth)
       g_avg.GetXaxis().SetTitle("m_{Z'} [GeV]")
       g_avg.GetYaxis().SetTitle("<N_{sig}>")
       g_ratio = TGraphErrors()
       g_ratio.GetYaxis().SetTitle("S_{spur} / #sigma_{fit}")
       g_ratio.GetXaxis().SetTitle("m_{Z'} [GeV]")
       h_sigma = TH1D("sigwidth_%d_sigma"%(sigwidth), ";m_{Y} [GeV]",len(sigmeans), array('d', meansCentered))
       for sigmean, i in zip(sigmeansExists, range(len(sigmeansExists))):
         n = g_avg.GetN()

         myMean =  h_allPoints_list[i].GetMean()

         quantiles = array('d', [0.] )
         xq = array('d', [0.5])
         h_allPoints_list[i].GetQuantiles(1, quantiles, xq);
         myMedian = quantiles[0]
         stdDev = h_allPoints_list[i].GetStdDev()
         myMean = myMedian

         h_sigma.Fill(sigmean, stdDev)



         g_avg.SetPoint(n, sigmean, myMean)
         g_avg.SetPointError(n, 0.001, h_allPoints_list[i].GetStdDev())
         if h_allPoints_list[i].GetStdDev() > 0:
           g_ratio.SetPoint(n, sigmean, myMean / h_allPoints_list[i].GetStdDev())
       h_sigmas.append(h_sigma)
       g_avg.GetXaxis().SetLimits(minMean-50, maxMean+50)
       g_ratio.GetXaxis().SetLimits(minMean-50, maxMean+50)

       graphs.append(g_avg)
       ratios.append(g_ratio)
       legendNames.append("#sigma / m = %d%%"%sigwidth)

    c2 = df.setup_canvas()
    graphs[0].GetYaxis().SetTitle("N_{extracted signal}")
    ratios[0].GetYaxis().SetRangeUser(-1.2,1.2)
    ratios[0].GetYaxis().SetTitle("S_{spur} / #sigma_{fit}")
    outfileName = config.getFileName("SpuriousSignal_PD_" + outfile + "Ratio", cdir, channelName, rangelow, rangehigh) + "_sigwidth_%d"%sigwidth + ".pdf"
    leg, upperPad, lowerPad = df.DrawRatioHists(c2, graphs, ratios, legendNames, labels=labels, sampleName = "", drawOptions = ["AP", "P", "P", "P", "P", "P", "P", "P", "P"], styleOptions=df.get_extraction_style_opt, isLogX=0, isLogY=0, ratioDrawOptions = ["AP", "P", "P", "P", "P", "P", "P", "P", "P", "P"], lumi=lumi)
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
    #for mean in sigmeansExists:
    for mean in sigmeans:
      legendNamesMasses.append("m_{Z'} = %d [GeV]"%mean)
 
    # Plotting:
    c = df.setup_canvas()
    outfileName = config.getFileName("SpuriousSignal"+outfile, cdir, channelName, rangelow, rangehigh) + "_sigwidth_%d"%sigwidth + ".pdf"
    df.SetRange(h_allPoints_list, myMin=0)
    leg = df.DrawHists(c, h_allPoints_list, legendNamesMasses, labels=labels, sampleName = "", drawOptions = ["HIST", "HIST", "HIST", "HIST", "HIST", "HIST", "HIST"], styleOptions=df.get_extraction_style_opt, isLogX=0, lumi=lumi)
    c.Print(outfileName)

    h_sigmas[0].GetYaxis().SetRangeUser(1, 100000)
    c.SetLogy()
    leg = df.DrawHists(c,h_sigmas, legendNames, [], drawOptions = ["HIST"], styleOptions=df.get_rainbow_style_opt, isLogX=0)
    path = config.getFileName("Sigma", cdir, channelName, rangelow, rangehigh) + "Width_%d.pdf"%sigwidth
    c.Print(path)
    c.SetLogy(0)
    for sigWidth in sigwidths:
      biasFileName = config.getFileName("bias_", cdir, channelName, rangelow, rangehigh) +"_sigwidth_%d.root"%(sigwidth)
      fout = TFile(biasFileName, "RECREATE")
      print biasFileName

      h_sigma.Write()
      fout.Close()


    # Plot the fit parameters for the different toys
    for h_par, i in zip(h_parList, range(len(h_parList))):
      leg = df.DrawHists(c, h_par, legendNamesMasses, labels=labels, drawOptions = ["hist"], styleOptions=df.get_extraction_style_opt, isLogX=0, lumi=lumi)
      path = config.getFileName("Spurious_" + h_pars[i].GetTitle(), cdir, channelName, rangelow, rangehigh) + "_sigwidth_%d"%sigwidth + ".pdf"
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

