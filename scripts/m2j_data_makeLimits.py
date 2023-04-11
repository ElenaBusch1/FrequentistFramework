import config as config
import python.run_limits as run_anaFit
import python.generatePseudoData as generatePseudoData
import os,sys,re,argparse,subprocess,shutil
import python.getBias as gb



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
  #channelNames = [ ["yxxjjjj_4j_alpha0"], ["yxxjjjj_4j_alpha1"], ["yxxjjjj_4j_alpha2"], ["yxxjjjj_4j_alpha3"], ["yxxjjjj_4j_alpha4"], ["yxxjjjj_4j_alpha5"], ["yxxjjjj_4j_alpha6"], ["yxxjjjj_4j_alpha7"], ["yxxjjjj_4j_alpha8"], ["yxxjjjj_4j_alpha9"], ["yxxjjjj_4j_alpha10"], ["yxxjjjj_4j_alpha11"], ]
  channelNames = [[ "0"], ]

  #channelNames = [ ["yxxjjjj_4j_alpha0"], ]
  #alphaBins = [0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33]
  alphaBins = [0.11]

  #sigmeans = [2500, 3500, 5000, 7000, 9000]
  sigmeans = [700]
  sigamps = [0]
  sigwidths = [10]
  signalfile =  "crystalBallHist"
  #signalfile =  "template"
  args.doRemake = 1


cdir = config.cdir
dosignal=1
dolimit=1

coutputdir = "fits2javg_data"

cdir = config.cdir
baseChannelName = "Data_2javg_alpha"
tagName = "m2j_"

nToys = 1
#nToys = config.nToys



for channelSuffix in channelNames:
  channelName = [baseChannelName + "%d"%(int(channelSuffix[0]))]
  alpha = config.alphaBins[int(channelSuffix[0])]

  pdFiles = []
  pdHists = []
  for channel in channelName:
    #outputdir = coutputdir + "_" + channel
    outputdir = coutputdir + channel
    pdFile = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channel, outputdir) + ".root"
    pdFiles.append(pdFile)

    pdHistName = "pseudodata"
    pdHists.append(pdHistName)

  for sigmean in sigmeans:
    mY = round( (sigmean/alpha)*10)/10
    if mY < 500:
      continue


    for sigamp in sigamps:
      for sigwidth in sigwidths:
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
        outputfile = config.getFileName("FitResult_limits_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", None, outputdir, sigmean, sigwidth, sigamp) + ".root"
        outputstring = "FitResult_limits_%d_%d_%d_%s_%s"%(sigamp, sigmean, sigwidth, signalfile, channelName[0])
        #binedges = None
        binedges = config.getBinningFromFile(channelName[0])
        topfile=config.samples[channelName[0]]["topfile"]
        biasMagnitude = gb.getSpuriousSignal(coutputdir, channelName[0], sigmean, sigwidth, biasFraction= 0.5, signalName=signalfile+"NoSyst")


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
             nsig=nsig,
             outputfile=outputfile,
             outputstring=outputstring,
             dosignal = dosignal,
             dolimit = dolimit,
             rebinEdges=binedges,
             signalfile = signalfile,
             rebinFile=None,
             rebinHist=None,
             maskthreshold=0.05,
             outdir=outputdir,
             datafiles=pdFiles,
             histnames=pdHists,
             doRemake = args.doRemake,
             useSysts = True,
             biasMagnitude = biasMagnitude,
             tagName=tagName,
             isMx = True,
            )






