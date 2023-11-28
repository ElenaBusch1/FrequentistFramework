import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config

#import python.prepareTemplates as pt

sigmeans = [250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
#sigmeans = [650, ]

doSysts = True
cdir = config.cdir
sigwidth = 0.1


for  sigmean in sigmeans:

    histName = "Morphed_m_%d"%(sigmean)
    channelName = "btagFinal"
    #systematicNameFile = config.getFileName("systematics", cdir + "/scripts/", channelName, 200, 1000, sigmean, sigwidth*100) + ".txt"
    #systematicNameFile = config.getFileName("systematics", cdir + "/scripts/", "uncertaintySets", 200, 1000, sigmean, sigwidth*100) + ".txt"

    #outfileName = pt.prepareTemplate(indir =  "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/test/", histName = histName, doSysts = doSysts, mY = sigmean, outfile = "templates/systematicsGaus_%d"%(sigwidth*100), sigma=sigwidth, pruneThreshold = 0.005, systematicNameFile = systematicNameFile)

    outfileTemplate = "signalTemplates/SignalTemplate_bbj_mZ_%d_width_%d.root"%(sigmean, sigwidth*100)
    outfileTemplate = outfileTemplate.replace("MEAN", "%d"%(sigmean))

    #infileName = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/signalMassSpectra/normalized_massSpectraWithSysts_sigpick2_10_BkgAlpha_20_dimVarsDphi_%d.root"%(sigmean)
    infileName = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/moment-morphing/dijetISRBtagjbbMorphing/morphed_jbb_g0.20.root"
    #pt.generateSignalWS(infileName, histName+"_", doSysts, outfile=outfileTemplate, systematicNameFile = "uncertaintySets/systematics.txt", suffix = "_")
    #print sigmean, "uncertaintySets/systematics_mass_%d_template.txt"%(sigmean)
    pt.generateSignalWS(infileName, histName+"_", doSysts, outfile=outfileTemplate, systematicNameFile = "uncertaintySets/systematics_bbj_mass_%d_template.txt"%(sigmean), suffix = "_", pruneThreshold = 0.003, jerPruneThreshold = 0.003)

    outfileTemplate = "signalTemplates/SignalTemplateNoSyst_bbj_mZ_%d_width_%d.root"%(sigmean, sigwidth*100)
    outfileTemplate = outfileTemplate.replace("MEAN", "%d"%(sigmean))
    pt.generateSignalWS(infileName, histName+"_", doSysts=False, outfile=outfileTemplate, suffix = "_")



