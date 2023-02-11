import scripts.config as config
import python.run_anaFit as run_anaFit
import os

cdir = config.cdir


#tenPercentData_2javg_alpha11
#channelNames = [ ["tenPercentData_2javg_alpha0"],[ "tenPercentData_2javg_alpha1"],[ "tenPercentData_2javg_alpha2"],[ "tenPercentData_2javg_alpha3"],[ "tenPercentData_2javg_alpha4"],[ "tenPercentData_2javg_alpha5"],[ "tenPercentData_2javg_alpha6"],[ "tenPercentData_2javg_alpha7"],[ "tenPercentData_2javg_alpha8"],[ "tenPercentData_2javg_alpha9"],[ "tenPercentData_2javg_alpha10"],[ "tenPercentData_2javg_alpha11"], ]
channelNames = [ ["tenPercentData_2javg_alpha8"],]

#channelNames = [ ["sherpa_yxxjjjj_2javg_alpha0"],[ "sherpa_yxxjjjj_2javg_alpha1"],[ "sherpa_yxxjjjj_2javg_alpha2"],[ "sherpa_yxxjjjj_2javg_alpha3"],[ "sherpa_yxxjjjj_2javg_alpha4"],[ "sherpa_yxxjjjj_2javg_alpha5"],[ "sherpa_yxxjjjj_2javg_alpha6"],[ "sherpa_yxxjjjj_2javg_alpha7"],[ "sherpa_yxxjjjj_2javg_alpha8"],[ "sherpa_yxxjjjj_2javg_alpha9"],[ "sherpa_yxxjjjj_2javg_alpha10"],[ "sherpa_yxxjjjj_2javg_alpha11"], ]
#fitNames = ["threePar", "fourPar", "fivePar", "sixPar"]
#fitNames = ["threeParM2j", "fourParM2j", "fiveParM2j"]
#fitNames = ["fourParM2j",]
fitNames = ["fiveParM2j",]
#fitNames = ["threePar"]
#fitNames = ["fourPar"]
#fitNames = ["fivePar"]
#fitNames = ["sixPar"]


for channelName in channelNames:
  for fitName in fitNames:
        nbkg="1E3,0,1E4"
        # These should all use the same top file
        topfile=config.samples[channelName[0]]["topfile"]
  
        outputdir = "fits2javg_10data_%s"%channelName[0]
        #outputdir = "fits_%s"%channelName[0]
        #outputdir = "fitsSherpa_%s"%channelName[0]
        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_%s_1GeVBin_GlobalFit"%(fitName), cdir + "/scripts/", None, outputdir) + ".root"
        outputfile = config.getFileName("FitResult_%s_bkgonly"%(fitName), cdir + "/scripts/", None, outputdir) + ".root"

        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        run_anaFit.run_anaFit(
               datahist=channelName,
               topfile=topfile,
               fitFunction=fitName,
               cdir=cdir ,
               wsfile=wsfile,
               nbkg=nbkg,
               ntoys = 0,
               outdir=outputdir,
               outputstring="%s"%(fitName),
               outputfile=outputfile,
               signalfile="Gaussian",
               maskthreshold=-0.01,
               dosignal=0,
               dolimit=0,
               useSysts = False,
               )
  

