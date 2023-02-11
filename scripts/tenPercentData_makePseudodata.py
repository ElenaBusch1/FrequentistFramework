import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir

fitNames = ["threePar", "fourPar", "fivePar"]

channelNames = [ "tenPercentData_yxxjjjj_4j_alpha0", "tenPercentData_yxxjjjj_4j_alpha1", "tenPercentData_yxxjjjj_4j_alpha2", "tenPercentData_yxxjjjj_4j_alpha3", "tenPercentData_yxxjjjj_4j_alpha4", "tenPercentData_yxxjjjj_4j_alpha5", "tenPercentData_yxxjjjj_4j_alpha6", "tenPercentData_yxxjjjj_4j_alpha7", "tenPercentData_yxxjjjj_4j_alpha8", "tenPercentData_yxxjjjj_4j_alpha9", "tenPercentData_yxxjjjj_4j_alpha10", "tenPercentData_yxxjjjj_4j_alpha11", ]
#channelNames = [ "tenPercentData_yxxjjjj_4j_alpha10",]

scaling = 1.

# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = "fitsTenPercentData_" + channelName

    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit%s_"%(channelName), nreplicas=config.nToys, scaling=scaling, outfile=pdFile, outhist=pdHistName)



