import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config

#import python.prepareTemplates as pt

sigmeans = [250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650]
#sigmeans = [250, 300, 350, 400, 450, 500, 550, 575, 600, 625, 650]
#sigmeans = [250, 350, 450, 550, 650]
#sigmeans = [650, ]

doSysts = True
cdir = config.cdir
sigwidth = 0.1


for  sigmean in sigmeans:

    histName = "Morphed_m_%d"%(sigmean)
    channelName = "test3New_15"
    #systematicNameFile = config.getFileName("systematics", cdir + "/scripts/", "uncertaintySets", 200, 1000, sigmean, sigwidth*100) + ".txt"


    outfileTemplate = "signalTemplates/SignalTemplate_trijet_mZ_%d_width_%d.root"%(sigmean, sigwidth*100)
    outfileTemplate = outfileTemplate.replace("MEAN", "%d"%(sigmean))

    infileName = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/moment-morphing/dijetISRtrijetMorphing/morphed_trijet_g0.20.root"
    #pt.generateSignalWS(infileName, histName+"_", doSysts, outfile=outfileTemplate, systematicNameFile = "uncertaintySets/systematics.txt", suffix = "_", pruneThreshold = 10, jerPruneThreshold = 10)
    #pt.generateSignalWS(infileName, histName+"_", doSysts, outfile=outfileTemplate, systematicNameFile = "uncertaintySets/systematics_trijet_mass_%d_template.txt"%(sigmean), suffix = "_", pruneThreshold = 0.003, jerPruneThreshold = 0.1)
    pt.generateSignalWS(infileName, histName+"_", doSysts, outfile=outfileTemplate, systematicNameFile = "uncertaintySets/systematics_trijet_mass_%d_template.txt"%(sigmean), suffix = "_", pruneThreshold = 0.3, jerPruneThreshold = 0.5)


    #outfileTemplate = "signalTemplates/SignalTemplateNoSyst_trijet_mZ_%d_width_%d.root"%(sigmean, sigwidth*100)
    #outfileTemplate = outfileTemplate.replace("MEAN", "%d"%(sigmean))
    #pt.generateSignalWS(infileName, histName+"_", doSysts=False, outfile=outfileTemplate, suffix = "_")



