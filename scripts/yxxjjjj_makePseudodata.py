import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir

#fitNames = ["threePar", "fourPar", "fivePar"]
fitNames = ["fourPar", "fivePar"]

channelNames = [ "yxxjjjj_4j_alpha0", "yxxjjjj_4j_alpha1", "yxxjjjj_4j_alpha2", "yxxjjjj_4j_alpha3", "yxxjjjj_4j_alpha4", "yxxjjjj_4j_alpha5", "yxxjjjj_4j_alpha6", "yxxjjjj_4j_alpha7", "yxxjjjj_4j_alpha8", "yxxjjjj_4j_alpha9", "yxxjjjj_4j_alpha10", "yxxjjjj_4j_alpha11", ]
#channelNames = [ "sherpa_yxxjjjj_4j_alpha0", "sherpa_yxxjjjj_4j_alpha1", "sherpa_yxxjjjj_4j_alpha2", "sherpa_yxxjjjj_4j_alpha3", "sherpa_yxxjjjj_4j_alpha4", "sherpa_yxxjjjj_4j_alpha5", "sherpa_yxxjjjj_4j_alpha6", "sherpa_yxxjjjj_4j_alpha7", "sherpa_yxxjjjj_4j_alpha8", "sherpa_yxxjjjj_4j_alpha9", "sherpa_yxxjjjj_4j_alpha10", "sherpa_yxxjjjj_4j_alpha11" ]

scaling = 1.0



# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = "fits_" + channelName

    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit%s_"%(channelName), nreplicas=config.nToys, scaling=scaling, outfile=pdFile, outhist=pdHistName)



