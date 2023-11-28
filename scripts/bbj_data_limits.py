import config as config
import python.getBias as gb
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
  pdFitName = "sixPar"
  fitName = "fivePar"
  #channelName="btagFinal"
  channelName="bbj_Data"
  rangelow = 160
  rangehigh = 700
  #signalfile = "templateHistBBJNoSyst"
  #signalfile = "Gaussian"
  #signalfile = "templateHistBBJ"
  signalfile = "gausHistBBJ"

  sigmeans = [250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
  #sigmeans = [200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
  #sigmeans = [350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
  #sigmeans = [300, 325, 350, 375, 400]
  sigmeans = [475]
  sigamps = [0]
  #sigwidths=[5, 7, 10, 12, 15]
  sigwidths=[15]


useSysts = True


cdir = config.cdir
if not os.path.exists(cdir + "/scripts/" + channelName):
      os.makedirs(cdir + "/scripts/" + channelName)

# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
dosignal=1
dolimit=1

nToys = 1
#nToys = config.nToys
sigamp=0

for sigmean in sigmeans:
    for sigwidth in sigwidths:
          nbkg="5E5,0,1E6"
          nsig="0,0,2e3"

          # Output file names, which will be written to outputdir
          topfile=config.samples[channelName]["topfile"]
          categoryfile=config.samples[channelName]["categoryfile"]
          if useSysts:
            categoryfile=config.samples[channelName]["categoryfileSysts"]
          dataFile=config.samples[channelName]["inputFile"]
          datahist=config.samples[channelName]["histname"]

          # Output file names, which will be written to outputdir
          wsfile = config.getFileName("FitResult_%s_1GeVBin_GlobalFit"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
          outputfile = config.getFileName("FitResult_%s_%s"%(fitName, signalfile), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth) + ".root"
          if signalfile == "gausHistBBJ":
            outputfile = config.getFileName("FitResult_%s"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth) + ".root"
          binedges = config.getBinning(rangelow, rangehigh, 25)
          outputstring = "FitResult_limits_%d_%d_%d_%s"%(0, sigmean, sigwidth, signalfile)
          biasMagnitude = gb.getSpuriousSignal(cdir + "/scripts", channelName, sigmean, sigwidth, biasFraction= 0.5, signalName=signalfile)
          #print biasMagnitude
          #continue

          systematicNameFile = "uncertaintySets/systematics_bjj_Fit_200_1000_Mean_%d_Width_%d_Amp_0.txt"%(sigmean, sigwidth)
          if signalfile == "templateHistBBJ":
            systematicNameFile = "uncertaintySets/systematics_bbj_mass_%d_template.txt"%(sigmean)


          # Then run the injection
          run_injections_anaFit.run_injections_anaFit(
               datafile=dataFile,
               datahist=datahist,
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
               signalfile=signalfile,
               rangehigh=rangehigh,
               useSysts = useSysts,
               histName = channelName,
               outputfile=outputfile,
               outputstring=outputstring,
               dosignal = dosignal,
               dolimit = dolimit,
               loopstart=0,
               loopend=0,
               rebinedges=binedges,
               systematicNameFile = systematicNameFile,
               systematicAllNameFile = "uncertaintySets/systematicsBtag.txt",
               rebinfile=None,
               rebinhist=None,
               maskthreshold=-0.01,
               outdir=cdir + "/scripts/" + channelName,
               biasMagnitude = biasMagnitude,
               inDirSysts = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/btagStudies/test/",
               initialGuess = "3000",
              )





