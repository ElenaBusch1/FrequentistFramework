import scripts.config as config
import python.run_anaFit as run_anaFit
import os


# May want to loop over these at some point?
cdir = config.cdir

channelNames=["mj2j3", "mjjmin", "mjjmindphi"]
rangeslow=[200]
rangeshigh = [1200]
fitNames = ["fourPar", "fivePar", "sixPar"]
nbkg="1E7,0,5E8"

for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    for fitName in fitNames:
      for channelName in channelNames:
        topfile      = config.samples[channelName]["topfile"]
        categoryfile = config.samples[channelName]["categoryfile"]
        dataFile     = config.samples[channelName]["inputFile"]
        datahist     = config.samples[channelName]["histname"]
  
        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_%s_1GeVBin_GlobalFit"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        outputfile = config.getFileName("FitResult_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    
        outputdir = channelName
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        run_anaFit.run_anaFit(
               datafile=dataFile, 
               datahist=datahist,
               categoryfile=categoryfile,
               topfile=topfile,
               fitFunction=fitName,
               cdir=cdir ,
               wsfile=wsfile,
               nbkg=nbkg,
               ntoys = 0, # For the initial fit, we don't want to use toys
               outdir=outputdir,
               outputstring="%s"%(fitName),
               rangelow=rangelow,
               rangehigh=rangehigh,
               outputfile=outputfile,
               signalfile="Gaussian", # This doesn't matter for this
               maskthreshold=-0.01, # This should be changed if you actually want to apply masking
               dosignal=False,
               dolimit=False,
               )
  

