import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls


# May want to loop over these at some point?
cdir = config.cdir
#channelName="BkgLow_3_alpha0_SR1_tagged"
channelName="BkgLow_2_alpha0_SR1_tagged"
fitFunction = "fivePar"


#rangeslow=[200, 250, 275, 300, 350, 400]
#rangeshigh=[1000, 1200, 1400, 1600, 1800]
rangeslow=[300]
rangeshigh=[900]

for rangelow in rangeslow:
  for rangehigh in rangeshigh:

    rebinedges = config.getBinning(rangelow, rangehigh, delta=25)

    infiles = [config.getFileName("PostFit_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"]

    outfileFits = config.getFileName("fits", cdir + "/scripts/", channelName, rangelow, rangehigh)
    plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, rebinedges=rebinedges, atlasLabel=config.atlasLabel)

    outfilePulls = config.getFileName("pulls", cdir + "/scripts/", channelName, rangelow, rangehigh)
    plotPulls.plotPulls(infiles=infiles, outfile=outfilePulls, atlasLabel=config.atlasLabel)


