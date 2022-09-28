import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.runFTest as runFTest


# May want to loop over these at some point?
cdir = config.cdir

#channelNames = [ ["nixon_4j_alpha8_MCErr"], ]
#channelNames = [ ["nixon_4j_alpha0", "nixon_4j_alpha1", "nixon_4j_alpha2", "nixon_4j_alpha3", "nixon_4j_alpha4", "nixon_4j_alpha5", "nixon_4j_alpha6", "nixon_4j_alpha7", "nixon_4j_alpha8", "nixon_4j_alpha9"], ]
channelNames = [ ["nixon_4j_alpha0", "nixon_4j_alpha1", "nixon_4j_alpha2", "nixon_4j_alpha3", "nixon_4j_alpha4", "nixon_4j_alpha5", "nixon_4j_alpha6", "nixon_4j_alpha7", "nixon_4j_alpha8", "nixon_4j_alpha9", "nixon_4j_alpha10", "nixon_4j_alpha11", "nixon_4j_alpha12"], ]

#channelNames = [ ["nixon_4j_alpha12"], ]

rebinFactors = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
#rebinFactors = [10]
#fitNames = ["fourPar"]
#fitNames = ["fivePar"]
fitNames = ["threePar","fourPar", "fivePar", "sixPar"]
#channelNames=["ambulance_2javg"]
#rangeslow=[500]
#rangeshigh=[3000]
#fitNames = ["threeParAmb", "fourParAmb", "fiveParAmb"]
#rebinFactors = [50]

signalfile =  "Gaussian"


outputdir = "fitsNixon"
for channelNameSet, rebinFactor in zip(channelNames, rebinFactors):
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
      #plotPulls.plotPulls(infiles=infiles, fitNames = fitNames, outfile=outfilePulls, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, atlasLabel=config.atlasLabel)


fitNames = ["threePar", "fourPar", "fivePar", "sixPar"]
for channelNameSet, rebinFactor in zip(channelNames, rebinFactors):
  for channelName in channelNameSet:
      rangelow=config.samples[channelName]["rangelow"]
      rangehigh=config.samples[channelName]["rangehigh"]
      rebinedges = config.getBinning(rangelow, rangehigh, delta=10)
      infiles = ["PostFit_threePar_bkgonly", "PostFit_fourPar_bkgonly", "PostFit_fivePar_bkgonly", "PostFit_sixPar_bkgonly"]
      outfile = "Fit"
      runFTest.runFTest(infiles=infiles, cdir=cdir + "/scripts/", outfile=outfile, rangelow=rangelow, rangehigh=rangehigh, channelName=channelName, lumi=lumi, atlasLabel=config.atlasLabel, rebinEdges=rebinedges, outputdir=outputdir, fitNames = fitNames)


