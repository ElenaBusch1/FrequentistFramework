import python.LocalFunctions as lf

def getSigma(dirName, channelName, sigmean=0, sigwidth=0, signalName=0):
  try:
    fileName = "%s_/bias_%s_%s_%d.root"%(dirName, signalName, channelName, sigwidth)
    histName = "%s_sigma"%(channelName)
    hist = lf.read_histogram(fileName, histName)

    print fileName, histName
    sigma = hist.Interpolate(sigmean)
  except:
    fileName = "%s/bias_%s_%s_%d.root"%(dirName, signalName, channelName, sigwidth)
    histName = "%s_sigma"%(channelName)
    hist = lf.read_histogram(fileName, histName)

    print fileName, histName
    sigma = hist.Interpolate(sigmean)
  
  return sigma

def getBiasFraction(dirName, channelName, sigmean=0, sigwidth=0, signalName=0):
  fileName = "bias"
  histName = "biasFrac"
  hist = lf.read_histogram(fileName, histName)
  #biasFrac = hist.Interpolate(sigmean)
  biasFrac = hist.GetBinContent(hist.FindBin(sigmean))
  return biasFrac

def getSpuriousSignal(dirName, channelName, sigmean=0, sigwidth=0, signalName=0, biasFraction = 0):
  sigma = getSigma(dirName, channelName, sigmean, sigwidth, signalName)
  if not biasFraction:
    biasFraction = getBiasFraction(dirName, channelName, sigmean, sigwidth, signalName)

  bias = sigma * biasFraction
  return bias

