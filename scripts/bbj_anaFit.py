import scripts.config as config
import python.run_anaFit as run_anaFit
import os


# May want to loop over these at some point?
cdir = config.cdir
#channelNames=["btagFinal"]
#channelNames=["bbj_Data15Partial"]
channelNames=["bbj_Data"]

#channelNames=["btag_32"]
#channelNames=["Btagged70_23"]
#channelNames=["Btagged70_23_ystar"]

#rangeslow=[160, 180, 200, 220, 240, 250]
#rangeshigh = [900, 1000, 1100, 1200]
#rangeshigh = [1250]
#rangeslow = [160]
#rangeslow = [170]
#rangeslow = [160]
#rangeshigh = [700]
#rangeslow = [200]
#rangeslow = [170]
#rangeshigh = [1000]
#rangeshigh = [700]
rangeslow = [160]
rangeshigh = [700]


#fitNames = ["fourPar", "fivePar"]
#fitNames = ["fourPar", "fivePar", "sixPar"]
#fitNames = ["UA2"]
#fitNames = ["threePar"]
#fitNames = ["fourPar"]
fitNames = ["fivePar"]
#fitNames = ["sixPar"]
#fitNames = ["sevenPar"]

for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    for fitName in fitNames:
      for channelName in channelNames:
        fitFunction = config.fitFunctions[fitName]["Config"]

        #nbkg="6E7,0,5E8"
        nbkg="1E6,0,1E7"
        topfile=config.samples[channelName]["topfile"]
        categoryfile=config.samples[channelName]["categoryfile"]
        dataFile=config.samples[channelName]["inputFile"]
        datahist=config.samples[channelName]["histname"]
  
        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_%s_1GeVBin_GlobalFit"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        outputfile = config.getFileName("FitResult_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        #binedges = config.getBinning(rangelow, rangehigh, 25)
        binedges = config.getBinning(rangelow, rangehigh)
        #outputstring = "FitResult_limits_%d_%d_%d_%s"%(0, sigmean, sigwidth, signalfile)
        #outputstring = "FitResult_limits_%d_%d_%d_%s"%(0, sigmean, sigwidth, signalfile)
        outputstring = config.getFileName("FitResult_%s_bkgonly"%(fitName), "", channelName, rangelow, rangehigh) + ".root"



    
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
               histName = channelName,
               outputfile=outputfile,
               signalfile="Gaussian",
               maskthreshold=-0.05,
               dosignal=0,
               dolimit=0,
               rebinEdges=binedges,
               rebinOnlyBH = True,
               )
  

