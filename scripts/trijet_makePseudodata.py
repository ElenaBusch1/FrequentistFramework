import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir
channelName="BkgLow_2_alpha0_SR1_tagged"
outputdir = channelName
if not os.path.exists(outputdir):
      os.makedirs(outputdir)

rangelow=300
rangehigh=900

# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
pdInputFile = config.getFileName("PostFit_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
pdFile = config.getFileName("PD_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
pdHistName = "pseudodata"
generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit", nreplicas=config.nToys, scaling=1, outfile=pdFile, outhist=pdHistName)



