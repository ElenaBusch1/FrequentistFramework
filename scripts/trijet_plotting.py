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
#sigmeans=[ 450, 550, 650, 750, 850]
#sigmeans=[ 450, 650]
#sigmeans=[ 450]
#sigmeans=[ 450, 550, 650]
#sigmeans=[ 250, 350, 450, 550, 650, 750]
sigmeans=[ 250, 350, 450, 550, 650, 750]
sigwidths=[ 7 ]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
#sigamps=[5,1,0]
#sigamps=[20, 10, 8, 7, 5, 3, 1, 0]
#sigamps=[5,4,3,2,1,0]
sigamps=[5,4,3,2,1,0]
rangelow=200
rangehigh=900
#channelName="BkgLow_2_alpha0_SR1_tagged"
#channelName="MassOrdered_2"
channelName="PtOrdered6"
lumi =  config.samples[channelName]["lumi"]
atlasLabel = "Simulation Internal"


#pdFitName = "fivePar"
#fitName = "fiveParV3"
#fitName = "fourPar"
#fitName = "fivePar"
pdFitName = "sixPar"
#fitName = "fiveParV3"
#pdFitName = "fivePar"
#fitName = "fourPar"
#pdFitName = "fiveParV2"
fitName = "fivePar"

rebinedges = config.getBinning(rangelow, rangehigh, delta=25)
#rebinedges = None

'''
for sigmean in sigmeans:
  for sigwidth in sigwidths:
    #infiles = [config.getFileName("PostFit_%s_sigPlusBkg"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"]
    infiles = [config.getFileName("PostFit_spuriousSignal", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"]

    #for toy in range(10):
    #  outfileFits = config.getFileName("fits_PD_%d"%(toy), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0)
    #  plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, suffix="_%d"%(toy))

    infile = config.getFileName("PostFit_spuriousSignal", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
    infileBkgOnly = config.getFileName("PostFit_PD_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    #infilePD = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"
    infilePD = config.getFileName("PD_%s_bkgonly"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
    for toy in range(10):
      outfileSignalInj = config.getFileName("SignalInjection_PD", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + "_%d"%(toy)
      plotSignalInjection.plotFits(infileName=infile, infilePDName = infilePD, outfile=outfileSignalInj, rangelow=rangelow, rangehigh=rangehigh, sigmean=sigmean, sigwidth=sigwidth, sigamp=0, rebinedges=rebinedges, atlasLabel=config.atlasLabel, suffix="_%d"%(toy), infileNameBkgOnly = infileBkgOnly)

    #outfilePulls = config.getFileName("pulls_PD", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0)
    #plotPulls.plotPulls(infiles=infiles, outfile=outfilePulls, atlasLabel=config.atlasLabel)

    #outfilePulls = config.getFileName("pulls_PD_spuriousSignal", cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0)
    #plotPulls.plotPulls(infiles=infiles, outfile=outfilePulls, atlasLabel=config.atlasLabel)

    #fitQualityTests.fitQualityTests("PostFit_sigPlusBkg", "PostFit_sigPlusBkg", "FitQuality", config.nToys, rangelow, rangehigh, sigmean, sigwidth, 0, cdir + "/scripts/", channelName)
'''




infilesChi2 = "PostFit_PD_bkgonly"
inhistChi2="chi2"
outfileChi2="chi2"
#getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=0, sigwidth=0, sigamp=0, lumi=lumi, atlasLabel=atlasLabel)


infilesChi2 = "PostFit_spuriousSignal"
inhistChi2="chi2"
outfileChi2="chi2_spuriousSignal"
#for sigmean in sigmeans:
#  for sigwidth in sigwidths:
#    getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=sigmean, sigwidth=sigwidth, sigamp=0, lumi=lumi, atlasLabel=atlasLabel)




infileExtraction="FitParameters_spuriousSignal_%s_%s"%(pdFitName, fitName)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "PD_spurious_%s_%s_bkgonly"%(pdFitName, fitName)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly)




# Extraction graphs
infileExtraction="FitParameters_sigPlusBkg"
infilesBkg = "PostFit_%s_PD_bkgonly"%(pdFitName)
infilePD='PD_bkgonly'
outfileExtraction = "PD_extraction"
createExtractionGraph.createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=infileExtraction, infilePD=infilePD, outfile=outfileExtraction, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/", lumi=lumi)


# Limits
pathsLimits = [ "Limits_limits"]
#plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel)

sigamps=[5, 4, 3, 2, 1, 0]
#sigamps=[5]
inputPDCoverage='PD_%s_bkgonly'%(pdFitName)
outfileCoverage='Coverage'
pathsLimits = "Limits_limits"
#createCoverageGraph.createCoverageGraph(pathsLimits, inputPDCoverage, sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, outfile=outfileCoverage, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh)
#plotFalseExclusionCandles.plotFalseExclusionCandles("Coverage", sigmeans, sigwidths, rangelow, rangehigh, channelName, cdir + "/scripts/", lumi=lumi, atlasLabel=atlasLabel)



'''
# Chi2
for sigamp in sigamps:
  for sigmean in sigmeans:
    for sigwidth in sigwidths:

      infilesChi2 = "PostFit_sigPlusBkg"
      inhistChi2="chi2"
      outfileChi2="chi2"

      getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=sigmean, sigwidth=sigwidth, sigamp=sigamp, lumi=lumi, atlasLabel=atlasLabel)
'''



