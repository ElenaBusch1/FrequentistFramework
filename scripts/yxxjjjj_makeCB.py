import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config

import python.prepareCBTemplates as pCBt

#sigmeans = [2000, 3000, 4000, 6000, 8000, 10000]
#sigmeans = [2000,2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250, 5500, 5750, 6000, 6250, 6500, 6750, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]
sigmeans = [10000]
#sigmeans = [8000]
#sigmeans = [8000, 10000]
#sigmeans = [8000]
alphaBins = [0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33]
#alphaBins = [0.11]

doSysts = True

for  sigmean in sigmeans:
  for alphaBin, alpha in enumerate(alphaBins):

    mY = round( (alpha * sigmean)/10)*10
    if mY < 500:
      continue

    print sigmean, alphaBin, mY, alpha

    histName = "h2_resonance_jet_m4j_alpha" 
    outfileName = pCBt.prepareCBTemplate(indir = "/afs/cern.ch/work/j/jroloff/nixon/signalMorphing/systs/", histName = histName, doSysts = True, mY = sigmean, alpha = alpha, outfile = "templates/systematics")

    outfileTemplate = "signalTemplates/SignalCB_mX_%d_mY_%d.root"%(sigmean, mY)
    outfileTemplate = outfileTemplate.replace("MEAN", "%d"%(sigmean))
    outfileTemplate = outfileTemplate.replace("MASSX", "%d"%(mY))
    outfileTemplate = outfileTemplate.replace("ALPHA", "%d"%(alphaBin))

    pt.generateSignalWS(outfileName, histName+"_", doSysts, outfile=outfileTemplate)
    outfileTemplate = "signalTemplates/SignalCBNoSyst_mX_%d_mY_%d.root"%(sigmean, mY)
    pt.generateSignalWS(outfileName, histName+"_", doSysts=False, outfile=outfileTemplate)




