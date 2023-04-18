import config as config
import python.run_anaFit as run_anaFit
import python.generatePseudoData as generatePseudoData
import os,sys,re,argparse,subprocess,shutil
import python.getBias as gb
from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument('--isBatch', dest='isBatch', type=int, default=0, help='Input data file')
parser.add_argument('--fitName', dest='fitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_argument('--signalFile', dest='signalFile', type=str, default=None, help='Name of the signal file')
parser.add_argument('--channelNames', dest='channelNames', nargs='+', help='Output workspace file')
parser.add_argument('--sigmean', dest='sigmean', type=int, default=1000, help='Mean of signal Gaussian for s+b fit (in GeV)')
parser.add_argument('--sigwidth', dest='sigwidth', type=int, default=7, help='Width of signal Gaussian for s+b fit (in %)')
parser.add_argument('--doRemake', dest='doRemake', type=int, default=0, help='Amplitude of signal Gaussian for s+b fit (in %)')
args = parser.parse_args()



if args.isBatch:
  fitName = args.fitName
  channelName = args.channelName
  sigmeans = [args.sigmean]
  sigwidths = [args.sigwidth]
  rangelow = args.rangelow
  rangehigh = args.rangehigh
  signalfile = args.signalFile


else:

  fitName = "fourParM2j"
  #fitName = "threeParM2j"
  #channelNames = [["Data_2javg_alpha0"],[ "Data_2javg_alpha1"],[ "Data_2javg_alpha2"],[ "Data_2javg_alpha3"],[ "Data_2javg_alpha4"],[ "Data_2javg_alpha5"],[ "Data_2javg_alpha6"],[ "Data_2javg_alpha7"],[ "Data_2javg_alpha8"],[ "Data_2javg_alpha9"],[ "Data_2javg_alpha10"],[ "Data_2javg_alpha11"], ]
  #channelNames = [[ "Data_2javg_alpha0"], ]
  channelNames = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11],]


  #sigmeans = [500, 700, 1000, 1500, 2000, 2500, 3000,]
  #sigmeans = [500, 600, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500]
  sigmeans = [600]

  sigwidths = [10]
  signalfile =  "crystalBallHist"
  #signalfile =  "crystalBallHistNoSyst"
  #signalfile =  "gausHist"
  coutputdir = "fits2javg_data"
  args.doRemake = 1

doSyst = True

cdir = config.cdir
dosignal=1
dolimit=1
baseChannelName = "Data_2javg_alpha"
tagName = "m2j_"




for channelSuffix in channelNames:
  channelName = [baseChannelName + "%d"%(int(channelSuffix[0]))]
  alpha = config.alphaBins[int(channelSuffix[0])]

  for sigmean in sigmeans:
    mY = round(sigmean / alpha / 10) * 10
    if sigmean < 500:
      continue
    if mY < 2000:
      continue
    if mY > 10000:
      continue

    for sigwidth in sigwidths:
        outputdir = coutputdir + channelName[0]
        nbkg="1E4,0,5E4"
        nsig="0,0,1000"
        if sigmean > 500:
          #nsig="0,0,600"
          nsig="0,0,50"
        if sigmean > 700:
          nsig="0,0,500"
        if sigmean > 1000:
          nsig="0,0,50"
        nsig="0,0,30"

        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_limits_1GeVBin_GlobalFit_%s"%(signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, 0) + ".root"
        outputfile = config.getFileName("FitResult_limits_%s_%s"%(fitName, signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, 0) + ".root"
        outputstring = "FitResult_limits_%d_%d_%d_%s_%s"%(0, sigmean, sigwidth, signalfile, channelName[0])
        binedges = config.getBinningFromFile(channelName[0])
        if sigmean+50 < binedges[0]:
          continue
        topfile=config.samples[channelName[0]]["topfile"]
        biasMagnitude = 0
        if doSyst:
          biasMagnitude = gb.getSpuriousSignal(coutputdir, channelName[0], sigmean, sigwidth, biasFraction= 0.5, signalName=signalfile+"NoSyst")
 
        systematicNameFile = config.getFileName("systematics", cdir + "/scripts/", "yxxjjjj_2javg_alpha%d"%(int(channelSuffix[0])), "uncertaintySets", sigmean, sigwidth) + "_" + signalfile + ".txt"


        run_anaFit.run_anaFit(
               datahist=channelName,
               topfile=topfile,
               fitFunction=fitName,
               cdir=cdir ,
               wsfile=wsfile,
               nbkg=nbkg,
               nsig=nsig,
               sigmean=sigmean,
               sigwidth=sigwidth,
               outdir=outputdir,
               outputstring="%s"%(fitName),
               outputfile=outputfile,
               signalfile=signalfile,
               maskthreshold=0.05,
               dosignal=1,
               doRemake = args.doRemake,
               dolimit=dolimit,
               useSysts = doSyst,
               rebinEdges=binedges,
               rebinOnlyBH=True,
               biasMagnitude = biasMagnitude,
               tagName=tagName,
               isMx = True,
               systematicNameFile = systematicNameFile,
               minTolerance = "1e-5",
               initialGuess = "%.2f"%(biasMagnitude),
               )

        print biasMagnitude






