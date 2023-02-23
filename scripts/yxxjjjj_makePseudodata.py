import scripts.config as config
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir

# The list of fit functions you are using
fitNames = ["threePar", "fourPar", "fivePar", "sixPar"]

# The list of signal regions/channels/etc
channelNames = [ "yxxjjjj_4j_alpha0", "yxxjjjj_4j_alpha1", "yxxjjjj_4j_alpha2", "yxxjjjj_4j_alpha3", "yxxjjjj_4j_alpha4", "yxxjjjj_4j_alpha5", "yxxjjjj_4j_alpha6", "yxxjjjj_4j_alpha7", "yxxjjjj_4j_alpha8", "yxxjjjj_4j_alpha9", "yxxjjjj_4j_alpha10", "yxxjjjj_4j_alpha11", ]

# If you want to upscale the results, do this here
scaling = 1.0


# Make the pseudodata for each fit function and channel
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = "fits_" + channelName

    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit%s_"%(channelName), nreplicas=config.nToys, scaling=scaling, outfile=pdFile, outhist=pdHistName)



