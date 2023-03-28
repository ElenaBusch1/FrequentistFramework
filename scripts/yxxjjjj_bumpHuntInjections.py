import scripts.config as config
import python.run_bumpHunt as run_bumpHunt
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
  pdFitName = "fivePar"
  fitName = "fourPar"
  #pdFitName = "fourPar"
  #fitName = "threePar"
  #channelNames = [ ["yxxjjjj_4j_alpha0"],[ "yxxjjjj_4j_alpha1"],[ "yxxjjjj_4j_alpha2"],[ "yxxjjjj_4j_alpha3"],[ "yxxjjjj_4j_alpha4"],[ "yxxjjjj_4j_alpha5"],[ "yxxjjjj_4j_alpha6"],[ "yxxjjjj_4j_alpha7"],[ "yxxjjjj_4j_alpha8"],[ "yxxjjjj_4j_alpha9"],[ "yxxjjjj_4j_alpha10"],[ "yxxjjjj_4j_alpha11"], ]
  channelNames = [ [ "yxxjjjj_4j_alpha5"]]

  #sigmeans = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
  #sigmeans = [2000, 3000,]
  sigmeans = [8000]
  #sigamps = [1,2,3,4,5]
  sigamps = [3]
  sigwidths = [10]
  signalfile =  "Gaussian"
  #coutputdir = "fits2javg_"
  coutputdir = "fits_"
  args.doRemake=1


#. scripts/setup_buildAndFit.sh
dosignal=1
dolimit=0

cdir = config.cdir

for channelName in channelNames:


  for sigmean in sigmeans:
    for sigamp in sigamps:
      for sigwidth in sigwidths:
        #nbkg="1E5,0,1e6"
        nbkg="1E4,0,1e6"
        #nsig="0,0,5e4"
        nsig="0,0,1e3"
        if sigmean > 3000:
          nsig="0,0,300"
        if sigmean > 5000:
          nsig="0,0,30"
        if sigmean > 9000:
          nsig="0,0,10"

        pdFiles = []
        pdHists = []
        for channel in channelName:
          outputdir = coutputdir+channelName[0]
          if not os.path.exists(outputdir):
            os.makedirs(outputdir)
          #pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir) + ".root"
          pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir, sigmean, sigwidth, sigamp) + "_Sig_Gaussian.root"
          pdFiles.append(pdFile)

          pdHistName = "pseudodata"
          pdHists.append(pdHistName)


        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_sigPlusBkg_1GeVBin_GlobalFit_%s"%(signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputfile = config.getFileName("FitResult_bkgOnlyInjections_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputstring = "FitResult_m4j_injections_%d_%d_%d_%s"%(sigamp, sigmean, sigwidth, signalfile)
        #binedges = config.getBinning(rangelow, rangehigh, delta=25)
        #binedges = None
        binedges = config.getBinningFromFile(channelName[0])

        topfile=config.samples[channelName[0]]["topfile"]

        #sigamp=sigamp,
        # Then run the injection
        run_bumpHunt.run_anaFit(
             datahist=channelName,
             topfile=topfile,
             fitFunction=fitName,
             cdir=cdir,
             wsfile=wsfile,
             sigmean=sigmean,
             sigwidth=sigwidth,
             nbkg=nbkg,
             nsig=nsig,
             outputfile=outputfile,
             outputstring=outputstring,
             dosignal = dosignal,
             dolimit = dolimit,
             rebinEdges=binedges,
             signalfile = signalfile,
             rebinFile=None,
             rebinHist=None,
             maskthreshold=-0.01,
             outdir=outputdir,
             datafiles=pdFiles,
             histnames=pdHists,
             doRemake = args.doRemake,
             useSysts = False,
            )





