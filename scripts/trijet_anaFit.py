import scripts.config as config
import python.run_anaFit as run_anaFit
import os


# May want to loop over these at some point?
cdir = config.cdir
channelName="BkgLow_3_alpha0_SR1_tagged"
#rangeslow=[200, 250, 275, 300, 350, 400]
#rangeshigh=[1000, 1200, 1400]

rangeslow=[300]
#rangeshigh=[1000]
rangeshigh=[900]

for rangelow in rangeslow:
  for rangehigh in rangeshigh:

    fitFunction = config.fitFunctions["fivePar"]["Config"]
    #fitFunction = config.fitFunctions["sixPar"]["Config"]

    nbkg="1E7,0,1E8"
    topfile=config.samples[channelName]["topfile"]
    categoryfile=config.samples[channelName]["categoryfile"]
    dataFile=config.samples[channelName]["inputFile"]
    datahist=config.samples[channelName]["histname"]

    # Output file names, which will be written to outputdir
    wsfile = config.getFileName("FitResult_1GeVBin_GlobalFit", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    outputfile = config.getFileName("FitResult_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    #binedges = config.getBinning(rangelow, rangehigh, delta=25)


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
           outputstring="",
           rangelow=rangelow,
           rangehigh=rangehigh,
           outputfile=outputfile,
           #rebinEdges=binedges,
           maskthreshold=-0.01,
           dosignal=0,
           dolimit=0,)


