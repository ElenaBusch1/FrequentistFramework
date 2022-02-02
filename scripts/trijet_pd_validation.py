import scripts.config as config
import os
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.fitQualityTests as fitQualityTests


# May want to loop over these at some point?
cdir = config.cdir
channelName="BkgLow_2_alpha0_SR1_tagged"
lumi =  config.samples[channelName]["lumi"]


#rangeslow=[200, 250, 275, 300, 350, 400]
#rangeshigh=[1000, 1200, 1400, 1600, 1800]
rangeslow=[300]
rangeshigh=[900]

for rangelow in rangeslow:
  for rangehigh in rangeshigh:

    rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
    #rebinedges=None

    infiles = [config.getFileName("PostFit_PD_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"]

    outfileFits = config.getFileName("fits_PD", cdir + "/scripts/", channelName, rangelow, rangehigh)
    plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, suffix="_0")

    outfilePulls = config.getFileName("pulls_PD", cdir + "/scripts/", channelName, rangelow, rangehigh)
    plotPulls.plotPulls(infiles=infiles, outfile=outfilePulls, lumi=lumi, atlasLabel=config.atlasLabel, suffix="_0")


    fitQualityTests.fitQualityTests("PostFit_PD_bkgonly", "PostFit_PD_bkgonly", "FitQuality", config.nToys, rangelow, rangehigh, 0, 0, 0, lumi=lumi, cdir + "/scripts/", channelName)



