import config as config
#import run_injections_anaFit as run_injections_anaFit
#import generatePseudoData as generatePseudoData
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os
import python.getBias as gb
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
  #channelName="FullRun2Data_NoNN"
  #channelName="FullRun2Data"
  #channelName="FullRun2Data_cut9"
  #channelName="test3New_15_data_mcEff"
  #channelName="test3New_15_dataErf"
  #channelName="test3New_15_dataErf_550"
  #channelName="test3New_15_MCwithMC"
  #channelName="test3New_15"
  #channelName="Data_m32"
  #channelName="Data_minMass"
  #channelName="DataNoInsitu"
  #channelName="DataAllJES"
  #channelName="DataMCJES"
  channelName = "FullRun2Data_NoNN_No21"
  #channelName = "test3New_15_MCEffOnData"
  #channelName = "test3New_15_data_mcEff"
  rangelow = 225
  rangehigh = 1000
  signalfile = "gausHist"
  #signalfile = "templateHistNoSyst"
  #signalfile = "templateHist"


  #sigmeans = [250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
  #sigmeans = [250, 300, 350, 400, 450, 500, 550, 600]
  sigmeans = [500]
  sigamps = [0]
  #sigwidths=[5, 7, 10, 12, 15]
  sigwidths=[15]



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

useSysts = True

for sigmean in sigmeans:
    for sigwidth in sigwidths:
          nbkg="1E7,0,1E8"
          nsig="0,0,3e4"

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
          binedges = config.getBinning(rangelow, rangehigh, 25)
          outputstring = "FitResult_limits_%d_%d_%d_%s"%(0, sigmean, sigwidth, signalfile)
          systematicNameFile = "uncertaintySets/systematics_Fit_200_1000_Mean_%d_Width_%d_Amp_0.txt"%(sigmean, sigwidth)
          if signalfile == "templateHist":
            systematicNameFile = "uncertaintySets/systematics_trijet_mass_%d_template.txt"%(sigmean)

          #biasMagnitude = gb.getSpuriousSignal(cdir + "/scripts", channelName, sigmean, sigwidth, biasFraction= 0.5, signalName=signalfile)
          biasMagnitude = 0

          #biasMagnitude = biasMagnitude*5

          #print biasMagnitude
          #continue

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
               histName = channelName,
               outputfile=outputfile,
               outputstring=outputstring,
               dosignal = dosignal,
               dolimit = dolimit,
               useSysts = useSysts,
               loopstart=0,
               loopend=0,
               rebinedges=binedges,
               rebinfile=None,
               rebinhist=None,
               maskthreshold=-0.01,
               outdir=cdir + "/scripts/" + channelName,
               biasMagnitude = biasMagnitude,
               systematicNameFile = systematicNameFile,
               initialGuess = "20000",
              )



