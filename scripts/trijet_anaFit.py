import scripts.config as config
import python.run_anaFit as run_anaFit
import os


# May want to loop over these at some point?
cdir = config.cdir
#channelNames = ["test3", "testSherpa", "sherpaReweight", "sherpaNoCut"]
#channelNames=["testSherpa_15"]
#channelNames=["Data18Partial", "Data15"]
#channelNames=["Data16"]
#channelNames=["test3New_15"]
#channelNames=["test3New_15_MCEffOnData"]
#channelNames = ["FullRun2Data"]
#channelNames = ["FullRun2Data_NoNN"]
#channelNames = ["test3New_15_dataEff", "test3New_15_data_mcEff"]
#channelNames = ["test3New_NoCut_no21"]
channelNames = ["FullRun2Data_NoNN_No21"]
#channelNames = ["test3New_15_data_mcEff"]
#channelNames = ["Data_m32"]
#channelNames = ["DataNoInsitu"]
#channelNames = ["DataMCJES"]
#channelNames = ["Data16_massAnd"]
#channelNames = ["Data16MCJES"]
#channelNames = ["Data_475_60"]
#channelNames = ["Data_minMass"]

#channelNames=["mj2j3", "mjjmin", "mjjmindphi"]
#rangeslow = [225]
rangeslow = [225]
rangeshigh = [1000, ]

#fitNames = ["fourPar", "fivePar", "sixPar"]
#fitNames = ["fivePar", "sixPar"]
#fitNames = ["fourPar"]
fitNames = ["fivePar"]
#fitNames = ["sixPar"]
#fitNames = ["sevenPar"]

for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    for fitName in fitNames:
      for channelName in channelNames:
        fitFunction = config.fitFunctions[fitName]["Config"]

        nbkg="3E7,0,1E8"
        #nbkg="1E5,0,5E6"
        topfile=config.samples[channelName]["topfile"]
        categoryfile=config.samples[channelName]["categoryfile"]
        dataFile=config.samples[channelName]["inputFile"]
        datahist=config.samples[channelName]["histname"]
  
        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_%s_1GeVBin_GlobalFit"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        outputfile = config.getFileName("FitResult_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        #binedges = config.getBinning(rangelow, rangehigh, 25)
        binedges = config.getBinning(rangelow, rangehigh)

    
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
               histName = channelName,
               maskthreshold=-0.05,
               dosignal=0,
               dolimit=0,
               rebinEdges=binedges,
               rebinOnlyBH = True,
               )

  

