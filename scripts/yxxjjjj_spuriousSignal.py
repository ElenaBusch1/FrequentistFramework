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
  outputdir = args.outputdir
  nToys = config.nToys


else:
  pdFitNames = ["fivePar"]
  fitName = "fourPar"
  channelNames = [ ["nixon_4j_alpha0"], ]
  #channelNames = [ ["nixon_4j_alpha0", "nixon_4j_alpha1", "nixon_4j_alpha2", "nixon_4j_alpha3", "nixon_4j_alpha4", "nixon_4j_alpha5", "nixon_4j_alpha6", "nixon_4j_alpha7", "nixon_4j_alpha8", "nixon_4j_alpha9", "nixon_4j_alpha10", "nixon_4j_alpha11", "nixon_4j_alpha12"], ]

  sigmeans = [3000]
  sigwidths = [10]
  #signalfile =  "Gaussian"
  signalfile =  "template"
  outputdir = "fitsNixon"
  #args.doRemake = 0
  args.doRemake = 1
  nToys = config.nToys
  #nToys = 1


dosignal=1
dolimit=0
cdir = config.cdir


for sigmean in sigmeans:
    for sigwidth in sigwidths:
      for pdFitName in pdFitNames:
        for channelName in channelNames:

          pdFiles = []
          pdHists = []
          for channel in channelName:
            pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir) + ".root"
            pdFiles.append(pdFile)

            pdHistName = "pseudodata"
            pdHists.append(pdHistName)

          if not os.path.exists(outputdir):
              os.makedirs(outputdir)
          nbkg="1E5,0,1E7"
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
               outputstring="SS_%s_%s_%d_%d_%s"%(pdFitName, fitName, sigmean, sigwidth, signalfile),
               dosignal = dosignal,
               dolimit = dolimit,
               nsig=nsig,
               ntoys=nToys,
               maskthreshold=-0.01,
               outdir=outputdir,
               datafiles=pdFiles, 
               histnames=pdHists, 
               doRemake=args.doRemake,
              )




