import scripts.config as config
import python.run_anaFit as run_anaFit
import os


# May want to loop over these at some point?
cdir = config.cdir
#channelNames=["BkgLow_2_alpha0_SR1_tagged", "BkgLow_3_alpha0_SR1_tagged"]
#channelNames=["MassOrdered_2"]
#channelNames=["PtOrdered5Tagged"]
channelNames=["PtOrdered6"]
#channelNames = ["PtOrderedSR1_tagged"]
#rangeslow=[200, 250, 275, 300, 350, 400]
#rangeshigh=[700, 800, 900, 1000, 1200, 1400]
#rangeslow=[150, 200, 300]
#rangeshigh=[800, 900]
rangeslow=[200]
rangeshigh=[900]
#rangeslow=[150, 200, 300]
#rangeshigh=[700, 800, 900, 1000, 1100]

#channelName="BkgMid_2_alpha0_SR2_tagged"
##rangeslow=[200, 250, 275, 300, 350, 400]
##rangeshigh=[700, 800, 900, 1000, 1200, 1400]
#rangeslow=[550]
#rangeshigh=[1050]

#channelNames = ["PtOrderedSR2_tagged"]
#rangeslow=[600, 700]
#rangeshigh=[1200, 1500]


#fitNames = ["fourPar", "fivePar", "fiveParV3", "sixPar"]
fitNames = ["fourPar", "fivePar", "sixPar"]
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

        run_anaFit.run_anaFit(
               datafile=dataFile, 
               datahist=datahist,
               categoryfile=categoryfile,
               topfile=topfile,
               fitFunction=fitFunction,
               cdir=cdir ,
               wsfile=wsfile,
               nbkg=nbkg,
               outdir=outputdir,
               outputstring="%s"%(fitName),
               rangelow=rangelow,
               rangehigh=rangehigh,
               outputfile=outputfile,
               maskthreshold=-0.01,
               dosignal=0,
               dolimit=0,)
  

