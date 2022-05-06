import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir
#channelNames=["BkgLow_2_alpha0_SR1_tagged", "BkgLow_3_alpha0_SR1_tagged"]
#channelNames = ["MassOrdered_2"]
channelNames = ["testSherpa"]
#channelNames = ["test3"]

rangelow=200
rangehigh=1200

#fitNames = ["fiveParV2"]
#fitNames = ["fourPar", "fivePar", "UA2", "sixPar"]
#fitNames = ["sevenPar"]
#fitNames = ["UA2"]
#fitNames = ["fourPar", "fivePar", "sixPar"]
fitNames = ["fivePar", "sixPar"]


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



