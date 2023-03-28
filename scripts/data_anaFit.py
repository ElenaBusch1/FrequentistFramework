import scripts.config as config
import python.run_anaFit as run_anaFit
import os

cdir = config.cdir


channelNames = [ ["Data_yxxjjjj_4j_alpha0"],[ "Data_yxxjjjj_4j_alpha1"],[ "Data_yxxjjjj_4j_alpha2"],[ "Data_yxxjjjj_4j_alpha3"],[ "Data_yxxjjjj_4j_alpha4"],[ "Data_yxxjjjj_4j_alpha5"],[ "Data_yxxjjjj_4j_alpha6"],[ "Data_yxxjjjj_4j_alpha7"],[ "Data_yxxjjjj_4j_alpha8"],[ "Data_yxxjjjj_4j_alpha9"],[ "Data_yxxjjjj_4j_alpha10"],[ "Data_yxxjjjj_4j_alpha11"], ]
#channelNames = [ [ "Data_yxxjjjj_4j_alpha11"], ]


#fitNames = ["threePar", "fourPar", "fivePar"]
#fitNames = ["threePar"]
fitNames = ["fourPar"]
#fitNames = ["fivePar"]


for channelName in channelNames:
  for fitName in fitNames:
        nbkg="1E4,0,3E6"
        # These should all use the same top file
        topfile=config.samples[channelName[0]]["topfile"]
  
        outputdir = "fitsData_%s"%channelName[0]
        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_%s_1GeVBin_GlobalFit"%(fitName), cdir + "/scripts/", None, outputdir) + ".root"
        outputfile = config.getFileName("FitResult_%s_bkgonly"%(fitName), cdir + "/scripts/", None, outputdir) + ".root"
        binedges = config.getBinningFromFile(channelName[0])


        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        run_anaFit.run_anaFit(
               datahist=channelName,
               topfile=topfile,
               fitFunction=fitName,
               cdir=cdir ,
               wsfile=wsfile,
               nbkg=nbkg,
               #ntoys = 0,
               outdir=outputdir,
               rebinEdges=binedges,
               outputstring="%s"%(fitName),
               outputfile=outputfile,
               signalfile="Gaussian",
               maskthreshold=-0.01,
               dosignal=0,
               dolimit=0,
               useSysts = False,
               rebinOnlyBH = True,
               )
  

