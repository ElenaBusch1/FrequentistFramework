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
args = parser.parse_args()


if args.isBatch:
  pdFitNames = [args.pdFitName]
  fitName = args.fitName
  channelNames = [args.channelNames]
  sigmeans = [args.sigmean]
  sigwidths = [args.sigwidth]
  signalfile = args.signalFile
  nToys = config.nToys


else:
  #pdFitNames = ["sixParM2j"]
  #fitName = "fiveParM2j"
  #pdFitNames = ["fourParM2j"]
  #fitName = "threeParM2j"
  pdFitNames = ["fiveParM2j"]
  fitName = "fourParM2j"
  channelNames = [["3"]]
  #channelNames = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11],]

  #sigmeans = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
  sigmeans = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500]

  #sigmeans = [1100]

  sigwidths = [10]
  #signalfile = "crystalBallHistNoSyst"
  signalfile = "gausHistNoSyst"

  args.doRemake = 0
  #args.doRemake = 1

#nToys = config.nToys
nToys = 50

coutputdir = "fits2javg_data_"
baseChannelName = "Data_2javg_alpha"

dosignal=1
dolimit=0
cdir = config.cdir
tagName = "m2j_"


for sigmean in sigmeans:
    for sigwidth in sigwidths:
      for pdFitName in pdFitNames:
        for channelSuffix in channelNames:
          channelName = [baseChannelName + "%d"%(int(channelSuffix[0]))]
          alpha = config.alphaBins[int(channelSuffix[0])]

          #mY = round( (alpha * sigmean)/10)*10
          #if mY < 500 and (signalfile=="crystalBallHistNoSyst" or signalfile=="crystalBallHist"):
          #  continue

          mY = round(sigmean / alpha / 10) * 10
          if sigmean < 500:
            continue
          if mY < 2000:
            continue

          if mY > 10000:
            continue

          outputdir = coutputdir+channelName[0]

          pdFiles = []
          pdHists = []
          for channel in channelName:
            if sigmean < config.samples[channel]["rangelow"]:
              continue
            pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir) + ".root"
            pdFiles.append(pdFile)

            pdHistName = "pseudodata"
            pdHists.append(pdHistName)
          if len(pdFiles)==0:
            continue
          if not os.path.exists(outputdir):
              os.makedirs(outputdir)
          nbkg="1E3,0,1E6"
          nbkgWindow = 1
          nsig="0,-500,500"
          if sigmean > 700 and alpha > 0.23:
            nsig="0,-200,200"
          elif sigmean > 700:
            nsig="0,-150,150"
          if sigmean > 1000 and alpha > 0.25:
            nsig="0,-100,100"
          elif sigmean > 1000:
            nsig="0,-50,50"

          if sigmean > 1300:
            nsig="0,-30,30"
          if sigmean > 1500 and alpha > 0.25:
            nsig="0,-10,10"
          elif sigmean > 1500:
            nsig="0,-5,5"
          if alpha < 0.17 and sigmean > 900:
            nsig="0,-5,5"
          elif alpha < 0.18 and sigmean > 1000:
            nsig="0,-10,10"
          elif alpha < 0.22 and sigmean > 1200:
            nsig="0,-10,10"
          elif alpha < 0.28 and sigmean > 1350:
            nsig="0,-10,10"
          elif alpha < 0.28 and sigmean > 1200:
            nsig="0,-30,30"

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
               outputstring="m2j_SS_%s_%s_%d_%d_%s"%(pdFitName, fitName, sigmean, sigwidth, signalfile),
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
               tagName = tagName,
               isMx = True,
               useBkgWindow = True,
               minTolerance = "1e-4",
               useNegWindow = True,
              )





