import config as config
import os

cdir = config.cdir

pdFitName = config.cPDFitName
fitName = config.cFitName
allChannelNames = [ ["yxxjjjj_4j_alpha0"],[ "yxxjjjj_4j_alpha1"],[ "yxxjjjj_4j_alpha2"],[ "yxxjjjj_4j_alpha3"],[ "yxxjjjj_4j_alpha4"],[ "yxxjjjj_4j_alpha5"],[ "yxxjjjj_4j_alpha6"],[ "yxxjjjj_4j_alpha7"],[ "yxxjjjj_4j_alpha8"],[ "yxxjjjj_4j_alpha9"],[ "yxxjjjj_4j_alpha10"],[ "yxxjjjj_4j_alpha11"], ]
#allChannelNames = [ [ "yxxjjjj_4j_alpha2"], ]
signalfile =  config.cSignal
overallName = config.cSample



#sigmeans = [3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
sigmeans = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
#sigmeans = [4000]
sigamps = [0,1,2,3,4,5]
#sigamps = [3]
#sigamps = [1]
sigwidths = [10]


for channelNames in allChannelNames:
  channelString = ""
  for channelName in channelNames:
    channelString = channelString + " " + channelName


  for sigmean in sigmeans:
    for sigamp in sigamps:
      for sigwidth in sigwidths:

        cmd = "python -b "+cdir + "/scripts/yxxjjjj_injections.py" +  \
                           " --pdFitName=" + pdFitName + \
                           " --fitName=" + fitName + \
                           " --signalFile=" + signalfile + \
                           " --channelNames " + channelString + \
                           " --sigmean=" + str(sigmean) +  \
                           " --sigwidth=" + str(sigwidth) +  \
                           " --sigamp=" + str(sigamp) +  \
                           " --outputdir=" + overallName +  \
                           " --doRemake=1 " \
                           " --isBatch=1"


        runfile = "batch/runInjections_" + str(sigmean) + "_" + str(sigwidth) + "_" + str(sigamp) + "_" + signalfile + "_" + overallName + "_" + channelNames[0] + ".sh"
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
