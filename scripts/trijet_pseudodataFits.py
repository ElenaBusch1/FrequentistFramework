import scripts.config as config
import python.run_anaFitWithToys as run_anaFitWithToys
import python.generatePseudoData as generatePseudoData
import os



from optparse import OptionParser

parser = OptionParser()
parser.add_option('--isBatch', dest='isBatch', type=int, default=0, help='Input data file')
parser.add_option('--fitName', dest='fitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_option('--pdFitName', dest='pdFitName', type=str, default=None, help='Name of the file with the fit function information')
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

else:
  pdFitNames = ["sixPar"]
  fitName = "fivePar"
  channelNames=["PtOrdered5"]
  sigmeans = [250]
  sigamps = [0]
  sigwidth = [7]
  rangelow=200
  rangehigh=900



dosignal=0
dolimit=0
cdir = config.cdir


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






