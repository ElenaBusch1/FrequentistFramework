import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os


cdir = config.cdir
#channelNames = ["testSherpa_15"]
#channelNames =  ["test3New_15"]
#channelNames =  ["Data_m32"]
channelNames = ["test3New_NoCut_no21"]


#rangelow=160
rangelow=225
rangehigh=1000

#fitNames = ["fourPar", "fivePar", "UA2", "sixPar"]
#fitNames = ["UA2"]
#fitNames = ["fourPar", "fivePar", "sixPar"]
fitNames = ["fivePar", "sixPar"]


# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
for fitName in fitNames:
  for channelName in channelNames:
    outputdir = channelName
    if not os.path.exists(outputdir):
      os.makedirs(outputdir)
    pdInputFile = config.getFileName("PostFit_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    pdFile = config.getFileName("PD_%s_bkgonly"%(fitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    pdHistName = "pseudodata"
    generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit", nreplicas=config.nToys, scaling=1.0, outfile=pdFile, outhist=pdHistName)



