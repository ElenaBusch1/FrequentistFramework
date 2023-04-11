import scripts.config as config
import python.run_anaFit as run_anaFit
import os

cdir = config.cdir


#channelNames = [ ["Data_2javg_alpha0"],[ "Data_2javg_alpha1"],[ "Data_2javg_alpha2"],[ "Data_2javg_alpha3"],[ "Data_2javg_alpha4"],[ "Data_2javg_alpha5"],[ "Data_2javg_alpha6"],[ "Data_2javg_alpha7"],[ "Data_2javg_alpha8"],[ "Data_2javg_alpha9"],[ "Data_2javg_alpha10"],[ "Data_2javg_alpha11"], ]
channelNames = [[ "Data_2javg_alpha5"],]

#fitNames = ["threeParM2j", "fourParM2j", "fiveParM2j"]
fitNames = ["fiveParM2j",]
#fitNames = ["fourParM2j",]


for channelName in channelNames:
  for fitName in fitNames:
        nbkg="1E3,0,1E5"
        # These should all use the same top file
        topfile=config.samples[channelName[0]]["topfile"]
  
        outputdir = "fits2javg_data_%s"%channelName[0]
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
               outdir=outputdir,
               rebinEdges=binedges,
               outputstring="%s"%(fitName),
               outputfile=outputfile,
               signalfile="Gaussian",
               maskthreshold=0.05,
               dosignal=0,
               dolimit=0,
               useSysts = False,
               rebinOnlyBH = True,
               doRemake=True,
               )
  

