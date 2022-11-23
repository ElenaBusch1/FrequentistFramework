import scripts.config as config
import python.run_anaFit as run_anaFit
import os

cdir = config.cdir


channelNames = [ ["yxxjjjj_2javg_alpha0"],[ "yxxjjjj_2javg_alpha1"],[ "yxxjjjj_2javg_alpha2"],[ "yxxjjjj_2javg_alpha3"],[ "yxxjjjj_2javg_alpha4"],[ "yxxjjjj_2javg_alpha5"],[ "yxxjjjj_2javg_alpha6"],[ "yxxjjjj_2javg_alpha7"],[ "yxxjjjj_2javg_alpha8"],[ "yxxjjjj_2javg_alpha9"],[ "yxxjjjj_2javg_alpha10"],[ "yxxjjjj_2javg_alpha11"], ]

#channelNames = [ ["sherpa_yxxjjjj_2javg_alpha0"],[ "sherpa_yxxjjjj_2javg_alpha1"],[ "sherpa_yxxjjjj_2javg_alpha2"],[ "sherpa_yxxjjjj_2javg_alpha3"],[ "sherpa_yxxjjjj_2javg_alpha4"],[ "sherpa_yxxjjjj_2javg_alpha5"],[ "sherpa_yxxjjjj_2javg_alpha6"],[ "sherpa_yxxjjjj_2javg_alpha7"],[ "sherpa_yxxjjjj_2javg_alpha8"],[ "sherpa_yxxjjjj_2javg_alpha9"],[ "sherpa_yxxjjjj_2javg_alpha10"],[ "sherpa_yxxjjjj_2javg_alpha11"], ]
#fitNames = ["threePar", "fourPar", "fivePar", "sixPar"]
fitNames = ["threePar", "fourPar", "fivePar"]
#fitNames = ["threePar"]
#fitNames = ["fourPar"]
#fitNames = ["fivePar"]
#fitNames = ["sixPar"]


for channelName in channelNames:
  for fitName in fitNames:
        nbkg="5E6,0,5E8"
        # These should all use the same top file
        topfile=config.samples[channelName[0]]["topfile"]
  
        outputdir = "fits2javg_%s"%channelName[0]
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
  

