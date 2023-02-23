import scripts.config as config
import python.run_anaFit as run_anaFit
import os

cdir = config.cdir


channelNames = [ ["hybrid10_yxxjjjj_4j_alpha0"],[ "hybrid10_yxxjjjj_4j_alpha1"],[ "hybrid10_yxxjjjj_4j_alpha2"],[ "hybrid10_yxxjjjj_4j_alpha3"],[ "hybrid10_yxxjjjj_4j_alpha4"],[ "hybrid10_yxxjjjj_4j_alpha5"],[ "hybrid10_yxxjjjj_4j_alpha6"],[ "hybrid10_yxxjjjj_4j_alpha7"],[ "hybrid10_yxxjjjj_4j_alpha8"],[ "hybrid10_yxxjjjj_4j_alpha9"],[ "hybrid10_yxxjjjj_4j_alpha10"],[ "hybrid10_yxxjjjj_4j_alpha11"], ]
#channelNames = [ [ "hybrid10_yxxjjjj_4j_alpha2"],]


fitNames = ["threePar", "fourPar", "fivePar",]
#fitNames = ["threePar", "fourPar", "fivePar", "sixPar"]
#fitNames = ["threePar"]
#fitNames = ["fourPar"]
#fitNames = ["fivePar"]
#fitNames = ["sixPar"]


for channelName in channelNames:
  for fitName in fitNames:
        nbkg="1E4,0,3E5"
        # These should all use the same top file
        topfile=config.samples[channelName[0]]["topfile"]
  
        outputdir = "fitsHybrid_%s"%channelName[0]
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
  

