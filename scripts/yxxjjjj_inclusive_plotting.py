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


#sigmeans=[3000, 4000, 5000, 6000, 7000, 8000]
#sigmeans=[5000,]
sigmeans=[3000, 4000, 5000, 6000, 7000, 8000]
spuriousRanges = [300, 100, 30, 10, 5, 5]
sigwidths=[ 10 ]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
#sigamps=[5,4,3,2,1,0]
sigamps=[5,4,3,2,1]

pdFitName = "fivePar"
fitName = "fourPar"
#pdFitName = "fourPar"
#fitName = "threePar"
channelNames = ["yxxjjjj_4j_inclusive"]

outputdir="fitsyxxjjjjInclusive"
signalfile =  "Gaussian"

lumi = 139000

atlasLabel = "Simulation Internal"

#rebinedges = config.getBinning(rangelow, rangehigh, delta=50)

'''
#sigmeans=[5000]
#sigamps = [5]
#channelNames =["yxxjjjj_4j_alpha9"]
for sigmean in sigmeans:
  for sigwidth in sigwidths:
    for channelName in channelNames:
      #infiles = ["PostFit_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile)]
      infiles = ["PostFit_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)]
      #infiles = [config.getFileName("PostFit_spuriousSignal", cdir + "/scripts/", channelName, outputdir, sigmean, sigwidth, 0)]

      fitNames = [fitName]
      for toy in range(1):
      #for toy in range(10):
        outfileFits = config.getFileName("fits_PD_%d"%(toy), cdir + "/scripts/", channelName, outputdir, sigmean, sigwidth, 0)
        rangelow=config.samples[channelName]["rangelow"]
        rangehigh=config.samples[channelName]["rangehigh"]
        rebinFactor = 100
        rebinedges = config.getBinning(rangelow, rangehigh, delta=rebinFactor)

        #plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir, suffix="_%d"%(toy), sigamp=0, sigwidth=sigwidth, sigmean=sigmean, toy=toy)

for sigmean in sigmeans:
  for sigwidth in sigwidths:
    for sigamp in sigamps:
      for channelName in channelNames:
        infiles = ["PostFit_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile)]
        #infiles = ["PostFit_sigPlusBkg_%s_%s_%s_Mean_%d_Width_%d_Amp_%d"%(pdFitName, fitName, signalfile, sigmean, sigwidth, sigamp)]
  
        fitNames = [fitName]
        #for toy in range(1):
        for toy in range(10):
          outfileFits = config.getFileName("fits_PD_%d"%(toy), cdir + "/scripts/", channelName, outputdir, sigmean, sigwidth, sigamp)
          rangelow=config.samples[channelName]["rangelow"]
          rangehigh=config.samples[channelName]["rangehigh"]
          rebinFactor = 100
          rebinedges = config.getBinning(rangelow, rangehigh, delta=rebinFactor)

          #plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir, suffix="_%d"%(toy), sigamp=sigamp, sigwidth=sigwidth, sigmean=sigmean, toy=toy)
'''










infilesChi2 = "PostFit_%s_PD_%s_bkgonly"%(pdFitName, fitName)
inhistChi2="chi2"
outfileChi2="chi2_%s_%s_%s"%(pdFitName, fitName, signalfile)
#getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=0, sigwidth=0, sigamp=0, lumi=lumi, atlasLabel=atlasLabel)


infilesChi2 = "PostFit_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
inhistChi2="chi2"
outfileChi2="chi2_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
#for sigmean in sigmeans:
#  for sigwidth in sigwidths:
#    getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=sigmean, sigwidth=sigwidth, sigamp=0, lumi=lumi, atlasLabel=atlasLabel)



#for channelName in channelNames:
#lumi =  config.samples[channelNames[0]]["lumi"]
#infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
#infilePD='PD_%s_bkgonly'%(pdFitName)
#outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
#infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
#rangelow = config.samples[channelNames[0]]["rangelow"]
#rangehigh = config.samples[channelNames[0]]["rangehigh"]
#spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=outputdir)




# Extraction graphs
for channelName in channelNames:
  lumi =  config.samples[channelName]["lumi"]
  infileExtraction="FitParameters_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile)
  infilesBkg = "PostFit_%s_PD_bkgonly"%(pdFitName)
  infilePD='PD_%s_bkgonly'%(pdFitName)
  outfileExtraction = "PD_extraction_%s_%s_%s"%(pdFitName, fitName, signalfile)
  rangelow = config.samples[channelName]["rangelow"]
  rangehigh = config.samples[channelName]["rangehigh"]
  #createExtractionGraph.createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=infileExtraction, infilePD=infilePD, outfile=outfileExtraction, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/", lumi=lumi, isNInjected=False, indir=outputdir)


# Limits
pathsLimits = [ "Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile)]
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelName=channelNames,atlasLabel=atlasLabel)

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


