import scripts.config as config
import python.run_anaFitWithToys as run_anaFitWithToys
import python.generatePseudoData as generatePseudoData
import os

#. scripts/setup_buildAndFit.sh
dosignal=0
dolimit=0

#fitFunction = config.fitFunctions["fourPar"]["Config"]
fitFunction = config.fitFunctions["fivePar"]["Config"]
cdir = config.cdir
channelName="BkgLow_2_alpha0_SR1_tagged"
outputdir = channelName
if not os.path.exists(outputdir):
      os.makedirs(outputdir)

#sigmeans = [0, 350, 450, 550, 650, 750, 850]
sigmeans = [0]
#sigmeans = [850]
#sigamps = [0, 1, 5]
sigamps = [0]

rangelow=300
rangehigh=900

pdFile = config.getFileName("PD_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
pdHistName = "pseudodata"


for sigmean in sigmeans:
  for sigamp in sigamps:
    nbkg="1E7,0,1E8"
    nsig="0,0,1e6"

    topfile=config.samples[channelName]["topfile"]
    categoryfile=config.samples[channelName]["categoryfile"]
    dataFile=config.samples[channelName]["inputFile"]

    # Output file names, which will be written to outputdir
    wsfile = config.getFileName("FitResult_PD_bkgonly_1GeVBin_GlobalFit", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    outputfile = config.getFileName("FitResult_PD_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    outputstring = "FitResult_PD_bkgonly"
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
           outputstring="",
           rangelow=rangelow,
           rangehigh=rangehigh,
           outputfile=outputfile,
           #rebinEdges=binedges,
           maskthreshold=-0.01,
           dosignal=0,
           dolimit=0,)






