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

rangeslow=[300]
rangeshigh=[900]
#rangeslow=[200]
#rangeshigh=[800]
#rangeshigh=[800]
signalfile =  config.cSignal
#swiftRangesLow=[300, 400, 500, 600, 700]
#swiftRangesHigh=[500, 600, 700, 800, 900]

swiftRangesLow = range(200, 900, 10)
swiftRangesHigh = range(400, 1100, 10)

#swiftRangesLow=[200, 300, 400, 500, 600, 700]
#swiftRangesHigh=[400, 500, 600, 700, 800, 900]

#swiftRangesLow = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
#swiftRangesHigh = [400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]



for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    for channelName in channelNames:
      lumi =  config.samples[channelName]["lumi"]
      infiles = []
      for pdFitName in fitNames:
        infiles.append("PostFit_%s_swift_bkgonly"%(pdFitName))
      outfile = "Swift"

      stitchSwift.stitchSwift(infiles, outfile, rangelow, rangehigh, lumi, cdir+"/scripts/", channelName, minMasses = swiftRangesLow, maxMasses = swiftRangesHigh)






