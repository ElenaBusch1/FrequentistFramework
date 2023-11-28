import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.runFTest as runFTest


# May want to loop over these at some point?
cdir = config.cdir
#fitNames = ["fourPar", "fivePar", "sixPar"]
#fitNames = ["fivePar", "sixPar"]
#fitNames = ["fourPar"]
fitNames = ["fivePar"]

#channelNames=["Data18Partial", "Data15"]
#channelNames=["test3New_15"]
#channelNames=["testSherpa_15"]
#channelNames=["mj2j3", "mjjmin", "mjjmindphi"]
#channelNames = ["FullRun2Data_NoNN", "FullRun2Data"]
channelNames = ["FullRun2Data_NoNN_No21"]
#channelNames = ["FullRun2Data"]
#channelNames = ["test3New_15_MCEffOnData"]
#channelNames = ["test3New_15_MCwithMC"]
#channelNames = ["test3New_15_dataEff"]
#channelNames = ["test3New_15_dataEff", "test3New_15_data_mcEff"]
#channelNames = ["test3New_15_data_mcEff"]

#channelNames = ["Data16", "Data17", "Data18"]
#channelNames = ["Data16"]
#channelNames = ["Data16_massAnd"]
#channelNames = ["Data16", "Data16MCJES", "Data16NoInsitu"]
#channelNames = ["Data_475_60"]
#channelNames = ["Data_minMass"]
#channelNames = ["test3New_NoCut_no21"]

rangeslow=[225]
rangeshigh=[1000]


signalfile =  config.cSignal


for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    #rebinedges = config.getBinning(rangelow, rangehigh, delta=10)
    rebinedges = config.getBinning(rangelow, rangehigh)
    #rebinedges = config.getBinning(rangelow, rangehigh, delta=1)
    #rebinedges = config.getBinning(rangelow, rangehigh, delta=100)
    for channelName in channelNames:
      lumi =  config.samples[channelName]["lumi"]/1000.
      print lumi, channelName
      infiles = []
      for pdFitName in fitNames:
        infiles.append("PostFit_%s_bkgonly"%(pdFitName))
      outfileFits = config.getFileName("fits", cdir + "/scripts/", channelName, rangelow, rangehigh)
      plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames)
    
      outfilePulls = "pulls_%s_Fit_%d_%d"%(channelName, rangelow, rangehigh)
      plotPulls.plotPulls(infiles=infiles, fitNames = fitNames, outfile=outfilePulls, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, atlasLabel=config.atlasLabel)




'''
fitNames = ["fivePar", "sixPar"]
for rangelow in rangeslow:
  for rangehigh in rangeshigh:
    rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
    for channelName in channelNames:
      infiles = ["PostFit_fourPar_bkgonly", "PostFit_fivePar_bkgonly", "PostFit_sixPar_bkgonly"]
      outfile = "%s_Fit_%d_%d"%(channelName, rangelow, rangehigh)
      runFTest.runFTest(infiles=infiles, cdir=cdir + "/scripts/", outfile=outfile, rangelow=rangelow, rangehigh=rangehigh, channelName=channelName, lumi=lumi, atlasLabel=config.atlasLabel, rebinEdges=rebinedges)


'''
