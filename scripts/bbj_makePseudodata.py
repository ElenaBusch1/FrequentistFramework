import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir
#channelNames =  ["btagFinal", "btag_32"]
channelNames =  ["btagFinal"]

rangelow=160
#rangehigh=1200
rangehigh=700

#fitNames = ["fiveParV2"]
#fitNames = ["fourPar", "fivePar", "UA2", "sixPar"]
#fitNames = ["sevenPar"]
#fitNames = ["UA2"]
fitNames = ["fourPar", "fivePar", "sixPar"]
#fitNames = ["sixPar"]


# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = channelName
    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit", nreplicas=config.nToys, scaling=1.0, outfile=pdFile, outhist=pdHistName)



