import config as config
import python.run_anaFit as run_anaFit
import python.generatePseudoData as generatePseudoData
import os,sys,re,argparse,subprocess,shutil
import python.getBias as gb



from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument('--isBatch', dest='isBatch', type=int, default=0, help='Input data file')
parser.add_argument('--fitName', dest='fitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_argument('--pdFitName', dest='pdFitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_argument('--signalFile', dest='signalFile', type=str, default=None, help='Name of the signal file')
parser.add_argument('--channelNames', dest='channelNames', nargs='+', help='Output workspace file')
parser.add_argument('--sigmean', dest='sigmean', type=int, default=1000, help='Mean of signal Gaussian for s+b fit (in GeV)')
parser.add_argument('--sigwidth', dest='sigwidth', type=int, default=7, help='Width of signal Gaussian for s+b fit (in %)')
parser.add_argument('--sigamp', dest='sigamp', type=int, default=3, help='Amplitude of signal Gaussian for s+b fit (in %)')
parser.add_argument('--doRemake', dest='doRemake', type=int, default=0, help='Amplitude of signal Gaussian for s+b fit (in %)')
parser.add_argument('--outputdir', dest='outputdir', type=str, default="fitsNixon", help='Amplitude of signal Gaussian for s+b fit (in %)')
args = parser.parse_args()




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

  fitName = "fourParM2j"
  #channelNames = [["Data_2javg_alpha0"],[ "Data_2javg_alpha1"],[ "Data_2javg_alpha2"],[ "Data_2javg_alpha3"],[ "Data_2javg_alpha4"],[ "Data_2javg_alpha5"],[ "Data_2javg_alpha6"],[ "Data_2javg_alpha7"],[ "Data_2javg_alpha8"],[ "Data_2javg_alpha9"],[ "Data_2javg_alpha10"],[ "Data_2javg_alpha11"], ]
  channelNames = [[ "Data_2javg_alpha9"], ]


  #sigmeans = [500, 700, 1000, 1500, 2000, 2500, 3000,]
  #sigmeans = [500, 600, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500]
  sigmeans = [1300]

  sigamps = [0]
  sigwidths = [10]
  signalfile =  "Gaussian"
  signalfile =  "crystalBallHist"

  coutputdir = "fits2javg_data_"
  args.doRemake = 1


cdir = config.cdir
dosignal=1
dolimit=1


for channelName in channelNames:
  for sigmean in sigmeans:
    for sigamp in sigamps:
      for sigwidth in sigwidths:
        outputdir = coutputdir + channelName[0]
        nbkg="1E4,0,1E6"
        nsig="0,0,1000"
        if sigmean > 500:
          nsig="0,0,800"
        if sigmean > 700:
          nsig="0,0,500"
        if sigmean > 1000:
          nsig="0,0,50"

        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_limits_1GeVBin_GlobalFit_%s"%(signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputfile = config.getFileName("FitResult_limits_%s_%s"%(fitName, signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputstring = "FitResult_limits_%d_%d_%d_%s_%s"%(sigamp, sigmean, sigwidth, signalfile, channelName[0])
        binedges = config.getBinningFromFile(channelName[0])
        if sigmean+50 < binedges[0]:
          continue
        topfile=config.samples[channelName[0]]["topfile"]
        biasMagnitude = gb.getSpuriousSignal(coutputdir, channelName[0], sigmean, sigwidth, biasFraction= 0.5)


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
               signalfile="Gaussian",
               maskthreshold=0.05,
               dosignal=1,
               dolimit=1,
               useSysts = True,
               rebinEdges=binedges,
               rebinOnlyBH=True,
               biasMagnitude = biasMagnitude,
               )







