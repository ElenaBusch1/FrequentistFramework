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
  fitName = args.fitName
  channelNames = [args.channelNames]
  signalfile = args.signalFile
  coutputdir = args.outputdir

else:
  fitName = "fivePar"
  channelName = "FullRun2Data_NoNN_No21"


  signalfile =  "Gaussian"
  #coutputdir = "fitsData_"
  coutputdir = ""
  args.doRemake=1
  rangelow = 225
  rangehigh = 1000

dosignal=1
dolimit=0

cdir = config.cdir

nbkg="1E4,0,1e6"

#outputdir = "fitsData_%s"%channelName
outputdir = channelName
# Output file names, which will be written to outputdir
wsfile = config.getFileName("FitResult_%s_1GeVBin_GlobalFit"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"

outputfile = config.getFileName("FitResult_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
#binedges = config.getBinningFromFile(channelName)
binedges = config.getBinning(rangelow, rangehigh)

topfile=config.samples[channelName]["topfile"]
outputstring = "BH_%s_%s"%(fitName, channelName)

pdFiles = []
pdHists = []
pdFile = config.samples[channelName]["inputFile"]
pdFiles.append(pdFile)

pdHistName = config.samples[channelName]["histname"]
pdHists.append(pdHistName)

# Then run the injection
run_bumpHunt.run_anaFit(
     datahist=[channelName],
     topfile=topfile,
     fitFunction=fitName,
     cdir=cdir,
     wsfile=wsfile,
     nbkg=nbkg,
     outputfile=outputfile,
     outputstring=outputstring,
     dosignal = dosignal,
     dolimit = dolimit,
     rebinEdges=binedges,
     signalfile = signalfile,
     rebinFile=None,
     rebinHist=None,
     datafiles=pdFiles,
     histnames=pdHists,
     maskthreshold=0.05,
     outdir=outputdir,
     doRemake = args.doRemake,
     useSysts = False,
     rangelow = rangelow,
     rangehigh = rangehigh,
    )


