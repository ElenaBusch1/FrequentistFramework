import config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os
import os,sys,re,argparse,subprocess,shutil


from optparse import OptionParser


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

  pdFitName = "fivePar"
  fitName = "fourPar"
  channelNames = [ ["tenPercentData_yxxjjjj_4j_alpha0"],  ]
  #channelNames = [ ["tenPercentData_yxxjjjj_4j_alpha0"], ["tenPercentData_yxxjjjj_4j_alpha1"], ["tenPercentData_yxxjjjj_4j_alpha2"], ["tenPercentData_yxxjjjj_4j_alpha3"], ["tenPercentData_yxxjjjj_4j_alpha4"], ["tenPercentData_yxxjjjj_4j_alpha5"], ["tenPercentData_yxxjjjj_4j_alpha6"], ["tenPercentData_yxxjjjj_4j_alpha7"], ["tenPercentData_yxxjjjj_4j_alpha8"], ["tenPercentData_yxxjjjj_4j_alpha9"], ["tenPercentData_yxxjjjj_4j_alpha10"], ["tenPercentData_yxxjjjj_4j_alpha11"], ]

  sigmeans = [2000,3000, 4000, 6000, 8000, 10000]
  #sigmeans = [2500, 3500, 5000, 7000, 9000]
  #sigmeans = [10000]
  sigamps = [0]
  sigwidths = [10]
  signalfile =  "Gaussian"
  #signalfile =  "template"
  coutputdir = "fitsTenPercentData"
  args.doRemake = 0


cdir = config.cdir
#if not os.path.exists(cdir + "/scripts/" + channelName):
#      os.makedirs(cdir + "/scripts/" + channelName)
#
# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
dosignal=1
dolimit=1

nToys = 1
#nToys = config.nToys


for channelName in channelNames:
  pdFiles = []
  pdHists = []
  for channel in channelName:
    outputdir = coutputdir + "_" + channel
    pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir) + ".root"
    pdFiles.append(pdFile)

    pdHistName = "pseudodata"
    pdHists.append(pdHistName)

  for sigmean in sigmeans:
    for sigamp in sigamps:
      for sigwidth in sigwidths:
        nbkg="1E7,0,5E8"
        nsig="0,0,1e6"

        # Output file names, which will be written to outputdir
        wsfile = config.getFileName("FitResult_limits_1GeVBin_GlobalFit_%s"%(signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputfile = config.getFileName("FitResult_limits_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputstring = "FitResult_limits_%d_%d_%d_%s_%s"%(sigamp, sigmean, sigwidth, signalfile, channelName[0])
        #binedges = None
        binedges = config.getBinningFromFile(channelName[0])
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
             loopend=nToys,
             rebinedges=binedges,
             signalfile = signalfile,
             rebinfile=None,
             rebinhist=None,
             maskthreshold=-0.01,
             outdir=outputdir,
             datafiles=pdFiles,
             histnames=pdHists,
             doRemake = args.doRemake,
             useSysts = True,
            )






