import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir

fitNames = ["fourParM2j", "fiveParM2j"]


channelNames = [ "hybrid10_2javg_alpha0", "hybrid10_2javg_alpha1", "hybrid10_2javg_alpha2", "hybrid10_2javg_alpha3", "hybrid10_2javg_alpha4", "hybrid10_2javg_alpha5", "hybrid10_2javg_alpha6", "hybrid10_2javg_alpha7", "hybrid10_2javg_alpha8", "hybrid10_2javg_alpha9", "hybrid10_2javg_alpha10", "hybrid10_2javg_alpha11", ]


scaling = 10.0



# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = "fits2javg_hybrid_" + channelName

    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit%s_"%(channelName), nreplicas=config.nToys, scaling=scaling, outfile=pdFile, outhist=pdHistName)



