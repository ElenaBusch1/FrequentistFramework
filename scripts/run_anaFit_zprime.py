#!/usr/bin/env python

import subprocess, os, sys
from condor_handler import CondorHandler
sys.path.append("config/dijetTLA/")
from InitialParameters import initialParameters

##########################
## CHECK THIS		##
##########################

# Run mode and dataset
useBatch = False
runData  = True
quietMode = False

# Specs
trigger = "J50"
dataset = 'partialDataset2'  # 'full', 'partialDataset', 'TLA2016'

# Range of fit:
low= initialParameters[dataset][trigger]['low']
high=initialParameters[dataset][trigger]['high']
# Number of parameters in fit:
pars = "five"

#sigmeans = [ 550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,1650,1700,1750,1800,1850,1900,1950,2000]
#sigmeans = [ 350, 400, 450, 500, 550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500]
sigmeans = ["bOnly"]
sigwidth=-999 

doLimit = False
doPrefit = True
maskthreshold=0.01

# Output folder -- where everything is stored:
# default in python/run_anaFit.py is run/
outFolder = "run/Unblinding2/J50/"

backgroundfile 	= "config/dijetTLA/background_dijetTLA_J100yStar06_{0}Par.template".format(pars)

if sigwidth == -999:
  # xml template cards for zprime:
  topfile 	= "config/dijetTLA/dijetTLA_J100yStar06_zprime.template"
  categoryfile 	= "config/dijetTLA/category_dijetTLA_zprime.template"
  signalfile 	= ""
else:
  # xml template cards for gaussians:
  topfile	= "config/dijetTLA/dijetTLA_J100yStar06.template"
  categoryfile  = "config/dijetTLA/category_dijetTLA.template"
  signalfile 	= "config/dijetTLA/signal/signal_dijetTLA.template"


############################################################################
# Don't modify this, unless running on PD
############################################################################

if runData:
  # Running on Data:
  datafile = initialParameters[dataset][trigger]['datafile']
  datahist = initialParameters[dataset][trigger]['datahist']
  # nbkg is overriden if doPrefit:
  nbkg	   = initialParameters[dataset][trigger]['nbkg']

else:
  # Running on PD for tests
  datafile = "Input/data/dijetTLA/PD_2016TLA_J100/PD_133ifb_WHW10_fixLow1_TR0_fixLow1_fixHigh_3par.root"
  datahist = "pseudodata"
  # 130ifb (overriden if doPrefit)
  nbkg = initialParameters['full'][trigger]['nbkg']
  # 0 for no signal injection
  sigamp=0
  loopstart=0
  loopend=1
  # smooothing test:
  sigmeans = ["bOnly"]

################## Create output folder:

# local or Condor, everything will be stored here:
if not os.path.isdir(outFolder):
  subprocess.call("mkdir -p " + outFolder, shell=True)


#######################################################3
# PREPARE CONDOR:

if useBatch:
  # Create location of .log, .sub and .sh files:
  batch_logs = outFolder + 'logs/'
  batch_scripts = outFolder +  'jobs/'
  if not os.path.isdir(batch_logs):
    subprocess.call("mkdir -p " + batch_logs, shell=True)
  if not os.path.isdir(batch_scripts):
    subprocess.call("mkdir -p " + batch_scripts, shell=True)

  # Prepare the handler:
  batchmanager = CondorHandler( batch_logs, batch_scripts)
  
  # In condor I store everything in an output/ folder and at the end I copy everything from $Condor/output to outFolder/
  folder = 'output/'
else:
  folder = outFolder
 
#######################################################3
# PREPARE COMMAND LINE: 
for sigmean in sigmeans:
  
  # WS file name for xmlAnaWSBuilder:
  wsfile= folder + "dijetTLA_combWS_{0}Par_{1}yStar06_{2}_gq0p1.root"
  # Output file name for quickFit:
  outputfile = folder + "FitResult_anaFit_{0}Par_{1}yStar06_{2}.root"

  if sigmean == "bOnly":
    wsfile = wsfile.format(pars, trigger, "bOnly")
    outputfile = outputfile.format(pars, trigger, "bOnly")
    doSignal = False
    doLimit = False
    # dummy signal mass point: won't do any s+b fit
    sigmean = 1000
  else:
    wsfile = wsfile.format(pars, trigger, "mR"+str(sigmean))
    outputfile = outputfile.format(pars, trigger, "mR"+str(sigmean))
    doSignal = True

  if runData:
    command = "python python/run_anaFit.py --datafile {0} --datahist {1} --topfile {2} --categoryfile {3} --backgroundfile {4} --wsfile {5} --outputfile {6} --nbkg {7} --rangelow {8} --rangehigh {9} --sigmean {10} --sigwidth {11} --folder {12} --maskthreshold {13}".format(datafile, datahist, topfile, categoryfile, backgroundfile, wsfile, outputfile, nbkg, low, high, sigmean, sigwidth, folder, maskthreshold)

  else: # run on PD:
    command = "python python/run_injections_anaFit.py --datafile {0} --datahist {1} --categoryfile {2} --topfile {3} --backgroundfile {4} --wsfile {5} --sigmean {6} --sigwidth {7} --nbkg {8} --rangelow {9} --rangehigh {10} --outputfile {11} --folder {12} --maskthreshold {13} --sigamp {14} --loopstart {15} --loopend {16}".format(datafile, datahist, categoryfile, topfile, backgroundfile,  wsfile, sigmean, sigwidth, nbkg, low, high, outputfile, folder, maskthreshold, sigamp, loopstart, loopend) 

  if signalfile != "":
    command += " --signalfile " + signalfile

  if doSignal:
    command += " --dosignal"

  if doLimit:
    command += " --dolimit"

  if doPrefit:
    command += " --doprefit"

#######################################################3
  # SUBMISSION:

  print "Submitting command:\n"
  print command

  if not quietMode:
    if not useBatch:
      # Not working properly, don't know why. Just run it beforehand
      subprocess.call(". scripts/setup_buildCombineFit.sh", shell=True)
      subprocess.call(command, shell=True)

    else:
      batchmanager.send_job( command,"mR{}".format(sigmean), outFolder )
      print("submitted for {}\n\n".format(sigmean))
    
