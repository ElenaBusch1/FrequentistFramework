import scripts.config as config
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir

# The list of fit functions you are using
#fitNames = ["threePar", "fourPar", "fivePar", "sixPar"]
fitNames = ["fiveParM2j", ]

# The list of signal regions/channels/etc

#channelNames = [ "Data_2javg_alpha0", "Data_2javg_alpha1", "Data_2javg_alpha2", "Data_2javg_alpha3", "Data_2javg_alpha4", "Data_2javg_alpha5", "Data_2javg_alpha6", "Data_2javg_alpha7", "Data_2javg_alpha8", "Data_2javg_alpha9", "Data_2javg_alpha10", "Data_2javg_alpha11", ]
channelNames = ["Data_2javg_alpha5",]



# If you want to upscale the results, do this here
scaling = 1.0


# Make the pseudodata for each fit function and channel
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = "fits2javg_data_%s"%channelName


    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit%s_"%(channelName), nreplicas=config.nToys, scaling=scaling, outfile=pdFile, outhist=pdHistName)



