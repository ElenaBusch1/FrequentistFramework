import scripts.config as config
import python.run_fitRangeFinder as run_fitRangeFinder
import os


# May want to loop over these at some point?
cdir = config.cdir
#channelNames=["BkgLow_2_alpha0_SR1_tagged", "BkgLow_3_alpha0_SR1_tagged"]
#channelNames=["MassOrdered_2"]
channelNames=["PtOrdered6"]
#channelNames=["Btagged70_23_ystar", "Btagged70_jj_ystar", "Btagged70_23", "Btagged70_jj"]
#channelNames=["ZeroBtagged70_23_ystar", "ZeroBtagged70_jj_ystar", "ZeroBtagged70_23", "ZeroBtagged70_jj"]
#channelNames = ["PtOrderedSR1_tagged"]
#rangeslow=[200, 250, 275, 300, 350, 400]
#rangeshigh=[700, 800, 900, 1000, 1200, 1400]
#rangeslow=[150, 200, 300]
#rangeshigh=[800, 900]
rangeslow=[140]
rangeshigh=[1000]
#rangeshigh=[1000, 1200]



#fitNames = ["fourPar", "fivePar", "fiveParV3", "sixPar"]
#fitNames = ["fourPar", "fivePar", "sixPar", "sevenPar"]
#fitNames = ["fourPar", "fivePar", "fiveParV2", "sixPar"]
#fitNames = ["fourPar", "fivePar", "sixPar"]
fitNames = ["fourPar"]
#fitNames = ["UA2"]
#fitNames = ["threePar"]
#fitNames = ["sixPar"]
#fitNames = ["fivePar"]
#fitNames = ["fiveParV2"]

for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    for fitName in fitNames:
      for channelName in channelNames:
        fitFunction = config.fitFunctions[fitName]["Config"]

        nbkg="1E7,0,1E8"
        topfile=config.samples[channelName]["topfile"]
        categoryfile=config.samples[channelName]["categoryfile"]
        dataFile=config.samples[channelName]["inputFile"]
        datahist=config.samples[channelName]["histname"]
  
        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_%s_1GeVBin_GlobalFit"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        outputfile = config.getFileName("FitResult_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    
        outputdir = channelName
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        run_fitRangeFinder.run_fitRangeFinder(
               datafile=dataFile, 
               datahist=datahist,
               categoryfile=categoryfile,
               topfile=topfile,
               fitFunction=fitName,
               cdir=cdir ,
               wsfile=wsfile,
               nbkg=nbkg,
               outdir=outputdir,
               outputstring="%s"%(fitName),
               rangelow=rangelow,
               rangehigh=rangehigh,
               minWindow = 500,
               pvalMin = 0.05,
               deltaWindow = 20,
               outputfile=outputfile,
               signalfile="Gaussian",
               maskthreshold=-0.01,
               )
  

