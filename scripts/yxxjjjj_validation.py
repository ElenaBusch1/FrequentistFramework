import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.runFTest as runFTest


# May want to loop over these at some point?
cdir = config.cdir

#channelNames = [ ["tenPercent_yxxjjjj_4j_alpha0"],[ "tenPercent_yxxjjjj_4j_alpha1"],[ "tenPercent_yxxjjjj_4j_alpha2"],[ "tenPercent_yxxjjjj_4j_alpha3"],[ "tenPercent_yxxjjjj_4j_alpha4"],[ "tenPercent_yxxjjjj_4j_alpha5"],[ "tenPercent_yxxjjjj_4j_alpha6"],[ "tenPercent_yxxjjjj_4j_alpha7"],[ "tenPercent_yxxjjjj_4j_alpha8"],[ "tenPercent_yxxjjjj_4j_alpha9"],[ "tenPercent_yxxjjjj_4j_alpha10"],[ "tenPercent_yxxjjjj_4j_alpha11"], ]

channelNames = [ ["yxxjjjj_4j_alpha0"],[ "yxxjjjj_4j_alpha1"],[ "yxxjjjj_4j_alpha2"],[ "yxxjjjj_4j_alpha3"],[ "yxxjjjj_4j_alpha4"],[ "yxxjjjj_4j_alpha5"],[ "yxxjjjj_4j_alpha6"],[ "yxxjjjj_4j_alpha7"],[ "yxxjjjj_4j_alpha8"],[ "yxxjjjj_4j_alpha9"],[ "yxxjjjj_4j_alpha10"],[ "yxxjjjj_4j_alpha11"], ]
#channelNames = [ [ "yxxjjjj_4j_alpha5"],[ "yxxjjjj_4j_alpha6"],[ "yxxjjjj_4j_alpha7"],[ "yxxjjjj_4j_alpha8"],[ "yxxjjjj_4j_alpha9"],[ "yxxjjjj_4j_alpha10"],[ "yxxjjjj_4j_alpha11"], ]

#channelNames = [ ["yxxjjjj_2javg_alpha0"],[ "yxxjjjj_2javg_alpha1"],[ "yxxjjjj_2javg_alpha2"],[ "yxxjjjj_2javg_alpha3"],[ "yxxjjjj_2javg_alpha4"],[ "yxxjjjj_2javg_alpha5"],[ "yxxjjjj_2javg_alpha6"],[ "yxxjjjj_2javg_alpha7"],[ "yxxjjjj_2javg_alpha8"],[ "yxxjjjj_2javg_alpha9"],[ "yxxjjjj_2javg_alpha10"],[ "yxxjjjj_2javg_alpha11"], ]
#channelNames = [ ["sherpa_yxxjjjj_2javg_alpha0"],[ "sherpa_yxxjjjj_2javg_alpha1"],[ "sherpa_yxxjjjj_2javg_alpha2"],[ "sherpa_yxxjjjj_2javg_alpha3"],[ "sherpa_yxxjjjj_2javg_alpha4"],[ "sherpa_yxxjjjj_2javg_alpha5"],[ "sherpa_yxxjjjj_2javg_alpha6"],[ "sherpa_yxxjjjj_2javg_alpha7"],[ "sherpa_yxxjjjj_2javg_alpha8"],[ "sherpa_yxxjjjj_2javg_alpha9"],[ "sherpa_yxxjjjj_2javg_alpha10"],[ "sherpa_yxxjjjj_2javg_alpha11"], ]



#rebinFactors = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
#rebinFactors = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
#rebinFactors = [50, 50, 50, 50, 50, 50, 5, 5, 5, 5, 5, 5, 5, 5, 5]
#rebinFactors = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
rebinFactors = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
#rebinFactors = [10]
#fitNames = ["fourPar"]
#fitNames = ["fivePar"]
fitNames = ["threePar","fourPar", "fivePar", "sixPar"]
#fitNames = ["fourPar", "fivePar"]
#fitNames = ["threePar","fourPar", "fivePar"]
#rangeslow=[100]
#rangeshigh=[3000]
#rebinFactors = [10]

signalfile =  "Gaussian"


base_outputdir = "fits_"

'''
for channelNameSet, rebinFactor in zip(channelNames, rebinFactors):
  outputdir = base_outputdir + channelNameSet[0]
  for channelName in channelNameSet:
      rangelow=config.samples[channelName]["rangelow"]
      rangehigh=config.samples[channelName]["rangehigh"]
      rebinedges = config.getBinning(rangelow, rangehigh, delta=rebinFactor)
      lumi =  config.samples[channelName]["lumi"]
      infiles = []
      for pdFitName in fitNames:
        infiles.append("PostFit_%s_bkgonly"%(pdFitName))
      outfileFits = config.getFileName("fits", cdir + "/scripts/", channelName, outputdir)
      #outfileFits = outputdir + "/Fits_" + channelName 
      plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir)
    
      #outfilePulls = "pulls_%s_Fit_%d_%d"%(channelName, rangelow, rangehigh)
      outfilePulls = config.getFileName("pulls", cdir + "/scripts/", channelName, outputdir)
      #plotPulls.plotPulls(infiles=infiles, fitNames = fitNames, outfile=outfilePulls, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, atlasLabel=config.atlasLabel, outputdir=outputdir)
      plotPulls.plotPulls(infiles=infiles, fitNames = fitNames, outfile="pulls", minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, atlasLabel=config.atlasLabel, outputdir=outputdir)
'''


fitNames = ["threePar", "fourPar", "fivePar", "sixPar"]
#fitNames = ["threePar", "fourPar", "fivePar"]
for channelNameSet, rebinFactor in zip(channelNames, rebinFactors):
  outputdir = base_outputdir + channelNameSet[0]
  for channelName in channelNameSet:
      lumi =  config.samples[channelName]["lumi"]
      rangelow=config.samples[channelName]["rangelow"]
      rangehigh=config.samples[channelName]["rangehigh"]
      #rebinedges = config.getBinning(rangelow, rangehigh, delta=1)
      rebinedges = config.getBinningFromFile(channelName)

      infiles = ["PostFit_threePar_bkgonly", "PostFit_fourPar_bkgonly", "PostFit_fivePar_bkgonly", "PostFit_sixPar_bkgonly"]
      outfile = "Fit"
      runFTest.runFTest(infiles=infiles, cdir=cdir + "/scripts/", outfile=outfile, rangelow=rangelow, rangehigh=rangehigh, channelName=channelName, lumi=lumi, atlasLabel=config.atlasLabel, rebinEdges=rebinedges, outputdir=outputdir, fitNames = fitNames)


