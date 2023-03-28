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


#sigmeans=[3000, 4000, 5000, 6000, 7000, 8000]
#sigmeans=[2000, 3000, 4000, 6000, 8000, 10000]
sigmeans = [2000,2250, 2500, 2750, 3000,3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250, 5500, 5750, 6000, 6250, 6500, 6750, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]

#sigmeans = [2000,2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250, 5500, 5750, 6000, 6250, 6500, 6750, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]
#sigmeans=[4000, 8000]
#sigmeans=[2000, 2500, 3000, 3500, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
#sigmeans=[8000]
#spuriousRanges = [300, 100, 30, 10, 5, 5]
spuriousRanges = [1500, 1500, 1500, 1500, 1000, 1000, 1000, 1000, 400, 400, 400, 400, 150, 150, 150, 150, 50, 50, 50, 15, 15, 15, 15, 15, 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5, 5, 5]
#spuriousRanges = [100, 50, 50, 30, 10, 5, 5]
#sigwidths=[ 5, 10, 15 ]
sigwidths=[ 10]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
#sigamps=[5,4,3,2,1,0]
#sigamps=[5,4,3,2,1]
sigamps=[5,3,1]

#pdFitName = "sixPar"
#fitName = "fivePar"
pdFitName = "fivePar"
fitName = "fourPar"
channelNames = [ "Data_yxxjjjj_4j_alpha0", "Data_yxxjjjj_4j_alpha1", "Data_yxxjjjj_4j_alpha2", "Data_yxxjjjj_4j_alpha3", "Data_yxxjjjj_4j_alpha4", "Data_yxxjjjj_4j_alpha5", "Data_yxxjjjj_4j_alpha6", "Data_yxxjjjj_4j_alpha7", "Data_yxxjjjj_4j_alpha8", "Data_yxxjjjj_4j_alpha9", "Data_yxxjjjj_4j_alpha10", "Data_yxxjjjj_4j_alpha11", ]
#channelNames = [ "Data_yxxjjjj_4j_alpha0", ]
alphaBins = [0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34]



coutputdir="fitsData_"
#signalfile =  "template"
#signalfile =  "Gaussian"
#signalfile =  "crystalBallHistNoSyst"
signalfile =  "crystalBallHist"

lumi = 140000

atlasLabel = "Simulation Internal"

#rebinedges = config.getBinning(rangelow, rangehigh, delta=50)

lumi =  config.samples[channelNames[0]]["lumi"]


lumi =  config.samples[channelNames[0]]["lumi"]
infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)
rangelow = config.samples[channelNames[0]]["rangelow"]
rangehigh = config.samples[channelNames[0]]["rangehigh"]
spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, rangelow=rangelow, rangehigh = rangehigh, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=coutputdir, signalName = "Y", labels = ["m_{4j}"])




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
  #plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelName=[channelName],atlasLabel=atlasLabel, deltaMassAboveFit=50)

pathsLimits = []
pathsPostFit = []
for channelName in channelNames:
  pathsLimits.append("Limits_limits_%s_%s"%(fitName, signalfile))
  pathsPostFit.append("PostFit_limits_%s_%s"%(fitName, signalfile))
outputdir = coutputdir 
#plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelNames=channelNames,atlasLabel=atlasLabel, deltaMassAboveFit=100)
#plotLimits2D.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumi, outdir=outputdir, cdir=cdir+"/scripts/",channelNames=channelNames,atlasLabel=atlasLabel, deltaMassAboveFit=50, alphaBins=alphaBins, postfitPaths = pathsPostFit)




