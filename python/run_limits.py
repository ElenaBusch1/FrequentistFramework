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
               ntoys=1,
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
               biasMagnitude=0,
               tagName = "",
               isMx = False,
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
      rtv=execute("quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 1 --minTolerance 1e-5  --minStrat 0  --nllOffset 1 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits").replace(".root","%s.root"%(toyString))))
      if rtv != 0:
          print("WARNING: Non-zero return code from quickLimit. Check if tolerable")
    
    return 0

