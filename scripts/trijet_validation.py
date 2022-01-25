import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls


# May want to loop over these at some point?
cdir = config.cdir
channelName="BkgLow_3_alpha0_SR1_tagged"
rangelow=300
rangehigh=1200


rebinedges=[300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200]

fitFunction = "fivePar"

infiles = [config.getFileName("PostFit_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"]

outfileFits = config.getFileName("fits", cdir + "/scripts/", channelName, rangelow, rangehigh)
plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, rebinedges=rebinedges, atlasLabel=config.atlasLabel)

outfilePulls = config.getFileName("pulls", cdir + "/scripts/", channelName, rangelow, rangehigh)
plotPulls.plotPulls(infiles=infiles, outfile=outfilePulls, atlasLabel=config.atlasLabel)


