import scripts.config as config
import python.run_anaFit as run_anaFit
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
(args, test) = parser.parse_args()



if args.isBatch:
  pdFitNames = [args.pdFitName]
  fitName = args.fitName
  channelNames = [args.channelName]
  rangelow = args.rangelow
  rangehigh = args.rangehigh
  signalfile = args.signalfile

else:
  pdFitNames = ["sixPar"]
  fitName = "fivePar"
  #channelNames=["testSherpa"]
  #channelNames=["test3New_15"]
  channelNames=["test3New_NoCut_no21"]
  rangelow=225
  rangehigh=1000
  signalfile = "Gaussian"



dosignal=0
dolimit=0
cdir = config.cdir


for pdFitName in pdFitNames:
  for channelName in channelNames:
    outputdir = channelName
    if not os.path.exists(outputdir):
          os.makedirs(outputdir)
    pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    pdHistName = "pseudodata_"
    #pdFile = "/afs/cern.ch/work/d/dmelini/public/toJennifer/PseudoFromSWIFTajj_DataStat.root"
    #pdHistName = "h_pseudo"

    nbkg="1E7,0,1E8"

    topfile=config.samples[channelName]["topfile"]
    categoryfile=config.samples[channelName]["categoryfile"]
    dataFile=config.samples[channelName]["inputFile"]

    # Output file names, which will be written to outputdir
    wsfile = config.getFileName("FitResult_PD_bkgonly_1GeVBin_GlobalFit", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    outputfile = config.getFileName("FitResult_%s_PD_%s_bkgonly"%(pdFitName, fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    outputstring = "FitResult_%s_PD_%s_bkgonly"%(pdFitName, fitName)
    binedges = config.getBinning(rangelow, rangehigh, delta=25)


    run_anaFit.run_anaFit(
             datafile=pdFile,
             datahist=pdHistName,
             categoryfile=categoryfile,
             topfile=topfile,
             fitFunction=fitName,
             cdir=cdir ,
             wsfile=wsfile,
             signalfile = signalfile,
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






