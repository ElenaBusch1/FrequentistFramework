import config as config
import python.run_limits as run_anaFit
import os,sys,re,argparse,subprocess,shutil

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('--isBatch', dest='isBatch', type=int, default=0, help='Input data file')
parser.add_argument('--fitName', dest='fitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_argument('--signalFile', dest='signalFile', type=str, default=None, help='Name of the signal file')
parser.add_argument('--channelNames', dest='channelNames', nargs='+', help='Output workspace file')
parser.add_argument('--sigmean', dest='sigmean', type=int, default=1000, help='Mean of signal Gaussian for s+b fit (in GeV)')
parser.add_argument('--sigwidth', dest='sigwidth', type=int, default=7, help='Width of signal Gaussian for s+b fit (in %)')
parser.add_argument('--doRemake', dest='doRemake', type=int, default=0, help='Amplitude of signal Gaussian for s+b fit (in %)')
parser.add_argument('--outputdir', dest='outputdir', type=str, default="fitsNixon", help='Amplitude of signal Gaussian for s+b fit (in %)')
args = parser.parse_args()


if args.isBatch:
  fitName = args.fitName
  channelName = [args.channelNames]
  sigmeans = [args.sigmean]
  sigwidths = [args.sigwidth]
  signalfile = args.signalFile


else:

  fitName = "fourPar"
  channelNames = [[ "6"], ]

  #sigmeans = [2500, 3500, 5000, 7000, 9000]
  sigmeans = [5000]
  sigwidths = [10]
  signalfile =  "crystalBallHist"
  args.doRemake = 1


cdir = config.cdir
coutputdir = "fitsData"
baseChannelName = "Data_yxxjjjj_4j_alpha"

tagName = ""

for channelSuffix in channelNames:
  alpha = config.alphaBins[int(channelSuffix[0])]
  channelName = [baseChannelName + "%d"%(int(channelSuffix[0]))]

  for channel in channelName:
    outputdir = coutputdir + "_" + channel

  for sigmean in sigmeans:
    mX = round( (sigmean*alpha)/10)*10
    if mX < 500:
      continue

    for sigwidth in sigwidths:
        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_limits_1GeVBin_GlobalFit_%s"%(signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, 0) + ".root"
        outputfile = config.getFileName("FitResult_limits_%s_%s"%(fitName, signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, 0) + ".root"

        # Then run the injection
        run_anaFit.run_anaFit(
             datahist=channelName,
             cdir=cdir,
             wsfile=wsfile,
             sigmean=sigmean,
             sigwidth=sigwidth,
             outputfile=outputfile,
             doRemake = args.doRemake,
            )







