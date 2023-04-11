import scripts.config as config
import python.generatePseudoData as generatePseudoData
import os
import python.run_anaFit as run_anaFit
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--isBatch', dest='isBatch', type=int, default=0, help='Input data file')
parser.add_argument('--fitName', dest='fitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_argument('--pdFitName', dest='pdFitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_argument('--signalFile', dest='signalFile', type=str, default=None, help='Name of the signal file')
parser.add_argument('--channelNames', dest='channelNames', nargs='+', help='Output workspace file')
parser.add_argument('--sigmean', dest='sigmean', type=int, default=1000, help='Mean of signal Gaussian for s+b fit (in GeV)')
parser.add_argument('--sigwidth', dest='sigwidth', type=int, default=7, help='Width of signal Gaussian for s+b fit (in %)')
parser.add_argument('--doRemake', dest='doRemake', type=int, default=0, help='Amplitude of signal Gaussian for s+b fit (in %)')
parser.add_argument('--outputdir', dest='outputdir', type=str, default="fitsNixon", help='Amplitude of signal Gaussian for s+b fit (in %)')
args = parser.parse_args()


if args.isBatch:
  pdFitNames = [args.pdFitName]
  fitName = args.fitName
  channelName = args.channelNames
  channelNames = [channelName]

  sigmeans = [args.sigmean]
  sigwidths = [args.sigwidth]
  signalfile = args.signalFile
  coutputdir = args.outputdir


else:
  #pdFitNames = ["fourPar"]
  #fitName = "threePar"

  # The function used to generate the pseudodata (used to get filenames)
  pdFitNames = ["fivePar"]
  # The function actually used for the fits
  fitName = "fourPar"

  #pdFitNames = ["sixPar"]
  #fitName = "fivePar"

  # The different channels you are using
  #channelNames = [ ["Data_yxxjjjj_4j_alpha0"],[ "Data_yxxjjjj_4j_alpha1"],[ "Data_yxxjjjj_4j_alpha2"],[ "Data_yxxjjjj_4j_alpha3"],[ "Data_yxxjjjj_4j_alpha4"],[ "Data_yxxjjjj_4j_alpha5"],[ "Data_yxxjjjj_4j_alpha6"],[ "Data_yxxjjjj_4j_alpha7"],[ "Data_yxxjjjj_4j_alpha8"],[ "Data_yxxjjjj_4j_alpha9"],[ "Data_yxxjjjj_4j_alpha10"],[ "Data_yxxjjjj_4j_alpha11"], ]
  #channelNames = [ ["Data_yxxjjjj_4j_alpha0"], ]
  channelNames = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11],]
  channelNames = [[10],]


  # The means of the signal distributions
  #sigmeans = [2000, 3000, 4000, 6000, 8000, 10000]
  #sigmeans = [2000,2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250, 5500, 5750, 6000, 6250, 6500, 6750, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]
  sigmeans = [3750]

  # The width of the signal distribution (in %)
  sigwidths = [10]

  # The signal file to use
  #signalfile =  "Gaussian"
  #signalfile =  "crystalBallHistNoSyst"
  signalfile =  "gausHistNoSyst"
  
  # This should match the output directory of previous steps
  # The actual output directory will also depend on the channel name
  coutputdir = "fitsData_"

  # Argument to control if you want to remake the results or just keep running them
  args.doRemake = 0

  # The number of toys used for the spurious signal tests
  # If this is larger than the number of toys you have produced, this will cause problems
  #nToys = config.nToys


nToys = 50
baseChannelName = "Data_yxxjjjj_4j_alpha"
dosignal=1
dolimit=0
cdir = config.cdir
# This is only necessary if you want to use templates, 
# but then it will be important for making sure you don't try to use signals that don't exist



for sigmean in sigmeans:
    for sigwidth in sigwidths:
      for pdFitName in pdFitNames:
        for channelSuffix in channelNames:
          channelName = [baseChannelName + "%d"%(int(channelSuffix[0]))]
          alpha = config.alphaBins[int(channelSuffix[0])]

          mY = round( (alpha * sigmean)/10)*10
          if mY < 500 and (signalfile=="crystalBallHistNoSyst" or signalfile=="crystalBallHist"):
            continue
          outputdir = coutputdir+channelName[0]

          pdFiles = []
          pdHists = []
          for channel in channelName:
            pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir) + ".root"
            pdFiles.append(pdFile)

            pdHistName = "pseudodata"
            pdHists.append(pdHistName)

          if not os.path.exists(outputdir):
              os.makedirs(outputdir)
          nbkg="1E3,0,1E6"
          nbkgWindow = 1
          nsig="0,-1e4,1e4"
          topfile=config.samples[channelName[0]]["topfile"]
  
          # Output file names, which will be written to outputdir
          wsfile = config.getFileName("FitResult_spuriousSignal_1GeVBin_GlobalFit", cdir + "/scripts/", None, outputdir, sigmean, sigwidth, 0) + ".root"
          outputfile = config.getFileName("FitResult_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, 0) + ".root"
  
          # Then run the injection
          run_anaFit.run_anaFit(
               datahist=channelName,
               topfile=topfile,
               fitFunction=fitName,
               cdir=cdir,
               wsfile=wsfile,
               sigmean=sigmean,
               sigwidth=sigwidth,
               nbkg=nbkg,
               nbkgWindow=[],
               outputfile=outputfile,
               signalfile = signalfile,
               outputstring="SS_%s_%s_%d_%d_%s_%s"%(pdFitName, fitName, sigmean, sigwidth, signalfile, channelName[0]),
               dosignal = dosignal,
               dolimit = dolimit,
               nsig=nsig,
               ntoys=nToys,
               maskthreshold=-0.01,
               outdir=outputdir,
               datafiles=pdFiles, 
               histnames=pdHists, 
               doRemake=args.doRemake,
               useSysts = False,
              )





