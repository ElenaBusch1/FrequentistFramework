import config as config
import os

cdir = config.cdir

pdFitName = config.cPDFitName
fitName = config.cFitName
channelNames=config.cChannelNames
signalfile =  config.cSignal
overallName = config.cSample 

pdHistName = "pseudodata"
sigmeans = [2000, 3000, 4000, 5000, 6000, 7000, 8000]
sigwidths = [10]

channelString = ""
for channelName in channelNames:
  channelString = channelString + " " + channelName


for sigmean in sigmeans:
  for sigwidth in sigwidths:
      cmd = "python -b "+cdir + "/scripts/nixon_spuriousSignal.py" +  \
                           " --pdFitName=" + pdFitName + \
                           " --fitName=" + fitName + \
                           " --signalFile=" + signalfile + \
                           " --channelNames " + channelString + \
                           " --sigmean=" + str(sigmean) +  \
                           " --sigwidth=" + str(sigwidth) +  \
                           " --outputdir=" + overallName +  \
                           " --doRemake=0 " \
                           " --isBatch=1"


      runfile = "batch/runSpurious_" + str(sigmean) + "_" + str(sigwidth) +  "_" + pdFitName + "_" + fitName + "_" + overallName + "_" + signalfile + ".sh"
      fr=open(runfile,'w')
      fr.write('#!/bin/sh\n')
      fr.write('export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
      fr.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
      fr.write('cd '+cdir +'\n')
      fr.write('echo $PWD \n')
      fr.write('source ' + cdir + '/scripts/setup_buildAndFit.sh \n')
      fr.write('cd '+cdir + "/scripts/"+'\n')
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
      fsubcondor.write('+JobFlavour        = "longlunch"\n')
      fsubcondor.write('stream_output = TRUE\n')
      fsubcondor.write('stream_error = TRUE\n')
      fsubcondor.write('\nqueue 1\n')
      fsubcondor.close()

      subcmd = "condor_submit "+fsubcondorname
      os.system(subcmd)
      print "Job submitted"

