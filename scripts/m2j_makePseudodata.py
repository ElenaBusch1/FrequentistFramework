import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir

#fitNames = ["fourParM2j", "fiveParM2j"]
fitNames = ["sixParM2j"]

#channelNames = [ "yxxjjjj_2javg_alpha3", ]
channelNames = [ "yxxjjjj_2javg_alpha0", "yxxjjjj_2javg_alpha1", "yxxjjjj_2javg_alpha2", "yxxjjjj_2javg_alpha3", "yxxjjjj_2javg_alpha4", "yxxjjjj_2javg_alpha5", "yxxjjjj_2javg_alpha6", "yxxjjjj_2javg_alpha7", "yxxjjjj_2javg_alpha8", "yxxjjjj_2javg_alpha9", "yxxjjjj_2javg_alpha10", "yxxjjjj_2javg_alpha11", ]
#channelNames = [ "sherpa_yxxjjjj_2javg_alpha0", "sherpa_yxxjjjj_2javg_alpha1", "sherpa_yxxjjjj_2javg_alpha2", "sherpa_yxxjjjj_2javg_alpha3", "sherpa_yxxjjjj_2javg_alpha4", "sherpa_yxxjjjj_2javg_alpha5", "sherpa_yxxjjjj_2javg_alpha6", "sherpa_yxxjjjj_2javg_alpha7", "sherpa_yxxjjjj_2javg_alpha8", "sherpa_yxxjjjj_2javg_alpha9", "sherpa_yxxjjjj_2javg_alpha10", "sherpa_yxxjjjj_2javg_alpha11" ]

scaling = 1.0



# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = "fits2javg_" + channelName

    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit%s_"%(channelName), nreplicas=config.nToys, scaling=scaling, outfile=pdFile, outhist=pdHistName)



