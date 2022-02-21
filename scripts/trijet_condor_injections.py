import config as config
import os

cdir = config.cdir

rangelow=200
rangehigh=900

pdHistName = "pseudodata"
pdFitName = "sixPar"
#pdFitName = "fiveParV2"
#fitName = "fiveParV3"
fitName = "fivePar"
channelName = "PtOrdered5"
sigmeans = [250, 350, 450, 550, 650, 750]
sigamps = [0,1,2,3,4,5]
sigwidths = [7]


for sigmean in sigmeans:
  for sigamp in sigamps:
    for sigwidth in sigwidths:

      cmd = "python -b "+cdir + "/scripts/trijet_injections.py" +  \
                           " --pdFitName=" + pdFitName + \
                           " --fitName=" + fitName + \
                           " --channelName=" + channelName + \
                           " --sigmean=" + str(sigmean) +  \
                           " --sigwidth=" + str(sigwidth) +  \
                           " --sigamp=" + str(sigamp) +  \
                           " --rangelow=" + str(rangelow) +  \
                           " --rangehigh=" + str(rangehigh) +  \
                           " --isBatch=1"


      runfile = "batch/runInjections_" + str(sigmean) + "_" + str(sigwidth) + "_" + str(sigamp) + ".sh"
      fr=open(runfile,'w')
      fr.write('#!/bin/sh\n')
      fr.write('export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
      fr.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
      fr.write('cd '+cdir +'\n')
      fr.write('echo $PWD \n')
      fr.write('source ' + cdir + '/scripts/setup_buildAndFit.sh \n')
      fr.write('cd '+cdir + "/scripts/"+'\n')
      #fr.write('lsetup \"root 6.14.04-x86_64-slc6-gcc62-opt\"\n')
      fr.write('export DISPLAY=\n')
      fr.write(cmd)
      fr.write('\n')
      fr.close()

      os.system('chmod a+x '+runfile)

      # Make a condor .job file for each foutname
      fsubcondorname = runfile.replace(".sh",".job")
      fsubcondor = open(fsubcondorname,"w")
      fsubcondor.write('Universe        = vanilla\n')
      fsubcondor.write('Executable      = '+runfile+'\n')
      fsubcondor.write('Output          = logs/'+runfile.replace('.sh','').split('/')[-1] +'_$(Cluster).$(Process).out\n')
      fsubcondor.write('Error           = logs/'+runfile.replace('.sh','').split('/')[-1] +'_$(Cluster).$(Process).err\n')
      fsubcondor.write('Log             = logs/'+runfile.replace('.sh','').split('/')[-1] +'_$(Cluster).$(Process).log\n')
      fsubcondor.write('+JobFlavour        = "workday"\n')
      fsubcondor.write('stream_output = TRUE\n')
      fsubcondor.write('stream_error = TRUE\n')
      fsubcondor.write('\nqueue 1\n')
      fsubcondor.close()

      subcmd = "condor_submit "+fsubcondorname
      os.system(subcmd)
      print "Job submitted"

