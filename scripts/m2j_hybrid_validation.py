import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.runFTest as runFTest


# May want to loop over these at some point?
cdir = config.cdir



channelNames = [ ["hybrid10_2javg_alpha0"],[ "hybrid10_2javg_alpha1"],[ "hybrid10_2javg_alpha2"],[ "hybrid10_2javg_alpha3"],[ "hybrid10_2javg_alpha4"],[ "hybrid10_2javg_alpha5"],[ "hybrid10_2javg_alpha6"],[ "hybrid10_2javg_alpha7"],[ "hybrid10_2javg_alpha8"],[ "hybrid10_2javg_alpha9"],[ "hybrid10_2javg_alpha10"],[ "hybrid10_2javg_alpha11"], ]
#channelNames = [ ["hybrid10_2javg_alpha3"],]



#rebinFactors = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
#rebinFactors = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
#rebinFactors = [50, 50, 50, 50, 50, 50, 5, 5, 5, 5, 5, 5, 5, 5, 5]
rebinFactors = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
#rebinFactors = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
#rebinFactors = [10]
#fitNames = ["fourPar"]
#fitNames = ["fivePar"]
#fitNames = ["threePar","fourPar", "fivePar", "sixPar"]
#fitNames = ["fourPar", "fivePar"]
fitNames = ["threeParM2j","fourParM2j", "fiveParM2j"]
#rangeslow=[100]
#rangeshigh=[3000]
#rebinFactors = [10]

signalfile =  "Gaussian"


base_outputdir = "fits2javg_hybrid_"
for channelNameSet, rebinFactor in zip(channelNames, rebinFactors):
  outputdir = base_outputdir + channelNameSet[0]
  for channelName in channelNameSet:
      rangelow=config.samples[channelName]["rangelow"]
      rangehigh=config.samples[channelName]["rangehigh"]
      #rebinedges = config.getBinning(rangelow, rangehigh, delta=rebinFactor)
      rebinedges = config.getBinningFromFile(channelName)

      lumi =  config.samples[channelName]["lumi"]
      infiles = []
      for pdFitName in fitNames:
        infiles.append("PostFit_%s_bkgonly"%(pdFitName))
      outfileFits = config.getFileName("fits", cdir + "/scripts/", channelName, outputdir)
      #outfileFits = outputdir + "/Fits_" + channelName 
      plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir, cutoffSpectrum = True)
    
      #outfilePulls = "pulls_%s_Fit_%d_%d"%(channelName, rangelow, rangehigh)
      outfilePulls = config.getFileName("pulls", cdir + "/scripts/", channelName, outputdir)
      #plotPulls.plotPulls(infiles=infiles, fitNames = fitNames, outfile=outfilePulls, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, atlasLabel=config.atlasLabel, outputdir=outputdir)
      plotPulls.plotPulls(infiles=infiles, fitNames = fitNames, outfile="pulls", minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, atlasLabel=config.atlasLabel, outputdir=outputdir)


#fitNames = ["threePar", "fourPar", "fivePar", "sixPar"]
fitNames = ["threeParM2j", "fourParM2j", "fiveParM2j"]
for channelNameSet, rebinFactor in zip(channelNames, rebinFactors):
  outputdir = base_outputdir + channelNameSet[0]
  for channelName in channelNameSet:
      lumi =  config.samples[channelName]["lumi"]
      rangelow=config.samples[channelName]["rangelow"]
      rangehigh=config.samples[channelName]["rangehigh"]
      rebinedges = config.getBinning(rangelow, rangehigh, delta=10)
      infiles = ["PostFit_threeParM2j_bkgonly", "PostFit_fourParM2j_bkgonly", "PostFit_fiveParM2j_bkgonly"]
      outfile = "Fit"
      runFTest.runFTest(infiles=infiles, cdir=cdir + "/scripts/", outfile=outfile, rangelow=rangelow, rangehigh=rangehigh, channelName=channelName, lumi=lumi, atlasLabel=config.atlasLabel, rebinEdges=rebinedges, outputdir=outputdir, fitNames = fitNames)


