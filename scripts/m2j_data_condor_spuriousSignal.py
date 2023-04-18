import config as config
import os

cdir = config.cdir

pdFitName = "fiveParM2j"
fitName = "fourParM2j"
#allChannelNames = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11],]
allChannelNames = [[5],]
overallName = "fitsData_" 
signalfile =  "crystalBallHistNoSyst"
#signalfile =  "Gaussian"


pdHistName = "pseudodata"
sigmeans = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
#sigmeans = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, ]

#sigwidths = [5, 10, 15]
sigwidths = [10,]

for channelNames in allChannelNames:
  channelString = ""
  for channelName in channelNames:
    channelString = channelString + " %d"%(channelName)
  for sigmean in sigmeans:
    for sigwidth in sigwidths:
      cmd = "python -b "+cdir + "/scripts/m2j_data_spuriousSignal.py" +  \
                           " --pdFitName=" + pdFitName + \
                           " --fitName=" + fitName + \
                           " --signalFile=" + signalfile + \
                           " --channelNames " + channelString + \
                           " --sigmean=" + str(sigmean) +  \
                           " --sigwidth=" + str(sigwidth) +  \
                           " --doRemake=1 " \
                           " --isBatch=1"


      runfile = "batch/runSpuriousM2j_" + str(sigmean) + "_" + str(sigwidth) +  "_" + pdFitName + "_" + fitName + "_" + overallName + "_" + signalfile + "_%d"%(channelNames[0]) + ".sh"
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

