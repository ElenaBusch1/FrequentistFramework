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
#sigmeans=[ 250, 350, 450, 550]
#sigmeans=[ 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
sigmeans=[ 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
#sigmeans=[ 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
#sigmeans=[ 300, 400, 500]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph

#pdFitName = config.cPDFitName
#fitName = config.cFitName
#pdFitName = "fivePar"
pdFitName = "sixPar"
fitName = "fivePar"
channelName="bbj_Data"

#signalfile =  "Gaussian"
#signalfile = "templateHistBBJNoSyst"
#signalfile = "templateHistBBJ"
#signalfile = "jbbNoSysts"

rangelow=160
rangehigh=700
#rangelow=config.cRangeLow
#rangehigh=config.cRangeHigh

lumi =  config.samples[channelName]["lumi"]
atlasLabel = "Simulation"

# Limits
signalfile =  "gausHistBBJ"
sigwidths=[ 5,7,10,12,15 ]
pathsLimits = [ "Limits_%s"%(fitName)]
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile = signalfile, minY = 0.001, maxY = 0.4)

sigmeans=[ 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]


signalfile =  "templateHistBBJ"
pathsLimits = [ "Limits_%s_%s"%(fitName, signalfile)]
sigwidths=[ 10 ]
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile = signalfile, minY = 0.001, maxY = 0.4)



