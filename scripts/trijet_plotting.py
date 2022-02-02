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


#sigmeans=[ 550]
#sigmeans=[ 350, 450, 550, 650, 750, 850]
sigmeans=[ 450, 550, 650, 750, 850]
#sigmeans=[ 750]
#sigmeans=[ 450, 550]
sigwidths=[ 7 ]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
#sigamps=[5,1,0]
#sigamps=[20, 10, 8, 7, 5, 3, 1, 0]
sigamps=[5,4,3,2,1,0]
rangelow=300
rangehigh=900
channelName="BkgLow_2_alpha0_SR1_tagged"
lumi =  config.samples[channelName]["lumi"]



#rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
rebinedges = None

'''
for sigmean in sigmeans:
  for sigwidth in sigwidths:
    infiles = [config.getFileName("PostFit_sigPlusBkg", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 8) + "_0.root"]

    outfileFits = config.getFileName("fits_PD", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 8)
    plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, rebinedges=rebinedges, atlasLabel=config.atlasLabel)

    infile = config.getFileName("PostFit_sigPlusBkg", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 10) + "_0.root"
    infilePD = config.getFileName("PD_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 10) + ".root"
    outfileSignalInj = config.getFileName("SignalInjection_PD", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 10)
    #plotSignalInjection.plotFits(infileName=infile, infilePDName = infilePD, outfile=outfileSignalInj, rangelow=rangelow, rangehigh=rangehigh, sigmean=sigmean, sigwidth=sigwidth, sigamp=10, rebinedges=rebinedges, atlasLabel=config.atlasLabel)

    #outfilePulls = config.getFileName("pulls_PD", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0)
    #plotPulls.plotPulls(infiles=infiles, outfile=outfilePulls, atlasLabel=config.atlasLabel)

    #fitQualityTests.fitQualityTests("PostFit_sigPlusBkg", "PostFit_sigPlusBkg", "FitQuality", config.nToys, rangelow, rangehigh, sigmean, sigwidth, 0, cdir + "/scripts/", channelName)

'''



# Extraction graphs
infileExtraction="FitParameters_sigPlusBkg"
infilePD='PD_bkgonly'
outfileExtraction = "PD_extraction"
#createExtractionGraph.createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=infileExtraction, infilePD=infilePD, outfile=outfileExtraction, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/", lumi=lumi)


infileExtraction="FitParameters_spuriousSignal"
infilePD='PD_bkgonly'
outfileSpurious = "PD_spurious_bkgonly"
#spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/")


# Limits
pathsLimits = [ "Limits_limits"]
#plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh)

sigamps=[5, 2, 1, 0]
#sigamps=[5]
inputPDCoverage='PD_bkgonly'
outfileCoverage='Coverage'
pathsLimits = "Limits_limits"
#createCoverageGraph.createCoverageGraph(pathsLimits, inputPDCoverage, sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, outfile=outfileCoverage, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh)
#plotFalseExclusionCandles.plotFalseExclusionCandles("Coverage", sigmeans, sigwidths, rangelow, rangehigh, channelName, cdir + "/scripts/")



'''
# Chi2
for sigamp in sigamps:
  for sigmean in sigmeans:
    for sigwidth in sigwidths:

      infilesChi2 = "PostFit_sigPlusBkg"
      inhistChi2="chi2"
      outfileChi2="chi2"

      getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=sigmean, sigwidth=sigwidth, sigamp=sigamp)
'''



