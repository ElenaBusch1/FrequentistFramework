#!/usr/bin/env python

import subprocess, os, sys
from condor_handler import CondorHandler

useBatch = True
runData  = True
quietMode = False

# Range of fit:
low="531"
#high="2058"
high ="2997"

# xml template cards:
topfile = "config/dijetTLA/dijetTLA_J100yStar06_zprime.template"
categoryfile = "config/dijetTLA/category_dijetTLA_J100yStar06_fivePar_zprime.template"

sigmeans = [ 550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,1650,1700,1750,1800,1850,1900,1950,2000]
#sigmeans = ["bOnly"]
sigwidth=-999
doLimit = True

# Output folder -- where everything is stored:
# default in python/run_anaFit.py is run/
outFolder = "run/Zprimes_10022022_extendedRange_muScan20/"

if runData:
  # Running on Data:
  
  # Original data file, for plotting script
  datafile = "Input/data/dijetTLA/lookInsideTheBoxWithUniformMjj.root"
  datahist = "Nominal/DSJ100yStar06_TriggerJets_J100_yStar06_mjj_finebinned_all_data"
  nbkg="2E8,0,3E8"

else:
  # Running on PD for tests

  datafile = "datafile=Input/data/dijetTLA/PD_130ifb_GlobalFit_531_2079_fivepar_finebinned_J100.root"
  datahist = "pseudodata"
  # 130ifb
  nbkg="9E8,0,15E8"
  # 0 for no signal injection
  sigamp=0
  loopstart=0
  loopend=9

  # spurious test:
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

 
#######################################################3
# PREPARE COMMAND LINE: 

if useBatch:
  # In condor I store everything in an output/ folder and at the end I copy everything from $Condor/output to outFolder/
  folder = 'output/'
else:
  folder = outFolder

for sigmean in sigmeans:
  
  # WS file name for xmlAnaWSBuilder:
  wsfile= folder + "dijetTLA_combWS_{}_gq0p1.root"
  # Output file name for quickFit:
  outputfile = folder + "FitResult_fivePar_J100yStar_{}.root"


  if sigmean == "bOnly":
    wsfile = wsfile.format("bOnly")
    outputfile = outputfile.format("bOnly")
    doSignal = False
    doLimit = False
    # dummy signal mass point: won't do any s+b fit
    sigmean = 1000
  else:
    wsfile = wsfile.format("mR"+str(sigmean))
    outputfile = outputfile.format("mR"+str(sigmean))
    doSignal = True

  command = "python python/run_anaFit.py --datafile {0} --datahist {1} --topfile {2} --categoryfile {3} --wsfile {4} --outputfile {5} --nbkg {6} --rangelow {7} --rangehigh {8} --sigmean {9} --sigwidth {10} --folder {11}".format(datafile, datahist, topfile, categoryfile, wsfile, outputfile, nbkg, low, high, sigmean, sigwidth, folder)

  if doSignal:
    command += " --dosignal "

  if doLimit:
    command += " --dolimit"

  #######################################################3
  # SUBMISSION:

  print "Submitting command:\n"
  print command

  if not quietMode:
    if not useBatch:
      # Not working properly, don't know why. Just run it beforehand
      #subprocess.call("bash scripts/setup_buildCombineFit.sh", shell=True)
      subprocess.call(command, shell=True)

    else:
      batchmanager.send_job( command,"mR{}".format(sigmean), outFolder )
      print("submitted for {}\n\n".format(sigmean))
    
