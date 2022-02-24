import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os



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
parser.add_option('--sigamp', dest='sigamp', type=int, default=3, help='Amplitude of signal Gaussian for s+b fit (in %)')
(args, test) = parser.parse_args()



if args.isBatch:
  pdFitName = args.pdFitName
  fitName = args.fitName
  channelName = args.channelName
  sigmeans = [args.sigmean]
  sigamps = [args.sigamp]
  sigwidths = [args.sigwidth]
  rangelow = args.rangelow
  rangehigh = args.rangehigh
  signalfile = args.signalFile

else:
  pdFitName = config.cPDFitName
  fitName = config.cFitName
  channelName=config.cSample
  sigmeans = [350]
  sigamps = [5]
  sigwidths = [7]
  rangelow=config.cRangeLow
  rangehigh=config.cRangeHigh
  signalfile =  config.cSignal


#. scripts/setup_buildAndFit.sh
dosignal=1
dolimit=0

cdir = config.cdir
outputdir = channelName
if not os.path.exists(outputdir):
      os.makedirs(outputdir)


pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
pdHistName = "pseudodata"


for sigmean in sigmeans:
  for sigamp in sigamps:
    for sigwidth in sigwidths:
      nbkg="1E7,0,1E8"
      nsig="0,0,1e6"
  
      topfile=config.samples[channelName]["topfile"]
      categoryfile=config.samples[channelName]["categoryfile"]
      dataFile=config.samples[channelName]["inputFile"]

      # Output file names, which will be written to outputdir
      wsfile = config.getFileName("FitResult_sigPlusBkg_1GeVBin_GlobalFit_%s"%(signalfile), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"
      outputfile = config.getFileName("FitResult_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, sigamp) + ".root"
      outputstring = "FitResult_injections_%d_%d_%d_%s"%(sigamp, sigmean, sigwidth, signalfile)
      #binedges = config.getBinning(rangelow, rangehigh, delta=25)
      binedges = None


      # Then run the injection
      run_injections_anaFit.run_injections_anaFit(
           datafile=pdFile, 
           datahist=pdHistName,
           categoryfile=categoryfile,
           topfile=topfile,
           fitFunction=fitName,
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
           rebinedges=binedges,
           signalfile = signalfile,
           rebinfile=None,
           rebinhist=None,
           maskthreshold=-0.01,
           outdir=outputdir,
          )





