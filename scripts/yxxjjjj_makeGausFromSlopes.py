import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config

import python.prepareGaussianTemplates as pgt

#sigmeans = [2000, 3000, 4000, 6000, 8000, 10000]
#sigmeans = [2000,2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250, 5500, 5750, 6000, 6250, 6500, 6750, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]
sigmeans = [9250, 9500, 9750, 10000]
#sigmeans = [6250, 6500, 6750, 7000, 7250, 7500, 7750, 8000, 8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]
#sigmeans = [8250, 8500, 8750, 9000, 9250, 9500, 9750, 10000]
#sigmeans = [8250]
#sigmeans = [10000]
sigwidths = [0.1]
#sigwidths = [0.05, 0.15]
alphaBins = [0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33]
#alphaBins = [0.11]

doSysts = True
cdir = config.cdir


for  sigmean in sigmeans:
 for sigwidth in sigwidths:
  for alphaBin, alpha in enumerate(alphaBins):

    mY = round( (alpha * sigmean)/10)*10
    if mY < 500:
      continue

    print sigmean, alphaBin, mY, alpha

    histName = "h2_resonance_jet_m4j_alpha" 
    channelName = "yxxjjjj_4j_alpha%d"%(alphaBin)
    systematicNameFile = config.getFileName("systematics", cdir + "/scripts/", channelName, "uncertaintySets", sigmean, sigwidth*100) + ".txt"
    print(systematicNameFile)
    outfileName = pgt.prepareGaussianTemplate(indir =  "/afs/cern.ch/work/j/jroloff/nixon/systematics/test/", histName = histName, doSysts = doSysts, mY = sigmean, alpha = alpha, outfile = "templates/systematicsGaus_%d"%(sigwidth*100), sigma=sigwidth, pruneThreshold = 0.05, systematicNameFile = systematicNameFile)

    outfileTemplate = "signalTemplates/SignalGaus_mX_%d_mY_%d_width_%d.root"%(sigmean, mY, sigwidth*100)
    outfileTemplate = outfileTemplate.replace("MEAN", "%d"%(sigmean))
    outfileTemplate = outfileTemplate.replace("MASSX", "%d"%(mY))
    outfileTemplate = outfileTemplate.replace("ALPHA", "%d"%(alphaBin))

    pt.generateSignalWS(outfileName, histName+"_", doSysts, outfile=outfileTemplate, systematicNameFile = systematicNameFile)
    outfileTemplate = "signalTemplates/SignalGausNoSyst_mX_%d_mY_%d_width_%d.root"%(sigmean, mY, sigwidth*100)
    pt.generateSignalWS(outfileName, histName+"_", doSysts=False, outfile=outfileTemplate)




