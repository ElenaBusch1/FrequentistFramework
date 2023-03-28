import python.LocalFunctions as lf

def getSigma(dirName, channelName, sigmean=0, sigwidth=0, signalName=0):
  fileName = "bias"
  fileName = "%s_/bias_Y_%s.root"%(dirName, channelName)
  histName = "%s_sigma"%(channelName)
  hist = lf.read_histogram(fileName, histName)

  sigma = hist.Interpolate(sigmean)
  
  return sigma

def getBiasFraction(dirName, channelName, sigmean=0, sigwidth=0, signalName=0):
  fileName = "bias"
  histName = "biasFrac"
  hist = lf.read_histogram(fileName, histName)
  biasFrac = hist.Interpolate(sigmean)
  return biasFrac

def getSpuriousSignal(dirName, channelName, sigmean=0, sigwidth=0, signalName=0, biasFraction = 0):
  sigma = getSigma(dirName, channelName, sigmean, sigwidth, signalName)
  if not biasFraction:
    biasFraction = getBiasFraction(dirName, channelName, sigmean, sigwidth, signalName)

  bias = sigma * biasFraction
  return bias

