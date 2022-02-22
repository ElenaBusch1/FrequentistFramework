import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.fitQualityTests as fitQualityTests
import python.getChi2Distribution as getChi2Distribution


# May want to loop over these at some point?
cdir = config.cdir
atlasLabel = "Simulation Internal"

pdFitName = config.cPDFitName
fitName = config.cFitName
channelNames=[config.cSample]
rangeslow=[config.cRangeLow]
rangeshigh=[config.cRangeHigh]
signalfile =  config.cSignal


for channelName in channelNames:
  lumi =  config.samples[channelName]["lumi"]
  for rangelow in rangeslow:
    for rangehigh in rangeshigh:

      #infilesChi2 = "PostFit_%s_PD_%s_bkgonly"%(pdFitName, fitName)
      #inhistChi2="chi2"
      #outfileChi2="chi2_pd_%s_%s_%s_%d_%d"%(channelName, pdFitName, fitName, rangelow, rangehigh)

      #getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=0, sigwidth=0, sigamp=0, lumi=lumi, atlasLabel=atlasLabel)

      #rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
  
      #infiles = ["PostFit_%s_PD_%s_bkgonly"%(pdFitName, fitName)]
      #outfileFits = config.getFileName("fits_PD_%s_%s"%(pdFitName, fitName), cdir + "/scripts/", channelName, rangelow, rangehigh)
      #plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, lumi=lumi, channelName=channelName, rebinedges=rebinedges, atlasLabel=config.atlasLabel, suffix="_0", cdir=cdir+"/scripts/")

  
      #outfilePulls = config.getFileName("pulls_PD_%s_%s_%s"%(channelName, pdFitName, fitName), cdir + "/scripts/", channelName, rangelow, rangehigh)
      #plotPulls.plotPulls(infiles=infiles, fitNames = ["five par"], outfile=outfilePulls, lumi=lumi, atlasLabel=config.atlasLabel, suffix="_0", cdir=cdir+"/scripts/", channelName=channelName, minMjj=rangelow, maxMjj=rangehigh)
  
      
      fit1 = "PostFit_%s_bkgonly"%(fitName)
      fit2 = "PostFit_%s_bkgonly"%(pdFitName)
      fitQualityTests.fitQualityTests("PostFit_%s_PD_%s_bkgonly"%(pdFitName, fitName), "PostFit_%s_PD_%s_bkgonly"%(pdFitName, fitName), fit1, fit2, "FitQuality_%s"%(channelName), config.nToys, rangelow, rangehigh, lumi, 0, 0, 0, cdir + "/scripts/", channelName)





