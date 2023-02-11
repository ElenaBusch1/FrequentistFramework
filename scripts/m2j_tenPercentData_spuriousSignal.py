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
  channelNames = [args.channelNames]
  sigmeans = [args.sigmean]
  sigwidths = [args.sigwidth]
  signalfile = args.signalFile
  coutputdir = args.outputdir
  nToys = config.nToys


else:
  pdFitNames = ["fiveParM2j"]
  fitName = "fourParM2j"
  #channelNames = [ ["tenPercentData_2javg_alpha0"],[ "tenPercentData_2javg_alpha1"],[ "tenPercentData_2javg_alpha2"],[ "tenPercentData_2javg_alpha3"],[ "tenPercentData_2javg_alpha4"],[ "tenPercentData_2javg_alpha5"],[ "tenPercentData_2javg_alpha6"],[ "tenPercentData_2javg_alpha7"],[ "tenPercentData_2javg_alpha8"],[ "tenPercentData_2javg_alpha9"],[ "tenPercentData_2javg_alpha10"],[ "tenPercentData_2javg_alpha11"], ]
  #channelNames = [ [ "tenPercentData_2javg_alpha9"],[ "tenPercentData_2javg_alpha10"],[ "tenPercentData_2javg_alpha11"], ]
  #channelNames = [ [ "tenPercentData_2javg_alpha3"],[ "tenPercentData_2javg_alpha4"],[ "tenPercentData_2javg_alpha5"],[ "tenPercentData_2javg_alpha6"],[ "tenPercentData_2javg_alpha7"],[ "tenPercentData_2javg_alpha8"],[ "tenPercentData_2javg_alpha9"],[ "tenPercentData_2javg_alpha10"],[ "tenPercentData_2javg_alpha11"], ]
  #channelNames = [ [ "tenPercentData_2javg_alpha2"],  [ "tenPercentData_2javg_alpha3"],[ "tenPercentData_2javg_alpha4"],]
  channelNames = [[ "tenPercentData_2javg_alpha10"],]


  #sigmeans = [500, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250]
  #sigmeans = [500, 700, 1000, 1500, 2000, 2500, 3000,]
  sigmeans = [700,]
  sigwidths = [10]
  signalfile =  "Gaussian"
  coutputdir = "fits2javg_10data_"
  #args.doRemake = 0
  args.doRemake = 1
  nToys = config.nToys


dosignal=1
dolimit=0
cdir = config.cdir


for sigmean in sigmeans:
    for sigwidth in sigwidths:
      for pdFitName in pdFitNames:
        for channelName in channelNames:
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
          #nsig="0,-1e3,1e3"
          #nsig="0,-300,300"
          nsig="0,-200,200"
          #nsig="0,-5,5"
          if sigmean > 500:
            #nsig="0,-200,200"
            #nsig="0,-300,300"
            #nsig="0,-200,200"
            #nsig="0,-10,20"
            nsig="0,-100,100"
          if sigmean > 700:
            #nsig="0,-10,20"
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
               outputstring="m2j_SS_%s_%s_%d_%d_%s_%s"%(pdFitName, fitName, sigmean, sigwidth, signalfile, channelName[0]),
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




