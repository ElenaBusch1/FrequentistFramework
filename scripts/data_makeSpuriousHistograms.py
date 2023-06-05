import scripts.config as config
import python.spuriousSignal as spuriousSignal

cdir = config.cdir

##############################################
# m4j
##############################################
sigmeans = [2000,2250, 2500, 2750, 3000,3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250, 5500, 5750, 6000, 6250, 6500, 6750, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]

spuriousRanges = [1500, 1500, 1500, 1500, 1000, 1000, 1000, 1000, 400, 400, 400, 400, 150, 150, 150, 150, 50, 50, 50, 15, 15, 15, 15, 15, 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5, 5, 5]
sigwidths=[ 5, 10, 15 ]
#sigwidths=[ 10]

pdFitName = "fivePar"
fitName = "fourPar"
channelNames = [ "Data_yxxjjjj_4j_alpha0", "Data_yxxjjjj_4j_alpha1", "Data_yxxjjjj_4j_alpha2", "Data_yxxjjjj_4j_alpha3", "Data_yxxjjjj_4j_alpha4", "Data_yxxjjjj_4j_alpha5", "Data_yxxjjjj_4j_alpha6", "Data_yxxjjjj_4j_alpha7", "Data_yxxjjjj_4j_alpha8", "Data_yxxjjjj_4j_alpha9", "Data_yxxjjjj_4j_alpha10", "Data_yxxjjjj_4j_alpha11", ]

coutputdir="fitsData_"
signalfile =  "gausHistNoSyst"

lumi =  config.samples[channelNames[0]]["lumi"]
infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)

#spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=coutputdir, signalName = "Y", labels = ["m_{4j}"], signalfile=signalfile)


##############################################
# <m2j>
##############################################
sigmeans = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500]
spuriousRanges = [500, 500, 500, 500, 300, 300, 300, 300, 300, 300, 300, 100, 100, 100, 100, 100,100, 100,100, 100,50, 30,30, 30,30, 10, 10, 10,10,10,10,10,10,10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]

sigwidths=[ 5, 10, 15 ]
#sigwidths=[ 10]

pdFitName = "fiveParM2j"
fitName = "fourParM2j"
channelNames =  [ "Data_2javg_alpha0", "Data_2javg_alpha1", "Data_2javg_alpha2", "Data_2javg_alpha3", "Data_2javg_alpha4", "Data_2javg_alpha5", "Data_2javg_alpha6", "Data_2javg_alpha7", "Data_2javg_alpha8", "Data_2javg_alpha9", "Data_2javg_alpha10", "Data_2javg_alpha11", ]


coutputdir="fits2javg_data_"
signalfile =  "gausHistNoSyst"
infileExtraction="FitParameters_spuriousSignal_%s_%s_%s"%(pdFitName, fitName, signalfile)
infilePD='PD_%s_bkgonly'%(pdFitName)
outfileSpurious = "%s_%s_%s"%(pdFitName, fitName, signalfile)
infileBkgOnly = "FitParameters_%s_PD_%s_bkgonly"%(pdFitName, fitName)

spuriousSignal.spuriousSignal(sigmeans=sigmeans, sigwidths=sigwidths, infile=infileExtraction, infilePD=infilePD, outfile=outfileSpurious, channelNames=channelNames, cdir=cdir+"/scripts/", bkgOnlyFitFile = infileBkgOnly, fitName = fitName, crange = spuriousRanges, outputdir=coutputdir, signalName = "Y", labels = ["m_{<2j>}"], signalfile=signalfile, delta=50./12.)




