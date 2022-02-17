import scripts.config as config
import python.run_anaFitWithToys as run_anaFitWithToys
import python.generatePseudoData as generatePseudoData
import os

#. scripts/setup_buildAndFit.sh
dosignal=0
dolimit=0

pdFitNames = ["sixPar"]
#pdFitNames = ["fivePar", "sixPar"]
#pdFitNames = ["fourPar", "fivePar", "fiveParV2", "sixPar"]

#pdFitName = "fivePar"

fitName = "fiveParV3"
cdir = config.cdir
#channelNames=["BkgLow_2_alpha0_SR1_tagged", "BkgLow_3_alpha0_SR1_tagged"]
channelNames = ["PtOrdered2"]


sigmeans = [0]
sigamps = [0]

rangelow=200
rangehigh=900


for sigmean in sigmeans:
  for sigamp in sigamps:
    for pdFitName in pdFitNames:
      for channelName in channelNames:
        outputdir = channelName
        if not os.path.exists(outputdir):
              os.makedirs(outputdir)
        pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        fitFunction = config.fitFunctions[fitName]["Config"]
        pdHistName = "pseudodata"
        nbkg="1E7,0,1E8"
        nsig="0,0,1e6"

        topfile=config.samples[channelName]["topfile"]
        categoryfile=config.samples[channelName]["categoryfile"]
        dataFile=config.samples[channelName]["inputFile"]
    
        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_PD_bkgonly_1GeVBin_GlobalFit", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        outputfile = config.getFileName("FitResult_%s_PD_%s_bkgonly"%(pdFitName, fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        outputstring = "FitResult_%s_PD_%s_bkgonly"%(pdFitName, fitName)
        binedges = config.getBinning(rangelow, rangehigh, delta=25)


        run_anaFitWithToys.run_anaFit(
             datafile=pdFile,
             datahist=pdHistName,
             categoryfile=categoryfile,
             topfile=topfile,
             fitFunction=fitFunction,
             cdir=cdir ,
             wsfile=wsfile,
             nbkg=nbkg,
             ntoys=config.nToys,
             outdir=outputdir,
             outputstring=outputstring,
             rangelow=rangelow,
             rangehigh=rangehigh,
             outputfile=outputfile,
             #rebinEdges=binedges,
             maskthreshold=-0.01,
             dosignal=0,
             dolimit=0,)






