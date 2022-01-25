import scripts.config as config
import python.createExtractionGraph as createExtractionGraph
import python.createCoverageGraph as createCoverageGraph
import python.plotLimits_jjj as plotLimits_jjj
import python.getChi2Distribution as getChi2Distribution
import python.plotFalseExclusionCandles as plotFalseExclusionCandles

cdir = config.cdir


sigmeans=[ 550]
sigwidths=[ 7 ]
# These cannot start with 0, because this will result in an incorrect determination of nbkg for createExtractionGraph
#sigamps=[5,1,0]
sigamps=[5,1]
rangelow=300
rangehigh=1200
channelName="BkgLow_3_alpha0_SR1_tagged"
lumis =  29300



# Extraction graphs
infileExtraction='FitResult_sigPlusBkg'
infilePD='PD_bkgonly'
outfileExtraction = "PD_extraction_bkgonly"
createExtractionGraph.createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=infileExtraction, infilePD=infilePD, outfile=outfileExtraction, rangelow=rangelow, rangehigh = rangehigh, channelName=channelName, cdir=cdir+"/scripts/")


sigmeans=[ 550, 650]
# Limits
pathsLimits = [ "Limits_sigPlusBkg"]
plotLimits_jjj.plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumis, outdir=channelName, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh)

inputPDCoverage='PD_bkgonly'
outfileCoverage='Coverage'
createCoverageGraph.createCoverageGraph(pathsLimits[0], inputPDCoverage, sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, outfile=outfileCoverage, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh)
plotFalseExclusionCandles.plotFalseExclusionCandles("Coverage.root", sigmeans, sigwidths, rangelow, rangehigh, channelName, cdir)




# Chi2
for sigamp in sigamps:
  for sigmean in sigmeans:
    for sigwidth in sigwidths:

      infilesChi2 = "PostFit_sigPlusBkg"
      inhistChi2="chi2"
      outfileChi2 = config.getFileName("chi2", cdir + "/scripts/", channelName, rangelow, rangehigh)
      outhistChi2="chi2"

      getChi2Distribution.getChi2Distribution(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, outhist=outhistChi2, cdir=cdir+"/scripts/", channelName=channelName, rangelow=rangelow, rangehigh=rangehigh, nToys = config.nToys, sigmean=sigmean, sigwidth=sigwidth, sigamp=sigamp)



