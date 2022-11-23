import scripts.config as config
import python.createMixedBackground  as generatePseudoData
import os


cdir = config.cdir
channelNames = ["ambulance_4j", "ambulance_2javg"]

fitNames = ["threePar", "fourPar"]

channelNames = ["yxxjjjj_4j_alpha0", "yxxjjjj_4j_alpha1", "yxxjjjj_4j_alpha2", "yxxjjjj_4j_alpha3", "yxxjjjj_4j_alpha4", "yxxjjjj_4j_alpha5", "yxxjjjj_4j_alpha6", "yxxjjjj_4j_alpha7", "yxxjjjj_4j_alpha8", "yxxjjjj_4j_alpha9"]

# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = "fitsNixon"

    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, outputdir) + ".root"

    pdHistName = "pseudodata"
    rangelow = config.samples[channelName]["rangelow"]


    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="data%s_"%(channelName), infit="postfit%s_"%channelName,nreplicas=config.nToys, scaling=1.0, outfile=pdFile, outhist=pdHistName, rangelow=rangelow)



