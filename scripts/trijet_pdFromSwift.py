import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir
#channelNames=["BkgLow_2_alpha0_SR1_tagged", "BkgLow_3_alpha0_SR1_tagged"]
#channelNames = ["MassOrdered_2"]
channelNames = ["PtOrdered6"]

rangelow=200
rangehigh=900

# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for channelName in channelNames:
  outputdir = channelName
  if not os.path.exists(outputdir):
    os.makedirs(outputdir)
  pdInputFile = config.getFileName("PostFit_fullSwift", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
  pdFile = config.getFileName("PD_fullSwift_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
  pdHistName = "pseudodata"
  generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit", nreplicas=config.nToys, scaling=1, outfile=pdFile, outhist=pdHistName)



