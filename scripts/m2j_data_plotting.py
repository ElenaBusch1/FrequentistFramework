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
#sigmeans = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500]
#sigmeans = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
sigmeans = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000]

spuriousRanges = [1500, 400, 150, 15, 5, 5, 5]
spuriousRanges = [500, 500, 500, 500, 300, 300, 300, 300, 300, 300, 300, 100, 100, 100, 100, 100,100, 100,100, 100,50, 30,30, 30,30, 10, 10, 10,10,10,10,10,10,10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]

#sigwidths=[ 5, 10, 15 ]
sigwidths=[ 10]

pdFitName = "fiveParM2j"
fitName = "fourParM2j"
#channelNames =  [ "Data_2javg_alpha0", "Data_2javg_alpha1", "Data_2javg_alpha2", "Data_2javg_alpha3", "Data_2javg_alpha4", "Data_2javg_alpha5", "Data_2javg_alpha6", "Data_2javg_alpha7", "Data_2javg_alpha8", "Data_2javg_alpha9", "Data_2javg_alpha10", "Data_2javg_alpha11", ]
channelNames =  [ "Data_2javg_alpha0", "Data_2javg_alpha1", "Data_2javg_alpha2", "Data_2javg_alpha3", "Data_2javg_alpha4", "Data_2javg_alpha5", "Data_2javg_alpha6", "Data_2javg_alpha7", ]
alphaBins = [0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34]


coutputdir="fits2javg_data_"
#signalfile =  "template"
#signalfile =  "Gaussian"
#signalfile =  "crystalBallHistNoSyst"
signalfile =  "crystalBallHist"

lumi = 140000
atlasLabel = "Simulation Internal"

lumi =  config.samples[channelNames[0]]["lumi"]
infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
rangelow = config.samples[channelNames[0]]["rangelow"]
rangehigh = config.samples[channelNames[0]]["rangehigh"]
spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=coutputdir, signalName = "Y", labels = ["m_{<2j>}"], signalfile=signalfile, delta=50./12.)


pathsLimits = []
for channelName in channelNames:
  outputdir = coutputdir + channelName
  pathsLimits.append("Limits_limits_%s_%s"%(fitName, signalfile))
outputdir = coutputdir + channelName
#fc.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelNames=channelNames,atlasLabel=atlasLabel, deltaMassAboveFit=100)

# Limits
pathsLimits = []
for channelName in channelNames:
  outputdir = coutputdir + channelName
  pathsLimits = [ "Limits_limits_%s_%s"%(fitName, signalfile)]
  plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelName=[channelName],atlasLabel=atlasLabel, deltaMassAboveFit=100, signalType=signalfile)

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
#plotLimits2D.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelNames=channelNames,atlasLabel=atlasLabel, deltaMassAboveFit=50, alphaBins=alphaBins, postfitPaths = pathsPostFit)




