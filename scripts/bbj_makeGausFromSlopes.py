import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config

import python.prepareGaussianTemplates as pgt

#sigmeans = [200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
sigmeans = [650,]
#sigwidths = [0.1]
#sigwidths = [0.05, 0.07, 0.1, 0.12, 0.15]
sigwidths = [0.15]

doSysts = True
cdir = config.cdir

#pruneThreshold = 0.005
#jerPruneThreshold = 0.05
pruneThreshold = 0.007
jerPruneThreshold = 0.08


for  sigmean in sigmeans:
 for sigwidth in sigwidths:

    histName = "btagFinal"
    channelName = "btagFinal"
    systematicNameFile = config.getFileName("systematics_bjj", cdir + "/scripts/", "uncertaintySets", 200, 1000, sigmean, sigwidth*100) + ".txt"

    #outfileName = pgt.prepareGaussianTemplate(indir =  "/afs/cern.ch/work/j/jroloff/dijetPlusISR/btagStudies/test/", histName = histName, doSysts = doSysts, mY = sigmean, outfile = "templates/systematicsGausBBJ_%d"%(int(sigwidth*100)), sigma=sigwidth, pruneThreshold = 0.003, systematicNameFile = systematicNameFile, jerPruneThreshold=0.05, inputSystName = "uncertaintySets/systematicsBtag")
    outfileName = pgt.prepareGaussianTemplate(indir =  "/afs/cern.ch/work/j/jroloff/dijetPlusISR/btagStudies/test/", histName = histName, doSysts = doSysts, mY = sigmean, outfile = "templates/systematicsGausBBJ_%d"%(int(sigwidth*100)), sigma=sigwidth, pruneThreshold = pruneThreshold, systematicNameFile = systematicNameFile, jerPruneThreshold=jerPruneThreshold, inputSystName = "uncertaintySets/systematicsBtag")

    outfileTemplate = "signalTemplates/SignalGaus_bbj_mZ_%d_width_%d.root"%(sigmean, int(sigwidth*100))
    pt.generateSignalWS(outfileName, histName+"_", doSysts, outfile=outfileTemplate, systematicNameFile = systematicNameFile, pruneThreshold = pruneThreshold, jerPruneThreshold = jerPruneThreshold, indirSysts = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/btagStudies/test/", inputSystName = "uncertaintySets/systematicsBtag.txt")

    outfileTemplate = "signalTemplates/SignalGausNoSyst_bbj_mZ_%d.root"%(sigmean)
    pt.generateSignalWS(outfileName, histName+"_", doSysts=False, outfile=outfileTemplate)








