import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config

import python.prepareGaussianTemplates as pgt

#sigmeans = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650]
#sigmeans = [250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
sigmeans = [450]
#sigmeans = [10000]
sigwidths = [0.15]
#sigwidths = [0.05, 0.07, 0.10, 0.12, 0.15]

doSysts = True
cdir = config.cdir

#pruneThreshold = 0.003
#jerPruneThreshold = 0.05
pruneThreshold = 0.006
jerPruneThreshold = 0.08

for  sigmean in sigmeans:
 for sigwidth in sigwidths:

    histName = "test3New_15"
    channelName = "test3New_15"
    systematicNameFile = config.getFileName("systematics", cdir + "/scripts/", "uncertaintySets", 200, 1000, sigmean, sigwidth*100) + ".txt"

    outfileName = pgt.prepareGaussianTemplate(indir =  "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/test/", histName = histName, doSysts = doSysts, mY = sigmean, outfile = "templates/systematicsGaus_%d"%(sigwidth*100), sigma=sigwidth, pruneThreshold = pruneThreshold, jerPruneThreshold = jerPruneThreshold, systematicNameFile = systematicNameFile)

    outfileTemplate = "signalTemplates/SignalGaus_trijet_mZ_%d_width_%d.root"%(sigmean, sigwidth*100)
    pt.generateSignalWS(outfileName, histName+"_", doSysts, outfile=outfileTemplate, systematicNameFile = systematicNameFile, pruneThreshold = pruneThreshold, jerPruneThreshold = jerPruneThreshold, indirSysts = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/test/")

    outfileTemplate = "signalTemplates/SignalGausNoSyst_trijet_mZ_%d.root"%(sigmean)
    pt.generateSignalWS(outfileName, histName+"_", doSysts=False, outfile=outfileTemplate)





