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


#sigmeans=[3000, 4000, 5000, 6000, 7000, 8000]
#sigmeans=[2000, 3000, 4000, 6000, 8000, 10000]
sigmeans=[2000, 3000, 4000, 6000, 8000, 10000]
#spuriousRanges = [300, 100, 30, 10, 5, 5]
spuriousRanges = [400, 80, 20, 10, 5, 5, 5]
#spuriousRanges = [100, 50, 50, 30, 10, 5, 5]
#spuriousRanges = [100,  10, 5, 5]
#spuriousRanges = [1000, 300, 100,  10, 5, 5]
sigwidths=[ 10 ]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
#sigamps=[3,1,]
sigamps=[5,4,3,2,1,0]
#sigamps=[5,4,3,2,1]
#sigamps=[1]

pdFitName = "fivePar"
fitName = "fourPar"
#pdFitName = "fourPar"
#fitName = "threePar"
channelNames = [ "tenPercentData_yxxjjjj_4j_alpha0", "tenPercentData_yxxjjjj_4j_alpha1", "tenPercentData_yxxjjjj_4j_alpha2", "tenPercentData_yxxjjjj_4j_alpha3", "tenPercentData_yxxjjjj_4j_alpha4", "tenPercentData_yxxjjjj_4j_alpha5", "tenPercentData_yxxjjjj_4j_alpha6", "tenPercentData_yxxjjjj_4j_alpha7", "tenPercentData_yxxjjjj_4j_alpha8", "tenPercentData_yxxjjjj_4j_alpha9", "tenPercentData_yxxjjjj_4j_alpha10", "tenPercentData_yxxjjjj_4j_alpha11", ]
#channelNames = [ "tenPercentData_yxxjjjj_4j_alpha10",]

coutputdir="fitsTenPercentData_"
#signalfile =  "template"
signalfile =  "Gaussian"
#signalfile =  "crystalBallHistNoSyst"

lumi = 139000

atlasLabel = "Simulation Internal"

#rebinedges = config.getBinning(rangelow, rangehigh, delta=50)



for sigmean in [4000]:
  for sigwidth in sigwidths:
    for channelName in ["tenPercentData_yxxjjjj_4j_alpha8"]:
      outputdir = coutputdir + channelName

      #infiles = ["PostFit_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile)]
      infiles = ["PostFit_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)]
      #infiles = [config.getFileName("PostFit_spuriousSignal", cdir + "/scripts/", channelName, outputdir, sigmean, sigwidth, 0)]

      fitNames = [fitName]
      #for toy in range(1):
      for toy in range(10):
        outfileFits = config.getFileName("fits_PD_%d"%(toy), cdir + "/scripts/", channelName, outputdir, sigmean, sigwidth, 0)
        rangelow=config.samples[channelName]["rangelow"]
        rangehigh=config.samples[channelName]["rangehigh"]
        rebinFactor = 100
        rebinedges = config.getBinning(rangelow, rangehigh, delta=rebinFactor)

        #plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir, suffix="", sigamp=0, sigwidth=sigwidth, sigmean=sigmean, toy=toy)



lumi =  config.samples[channelNames[0]]["lumi"]
infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
rangelow = config.samples[channelNames[0]]["rangelow"]
rangehigh = config.samples[channelNames[0]]["rangehigh"]
spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=coutputdir, signalName = "Y")



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

