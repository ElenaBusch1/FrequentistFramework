import scripts.config as config
import python.run_anaFit as run_anaFit
import os


# May want to loop over these at some point?
cdir = config.cdir
#channelNames=["BkgLow_2_alpha0_SR1_tagged", "BkgLow_3_alpha0_SR1_tagged"]
#channelNames = ["test3"]

channelNames=["mj2j3", "mjjmin", "mjjmindphi"]
#channelNames=["Btagged70_23_ystar", "Btagged70_jj_ystar", "Btagged70_23", "Btagged70_jj", "ZeroBtagged70_23_ystar", "ZeroBtagged70_jj_ystar", "ZeroBtagged70_23", "ZeroBtagged70_jj"]
#channelNames=["ZeroBtagged70_23_ystar", "ZeroBtagged70_jj_ystar", "ZeroBtagged70_23", "ZeroBtagged70_jj"]
#channelNames=["ZeroBtagged70_23_ystar"]
#channelNames = ["PtOrderedSR1_tagged"]
#rangeslow=[200, 250, 275, 300, 350, 400]
#rangeshigh=[700, 800, 900, 1000, 1200, 1400]
#rangeslow=[150, 200, 300]
rangeslow=[200]
rangeshigh = [1200]


#channelNames=["ambulance_2javg"]
#rangeslow=[800]
#rangeshigh=[3500]
#fitNames = ["threeParAmb", "fourParAmb"]

#channelNames=["ambulance_4jMCErr"]
#rangeslow=[2000]
#rangeshigh=[9000]
#fitNames = ["threeParAmb", "fourParAmb", "fiveParAmb"]
#fitNames = ["fiveParAmb", "fiveParAmbMod", "fiveParAmbPow"]
#fitNames = ["sixParAmb"]




#fitNames = ["fourPar", "fivePar", "fiveParV3", "sixPar"]
fitNames = ["fourPar", "fivePar", "sixPar"]
#fitNames = ["fourPar", "fivePar", "fiveParV2", "sixPar"]
#fitNames = ["fiveParAmbPow"]
#fitNames = ["threeParAmb", "fourParAmb", "fiveParAmb", "sixParAmb"]
#fitNames = ["UA2"]
#fitNames = ["threePar"]
#fitNames = ["sixPar"]
#fitNames = ["sevenPar"]
#fitNames = ["fivePar"]
#fitNames = ["fourPar"]

for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    for fitName in fitNames:
      for channelName in channelNames:
        fitFunction = config.fitFunctions[fitName]["Config"]

        nbkg="1E7,0,5E8"
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
               fitFunction=fitName,
               cdir=cdir ,
               wsfile=wsfile,
               nbkg=nbkg,
               ntoys = 0,
               outdir=outputdir,
               outputstring="%s"%(fitName),
               rangelow=rangelow,
               rangehigh=rangehigh,
               outputfile=outputfile,
               signalfile="Gaussian",
               maskthreshold=-0.01,
               dosignal=0,
               dolimit=0,
               )
  

