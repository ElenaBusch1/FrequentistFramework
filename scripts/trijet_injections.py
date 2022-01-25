import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os

#. scripts/setup_buildAndFit.sh
dosignal=1
dolimit=1

fitFunction = config.fitFunctions["fourPar"]["Config"]
cdir = config.cdir
channelName="BkgLow_3_alpha0_SR1_tagged"
outputdir = channelName
if not os.path.exists(outputdir):
      os.makedirs(outputdir)

sigmeans = [550, 650]
#sigamps = [0, 1]
sigamps = [1]
rangelow=300
rangehigh=1200

# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
pdInputFile = config.getFileName("PostFit_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
pdFile = config.getFileName("PD_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
pdHistName = "pseudodata"
generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit", nreplicas=config.nToys, scaling=1,outfile=pdFile, outhist=pdHistName)


for sigmean in sigmeans:
  for sigamp in sigamps:
    sigwidth=7
    nbkg="1E7,0,1E8"
    topfile=config.samples[channelName]["topfile"]
    categoryfile=config.samples[channelName]["categoryfile"]
    dataFile=config.samples[channelName]["inputFile"]

    # Output file names, which will be written to outputdir
    wsfile = config.getFileName("FitResult_sigPlusBkg_1GeVBin_GlobalFit", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"
    outputfile = config.getFileName("FitResult_sigPlusBkg", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"
    binedges=[300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200]


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
           rangelow=rangelow,
           rangehigh=rangehigh,
           outputfile=outputfile,
           dosignal = dosignal,
           dolimit = dolimit,
           loopstart=0,
           loopend=config.nToys-1,
           rebinedges=binedges,
           rebinfile=None,
           rebinhist=None,
           maskthreshold=0.01,
           outdir=outputdir,
          )





