import scripts.config as config
import python.run_anaFit as run_anaFit
import os

cdir = config.cdir

#channelNames = [ ["nixon_4j_alpha9"], ]
channelNames = [ ["nixon_4j_alpha0", "nixon_4j_alpha1", "nixon_4j_alpha2", "nixon_4j_alpha3", "nixon_4j_alpha4", "nixon_4j_alpha5", "nixon_4j_alpha6", "nixon_4j_alpha7", "nixon_4j_alpha8", "nixon_4j_alpha9", "nixon_4j_alpha10", "nixon_4j_alpha11", "nixon_4j_alpha12"], ]
#channelNames = [ ["nixon_4j_alpha10", "nixon_4j_alpha11", "nixon_4j_alpha12"], ]
#channelNames = [ ["nixon_4j_alpha12"], ]
#fitNames = ["threePar", "fourPar", "fivePar", "sixPar"]
#fitNames = ["threePar"]
#fitNames = ["fourPar"]
#fitNames = ["fivePar"]
fitNames = ["sixPar"]


for channelName in channelNames:
  for fitName in fitNames:
        #nbkg="1E7,0,5E8"
        nbkg="5E4,0,5E6"
        # These should all use the same top file
        topfile=config.samples[channelName[0]]["topfile"]
  
        outputdir = "fitsNixon"
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
               )
  

