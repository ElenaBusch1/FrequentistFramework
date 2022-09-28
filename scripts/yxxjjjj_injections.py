import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import os


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
  channelNames = [args.channelNames]
  sigmeans = [args.sigmean]
  sigamps = [args.sigamp]
  sigwidths = [args.sigwidth]
  signalfile = args.signalFile
  outputdir = args.outputdir

else:
  pdFitName = "fivePar"
  fitName = "fourPar"
  #channelNames = [ ["nixon_4j_alpha0", "nixon_4j_alpha1", "nixon_4j_alpha2", "nixon_4j_alpha3", "nixon_4j_alpha4", "nixon_4j_alpha5", "nixon_4j_alpha6", "nixon_4j_alpha7", "nixon_4j_alpha8", "nixon_4j_alpha9"], ]
  channelNames =[ ["nixon_4j_alpha0", "nixon_4j_alpha1", "nixon_4j_alpha2", "nixon_4j_alpha3", "nixon_4j_alpha4", "nixon_4j_alpha5", "nixon_4j_alpha6", "nixon_4j_alpha7", "nixon_4j_alpha8", "nixon_4j_alpha9", "nixon_4j_alpha10", "nixon_4j_alpha11", "nixon_4j_alpha12"],]

  sigmeans = [6000]
  sigamps = [1]
  sigwidths = [10]
  signalfile =  "template"
  outputdir = "fitsNixon"
  args.doRemake=0


#. scripts/setup_buildAndFit.sh
dosignal=1
dolimit=0

cdir = config.cdir


if not os.path.exists(outputdir):
      os.makedirs(outputdir)

pdFiles = []
pdHists = []
for channelName in channelNames:
  for channel in channelName:
    pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir) + ".root"
    pdFiles.append(pdFile)

    pdHistName = "pseudodata"
    pdHists.append(pdHistName)


  for sigmean in sigmeans:
    for sigamp in sigamps:
      for sigwidth in sigwidths:
        nbkg="1E5,0,1e6"
        nsig="0,0,5e3"
        if sigmean > 5000:
          nsig="0,0,15"
          
    
        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_sigPlusBkg_1GeVBin_GlobalFit_%s"%(signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputfile = config.getFileName("FitResult_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputstring = "FitResult_injections_%d_%d_%d_%s"%(sigamp, sigmean, sigwidth, signalfile)
        #binedges = config.getBinning(rangelow, rangehigh, delta=25)
        binedges = None
        topfile=config.samples[channelName[0]]["topfile"]

        # Then run the injection
        run_injections_anaFit.run_injections_anaFit(
             datahist=channelName,
             topfile=topfile,
             fitFunction=fitName,
             cdir=cdir,
             wsfile=wsfile,
             sigmean=sigmean,
             sigwidth=sigwidth,
             sigamp=sigamp,
             nbkg=nbkg,
             nsig=nsig,
             outputfile=outputfile,
             outputstring=outputstring,
             dosignal = dosignal,
             dolimit = dolimit,
             loopstart=0,
             loopend=config.nToys,
             rebinedges=binedges,
             signalfile = signalfile,
             rebinfile=None,
             rebinhist=None,
             maskthreshold=-0.01,
             outdir=outputdir,
             datafiles=pdFiles,
             histnames=pdHists,
             doRemake = args.doRemake,
            )





