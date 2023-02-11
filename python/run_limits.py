#!/usr/bin/env python

from __future__ import print_function
import os,sys,re,argparse,subprocess,shutil
import json
from python.ExtractPostfitFromWS import PostfitExtractor
from python.ExtractFitParameters import FitParameterExtractor
import config as config
import ROOT as r
from scipy.stats.distributions import chi2
import python.LocalFunctions as lf
import getSystematics as gs

def execute(cmd):  
    print("EXECUTE:", cmd)
    sys.stdout.flush() # keeps print and subprocess output in sync
    rtv = subprocess.call(cmd, shell=True, close_fds=True)
    return rtv



def run_anaFit(datahist,
               topfile,
               signalfile,
               wsfile,
               outputfile,
               outputstring,
               cdir,
               nbkg,
               outdir,
               dosignal=False,
               dolimit=False,
               sigmean=0,
               sigwidth=7,
               ntoys=10,
               maskthreshold=0.01,
               nsig="0,0,1e6",
               nbkgWindow = [],
               rebinFile=None,
               rebinHist=None,
               rebinEdges=None,
               fitFunction=None,
               datafiles = None,
               histnames = None,
               doRemake = False,
               useSysts = False,
               alphaBin = 0,
              ):


    # generate the config files on the fly in run dir
    if not os.path.isfile("%s/run/AnaWSBuilder.dtd"%(cdir)):
        execute("ln -s ../config/dijetTLA/AnaWSBuilder.dtd %s/run/AnaWSBuilder.dtd"%(cdir))

    
    for toy in range(max(ntoys, 1)):
      if ntoys == 0:
        toyString = ""
      else:
        toyString = "_%d"%(toy)

      poi="nsig_mean%s_%s" % (sigmean, datahist[0])

      if dosignal:
          poi=poi
      else:
          poi=None
      
      #rtv=execute("timeout --foreground 6000 quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 10000 --minTolerance 1E-5  --minStrat 1 --muScanPoints 0 --nllOffset 1 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits").replace(".root","%s.root"%(toyString))))
      #rtv=execute("timeout --foreground 6000 quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 10000 --minTolerance 1E-5  --minStrat 1  --nllOffset 1 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits").replace(".root","%s.root"%(toyString))))
      rtv=execute("quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 10 --minTolerance 1E-3  --minStrat 1  --nllOffset 0 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits").replace(".root","%s.root"%(toyString))))
      if rtv != 0:
          print("WARNING: Non-zero return code from quickLimit. Check if tolerable")
    
    return 0

def main(args):
    
    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--datafile', dest='datafile', type=str, required=True, help='Input data file')
    parser.add_argument('--datahist', dest='datahist', type=str, required=True, help='Input finebinned data histogram name')
    parser.add_argument('--topfile', dest='topfile', type=str, required=True, help='Input top-level xml card')
    parser.add_argument('--categoryfile', dest='categoryfile', type=str, required=True, help='Input category xml card')
    parser.add_argument('--fitFunction', dest='fitFunction', type=str, default=None, help='Name of the file with the fit function information')
    parser.add_argument('--cdir', dest='cdir', type=str, default=None, help='Full path to current directory')
    parser.add_argument('--wsfile', dest='wsfile', type=str, required=True, help='Output workspace file')
    parser.add_argument('--outputfile', dest='outputfile', type=str, required=True, help='Output fitresult file')
    parser.add_argument('--outputdir', dest='outputdir', type=str, required=True, help='Output fitresult file')
    parser.add_argument('--nbkg', dest='nbkg', type=str, required=True, help='Initial value and range of nbkg par (e.g. "2E8,0,3E8")')
    parser.add_argument('--rangelow', dest='rangelow', type=int, help='Start of fit range (in GeV)')
    parser.add_argument('--rangehigh', dest='rangehigh', type=int, help='End Start of fit range (in GeV)')
    parser.add_argument('--dosignal', dest='dosignal', action="store_true", help='Perform s+b fit (default: bkg-only)')
    parser.add_argument('--dolimit', dest='dolimit', action="store_true", help='Perform limit setting')
    parser.add_argument('--sigmean', dest='sigmean', type=int, default=0, help='Mean of signal Gaussian for s+b fit (in GeV)')
    parser.add_argument('--sigwidth', dest='sigwidth', type=int, default=7, help='Width of signal Gaussian for s+b fit (in %)')
    parser.add_argument('--rebinfile', dest='rebinfile', type=str, required=False, help='File containing histogram with template histogram for rebinning result')
    parser.add_argument('--rebinhist', dest='rebinhist', type=str, required=False, help='Name of template histogram for rebinning result')
    parser.add_argument('--rebinedges', dest='rebinedges', type=int, nargs="*", default=None, help='Name of template hist')
    parser.add_argument('--maskthreshold', dest='maskthreshold', type=float, default=0.01, help='Threshold of p(chi2) below which to run BH and mask the most significant window')

    args = parser.parse_args(args)
    print(args.datafile)

    if not os.path.exists(args.outputdir):
        os.makedirs(args.outputdir)

    run_anaFit(datafile=args.datafile,
               datahist=args.datahist,
               topfile=args.topfile,
               categoryfile=args.categoryfile,
               wsfile=args.outputdir + "/" + args.wsfile,
               outputfile=args.outputdir + "/" + args.outputfile,
               cdir=args.cdir,
               nbkg=args.nbkg,
               rangelow=args.rangelow,
               rangehigh=args.rangehigh,
               dosignal=args.dosignal,
               dolimit=args.dolimit,
               sigmean=args.sigmean,
               sigwidth=args.sigwidth,
               rebinFile=args.rebinfile,
               rebinHist=args.rebinhist,
               rebinEdges=args.rebinedges,
               maskthreshold=args.maskthreshold,
               fitFunction=args.fitFunction)


if __name__ == "__main__":  
    sys.exit(main(sys.argv[1:]))
