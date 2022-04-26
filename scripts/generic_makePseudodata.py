import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir
channelNames = ["test3"]
rangelow=200
rangehigh=1200
fitNames = ["fivePar", "sixPar"]


# Generate pseudodata using the different fits you are considering
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = channelName
    if not os.path.exists(outputdir):
      os.makedirs(outputdir)

    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit", nreplicas=config.nToys, scaling=1.0, outfile=pdFile, outhist="pseudodata")



