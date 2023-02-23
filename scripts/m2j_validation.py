import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.runFTest as runFTest

cdir = config.cdir

channelNames = [ ["yxxjjjj_2javg_alpha0"],[ "yxxjjjj_2javg_alpha1"],[ "yxxjjjj_2javg_alpha2"],[ "yxxjjjj_2javg_alpha3"],[ "yxxjjjj_2javg_alpha4"],[ "yxxjjjj_2javg_alpha5"],[ "yxxjjjj_2javg_alpha6"],[ "yxxjjjj_2javg_alpha7"],[ "yxxjjjj_2javg_alpha8"],[ "yxxjjjj_2javg_alpha9"],[ "yxxjjjj_2javg_alpha10"],[ "yxxjjjj_2javg_alpha11"], ]

rebinFactors = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
fitNames = ["threeParM2j","fourParM2j", "fiveParM2j", "sixParM2j"]

base_outputdir = "fits2javg_"
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
      plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir,cutoffSpectrum=True)
    
      outfilePulls = config.getFileName("pulls", cdir + "/scripts/", channelName, outputdir)
      plotPulls.plotPulls(infiles=infiles, fitNames = fitNames, outfile="pulls", minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, atlasLabel=config.atlasLabel, outputdir=outputdir)


fitNames = ["threeParM2j", "fourParM2j", "fiveParM2j", "sixParM2j"]
for channelNameSet, rebinFactor in zip(channelNames, rebinFactors):
  outputdir = base_outputdir + channelNameSet[0]
  for channelName in channelNameSet:
      rangelow=config.samples[channelName]["rangelow"]
      rangehigh=config.samples[channelName]["rangehigh"]
      #rebinedges = config.getBinning(rangelow, rangehigh, delta=10)
      rebinedges = config.getBinningFromFile(channelName)

      infiles = ["PostFit_threeParM2j_bkgonly", "PostFit_fourParM2j_bkgonly", "PostFit_fiveParM2j_bkgonly", "PostFit_sixParM2j_bkgonly"]
      outfile = "Fit"
      runFTest.runFTest(infiles=infiles, cdir=cdir + "/scripts/", outfile=outfile, rangelow=rangelow, rangehigh=rangehigh, channelName=channelName, lumi=lumi, atlasLabel=config.atlasLabel, rebinEdges=rebinedges, outputdir=outputdir, fitNames = fitNames)


