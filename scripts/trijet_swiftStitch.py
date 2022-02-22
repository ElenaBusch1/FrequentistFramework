import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.runFTest as runFTest


import python.stitchSwift as stitchSwift

# May want to loop over these at some point?
cdir = config.cdir
fitNames = ["threePar"]


channelNames=[config.cSample]

rangeslow=[200]
rangeshigh=[900]
signalfile =  config.cSignal
#rangeslow=[200, 300, 400, 500, 600, 700]
#rangeshigh=[400, 500, 600, 700, 800, 900]


for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    for channelName in channelNames:
      lumi =  config.samples[channelName]["lumi"]
      infiles = []
      for pdFitName in fitNames:
        infiles.append("PostFit_%s_swift_bkgonly"%(pdFitName))
      outfile = "Swift"

      stitchSwift.stitchSwift(infiles, outfile, rangelow, rangehigh, lumi, cdir+"/scripts/", channelName, minMasses = [200, 300, 400, 500, 600, 700], maxMasses = [400, 500, 600, 700, 800, 900])






