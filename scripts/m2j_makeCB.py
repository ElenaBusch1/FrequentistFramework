import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config

import python.prepareCBTemplates as pCBt

#sigmeans = [2000, 3000, 4000, 6000, 8000, 10000]
#sigmeans = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
sigmeans = [1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
#sigmeans = [1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
#sigmeans = [2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
#sigmeans = [700,]
#sigmeans = [800,]
#sigmeans = [2000,2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250, 5500, 5750, 6000, 6250, 6500, 6750, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]


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

    mY = round(sigmean / alpha / 10) * 10
    if sigmean < 500:
      continue
    if mY < 2000:
      continue
    if mY > 10000:
      continue

    print sigmean, alphaBin, mY, alpha

    outfileTemplate = "signalTemplates/%sSignalCB_mX_%d_mY_%d.root"%(tagName, mY, sigmean)
    outfileTemplate = outfileTemplate.replace("MEAN", "%d"%(mY))
    outfileTemplate = outfileTemplate.replace("MASSX", "%d"%(sigmean))
    outfileTemplate = outfileTemplate.replace("ALPHA", "%d"%(alphaBin))
    channelName = "yxxjjjj_2javg_alpha%d"%(alphaBin)
    systematicNameFile = config.getFileName("systematics", cdir + "/scripts/", channelName, "uncertaintySets", sigmean, sigwidth*100) + "_" + signalfile + ".txt"

    outfileName = pCBt.prepareCBTemplate(indir = "/afs/cern.ch/work/j/jroloff/nixon/signalMorphing/systs/", histName = histName, doSysts = doSysts, mY = mY, alpha = alpha, outfile = "templates/%ssystematics"%(tagName), maxX=3500,pruneThreshold = 0.05, systematicNameFile = systematicNameFile)

    pt.generateSignalWS(outfileName, histName+"_", doSysts, outfile=outfileTemplate,  systematicNameFile = systematicNameFile)

    outfileTemplate = "signalTemplates/%sSignalCBNoSyst_mX_%d_mY_%d.root"%(tagName, mY, sigmean)
    pt.generateSignalWS(outfileName, histName+"_", doSysts=False, outfile=outfileTemplate)





