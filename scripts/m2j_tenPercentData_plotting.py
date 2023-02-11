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


cdir = config.cdir


#sigmeans= [500, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250]
sigmeans=[500, 700, 1000, 1500, 2000, 2500, 3000]
#spuriousRanges = [400, 300, 100, 20, 10, 5, 5, 5]
spuriousRanges = [100, 100, 50, 20, 10, 5, 5, 5]
#sigwidths=[ 5,10,15]
sigwidths=[10]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
sigamps=[5,4,3,2,1]

pdFitName = "fiveParM2j"
fitName = "fourParM2j"
#pdFitName = "fourParM2j"
#fitName = "threeParM2j"
channelNames = [ "tenPercentData_2javg_alpha0", "tenPercentData_2javg_alpha1", "tenPercentData_2javg_alpha2", "tenPercentData_2javg_alpha3", "tenPercentData_2javg_alpha4", "tenPercentData_2javg_alpha5", "tenPercentData_2javg_alpha6", "tenPercentData_2javg_alpha7", "tenPercentData_2javg_alpha8", "tenPercentData_2javg_alpha9", "tenPercentData_2javg_alpha10", "tenPercentData_2javg_alpha11", ]
#channelNames = [ "tenPercentData_2javg_alpha0", "tenPercentData_2javg_alpha1", "tenPercentData_2javg_alpha2", "tenPercentData_2javg_alpha3",]

coutputdir = "fits2javg_10data_"

signalfile =  "Gaussian"
lumi =  config.samples[channelNames[0]]["lumi"]
atlasLabel = "Simulation Internal"

for sigmean in [700]:
  for sigwidth in sigwidths:
    for channelName in ["tenPercentData_2javg_alpha3"]:
      outputdir = coutputdir + channelName

      #infiles = ["PostFit_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile)]
      infiles = ["PostFit_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)]
      #infiles = [config.getFileName("PostFit_spuriousSignal", cdir + "/scripts/", channelName, outputdir, sigmean, sigwidth, 0)]

      fitNames = [fitName]
      for toy in range(10):
        outfileFits = config.getFileName("fits_PD_%d"%(toy), cdir + "/scripts/", channelName, outputdir, sigmean, sigwidth, 0)
        rangelow=config.samples[channelName]["rangelow"]
        rangehigh=config.samples[channelName]["rangehigh"]
        rebinFactor = 10
        rebinedges = config.getBinning(rangelow, rangehigh, delta=rebinFactor)

        #plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir, suffix="", sigamp=0, sigwidth=sigwidth, sigmean=sigmean, toy=toy, cutoffSpectrum=True)



infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
rangelow = config.samples[channelNames[0]]["rangelow"]
rangehigh = config.samples[channelNames[0]]["rangehigh"]
spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=coutputdir, signalName = "X", labels = ["m_{#LT 2j #GT} [GeV]"], delta=10, deltaMassAboveFit = 50)






