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



def spuriousSignal(sigmeans, sigwidths, infile, infilePD, outfile, rangelow, rangehigh, channelName, cdir, atlasLabel="Simulation Internal", bkgOnlyFitFile = None, fitName = ""):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    sigmeansExists = []

    h_pars = []
    configName = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/" + config.fitFunctions[fitName]["Config"]

    with open(configName) as f:
      lines = f.readlines()
      configFile = lines[2]

    parNum = 1
    # Do this for the systematics instead
    while configFile.find("p%d"%(parNum)) >= 0:
      index1 = configFile.find("p%d["%(parNum))
      substr1 = configFile[index1:-1]
      substr2 = substr1[3:substr1.find("]")]
      substr3 = substr2[substr2.find(",")+1:]
      substr4 = substr3[0:substr3.find(",")]
      substr5 = substr3[substr3.find(",")+1:]
      pMin = float(substr4)
      pMax = float(substr5)
      if pMin < pMax:
        h_p = TH1F("p%d"%(parNum), "p%d;p%d;No. of toys"%(parNum,parNum), 500, -2, 2)
        h_p.SetDirectory(0)
        h_pars.append(h_p)
      parNum += 1


    h_parList = []
    for i in range(len(h_pars)):
      clist = []
      h_parList.append(clist)

    massIndex = 0
    for j,sigmean in enumerate(sigmeans):
        for i,sigwidth in enumerate(sigwidths):
            tmp_path_fitresults = glob(config.getFileName(infile, cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root")

            if len(tmp_path_fitresults) == 0:
                print "No fit results for ", sigmean, sigwidth, tmp_path_fitresult
                continue
            sigmeansExists.append(sigmean)

            tmp_path_fitpar = config.getFileName(infile.replace("FitParameters", "PostFit"), cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
            tmp_path_fitpars = glob(tmp_path_fitpar)

            if len(tmp_path_fitresults) == 0:
                print "No fit results for ", sigmean, sigwidth, tmp_path_fitresult
                continue

            for hpar, index in zip(h_pars, range(len(h_pars))):
              h_parMass = hpar.Clone("%s_%d_%d"%(hpar.GetTitle(), sigmean, sigwidth))
              h_parMass.SetDirectory(0)
              h_parList[index].append(h_parMass)


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
                #if pval < 0.01:
                #   continue

                try:
                    fpe.suffix = "_%d"%(toy)
                    fpe.ExtractFromFile( "_%d"%(toy))
                    nsig = fpe.GetNsig()
                    params = fpe.GetH1Params()
                except:
                    continue

                if nsig == None or  math.isnan(nsig):
                    continue

                for index in range(len(h_pars)):
                  h_parList[index][massIndex].Fill(params.GetBinContent(3+index))
              massIndex += 1
  

    c = df.setup_canvas()
    legendNamesMasses = []
    for mean in sigmeansExists:
      legendNamesMasses.append("m_{Z'} = %d"%mean)
 
    print (len(h_parList))
    for h_par, i in zip(h_parList, range(len(h_parList))):
      print( len(h_par), len(legendNamesMasses))
      leg = df.DrawHists(c, h_par, legendNamesMasses, [], drawOptions = ["hist"], styleOptions=df.get_extraction_style_opt, isLogX=0)
      path = config.getFileName("JES_" + h_pars[i].GetTitle(), cdir, channelName, rangelow, rangehigh) + ".pdf"
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

