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
sigmeans=[ 250, 350, 450, 550, 650]
#sigmeans=[ 250, 350, 450, 550, 650, 750]
#sigmeans=[ 250]
#sigmeans=[ 250, 350, 450, 500, 550, 600, 650, 750]
sigwidths=[ 7 ]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
sigamps=[5,4,3,2,1,0]

#pdFitName = config.cPDFitName
#fitName = config.cFitName
pdFitName = "sixPar"
fitName = "fivePar"
#pdFitName = "fivePar"
#fitName = "fourPar"
channelName="test3"
#signalfile =  config.cSignal
#signalfile =  "Gaussian"
#signalfile =  "test3_NoCut_some"
#signalfile =  "test3_some"
#signalfile =  "test3"
#signalfile =  "test3_NoCut"
#signalfile =  "test3_inverted"
signalfile =  "test3_inverted_some"

rangelow=200
rangehigh=1200
#rangelow=config.cRangeLow
#rangehigh=config.cRangeHigh

lumi =  config.samples[channelName]["lumi"]
atlasLabel = "Simulation Internal"

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

'''
for sigmean in sigmeans:
  for sigwidth in sigwidths:
    #infiles = [config.getFileName("PostFit_%s_sigPlusBkg"%(pdFitName), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"]
    infiles = [config.getFileName("PostFit_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 5) + ".root"]

    fitNames = [fitName]
    for toy in range(10):
      outfileFits = config.getFileName("fits_PD_%d"%(toy), cdir + "/scripts/", channelName, rangelow, rangehigh, sigmean, sigwidth, 0)
      plotFits.plotFits(infiles=infiles, outfile=outfileFits, minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName,  lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, suffix="_%d"%(toy), fitNames=fitNames)

'''



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




infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
#spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange=50000)




# Extraction graphs
infileExtraction="FitParameters_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilesBkg = "PostFit_%s_PD_bkgonly"%(pdFitName)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileExtraction = "PD_extraction_%s_%s_%s"%(pdFitName, fitName, signalfile)
createExtractionGraph.createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=infileExtraction, infilePD=infilePD, outfile=outfileExtraction, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/", lumi=lumi)


# Limits
pathsLimits = [ "Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile)]
#plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=channelName, cdir=cdir+"/scripts/",channelName=channelName,rangelow=rangelow, rangehigh=rangehigh, atlasLabel=atlasLabel)

sigamps=[5, 4, 3, 2, 1, 0]
#sigamps=[5]
inputPDCoverage='PD_%s_bkgonly'%(pdFitName)
outfileCoverage='Coverage_%s_%s_%s'%(pdFitName, fitName, signalfile)
pathsLimits = "Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile)
#createCoverageGraph.createCoverageGraph(pathsLimits, inputPDCoverage, sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, outfile=outfileCoverage, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, signalfile=signalfile)
#plotFalseExclusionCandles.plotFalseExclusionCandles(outfileCoverage, sigmeans, sigwidths, rangelow, rangehigh, channelName, cdir + "/scripts/", lumi=lumi, atlasLabel=atlasLabel)



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



