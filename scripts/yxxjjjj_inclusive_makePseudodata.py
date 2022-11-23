import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir

fitNames = ["fourPar", "fivePar", "sixPar"]

channelNames = ["yxxjjjj_4j_inclusive"]


# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = "fitsyxxjjjjInclusive"

    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit%s_"%(channelName), nreplicas=config.nToys, scaling=1.0, outfile=pdFile, outhist=pdHistName)



