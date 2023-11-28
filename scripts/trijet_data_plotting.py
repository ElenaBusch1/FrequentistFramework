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


#sigmeans=[ 250, 350, 450, 550, 650]
#sigmeans=[ 450, 550, 650]
#sigmeans=[ 250, 300, 350, 400, 450, 500, 550, 600]
#sigmeans=[ 300, 350, 400, 450, 500, 550, 600]
#sigmeans=[ 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600]
#sigmeans=[ 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500]
sigmeans=[ 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
#sigwidths=[ 5,7,10,12,15,]
sigwidths=[ 10]
#sigwidths=[ 12,]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
sigamps=[5,4,3,2,1]

fitName = "fivePar"
#pdFitName = "fivePar"
#fitName = "fourPar"
#channelName="testSherpa_15"

#signalfile =  "Gaussian"
#signalfile =  "templateHistNoSyst"
signalfile =  "gausHist"
#signalfile =  "templateHist"


#channelName="Data16"
#channelName="FullRun2Data_NoNN"
#channelName = "test3New_15_MCEffOnData"
channelName = "FullRun2Data_NoNN_No21"
rangelow=225
rangehigh=1000
#rangelow=200
#rangehigh=1000
#rangelow=250
#rangehigh=1000

lumi =  config.samples[channelName]["lumi"]
atlasLabel = "Internal"

rebinedges = config.getBinning(rangelow, rangehigh, delta=5)



#channelName = "FullRun2Data"
#channelName = "test3New_15_data_mcEff"
#channelName = "test3New_15_MCwithMC"
#channelName = "Data16MCJES"
#channelName = "Data16NoInsitu"
#channelName = "test3New_15"
#channelName = "test3New_15_data_mcEff"
#channelName = "DataNoInsitu"
#channelName = "DataAllJES"

#channelName = "Data16"
#rangelow=250
#rangehigh=1000
#signalfile =  "Gaussian"
#sigmeans=[ 300, 350, 400, 450, 500, 550, 600]

sigwidths = [5, 7, 10, 12, 15]
signalfile =  "gausHist"
pathsLimits = [ "Limits_%s_%s"%(fitName, signalfile)]
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile=signalfile, minY = 0.02, maxY = 5)


signalfile =  "templateHist"
sigwidths = [10]
pathsLimits = [ "Limits_%s_%s"%(fitName, signalfile)]
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile=signalfile, minY = 0.02, maxY = 5)



#channelName="Data_m32"
#plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile=signalfile)

#channelName = "Data_m32"
#plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile=signalfile)

#
#channelName = "FullRun2Data_NoNN"
#plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile=signalfile)


'''

channelName="Data16"
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile=signalfile)


channelName="Data17"
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile=signalfile)

channelName = "FullRun2Data"
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile=signalfile)

channelName="Data18"
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel, signalfile=signalfile)

'''

