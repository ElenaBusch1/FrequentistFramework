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

cdir = config.cdir


sigmeans=[2000, 3000, 4000, 6000, 8000, 10000]
#sigmeans=[2000, 2500, 3000, 3500, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
#sigmeans=[8000]
#spuriousRanges = [300, 100, 30, 10, 5, 5]
spuriousRanges = [1000, 300, 100, 30, 10, 5, 5]
#spuriousRanges = [100, 50, 50, 30, 10, 5, 5]
sigwidths=[ 10]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
#sigamps=[5,4,3,2,1,0]
sigamps=[5,4,3,2,1]

pdFitName = "fivePar"
fitName = "fourPar"
#pdFitName = "fourPar"
#fitName = "threePar"
channelNames = [ "sherpa_yxxjjjj_4j_alpha0", "sherpa_yxxjjjj_4j_alpha1", "sherpa_yxxjjjj_4j_alpha2", "sherpa_yxxjjjj_4j_alpha3", "sherpa_yxxjjjj_4j_alpha4", "sherpa_yxxjjjj_4j_alpha5", "sherpa_yxxjjjj_4j_alpha6", "sherpa_yxxjjjj_4j_alpha7", "sherpa_yxxjjjj_4j_alpha8", "sherpa_yxxjjjj_4j_alpha9", "sherpa_yxxjjjj_4j_alpha10", ]

coutputdir="fitsSherpa_"
signalfile =  "Gaussian"

lumi = 139000

atlasLabel = "Simulation Internal"


lumi =  config.samples[channelNames[0]]["lumi"]
infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
rangelow = config.samples[channelNames[0]]["rangelow"]
rangehigh = config.samples[channelNames[0]]["rangehigh"]
spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=coutputdir, signalName = "Y", labels = ["m_{4j}"])



# Extraction graphs
for channelName in channelNames:
  outputdir = coutputdir + channelName
  lumi =  config.samples[channelName]["lumi"]
  infileExtraction="FitParameters_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile)
  infilesBkg = "PostFit_%s_PD_bkgonly"%(pdFitName)
  infilePD='PD_%s_bkgonly'%(pdFitName)
  outfileExtraction = "PD_extraction_%s_%s_%s"%(pdFitName, fitName, signalfile)
  rangelow = config.samples[channelName]["rangelow"]
  rangehigh = config.samples[channelName]["rangehigh"]
  #createExtractionGraph.createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=infileExtraction, infilePD=infilePD, outfile=outfileExtraction, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/", lumi=lumi, isNInjected=False, indir=outputdir)

# Limits
for channelName in channelNames:
  outputdir = coutputdir + channelName
  pathsLimits = [ "Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile)]
  #plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelName=[channelName],atlasLabel=atlasLabel)


sigamps=[5, 4, 3, 2, 1, 0]
#sigamps=[5]
inputPDCoverage='PD_%s_bkgonly'%(pdFitName)
outfileCoverage='Coverage_%s_%s_%s'%(pdFitName, fitName, signalfile)
pathsLimits = "Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile)
#createCoverageGraph.createCoverageGraph(pathsLimits, inputPDCoverage, sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, outfile=outfileCoverage, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, signalfile=signalfile)
#plotFalseExclusionCandles.plotFalseExclusionCandles(outfileCoverage, sigmeans, sigwidths, rangelow, rangehigh, channelName, cdir + "/scripts/", lumi=lumi, atlasLabel=atlasLabel)



