import scripts.config as config
import python.run_bumpHunt as run_bumpHunt
import os


from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument('--isBatch', dest='isBatch', type=int, default=0, help='Input data file')
parser.add_argument('--fitName', dest='fitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_argument('--pdFitName', dest='pdFitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_argument('--signalFile', dest='signalFile', type=str, default=None, help='Name of the signal file')
parser.add_argument('--channelNames', dest='channelNames', nargs='+', help='Output workspace file')
parser.add_argument('--sigmean', dest='sigmean', type=int, default=1000, help='Mean of signal Gaussian for s+b fit (in GeV)')
parser.add_argument('--sigwidth', dest='sigwidth', type=int, default=7, help='Width of signal Gaussian for s+b fit (in %)')
parser.add_argument('--sigamp', dest='sigamp', type=int, default=3, help='Amplitude of signal Gaussian for s+b fit (in %)')
parser.add_argument('--doRemake', dest='doRemake', type=int, default=0, help='Amplitude of signal Gaussian for s+b fit (in %)')
parser.add_argument('--outputdir', dest='outputdir', type=str, default="fitsNixon", help='Amplitude of signal Gaussian for s+b fit (in %)')
args = parser.parse_args()


if args.isBatch:
  pdFitName = args.pdFitName
  fitName = args.fitName
  channelNames = [args.channelNames]
  sigmeans = [args.sigmean]
  sigamps = [args.sigamp]
  sigwidths = [args.sigwidth]
  signalfile = args.signalFile
  outputdir = args.outputdir

else:
  #pdFitName = "sixPar"
  fitName = "fivePar"
  channelName="test3New_15"
  channelName = "FullRun2Data"


  sigmeans = [550]
  #sigamps = [1,2,3,4,5]
  sigamps = [5]
  sigwidths = [10]
  signalfile =  "Gaussian"
  outputdir = "fits_"
  args.doRemake=1
  rangelow = 200
  rangehigh = 900


#. scripts/setup_buildAndFit.sh
dosignal=1

cdir = config.cdir



for sigmean in sigmeans:
    for sigamp in sigamps:
      for sigwidth in sigwidths:
        nbkg="1E7,0,1e8"
        nsig="0,0,5e4"
        #pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + "_Sig_Gaussian.root"

        #pdHistName = "pseudodata"

        # Output file names, which will be written to outputdir
        #outputfile = config.getFileName("FitResult_bkgOnlyInjections_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"
        outputstring = "FitResult_m4j_injections_%d_%d_%d_%s"%(sigamp, sigmean, sigwidth, signalfile)
        binedges = config.getBinning(rangelow, rangehigh, delta=25)


        nbkg="6E7,0,1E8"
        topfile=config.samples[channelName]["topfile"]
        categoryfile=config.samples[channelName]["categoryfile"]
        dataFile=config.samples[channelName]["inputFile"]
        datahist=config.samples[channelName]["histname"]

        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_bumpHunt_%s_1GeVBin_GlobalFit"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        outputfile = config.getFileName("FitResult_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
        binedges = config.getBinning(rangelow, rangehigh, 25)


        outputdir = channelName
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)


        #sigamp=sigamp,
        # Then run the injection
        run_bumpHunt.run_anaFit(
             datafile = dataFile,
             datahist=channelName,
             cdir=cdir,
             sigmean=sigmean,
             sigwidth=sigwidth,
             nbkg=nbkg,
             nsig=nsig,
             outputfile=outputfile,
             outputstring=outputstring,
             dosignal = 0,
             dolimit = 0,
             rebinEdges=binedges,
             outdir=outputdir,
             doRemake = args.doRemake,
             useSysts = False,
            )





