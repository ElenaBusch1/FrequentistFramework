import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os
import python.run_anaFitWithToys as run_anaFitWithToys


#. scripts/setup_buildAndFit.sh
dosignal=1
dolimit=0

#pdFitNames = ["fivePar", "sixPar"]
pdFitNames = ["sixPar"]
#pdFitNames = ["fivePar"]
#pdFitName = "fiveParV2"
#fitName = "fourPar"
fitName = "fiveParV3"
fitFunction = config.fitFunctions[fitName]["Config"]
cdir = config.cdir
#channelNames=["BkgLow_2_alpha0_SR1_tagged", "BkgLow_3_alpha0_SR1_tagged"]
#channelNames=["MassOrdered_2"]
channelNames=["PtOrdered2"]

#sigmeans = [350, 450, 550, 650, 750, 850]
#sigmeans = [450, 550, 650, 750, 850]
sigmeans = [250]
sigamps = [0]
sigwidth=7

rangelow=200
rangehigh=900
binedges = config.getBinning(rangelow, rangehigh, delta=25)



for sigmean in sigmeans:
  for sigamp in sigamps:
    for pdFitName in pdFitNames:
      for channelName in channelNames:
        pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        pdHistName = "pseudodata"
        outputdir = channelName
        if not os.path.exists(outputdir):
              os.makedirs(outputdir)
        nbkg="1E7,0,1E8"
        nsig="0,-1e6,1e6"
        topfile=config.samples[channelName]["topfile"]
        categoryfile=config.samples[channelName]["categoryfile"]
        dataFile=config.samples[channelName]["inputFile"]

        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_spuriousSignal_1GeVBin_GlobalFit", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"
        outputfile = config.getFileName("FitResult_spuriousSignal_%s_%s"%(pdFitName, fitName), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"

        # Then run the injection
        #run_injections_anaFit.run_injections_anaFit(
        run_anaFitWithToys.run_anaFit(
               datafile=pdFile, 
               datahist=pdHistName,
               categoryfile=categoryfile,
               topfile=topfile,
               fitFunction=fitFunction,
               cdir=cdir,
               wsfile=wsfile,
               sigmean=sigmean,
               sigwidth=sigwidth,
               #sigamp=sigamp,
               nbkg=nbkg,
               rangelow=rangelow,
               rangehigh=rangehigh,
               outputfile=outputfile,
               outputstring="SS_%s_%s_%d_%d_%d"%(pdFitName, fitName, sigmean, sigamp, rangehigh),
               dosignal = dosignal,
               dolimit = dolimit,
               nsig=nsig,
               #loopstart=0,
               #loopend=config.nToys,
               ntoys=config.nToys,
               #rebinedges=binedges,
               #rebinfile=None,
               #rebinhist=None,
               maskthreshold=-0.01,
               outdir=outputdir,
              )





