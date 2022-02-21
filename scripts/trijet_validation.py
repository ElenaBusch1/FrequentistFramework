import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.runFTest as runFTest


# May want to loop over these at some point?
cdir = config.cdir
#channelNames =["BkgLow_2_alpha0_SR1_tagged", "BkgLow_3_alpha0_SR1_tagged"]
#fitNames = ["fourPar", "fivePar", "fiveParV2", "fiveParV3","sixPar"]
fitNames = ["fourPar", "fivePar", "fiveParV3", "sixPar"]
#fitNames = ["fourPar", "fivePar", "sixPar"]


#rangeslow=[300]
#rangeshigh=[900]
#rangeslow=[200, 250, 275, 300, 350, 400]
#rangeshigh=[700, 800, 900, 1000, 1200, 1400]

#rangeslow=[300]
#rangeshigh=[900]


#channelNames=["MassOrdered_2"]
#channelNames=["PtOrdered5Tagged"]
channelNames=["PtOrdered6"]
#rangeslow=[200, 250, 275, 300, 350, 400]
#rangeshigh=[700, 800, 900, 1000, 1200, 1400]
#rangeshigh=[700, 800, 900, 1000, 1100]
#rangeslow=[200, 300]
#rangeshigh=[800, 900]
#rangeslow=[150, 200]
#rangeshigh=[800, 900]
rangeslow=[200]
rangeshigh=[900, 1000]



#channelNames = ["PtOrderedSR2_tagged"]
#rangeslow=[600, 700]
#rangeshigh=[1200, 1500]


#channelNames = ["PtOrderedSR1_tagged"]
#rangeslow=[150, 200, 300]
#rangeshigh=[800, 900]


for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
    for channelName in channelNames:
      lumi =  config.samples[channelName]["lumi"]
      infiles = []
      for pdFitName in fitNames:
        infiles.append("PostFit_%s_bkgonly"%(pdFitName))
      outfileFits = config.getFileName("fits", cdir + "/scripts/", channelName, rangelow, rangehigh)
      plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel)
    
      #outfilePulls = config.getFileName("pulls_%s"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh)
      outfilePulls = "pulls"
      plotPulls.plotPulls(infiles=infiles, fitNames = fitNames, outfile=outfilePulls, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, atlasLabel=config.atlasLabel)




for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
    for channelName in channelNames:
      infiles = ["PostFit_fourPar_bkgonly", "PostFit_fivePar_bkgonly", "PostFit_sixPar_bkgonly"]
      runFTest.runFTest(infiles=infiles, cdir=cdir + "/scripts/", outfile="test", rangelow=rangelow, rangehigh=rangehigh, channelName=channelName, lumi=lumi, atlasLabel=config.atlasLabel, rebinEdges=rebinedges)


