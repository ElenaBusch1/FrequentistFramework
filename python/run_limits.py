#!/usr/bin/env python

#from __future__ import print_function
#import os,sys,re,argparse,subprocess,shutil
import os,sys,subprocess
#import config as config
#import ROOT as r

def execute(cmd):  
    print("EXECUTE:", cmd)
    sys.stdout.flush() # keeps print and subprocess output in sync
    rtv = subprocess.call(cmd, shell=True, close_fds=True)
    return rtv


def run_anaFit(datahist,
               wsfile,
               outputfile,
               cdir,
               sigmean=0,
               sigwidth=7,
               doRemake = False,
              ):

    limitFile =  outputfile.replace("FitResult","Limits")
    if not doRemake:
        postfitfile=outputfile.replace("FitResult","PostFit")
        postfitfile=postfitfile.replace("CHANNEL", histName)
        print(postfitfile)
        if lf.read_histogram(postfitfile, "data%s_%s"%(histName, toyString)):
          print( "Already found toy for ", toy)
          return 0



    poi="nsig_mean%s_%s" % (sigmean, datahist[0])

    rtv=execute("quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 1000 --minTolerance 1e-3  --minStrat 2 --betterBands 1  --nllOffset 1 -o %s" % (wsfile, poi, limitFile))


    if rtv != 0:
          print("WARNING: Non-zero return code from quickLimit. Check if tolerable")
    
    return 0

