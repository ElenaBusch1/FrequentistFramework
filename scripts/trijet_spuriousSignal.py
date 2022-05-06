import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os
import python.run_anaFit as run_anaFit


from optparse import OptionParser

parser = OptionParser()
parser.add_option('--isBatch', dest='isBatch', type=int, default=0, help='Input data file')
parser.add_option('--fitName', dest='fitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_option('--pdFitName', dest='pdFitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_option('--signalFile', dest='signalFile', type=str, default=None, help='Name of the signal file')
parser.add_option('--channelName', dest='channelName', type=str, help='Output workspace file')
parser.add_option('--rangelow', dest='rangelow', type=int, help='Start of fit range (in GeV)')
parser.add_option('--rangehigh', dest='rangehigh', type=int, help='End Start of fit range (in GeV)')
parser.add_option('--sigmean', dest='sigmean', type=int, default=1000, help='Mean of signal Gaussian for s+b fit (in GeV)')
parser.add_option('--sigwidth', dest='sigwidth', type=int, default=7, help='Width of signal Gaussian for s+b fit (in %)')
parser.add_option('--sigamp', dest='sigamp', type=int, default=0, help='Amplitude of signal Gaussian for s+b fit (in %)')
(args, test) = parser.parse_args()



if args.isBatch:
  pdFitNames = [args.pdFitName]
  fitName = args.fitName
  channelNames = [args.channelName]
  sigmeans = [args.sigmean]
  sigamps = [args.sigamp]
  sigwidths = [args.sigwidth]
  rangelow = args.rangelow
  rangehigh = args.rangehigh
  signalfile = args.signalFile


else:
  pdFitNames = ["sixPar"]
  fitName = "fivePar"
  channelNames=["test3"]
  sigmeans = [550]
  sigamps = [0]
  sigwidths = [7]
  rangelow=200
  rangehigh=1200
  #rangelow=config.cRangeLow
  #rangehigh=config.cRangeHigh
  #signalfile =  "test3_15"
  signalfile =  "test3_inverted"
  #signalfile =  "Gaussian"
  #signalfile =  config.cSignal



#. scripts/setup_buildAndFit.sh
dosignal=1
dolimit=0

cdir = config.cdir


for sigmean in sigmeans:
  for sigamp in sigamps:
    for sigwidth in sigwidths:
      for pdFitName in pdFitNames:
        for channelName in channelNames:
          pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
          pdHistName = "pseudodata"
          outputdir = channelName
          if not os.path.exists(outputdir):
              os.makedirs(outputdir)
          nbkg="1E7,0,1E9"
          nbkgWindow = 1
          nsig="0,-1e6,1e6"
          topfile=config.samples[channelName]["topfile"]
          categoryfile=config.samples[channelName]["categoryfile"]
          dataFile=config.samples[channelName]["inputFile"]
  
          # Output file names, which will be written to outputdir
          wsfile = config.getFileName("FitResult_spuriousSignal_1GeVBin_GlobalFit", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"
          outputfile = config.getFileName("FitResult_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"
  
          # Then run the injection
          run_anaFit.run_anaFit(
               datafile=pdFile, 
               datahist=pdHistName,
               categoryfile=categoryfile,
               topfile=topfile,
               fitFunction=fitName,
               cdir=cdir,
               wsfile=wsfile,
               sigmean=sigmean,
               sigwidth=sigwidth,
               nbkg=nbkg,
               rangelow=rangelow,
               rangehigh=rangehigh,
               outputfile=outputfile,
               signalfile = signalfile,
               outputstring="SS_%s_%s_%d_%d_%d_%d_%s"%(pdFitName, fitName, sigmean, sigamp, sigwidth, rangehigh, signalfile),
               dosignal = dosignal,
               dolimit = dolimit,
               nsig=nsig,
               nbkgWindow=nbkgWindow,
               ntoys=config.nToys,
               maskthreshold=-0.01,
               outdir=outputdir,
              )





