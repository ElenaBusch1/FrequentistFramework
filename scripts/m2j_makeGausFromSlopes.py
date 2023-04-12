import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config

import python.prepareGaussianTemplates as pgt

#sigmeans = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]
sigmeans = [1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500]

sigwidths = [0.1]
#sigwidths = [0.05, 0.15]

alphaBins = [0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33]
#alphaBins = [0.11]

doSysts = True
tagName = "m2j_"
histName = "h2_resonance_jet_m2javg_alpha"


for  sigmean in sigmeans:
 for sigwidth in sigwidths:
  for alphaBin, alpha in enumerate(alphaBins):

    mY = round(sigmean / alpha / 10) * 10

    if mY < 500:
      continue
    if mY > 10000:
      continue

    print sigmean, alphaBin, mY, alpha

    outfileName = pgt.prepareGaussianTemplate(indir =  "/afs/cern.ch/work/j/jroloff/nixon/systematics/test/", histName = histName, doSysts = doSysts, mY = sigmean, alpha = alpha, outfile = "templates/%ssystematicsGaus_%d"%(tagName, sigwidth*100), sigma=sigwidth, maxX=3500)

    outfileTemplate = "signalTemplates/%sSignalGaus_mX_%d_mY_%d_width_%d.root"%(tagName, sigmean, mY, sigwidth*100)
    outfileTemplate = outfileTemplate.replace("MEAN", "%d"%(sigmean))
    outfileTemplate = outfileTemplate.replace("MASSX", "%d"%(mY))
    outfileTemplate = outfileTemplate.replace("ALPHA", "%d"%(alphaBin))

    pt.generateSignalWS(outfileName, histName+"_", doSysts, outfile=outfileTemplate)
    outfileTemplate = "signalTemplates/%sSignalGausNoSyst_mX_%d_mY_%d.root"%(tagName, sigmean, mY)
    pt.generateSignalWS(outfileName, histName+"_", doSysts=False, outfile=outfileTemplate)




