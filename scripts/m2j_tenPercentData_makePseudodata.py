import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir

fitNames = ["fourParM2j", "fiveParM2j"]


channelNames = [ "tenPercentData_2javg_alpha0", "tenPercentData_2javg_alpha1", "tenPercentData_2javg_alpha2", "tenPercentData_2javg_alpha3", "tenPercentData_2javg_alpha4", "tenPercentData_2javg_alpha5", "tenPercentData_2javg_alpha6", "tenPercentData_2javg_alpha7", "tenPercentData_2javg_alpha8", "tenPercentData_2javg_alpha9", "tenPercentData_2javg_alpha10", "tenPercentData_2javg_alpha11", ]
#channelNames = [ "tenPercentData_2javg_alpha8",]


scaling = 1.0



# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = "fits2javg_10data_" + channelName

    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit%s_"%(channelName), nreplicas=config.nToys, scaling=scaling, outfile=pdFile, outhist=pdHistName)



