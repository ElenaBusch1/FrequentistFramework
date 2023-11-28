import config as config
#import run_injections_anaFit as run_injections_anaFit
#import generatePseudoData as generatePseudoData
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os
import os,sys,re,argparse,subprocess,shutil


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
(args, test) = parser.parse_args()



if args.isBatch:
  pdFitName = args.pdFitName
  fitName = args.fitName
  channelName = args.channelName
  sigmeans = [args.sigmean]
  sigwidths = [args.sigwidth]
  rangelow = args.rangelow
  rangehigh = args.rangehigh
  signalfile = args.signalFile


else:
  pdFitName = "sixPar"
  fitName = "fivePar"
  #channelName="test3New_15"
  channelName = "test3New_NoCut_no21"
  #channelName="yxxjjjj_4j_alpha0"
  #channelName="test3New"
  #channelName="testSherpa"
  #rangelow=1800
  #rangehigh=9000
  rangelow = 225
  rangehigh = 1000
  #signalfile = "Gaussian"
  #signalfile = "gausHist"
  #signalfile = "templateHist"
  signalfile = "templateHistNoSyst"
  #signalfile =  "test3_15NoSysts"

  #sigmeans = [250, ]
  sigmeans = [250, 300, 350, 400, 450, 500, 550, 600, 650]
  #sigmeans = [350, 400, 450, 500, ]
  #sigmeans = [250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
  #sigmeans = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
  #sigmeans = [250]
  #sigmeans = [2000]
  sigwidths=[10]



cdir = config.cdir
if not os.path.exists(cdir + "/scripts/" + channelName):
      os.makedirs(cdir + "/scripts/" + channelName)

# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
pdInputFile = config.getFileName("PostFit_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
pdHistName = "pseudodata_"
dosignal=1
dolimit=1

useSysts = False
nToys = 1
#nToys = config.nToys

for sigmean in sigmeans:
    for sigwidth in sigwidths:
          nbkg="1E7,0,5E8"
          nsig="0,0,5e4"
          topfile=config.samples[channelName]["topfile"]
          categoryfile=config.samples[channelName]["categoryfile"]
          dataFile=config.samples[channelName]["inputFile"]

          # Output file names, which will be written to outputdir
          wsfile = config.getFileName("FitResult_limits_1GeVBin_GlobalFit", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
          outputfile = config.getFileName("FitResult_limits_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
          outputstring = "FitResult_limits_%d_%d_%d_%s"%(0, sigmean, sigwidth, signalfile)
          #binedges = None
          binedges = config.getBinning(rangelow, rangehigh, delta=25)

          #systematicNameFile = config.getFileName("systematics", cdir + "/scripts/uncertaintySets/", channelName, rangelow, rangehigh, sigmean, sigwidth) + "_" + signalfile + ".txt"
          #systematicNameFile = config.getFileName("systematics", cdir + "/scripts/", "uncertaintySets", rangelow, rangehigh, sigmean, sigwidth) + ".txt"
          #systematicNameFile = "uncertaintySets/systematics.txt"
          systematicNameFile = "uncertaintySets/systematics_mass_%d_template.txt"%(sigmean)
          #systematicNameFile = "uncertaintySets/systematics_Fit_200_1000_Mean_%d_Width_%d_Amp_0.txt"%(sigmean, sigwidth)



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
               sigamp=0,
               nbkg=nbkg,
               nsig=nsig,
               rangelow=rangelow,
               signalfile=signalfile,
               rangehigh=rangehigh,
               outputfile=outputfile,
               outputstring=outputstring,
               dosignal = dosignal,
               dolimit = dolimit,
               loopstart=0,
               loopend=nToys,
               rebinedges=binedges,
               rebinfile=None,
               rebinhist=None,
               maskthreshold=-0.01,
               outdir=cdir + "/scripts/" + channelName,
               useSysts = useSysts,
               #histName = "SigLowNorm_15_SR1_tagged_",
               histName = channelName,
               systematicNameFile = systematicNameFile,
               biasMagnitude=0,
              )

           #histName = channelName,


