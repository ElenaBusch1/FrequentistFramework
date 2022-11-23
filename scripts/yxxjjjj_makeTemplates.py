import python.PrepareTemplates.dijetTLA_genJJJSignals as pt
import config


sigmeans = [2000, 3000, 4000, 6000, 8000]
alphaBins = [0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33]
signal = "gausHist"

#sigmeans = [6000]
#alphaBins = [0.11]

doSysts = True

for  sigmean in sigmeans:
  for alphaBin, alpha in enumerate(alphaBins):

    mY = round( (alpha * sigmean)/10)*10
    if mY < 500:
      continue

    print sigmean, alphaBin, mY, alpha
    histName = config.signals[signal]["histname"]
    infile = config.signals[signal]["histfile"]


    histName = histName.replace("MEAN", "%d"%(sigmean))
    histName = histName.replace("MASSX", "%d"%(mY))
    histName = histName.replace("ALPHA", "%d"%(alphaBin))

    infile = infile.replace("MEAN", "%d"%(sigmean))
    infile = infile.replace("MASSX", "%d"%(mY))
    infile = infile.replace("ALPHA", "%d"%(alphaBin))


    outfile = "signalTemplates/SignalGaus_mX_%d_mY_%d.root"%(sigmean, mY)
    outfile = outfile.replace("MEAN", "%d"%(sigmean))
    outfile = outfile.replace("MASSX", "%d"%(mY))
    outfile = outfile.replace("ALPHA", "%d"%(alphaBin))

    print infile, histName, outfile

    pt.generateSignalWS(infile, histName, doSysts, outfile=outfile)



