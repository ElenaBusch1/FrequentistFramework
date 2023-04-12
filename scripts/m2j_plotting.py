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
#sigmeans=[500, 700, 1000, 1500, 2000, 2500, 3000]
sigmeans=[500, 700, 1000, 1500, 2000, 2500]
sigmeans = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]

spuriousRanges = [500, 500, 500, 500, 300, 300, 300, 300, 100, 100, 100, 100, 100, 10, 10, 10,10, 10,10, 10,10, 10,10, 10,10, 5, 5, 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
#sigwidths=[ 5,10,15]
sigwidths=[10]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
#sigamps=[3,1,]
#sigamps=[5,4,3,2,1,0]
sigamps=[5,4,3,2,1]

#pdFitName = "fivePar"
#fitName = "fourPar"
#pdFitName = "fourParM2j"
#fitName = "threeParM2j"
pdFitName = "sixParM2j"
fitName = "fiveParM2j"
channelNames = [ "yxxjjjj_2javg_alpha0", "yxxjjjj_2javg_alpha1", "yxxjjjj_2javg_alpha2", "yxxjjjj_2javg_alpha3", "yxxjjjj_2javg_alpha4", "yxxjjjj_2javg_alpha5", "yxxjjjj_2javg_alpha6", "yxxjjjj_2javg_alpha7", "yxxjjjj_2javg_alpha8", "yxxjjjj_2javg_alpha9", "yxxjjjj_2javg_alpha10", "yxxjjjj_2javg_alpha11", ]
#channelNames = [ "yxxjjjj_2javg_alpha3", ]
#channelNames = [ "yxxjjjj_2javg_alpha5", "yxxjjjj_2javg_alpha6", "yxxjjjj_2javg_alpha7", "yxxjjjj_2javg_alpha8", "yxxjjjj_2javg_alpha9", "yxxjjjj_2javg_alpha10", "yxxjjjj_2javg_alpha11", ]
#channelNames = [ "yxxjjjj_2javg_alpha10", "yxxjjjj_2javg_alpha11", ]
#channelNames = [ "yxxjjjj_2javg_alpha3", ]
#channelNames = [ "yxxjjjj_2javg_alpha9", "yxxjjjj_2javg_alpha10",]


coutputdir="fits2javg_"
signalfile =  "Gaussian"

lumi = 140000

atlasLabel = "Simulation Internal"

#rebinedges = config.getBinning(rangelow, rangehigh, delta=50)


lumi =  config.samples[channelNames[0]]["lumi"]
#infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
infileExtraction="FitParameters_sigPlusBkg_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
rangelow = config.samples[channelNames[0]]["rangelow"]
rangehigh = config.samples[channelNames[0]]["rangehigh"]
#compareFitParams.compareFitParams(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=coutputdir, signalName = "Y", sigamps = sigamps)





# Plot PD fit results (not spurious signal)
for channelName in channelNames:
      outputdir = coutputdir + channelName
      #infiles = [config.getFileName("PostFit_MCPD_bkgOnly_threePar_fourPar", cdir + "/scripts/", channelName, outputdir)]
      #infiles = [config.getFileName("PostFit_MCPD_bkgOnly_threePar_fourPar", cdir + "/scripts/", channelName, outputdir)]
      infiles = ["PostFit_MCPD_bkgOnly_threePar_fourPar"]

      fitNames = [fitName]
      #for toy in range(1):
      for toy in range(10):
        outfileFits = config.getFileName("fits_MCPD_%d"%(toy), cdir + "/scripts/", channelName, outputdir)
        rangelow=config.samples[channelName]["rangelow"]
        rangehigh=config.samples[channelName]["rangehigh"]
        rebinFactor = 100
        rebinedges = config.getBinning(rangelow, rangehigh, delta=rebinFactor)

        #plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir, suffix="_%d"%(toy), toy=toy)
        #plotFits.plotFits(infiles=infiles, outfile=outfileFits,  minMjj=rangelow, maxMjj=rangehigh, cdir=cdir+"/scripts/", channelName=channelName, lumi=lumi, rebinedges=rebinedges, atlasLabel=config.atlasLabel, fitNames = fitNames, indir = outputdir, toy=toy)




'''
#sigmeans=[5000]
#sigamps = [5]
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


infilesChi2 = "PostFit_bkgOnly_%s_%s"%(pdFitName, fitName)
inhistChi2="chi2"
outfileChi2="chi2_%s_%s_%s"%(pdFitName, fitName, signalfile)
#getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelNames=channelNames, nToys = config.nToys, sigmean=0, sigwidth=0, sigamp=0, lumi=lumi, atlasLabel=atlasLabel, indir = coutputdir)


infilesChi2 = "PostFit_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
inhistChi2="chi2"
outfileChi2="chi2_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
#getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=sigmean, sigwidth=sigwidth, sigamp=0, lumi=lumi, atlasLabel=atlasLabel)
#for sigmean in sigmeans:
#  for sigwidth in sigwidths:
#    getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=sigmean, sigwidth=sigwidth, sigamp=0, lumi=lumi, atlasLabel=atlasLabel)



lumi =  config.samples[channelNames[0]]["lumi"]
infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
rangelow = config.samples[channelNames[0]]["rangelow"]
rangehigh = config.samples[channelNames[0]]["rangehigh"]
spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=coutputdir, signalName = "X", labels = ["m_{#LT 2j #GT} [GeV]"], delta=10)



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
  #createExtractionGraph.createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=infileExtraction, infilePD=infilePD, outfile=outfileExtraction, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/", lumi=lumi, isNInjected=False, indir=outputdir, deltaMassAboveFit = 50)

# Limits
for channelName in channelNames:
  outputdir = coutputdir + channelName
  pathsLimits = [ "Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile)]
  #plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelName=[channelName],atlasLabel=atlasLabel, deltaMassAboveFit=50)


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



