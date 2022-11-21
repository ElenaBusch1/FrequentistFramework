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



def compareFitParams(sigmeans, sigwidths, infile, infilePD, outfile, rangelow, rangehigh, channelNames, cdir, atlasLabel="Simulation Internal", bkgOnlyFitFile = None, fitName = "", crange = 30000, isNInjected=False, outputdir="", signalName = "Z'", sigamps = [0,1,2]):
  ROOT.gROOT.SetBatch(ROOT.kTRUE)


  c = df.setup_canvas("test1")
  c2 = df.setup_canvas("test2")
  # This is a hacky way of getting all of the fit parameters, and the ranges that they are allowed to span, just to make some plots of this
  configName = config.cdir + "/" + config.fitFunctions[fitName]["Config"]

  with open(configName) as f:
    lines = f.readlines()
    configFile = lines[2]

  '''
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
  '''


  for index, channelName in enumerate(channelNames):
    for j,sigmean in enumerate(sigmeans):
      for i,sigwidth in enumerate(sigwidths):

        legendNames = []
        massIndex = 0
        h_parList = []
        parNum = 1
        h_pars = []

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


        for k,sigamp in enumerate(sigamps):

          path = config.getFileName(infile, cdir, channelName, outputdir + channelName, sigmean, sigwidth, sigamp) + ".root"
          tmp_path_fitresults = glob(path)

          if len(tmp_path_fitresults) == 0:
              # Depending on how the code is run, we might be missing some inputs
              print "No fit results for ", sigmean, sigwidth, path
              continue

          for parindex, hpar in enumerate(h_pars):
            h_parMass = hpar.Clone("%s_%d_%d_%d"%(hpar.GetTitle(), sigmean, sigwidth, sigamp))
            h_parMass.SetDirectory(0)
            h_parList[parindex].append(h_parMass)

          fpe = efp.FitParameterExtractor(path)
          
          isBroken=True;
          for toy in range(config.nToys):
            try:
              fpe.suffix = "%s__%d"%(channelName,toy)
              fpe.ExtractFromFile( "%s__%d"%(channelName,toy), channelName)
              params = fpe.GetH1Params()
              isBroken=False
            except:
              # Note: not writing an error message, because this makes it cleaner 
              #       if we haven't finished running all of the toys
              if isBroken:
                isBroken=False
                #print(fpe.suffix, path)
              continue

            for parindex in range(len(h_pars)):
              # The first 2 parameters are the number of background and number of signal, and the indexing starts at 1 --> 3+index
              for cbin in range(params.GetNbinsX()):
                if params.GetXaxis().GetBinLabel(cbin+1).find(h_pars[parindex].GetTitle()) >= 0:
                  h_parList[parindex][massIndex].Fill(params.GetBinContent(cbin+1))

          massIndex += 1
          legendNames.append("Sig amp = %d"%sigamp)

          labels = []
          labels.append("m_{X} = %d GeV, #sigma_{m} = %d %%"%(sigmean, sigwidth))


        # Plot the fit parameters for the different toys
        for m, h_par in enumerate(h_parList):
          print sigmean, sigwidth, channelName
          print(len(h_par), len(h_pars), len(h_parList), len(legendNames), legendNames)
          leg = df.DrawHists(c, h_par, legendNames, [], drawOptions = ["hist"], styleOptions=df.get_rainbow_style_opt, isLogX=0)
          path = config.getFileName("FitParams_sigmean_%d_sigwidth_%d_"%(sigmean, sigwidth) + h_pars[m].GetTitle(), cdir, channelName, outputdir) + ".pdf"
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

