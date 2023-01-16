import scripts.config as config
import python.run_anaFit as run_anaFit
import python.generatePseudoData as generatePseudoData
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
  coutputdir = "fits2javg_"

else:
  pdFitNames = ["threePar"]
  fitName = "fourPar"
  #channelNames = [ ["yxxjjjj_2javg_alpha0"],[ "yxxjjjj_2javg_alpha1"],[ "yxxjjjj_2javg_alpha2"],[ "yxxjjjj_2javg_alpha3"],[ "yxxjjjj_2javg_alpha4"],[ "yxxjjjj_2javg_alpha5"],[ "yxxjjjj_2javg_alpha6"],[ "yxxjjjj_2javg_alpha7"],[ "yxxjjjj_2javg_alpha8"],[ "yxxjjjj_2javg_alpha9"],[ "yxxjjjj_2javg_alpha10"],[ "yxxjjjj_2javg_alpha11"], ]
  channelNames = [ [ "yxxjjjj_2javg_alpha9"],[ "yxxjjjj_2javg_alpha10"],[ "yxxjjjj_2javg_alpha11"], ]

  signalfile = "Gaussian"
  coutputdir = "fits2javg_"
  args.doRemake = 1



dosignal=0
dolimit=0
cdir = config.cdir

nToys = config.nToys

for pdFitName in pdFitNames:
  for channelName in channelNames:
    outputdir = coutputdir+channelName[0]

    if not os.path.exists(outputdir):
          os.makedirs(outputdir)
    pdFiles = []
    pdHists = []
    for channel in channelName:
            pdFile = config.getFileName("PDfromMC_%s__bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir) + ".root"
            pdFiles.append(pdFile)

            pdHistName = "pseudodata"
            pdHists.append(pdHistName)

    pdHistName = "pseudodata"
    nbkg="1E3,0,1E5"
    nbkgWindow = 1
    nsig="0,-1e4,1e4"
    topfile=config.samples[channelName[0]]["topfile"]


    # Output file names, which will be written to outputdir
    wsfile = config.getFileName("FitResult_MCPD_bkgOnly_1GeVBin_GlobalFit", cdir + "/scripts/", None, outputdir) + ".root"
    outputfile = config.getFileName("FitResult_MCPD_bkgOnly_%s_%s"%(pdFitName, fitName), cdir + "/scripts/", None, outputdir) + ".root"

    # Then run the injection
    run_anaFit.run_anaFit(
         datahist=channelName,
         topfile=topfile,
         fitFunction=fitName,
         cdir=cdir,
         wsfile=wsfile,
         nbkg=nbkg,
         nbkgWindow=[],
         outputfile=outputfile,
         signalfile = signalfile,
         outputstring="SS_%s_%s_%s"%(pdFitName, fitName, signalfile),
         dosignal = dosignal,
         dolimit = dolimit,
         ntoys=nToys,
         maskthreshold=-0.01,
         outdir=outputdir,
         datafiles=pdFiles,
         histnames=pdHists,
         doRemake=args.doRemake,
        )







