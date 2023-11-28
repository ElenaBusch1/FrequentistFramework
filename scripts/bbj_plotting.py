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

cdir = config.cdir


#sigmeans=[ 250, 350, 450, 550, 650, 750, 850, 950]
sigmeans=[ 250, 350, 450, 550]
#sigmeans=[ 250, 350, 450, 550]
#sigmeans=[ 250, 300, 350, 400, 450, 500, 550, 600, 650]
#sigmeans=[ 350, ]
sigwidths=[ 5,7,10,12,15 ]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
sigamps=[5,4,3,2,1]

#pdFitName = config.cPDFitName
#fitName = config.cFitName
#pdFitName = "fivePar"
pdFitName = "sixPar"
fitName = "fivePar"
#pdFitName = "fivePar"
#fitName = "fourPar"
#pdFitName = "fourPar"
#fitName = "threePar"
channelName="btagFinal"

signalfile =  "Gaussian"
#signalfile = "templateHistBBJNoSyst"
#signalfile = "jbbNoSysts"

rangelow=160
rangehigh=700
#rangelow=config.cRangeLow
#rangehigh=config.cRangeHigh

lumi =  config.samples[channelName]["lumi"]
atlasLabel = "Simulation Internal"

rebinedges = config.getBinning(rangelow, rangehigh, delta=5)
#rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
#rebinedges = None


infilesChi2 = "PostFit_PD_bkgonly_%s_%s_%s"%(pdFitName, fitName, signalfile)
inhistChi2="chi2"
outfileChi2="chi2_%s_%s_%s"%(pdFitName, fitName, signalfile)
#getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=0, sigwidth=0, sigamp=0, lumi=lumi, atlasLabel=atlasLabel)


infilesChi2 = "PostFit_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
inhistChi2="chi2"
outfileChi2="chi2_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
#for sigmean in sigmeans:
#  for sigwidth in sigwidths:
#    getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=sigmean, sigwidth=sigwidth, sigamp=0, lumi=lumi, atlasLabel=atlasLabel)


for sigwidth in sigwidths:
  infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
  infilePD='PD_%s_bkgonly'%(pdFitName)
  outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
  infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
  #spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=[sigwidth], infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange=2000)


for sigwidth in sigwidths:
  # Extraction graphs
  infileExtraction="FitParameters_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile)
  infilesBkg = "PostFit_%s_PD_bkgonly"%(pdFitName)
  infilePD='PD_%s_bkgonly'%(pdFitName)
  outfileExtraction = "PD_extraction_%s_%s_%s"%(pdFitName, fitName, signalfile)
  #createExtractionGraph.createExtractionGraphs(sigmeans=sigmeans, sigwidths=[sigwidth], sigamps=sigamps, infile=infileExtraction, infilePD=infilePD, outfile=outfileExtraction, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/", lumi=lumi)


signalfile = "templateHistBBJNoSyst"
sigwidths = [10]
# Limits
pathsLimits = [ "Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile)]
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile = signalfile)



signalfile = "gausHist"
sigwidths = [10]
# Limits
pathsLimits = [ "Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile)]
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile = signalfile)

sigamps=[5, 4, 3, 2, 1, 0]
#sigamps=[5]
inputPDCoverage='PD_%s_bkgonly'%(pdFitName)
outfileCoverage='Coverage_%s_%s_%s'%(pdFitName, fitName, signalfile)
pathsLimits = "Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile)
#createCoverageGraph.createCoverageGraph(pathsLimits, inputPDCoverage, sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, outfile=outfileCoverage, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, signalfile=signalfile)
#plotFalseExclusionCandles.plotFalseExclusionCandles(outfileCoverage, sigmeans, sigwidths, rangelow, rangehigh, channelName, cdir + "/scripts/", lumi=lumi, atlasLabel=atlasLabel)




