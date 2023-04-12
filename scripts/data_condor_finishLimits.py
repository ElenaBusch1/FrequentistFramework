import config as config
import os

cdir = config.cdir

signalfile =  config.cSignal
overallName = config.cSample

fitName = "fourPar"
#allChannelNames = [ ["Data_yxxjjjj_4j_alpha0"], ["Data_yxxjjjj_4j_alpha1"], ["Data_yxxjjjj_4j_alpha2"], ["Data_yxxjjjj_4j_alpha3"], ["Data_yxxjjjj_4j_alpha4"], ["Data_yxxjjjj_4j_alpha5"], ["Data_yxxjjjj_4j_alpha6"], ["Data_yxxjjjj_4j_alpha7"], ["Data_yxxjjjj_4j_alpha8"], ["Data_yxxjjjj_4j_alpha9"], ["Data_yxxjjjj_4j_alpha10"], ["Data_yxxjjjj_4j_alpha11"], ]
#allChannelNames = [ ["Data_yxxjjjj_4j_alpha0"], ]
allChannelNames = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11],]

#signalfile =  "Gaussian"
signalfile =  "crystalBallHist"
coutputdir = "fitsData"

sigmeans = [2000, 2250, 2500, 2750, 3000, 3250, 3500,3750, 4000,4250, 4500,4750, 5000,5250, 5500,5750, 6000,6250, 6500,6750, 7000,7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]
sigwidths = [10]


for channelNames in allChannelNames:
  channelString = ""
  for channelName in channelNames:
    channelString = channelString + " %d"%(channelName)


  for sigmean in sigmeans:
      for sigwidth in sigwidths:

        cmd = "python -b "+cdir + "/scripts/data_makeLimits.py" +  \
                           " --fitName=" + fitName + \
                           " --signalFile=" + signalfile + \
                           " --channelNames " + channelString + \
                           " --sigmean=" + str(sigmean) +  \
                           " --sigwidth=" + str(sigwidth) +  \
                           " --outputdir=" + overallName +  \
                           " --doRemake=1 " \
                           " --isBatch=1"


        runfile = "batch/runLimits_" + str(sigmean) + "_" + str(sigwidth)  + "_" + signalfile + "_" + overallName + "_%d"%(channelNames[0]) + ".sh"
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
        fsubcondor.write('+JobFlavour        = "tomorrow"\n')
        fsubcondor.write('stream_output = TRUE\n')
        fsubcondor.write('stream_error = TRUE\n')
        fsubcondor.write('\nqueue 1\n')
        fsubcondor.close()

        subcmd = "condor_submit "+fsubcondorname
        os.system(subcmd)
        print "Job submitted"

