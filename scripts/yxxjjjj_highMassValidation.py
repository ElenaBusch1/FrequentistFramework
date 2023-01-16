import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.runFTest as runFTest


# May want to loop over these at some point?
cdir = config.cdir

#channelNames = [ ["tenPercent_yxxjjjj_4j_alpha0"],[ "tenPercent_yxxjjjj_4j_alpha1"],[ "tenPercent_yxxjjjj_4j_alpha2"],[ "tenPercent_yxxjjjj_4j_alpha3"],[ "tenPercent_yxxjjjj_4j_alpha4"],[ "tenPercent_yxxjjjj_4j_alpha5"],[ "tenPercent_yxxjjjj_4j_alpha6"],[ "tenPercent_yxxjjjj_4j_alpha7"],[ "tenPercent_yxxjjjj_4j_alpha8"],[ "tenPercent_yxxjjjj_4j_alpha9"],[ "tenPercent_yxxjjjj_4j_alpha10"],[ "tenPercent_yxxjjjj_4j_alpha11"], ]

#channelNames = [ ["yxxjjjj_4j_alpha0"],[ "yxxjjjj_4j_alpha1"],[ "yxxjjjj_4j_alpha2"],[ "yxxjjjj_4j_alpha3"],[ "yxxjjjj_4j_alpha4"],[ "yxxjjjj_4j_alpha5"],[ "yxxjjjj_4j_alpha6"],[ "yxxjjjj_4j_alpha7"],[ "yxxjjjj_4j_alpha8"],[ "yxxjjjj_4j_alpha9"],[ "yxxjjjj_4j_alpha10"],[ "yxxjjjj_4j_alpha11"], ]

#channelNames = [ ["yxxjjjj_2javg_alpha0"],[ "yxxjjjj_2javg_alpha1"],[ "yxxjjjj_2javg_alpha2"],[ "yxxjjjj_2javg_alpha3"],[ "yxxjjjj_2javg_alpha4"],[ "yxxjjjj_2javg_alpha5"],[ "yxxjjjj_2javg_alpha6"],[ "yxxjjjj_2javg_alpha7"],[ "yxxjjjj_2javg_alpha8"],[ "yxxjjjj_2javg_alpha9"],[ "yxxjjjj_2javg_alpha10"],[ "yxxjjjj_2javg_alpha11"], ]
channelNames = [ [ "yxxjjjj_4j_alpha5"]]




rebinFactors = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
#fitNames = ["threePar","fourPar", "fivePar"]
fitNames = ["threePar"]
pdFitNames = ["fourPar"]
#fitNames = ["fourPar"]
#pdFitNames = ["fivePar"]
sigmeans = [10000]
sigwidths = [10]
sigamps = [1,0]


signalfile =  "Gaussian"


base_outputdir = "fits_"

for channelNameSet, rebinFactor in zip(channelNames, rebinFactors):
  outputdir = base_outputdir + channelNameSet[0]
  for channelName in channelNameSet:
    for sigmean in sigmeans:
     for sigwidth in sigwidths:
      for sigamp in sigamps:
        for toy in range(5):
          rangelow=config.samples[channelName]["rangelow"]
          rangehigh=config.samples[channelName]["rangehigh"]
          rebinedges = config.getBinning(rangelow, rangehigh, delta=rebinFactor)
          lumi =  config.samples[channelName]["lumi"]
    
          infiles = []
          for pdFitName, fitName in zip(pdFitNames, fitNames):
            #infiles.append("PostFit_%s_bkgonly"%(pdFitName))
            infiles.append("PostFit_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile))

          outfileFits = config.getFileName("fits_%d"%(toy), cdir + "/scripts/", channelName, outputdir, sigmean=sigmean, sigwidth=sigwidth, sigamp=sigamp)

          plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir, sigmean= sigmean, sigamp=sigamp, sigwidth=sigwidth, toy = toy)
    




