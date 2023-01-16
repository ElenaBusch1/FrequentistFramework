import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir

fitNames = ["threePar"]

channelNames = [ "yxxjjjj_2javg_alpha0", "yxxjjjj_2javg_alpha1", "yxxjjjj_2javg_alpha2", "yxxjjjj_2javg_alpha3", "yxxjjjj_2javg_alpha4", "yxxjjjj_2javg_alpha5", "yxxjjjj_2javg_alpha6", "yxxjjjj_2javg_alpha7", "yxxjjjj_2javg_alpha8", "yxxjjjj_2javg_alpha9", "yxxjjjj_2javg_alpha10", "yxxjjjj_2javg_alpha11", ]


scaling = 1.0



# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = "fits2javg_" + channelName

    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    #pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PDfromMC_%s__bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    pdInputFile = config.samples[channelName]["inputFile"]
    inhist = config.samples[channelName]["histname"]
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist =inhist, nreplicas=config.nToys, scaling=scaling, outfile=pdFile, outhist=pdHistName)



