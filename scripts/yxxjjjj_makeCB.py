import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config

import python.prepareCBTemplates as pCBt

sigmeans = [2000, 3000, 4000, 6000, 8000, 10000]
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

    histName =  "h2_resonance_jet_m4j_alpha"
    outfileName = pCBt.prepareCBTemplate(histName = "h2_resonance_jet_m4j_alpha", doSysts = True, mY = sigmean, alpha = alpha, outfile = "templates/systematics")

    print sigmean, alphaBin, mY, alpha


    outfileTemplate = "signalTemplates/SignalCB_mX_%d_mY_%d.root"%(sigmean, mY)
    outfileTemplate = outfileTemplate.replace("MEAN", "%d"%(sigmean))
    outfileTemplate = outfileTemplate.replace("MASSX", "%d"%(mY))
    outfileTemplate = outfileTemplate.replace("ALPHA", "%d"%(alphaBin))

    pt.generateSignalWS(outfileName, histName+"_", doSysts, outfile=outfileTemplate)
    outfileTemplate = "signalTemplates/SignalCBNoSyst_mX_%d_mY_%d.root"%(sigmean, mY)
    pt.generateSignalWS(outfileName, histName+"_", doSysts=False, outfile=outfileTemplate)




