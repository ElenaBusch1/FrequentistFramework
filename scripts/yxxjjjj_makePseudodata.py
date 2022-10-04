import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir

fitNames = ["fourPar", "fivePar", "sixPar"]
channelNames = [ "bba", ]


# First make the pseudodata
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = config.cSample

    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit%s_"%(channelName), nreplicas=config.nToys, scaling=1.0, outfile=pdFile, outhist=pdHistName)



