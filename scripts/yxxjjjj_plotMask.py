import scripts.config as config
import python.createExtractionGraph as createExtractionGraph
import python.createCoverageGraph as createCoverageGraph
import python.plotLimits_jjj as plotLimits_jjj
import python.getChi2Distribution as getChi2Distribution
import python.plotFalseExclusionCandles as plotFalseExclusionCandles
import python.spuriousSignal as spuriousSignal
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.fitQualityTests as fitQualityTests
import python.plotSignalInjection as plotSignalInjection
import python.compareFitParams as compareFitParams
import python.plotBkgOnly as pbo
import python.fluctuationsCheck as fc

cdir = config.cdir



#pdFitName = "sixPar"
#fitName = "fivePar"
pdFitName = "fivePar"
fitName = "fourPar"
#pdFitName = "fourPar"
#fitName = "threePar"
#channelNames = [ "yxxjjjj_4j_alpha0", "yxxjjjj_4j_alpha1", "yxxjjjj_4j_alpha2", "yxxjjjj_4j_alpha3", "yxxjjjj_4j_alpha4", "yxxjjjj_4j_alpha5", "yxxjjjj_4j_alpha6", "yxxjjjj_4j_alpha7", "yxxjjjj_4j_alpha8", "yxxjjjj_4j_alpha9", "yxxjjjj_4j_alpha10", "yxxjjjj_4j_alpha11", ]
channelNames = [ "yxxjjjj_4j_alpha0", ]


coutputdir="fits_"
#signalfile =  "template"
signalfile =  "Gaussian"
lumi = 140000

atlasLabel = "Simulation Internal"


#sigmeans=[3000]
#sigamps = [3]
sigmeans=[0]
sigamps = [0]
sigwidths=[ 0]
for sigmean in sigmeans:
  for sigwidth in sigwidths:
    for channelName in channelNames:
      outputdir = coutputdir + channelName

      infiles = ["PostFit_masked_bkgOnly_%s_%s"%(pdFitName, fitName)]

      fitNames = [fitName]
      for toy in range(1):
        outfileFits = config.getFileName("fits_mask_PD_%d"%(toy), cdir + "/scripts/", channelName, outputdir, sigmean, sigwidth, 0)
        rangelow=config.samples[channelName]["rangelow"]
        rangehigh=config.samples[channelName]["rangehigh"]
        rebinFactor = 1
        #rebinedges = config.getBinning(rangelow, rangehigh, delta=rebinFactor)
        rebinedges = None

        plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir, suffix="", sigamp=0, sigwidth=sigwidth, sigmean=sigmean, toy=toy)



