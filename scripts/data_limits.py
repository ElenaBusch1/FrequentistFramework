import config as config
#import python.run_injections_anaFit as run_injections_anaFit
import python.run_anaFit as run_anaFit
import python.generatePseudoData as generatePseudoData
import os
import os,sys,re,argparse,subprocess,shutil
import python.getBias as gb


from optparse import OptionParser


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
  pdFitName = args.pdFitName
  fitName = args.fitName
  channelName = args.channelNames
  sigmeans = [args.sigmean]
  sigwidths = [args.sigwidth]
  signalfile = args.signalFile
  channelNames = [channelName]
  


else:

  fitName = "fourPar"
  #channelNames = [ ["Data_yxxjjjj_4j_alpha0"], ["Data_yxxjjjj_4j_alpha1"], ["Data_yxxjjjj_4j_alpha2"], ["Data_yxxjjjj_4j_alpha3"], ["Data_yxxjjjj_4j_alpha4"], ["Data_yxxjjjj_4j_alpha5"], ["Data_yxxjjjj_4j_alpha6"], ["Data_yxxjjjj_4j_alpha7"], ["Data_yxxjjjj_4j_alpha8"], ["Data_yxxjjjj_4j_alpha9"], ["Data_yxxjjjj_4j_alpha10"], ["Data_yxxjjjj_4j_alpha11"], ]
  #channelNames = [ ["Data_yxxjjjj_4j_alpha5"], ["Data_yxxjjjj_4j_alpha6"], ["Data_yxxjjjj_4j_alpha7"], ["Data_yxxjjjj_4j_alpha8"], ["Data_yxxjjjj_4j_alpha9"], ["Data_yxxjjjj_4j_alpha10"], ["Data_yxxjjjj_4j_alpha11"], ]
  #channelNames = [ ["Data_yxxjjjj_4j_alpha0"]]
  channelNames = [ [3]]
 

  sigmeans = [3000]
  #sigmeans = [2500, 3500, 5000, 7000, 9000]
  #sigmeans = [2000,2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250, 5500, 5750, 6000, 6250, 6500, 6750, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]
  #sigmeans = [2250, 2500, 2750, 3250, 3500, 3750, 4250, 4500, 4750, 5000, 5250, 5500, 5750, 6250, 6500, 6750, 7000, 7250, 7500, 7750, 8250, 8500, 8750, 9000, 9250, 9500, 9750]
  sigwidths = [10]
  #signalfile =  "Gaussian"
  #signalfile =  "gausHist"
  signalfile =  "crystalBallHist"
  #signalfile =  "template"
  args.doRemake = 0


coutputdir = "fitsData"
cdir = config.cdir
#if not os.path.exists(cdir + "/scripts/" + channelName):
#      os.makedirs(cdir + "/scripts/" + channelName)
#
# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
dosignal=1
dolimit=1
alphaBins = [0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33]

baseChannelName = "Data_yxxjjjj_4j_alpha"


for channelSuffix in channelNames:
  channelName = baseChannelName + "%d"%(int(channelSuffix[0]))

  alpha = alphaBins[int(channelSuffix[0])]
  for sigmean in sigmeans:
    mY = round( (alpha * sigmean)/10)*10
    if mY < 500:
      print alpha, mY, channelSuffix
      print "mass too low, continuing"
      continue
    for sigwidth in sigwidths:
        outputdir = coutputdir + "_" + channelName
        nbkg="1E4,0,1E6"
        nsig="0,0,1e3"
        if sigmean > 3000:
          nsig="0,0,300"
        if sigmean > 5000:
          nsig="0,0,30"
        if sigmean > 9000:
          nsig="0,0,10"

        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_limits_1GeVBin_GlobalFit_%s"%(signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, 0) + ".root"
        outputfile = config.getFileName("FitResult_limits_%s_%s"%(fitName, signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, 0) + ".root"
        outputstring = "FitResult_limits_%d_%d_%d_%s_%s"%(0, sigmean, sigwidth, signalfile, channelName)
        binedges = config.getBinningFromFile(channelName)
        topfile=config.samples[channelName]["topfile"]
 
        biasMagnitude = gb.getSpuriousSignal(coutputdir, channelName, sigmean, sigwidth, biasFraction= 0.4, signalName=signalfile+"NoSyst")
        print biasMagnitude

        run_anaFit.run_anaFit(
               datahist=[channelName],
               topfile=topfile,
               fitFunction=fitName,
               cdir=cdir ,
               wsfile=wsfile,
               nbkg=nbkg,
               sigmean=sigmean,
               sigwidth=sigwidth,
               outdir=outputdir,
               outputstring="%s"%(fitName),
               outputfile=outputfile,
               signalfile=signalfile,
               maskthreshold=0.05,
               dosignal=1,
               dolimit=1,
               useSysts = True,
               doRemake = args.doRemake,
               biasMagnitude = biasMagnitude,
               rebinOnlyBH=True,
               )





