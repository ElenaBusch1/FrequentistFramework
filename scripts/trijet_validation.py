import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.runFTest as runFTest


# May want to loop over these at some point?
cdir = config.cdir
#fitNames = ["fourPar", "fivePar", "fiveParV2", "fiveParV3","sixPar"]
#fitNames = ["fourPar", "fivePar", "fiveParV3", "sixPar"]
#fitNames = ["fourPar", "fivePar", "fiveParV2", "sixPar", "sevenPar"]
#fitNames = ["fourPar", "fivePar", "sixPar", "UA2"]
fitNames = ["fourPar", "fivePar", "sixPar"]
#fitNames = ["fourPar", "fivePar", "sixPar", "UA2", "fullSwift"]
#fitNames = ["fourPar", "fivePar", "sixPar", "fullSwift"]
#fitNames = ["fivePar", "sixPar", "fullSwift", "UA2"]


#channelNames=[config.cSample]
channelNames=["ZeroBtagged70_23_ystar", "ZeroBtagged70_jj_ystar", "ZeroBtagged70_23", "ZeroBtagged70_jj"]

#channelNames=["Btagged70_23_ystar"]
#channelNames=["Btagged70_23_ystar", "Btagged70_jj_ystar", "Btagged70_23", "Btagged70_jj"]

rangeslow=[200]
rangeshigh=[900]
#rangeshigh=[800]
#rangeshigh=[1000, 1200]
#rangeslow=[config.cRangeLow]
#rangeshigh=[config.cRangeHigh]
signalfile =  config.cSignal


for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    #rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
    rebinedges = config.getBinning(rangelow, rangehigh, delta=20)
    for channelName in channelNames:
      lumi =  config.samples[channelName]["lumi"]
      infiles = []
      for pdFitName in fitNames:
        infiles.append("PostFit_%s_bkgonly"%(pdFitName))
      outfileFits = config.getFileName("fits", cdir + "/scripts/", channelName, rangelow, rangehigh)
      plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames)
    
      outfilePulls = "pulls_%s_Fit_%d_%d"%(channelName, rangelow, rangehigh)
      plotPulls.plotPulls(infiles=infiles, fitNames = fitNames, outfile=outfilePulls, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, atlasLabel=config.atlasLabel)




fitNames = ["fourPar", "fivePar", "sixPar"]
for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
    for channelName in channelNames:
      infiles = ["PostFit_fourPar_bkgonly", "PostFit_fivePar_bkgonly", "PostFit_sixPar_bkgonly"]
      outfile = "%s_Fit_%d_%d"%(channelName, rangelow, rangehigh)
      runFTest.runFTest(infiles=infiles, cdir=cdir + "/scripts/", outfile=outfile, rangelow=rangelow, rangehigh=rangehigh, channelName=channelName, lumi=lumi, atlasLabel=config.atlasLabel, rebinEdges=rebinedges)


