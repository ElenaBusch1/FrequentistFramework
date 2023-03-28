import scripts.config as config
import python.createExtractionGraph as createExtractionGraph
import python.createCoverageGraph as createCoverageGraph
import python.plotLimits_jjj as plotLimits_jjj
import python.plotLimits2D as plotLimits2D
import python.getChi2Distribution as getChi2Distribution
import python.plotFalseExclusionCandles as plotFalseExclusionCandles
import python.spuriousSignal as spuriousSignal
import python.plotFits as plotFits
import python.plotPulls as plotPulls
import python.fitQualityTests as fitQualityTests
import python.plotSignalInjection as plotSignalInjection
import python.compareFitParams as compareFitParams
import python.plotBkgOnly as pbo
import python.fluctuationsCheck as fc

cdir = config.cdir


#sigmeans= [500, 700, 1000, 1500, 2000, 2500, 3000,]
sigmeans = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500]

#spuriousRanges = [300, 100, 30, 10, 5, 5]
spuriousRanges = [1500, 400, 150, 15, 5, 5, 5]
#spuriousRanges = [100, 50, 50, 30, 10, 5, 5]
#sigwidths=[ 5, 10, 15 ]
sigwidths=[ 10]

#pdFitName = "sixPar"
#fitName = "fivePar"
pdFitName = "fiveParM2j"
fitName = "fourParM2j"
channelNames =  [ "Data_2javg_alpha0", "Data_2javg_alpha1", "Data_2javg_alpha2", "Data_2javg_alpha3", "Data_2javg_alpha4", "Data_2javg_alpha5", "Data_2javg_alpha6", "Data_2javg_alpha7", "Data_2javg_alpha8", "Data_2javg_alpha9", "Data_2javg_alpha10", "Data_2javg_alpha11", ]
alphaBins = [0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34]



coutputdir="fits2javg_data_"
#signalfile =  "template"
signalfile =  "Gaussian"
#signalfile =  "crystalBallHistNoSyst"
#signalfile =  "crystalBallHist"

lumi = 140000

atlasLabel = "Simulation Internal"

#rebinedges = config.getBinning(rangelow, rangehigh, delta=50)

lumi =  config.samples[channelNames[0]]["lumi"]


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
#spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=coutputdir, signalName = "Y", labels = ["m_{4j}"])

pathsLimits = []
for channelName in channelNames:
  outputdir = coutputdir + channelName
  pathsLimits.append("Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile))
outputdir = coutputdir + channelName
#fc.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelNames=channelNames,atlasLabel=atlasLabel, deltaMassAboveFit=100)

# Limits
pathsLimits = []
for channelName in channelNames:
  outputdir = coutputdir + channelName
  pathsLimits = [ "Limits_limits_%s_%s"%(fitName, signalfile)]
  plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelName=[channelName],atlasLabel=atlasLabel, deltaMassAboveFit=100)

#pathsLimits = []
#for channelName in channelNames:
#  pathsLimits.append("Limits_limits_%s_%s_%s"%(pdFitName, fitName, signalfile))
#outputdir = coutputdir 
##plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelNames=channelNames,atlasLabel=atlasLabel, deltaMassAboveFit=100)
#plotLimits2D.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelNames=channelNames,atlasLabel=atlasLabel, deltaMassAboveFit=50, alphaBins=alphaBins)

pathsLimits = []
pathsPostFit = []
for channelName in channelNames:
  pathsLimits.append("Limits_limits_%s_%s"%(fitName, signalfile))
  pathsPostFit.append("PostFit_limits_%s_%s"%(fitName, signalfile))
outputdir = coutputdir
#plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelNames=channelNames,atlasLabel=atlasLabel, deltaMassAboveFit=100)
plotLimits2D.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelNames=channelNames,atlasLabel=atlasLabel, deltaMassAboveFit=50, alphaBins=alphaBins, postfitPaths = pathsPostFit)




