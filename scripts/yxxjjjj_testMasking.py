import scripts.config as config
import python.run_anaFit as run_anaFit
import python.generatePseudoData as generatePseudoData
import python.run_injections_anaFit as run_injections_anaFit

import os



from optparse import OptionParser

parser = OptionParser()
parser.add_option('--isBatch', dest='isBatch', type=int, default=0, help='Input data file')
parser.add_option('--fitName', dest='fitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_option('--pdFitName', dest='pdFitName', type=str, default=None, help='Name of the file with the fit function information')
parser.add_option('--signalFile', dest='signalFile', type=str, default=None, help='Name of the signal file')
parser.add_option('--channelName', dest='channelName', type=str, help='Output workspace file')
parser.add_option('--doRemake', dest='doRemake', type=int, default=0, help='Amplitude of signal Gaussian for s+b fit (in %)')
parser.add_option('--rangelow', dest='rangelow', type=int, help='Start of fit range (in GeV)')
parser.add_option('--rangehigh', dest='rangehigh', type=int, help='End Start of fit range (in GeV)')
(args, test) = parser.parse_args()



if args.isBatch:
  pdFitNames = [args.pdFitName]
  fitName = args.fitName
  channelNames = [args.channelName]
  signalfile = args.signalfile
  coutputdir = "fits_"

else:
  pdFitNames = ["fivePar"]
  fitName = "fourPar"
  #channelNames = [ ["yxxjjjj_4j_alpha0"],[ "yxxjjjj_4j_alpha1"],[ "yxxjjjj_4j_alpha2"],[ "yxxjjjj_4j_alpha3"],[ "yxxjjjj_4j_alpha4"],[ "yxxjjjj_4j_alpha5"],[ "yxxjjjj_4j_alpha6"],[ "yxxjjjj_4j_alpha7"],[ "yxxjjjj_4j_alpha8"],[ "yxxjjjj_4j_alpha9"],[ "yxxjjjj_4j_alpha10"],[ "yxxjjjj_4j_alpha11"], ]
  channelNames = [ ["yxxjjjj_4j_alpha0"],]
  signalfile = "Gaussian"
  coutputdir = "fits_"
  args.doRemake = 1

sigamp = 8

dosignal=0
dolimit=0
cdir = config.cdir

sigmean = 3000
sigwidth = 5
#nToys = config.nToys
nToys = 1

for pdFitName in pdFitNames:
  for channelName in channelNames:
    outputdir = coutputdir+channelName[0]

    if not os.path.exists(outputdir):
          os.makedirs(outputdir)
    pdFiles = []
    pdHists = []
    for channel in channelName:
            pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir) + ".root"
            pdFiles.append(pdFile)

            pdHistName = "pseudodata"
            pdHists.append(pdHistName)

    pdHistName = "pseudodata"
    nbkg="1E3,0,1E5"
    nbkgWindow = 1
    nsig="0,-1e4,1e4"
    topfile=config.samples[channelName[0]]["topfile"]


    # Output file names, which will be written to outputdir
    wsfile = config.getFileName("FitResult_bkgOnly_1GeVBin_GlobalFit", cdir + "/scripts/", None, outputdir) + ".root"
    outputfile = config.getFileName("FitResult_bkgOnly_%s_%s"%(pdFitName, fitName), cdir + "/scripts/", None, outputdir) + ".root"
    outputstring = "FitResultInjections_m4j_injections_%d_%d_%d_%s"%(sigamp, sigmean, sigwidth, signalfile)
    binedges = config.getBinningFromFile(channelName[0])


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
             loopend=nToys,
             rebinedges=binedges,
             signalfile = signalfile,
             rebinfile=None,
             rebinhist=None,
             maskthreshold=0.05,
             outdir=outputdir,
             datafiles=pdFiles,
             histnames=pdHists,
             doRemake = args.doRemake,
             useSysts = False,
            )



    ## Then run the injection
    ##run_anaFit.run_anaFit(
    #run_anaFit.run_anaFit(
    #     datahist=channelName,
    #     topfile=topfile,
    #     fitFunction=fitName,
    #     cdir=cdir,
    #     wsfile=wsfile,
    #     nbkg=nbkg,
    #     nbkgWindow=[],
    #     outputfile=outputfile,
    #     signalfile = signalfile,
    #     outputstring="SS_%s_%s_%s"%(pdFitName, fitName, signalfile),
    #     dosignal = dosignal,
    #     dolimit = dolimit,
    #     ntoys=nToys,
    #     maskthreshold=0.05,
    #     outdir=outputdir,
    #     datafiles=pdFiles,
    #     histnames=pdHists,
    #     doRemake=args.doRemake,
    #    )







