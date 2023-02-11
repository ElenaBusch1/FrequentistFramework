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
  coutputdir = args.outputdir

else:
  pdFitName = "fourParM2j"
  fitName = "threeParM2j"
  #pdFitName = "fiveParM2j"
  #fitName = "fourParM2j"
  #channelNames = [ ["yxxjjjj_2javg_alpha0"],[ "yxxjjjj_2javg_alpha1"],[ "yxxjjjj_2javg_alpha2"],[ "yxxjjjj_2javg_alpha3"],[ "yxxjjjj_2javg_alpha4"],[ "yxxjjjj_2javg_alpha5"],[ "yxxjjjj_2javg_alpha6"],[ "yxxjjjj_2javg_alpha7"],[ "yxxjjjj_2javg_alpha8"],[ "yxxjjjj_2javg_alpha9"],[ "yxxjjjj_2javg_alpha10"],[ "yxxjjjj_2javg_alpha11"], ]
  #channelNames = [ [ "yxxjjjj_2javg_alpha8"],[ "yxxjjjj_2javg_alpha9"],[ "yxxjjjj_2javg_alpha10"],[ "yxxjjjj_2javg_alpha11"], ]
  channelNames = [ [ "yxxjjjj_2javg_alpha3"], ]


  #sigmeans = [500, 700, 1000, 1500, 2000, 2500, 3000]
  sigmeans = [500]
  #sigamps = [0,1,2,3,4,5]
  sigamps = [2]
  sigwidths = [10]
  signalfile =  "Gaussian"
  coutputdir = "fits2javg_"
  args.doRemake=1


#. scripts/setup_buildAndFit.sh
dosignal=1
dolimit=0

cdir = config.cdir

for channelName in channelNames:
  pdFiles = []
  pdHists = []
  for channel in channelName:
    outputdir = coutputdir+channelName[0]
    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir) + ".root"
    pdFiles.append(pdFile)

    pdHistName = "pseudodata"
    pdHists.append(pdHistName)


  for sigmean in sigmeans:
    for sigamp in sigamps:
      for sigwidth in sigwidths:
        nbkg="1E4,0,5e5"
        nsig="0,0,1000"
        if sigmean > 500:
          nsig="0,0,800"
        if sigmean > 700:
          nsig="0,0,500"
        if sigmean > 1000:
          nsig="0,0,50"


        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_sigPlusBkg_1GeVBin_GlobalFit_%s"%(signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputfile = config.getFileName("FitResult_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputstring = "FitResult_injections_%d_%d_%d_%s_%s"%(sigamp, sigmean, sigwidth, signalfile, channelName[0])
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
             useSysts = False,
            )




