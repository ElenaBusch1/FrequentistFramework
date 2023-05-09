import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config

import python.prepareCBTemplates as pCBt

#sigmeans = [2000, 3000, 4000, 6000, 8000, 10000]
#sigmeans = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
#sigmeans = [500, 600, 700,  800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500]
#sigmeans = [1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
#sigmeans = [1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
#sigmeans = [2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
#sigmeans = [1400,1500]
sigmeans = [800,]


alphaBins = [0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33]
#alphaBins = [0.11]

doSysts = True
tagName = "m2j_"
histName = "h2_resonance_jet_m2javg_alpha" 
cdir = config.cdir
sigwidth = 0.1
signalfile = "crystalBallHist"

for  sigmean in sigmeans:
  for alphaBin, alpha in enumerate(alphaBins):
    if alphaBin != 3:
      continue

    mY = round(sigmean / alpha / 10) * 10
    if sigmean < 500:
      continue
    if mY < 2000:
      continue
    if mY > 10000:
      continue

    print sigmean, alphaBin, mY, alpha

    #outfileTemplate = "signalTemplates/%sNoPruneSignalCB_mX_%d_mY_%d.root"%(tagName, mY, sigmean)
    outfileTemplate = "signalTemplates/%sExtraPruneSignalCB_mX_%d_mY_%d.root"%(tagName, mY, sigmean)
    outfileTemplate = outfileTemplate.replace("MEAN", "%d"%(mY))
    outfileTemplate = outfileTemplate.replace("MASSX", "%d"%(sigmean))
    outfileTemplate = outfileTemplate.replace("ALPHA", "%d"%(alphaBin))
    channelName = "yxxjjjj_2javg_alpha%d"%(alphaBin)
    #systematicNameFile = config.getFileName("systematicsNoPrune", cdir + "/scripts/", channelName, "uncertaintySets", sigmean, sigwidth*100) + "_" + signalfile + ".txt"
    systematicNameFile = config.getFileName("systematicsExtraPrune", cdir + "/scripts/", channelName, "uncertaintySets", sigmean, sigwidth*100) + "_" + signalfile + ".txt"

    #outfileName = pCBt.prepareCBTemplate(indir = "/afs/cern.ch/work/j/jroloff/nixon/signalMorphing/systs/", histName = histName, doSysts = doSysts, mY = mY, alpha = alpha, outfile = "templates/%ssystematics"%(tagName), maxX=3500,pruneThreshold = 0.05, systematicNameFile = systematicNameFile)
    outfileName = pCBt.prepareCBTemplate(indir = "/afs/cern.ch/work/j/jroloff/nixon/signalMorphing/systs/", histName = histName, doSysts = doSysts, mY = mY, alpha = alpha, outfile = "templates/%sExtraPrunesystematics"%(tagName), maxX=3500,pruneThreshold = 0.1, systematicNameFile = systematicNameFile, pruneThresholdJer = 8)
    #outfileName = pCBt.prepareCBTemplate(indir = "/afs/cern.ch/work/j/jroloff/nixon/signalMorphing/systs/", histName = histName, doSysts = doSysts, mY = mY, alpha = alpha, outfile = "templates/%sNoPruneSystematics"%(tagName), maxX=3500,pruneThreshold = 0.0, systematicNameFile = systematicNameFile, pruneThresholdJer = 0)
    #outfileName = pCBt.prepareCBTemplate(indir = "/afs/cern.ch/work/j/jroloff/nixon/signalMorphing/systs/", histName = histName, doSysts = doSysts, mY = mY, alpha = alpha, outfile = "templates/%ssystematics"%(tagName), maxX=3500,pruneThreshold = 0.2, systematicNameFile = systematicNameFile)

    pt.generateSignalWS(outfileName, histName+"_", doSysts, outfile=outfileTemplate,  systematicNameFile = systematicNameFile)

    #outfileTemplate = "signalTemplates/%sSignalCBNoSyst_mX_%d_mY_%d.root"%(tagName, mY, sigmean)
    #pt.generateSignalWS(outfileName, histName+"_", doSysts=False, outfile=outfileTemplate)





