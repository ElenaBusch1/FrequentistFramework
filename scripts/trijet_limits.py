import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os

#. scripts/setup_buildAndFit.sh
dosignal=1
dolimit=1

pdFitName = "sixPar"
fitName = "fiveParV3"
#fitFunction = config.fitFunctions["fourPar"]["Config"]
fitFunction = config.fitFunctions[fitName]["Config"]
cdir = config.cdir
#channelName="BkgLow_2_alpha0_SR1_tagged"
channelName="PtOrdered2"
outputdir = channelName
if not os.path.exists(outputdir):
      os.makedirs(outputdir)

#sigmeans = [350, 450, 550, 650, 750, 850]
#sigmeans = [450, 550, 650, 750, 850]
#sigmeans = [450, 550, 650, 750, 850]
sigmeans = [650]
#sigmeans = [0]
#sigmeans = [850]
#sigamps = [0, 1, 5]
#sigamps = [1, 2, 5]
sigamps = [1]
sigwidth=7

rangelow=200
rangehigh=900

# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
pdInputFile = config.getFileName("PostFit_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"

pdHistName = "pseudodata"


for sigmean in sigmeans:
  for sigamp in sigamps:
    nbkg="1E7,0,1E8"
    nsig="0,0,1e6"

    topfile=config.samples[channelName]["topfile"]
    categoryfile=config.samples[channelName]["categoryfile"]
    dataFile=config.samples[channelName]["inputFile"]

    # Output file names, which will be written to outputdir
    wsfile = config.getFileName("FitResult_limits_1GeVBin_GlobalFit", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"
    outputfile = config.getFileName("FitResult_limits", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"
    outputstring = "FitResult_limits_%d_%d"%(sigamp, sigmean)
    #binedges = config.getBinning(rangelow, rangehigh, delta=25)
    binedges = None


    # Then run the injection
    run_injections_anaFit.run_injections_anaFit(
           datafile=pdFile, 
           datahist=pdHistName,
           categoryfile=categoryfile,
           topfile=topfile,
           fitFunction=fitFunction,
           cdir=cdir,
           wsfile=wsfile,
           sigmean=sigmean,
           sigwidth=sigwidth,
           sigamp=sigamp,
           nbkg=nbkg,
           nsig=nsig,
           rangelow=rangelow,
           rangehigh=rangehigh,
           outputfile=outputfile,
           outputstring=outputstring,
           dosignal = dosignal,
           dolimit = dolimit,
           loopstart=0,
           loopend=config.nToys,
           #loopend=5,
           rebinedges=binedges,
           rebinfile=None,
           rebinhist=None,
           maskthreshold=-0.01,
           outdir=outputdir,
          )





