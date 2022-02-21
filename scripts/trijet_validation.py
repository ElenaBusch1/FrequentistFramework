import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.runFTest as runFTest


# May want to loop over these at some point?
cdir = config.cdir
#fitNames = ["fourPar", "fivePar", "fiveParV2", "fiveParV3","sixPar"]
#fitNames = ["fourPar", "fivePar", "fiveParV3", "sixPar"]
fitNames = ["fourPar", "fivePar", "sixPar"]


channelNames=[config.cSample]
rangeslow=[config.cRangeLow]
rangeshigh=[config.cRangeHigh]
signalfile =  config.cSignal


for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
    for channelName in channelNames:
      lumi =  config.samples[channelName]["lumi"]
      infiles = []
      for pdFitName in fitNames:
        infiles.append("PostFit_%s_bkgonly"%(pdFitName))
      outfileFits = config.getFileName("fits", cdir + "/scripts/", channelName, rangelow, rangehigh)
      plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames)
    
      outfilePulls = "pulls_%s_Fit_%d_%d"%(channelName, rangelow, rangehigh)
      plotPulls.plotPulls(infiles=infiles, fitNames = fitNames, outfile=outfilePulls, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, atlasLabel=config.atlasLabel)




for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
    for channelName in channelNames:
      infiles = ["PostFit_fourPar_bkgonly", "PostFit_fivePar_bkgonly", "PostFit_sixPar_bkgonly"]
      outfile = "%s_Fit_%d_%d"%(channelName, rangelow, rangehigh)
      runFTest.runFTest(infiles=infiles, cdir=cdir + "/scripts/", outfile=outfile, rangelow=rangelow, rangehigh=rangehigh, channelName=channelName, lumi=lumi, atlasLabel=config.atlasLabel, rebinEdges=rebinedges)


