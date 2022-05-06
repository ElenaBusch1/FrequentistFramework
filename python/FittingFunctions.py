import ROOT as r 
import array 
import time 
#import numpy as np

from array import array
from math import sqrt, ceil


def DivideWithErrors(cutSig, cutSigErr, totSig, totSigErr):
    num=r.TH1D("num_"+str(int(time.time())),"num",1,0,1)
    den=r.TH1D("den_"+str(int(time.time())),"den",1,0,1)
    num.SetBinContent(1,cutSig)
    num.SetBinError(1, cutSigErr)
    den.SetBinContent(1,totSig)
    den.SetBinError(1, totSigErr)

    num.Divide(den)

    fracSig    = num.GetBinContent(1)
    fracSigErr = num.GetBinError(1)
    return fracSig, fracSigErr


# Function to find the smallest window in a histogram that contains some fraction (frac) of the total events in that histo
def MinWindow( histo, frac):
  minWidth = 1e5
  if not isinstance(histo, r.TH1):
    return 0, 0
  if histo.Integral()==0:
    return 0, 0

  #histo.Scale(1.0/histo.Integral(0, histo.GetNbinsX()+1), "width");
  integral = histo.Integral(0, histo.GetNbinsX()+1)
  Nbins = histo.GetNbinsX()
  bestTopEdge = 0

  tempFrac = 0.0
  for imax in range(0, Nbins+1):
     #tempFrac += histo.GetBinContent(imax)/integral 
     tempFrac += histo.GetBinContent(imax)

  # The i in this loop will be the starting bin for a scan over histo
  for i in range(Nbins):
       tempFrac = 0.0
       imax = i

       # Scan over histo, starting at bin i until it contains a fraction of events > frac or it reaches the end of the histogram
       while tempFrac<float(frac) and imax != Nbins:
          tempFrac += histo.GetBinContent(imax)/integral 
          imax += 1

       # Width of the window found by the scan above
       width = histo.GetBinCenter(imax) - histo.GetBinCenter(i)
       # Bin center where the scan ended
       top_edge = histo.GetBinCenter(imax)

       # We want to find the smallest window containing fraction of signal ~= frac
       # So we check that our new width is smaller than the previous one (minwidth) and the scan didn't reach the end of the histo
       if imax != Nbins and width<minWidth:
          minWidth = width
          bestTopEdge = top_edge

  if minWidth > (histo.GetBinCenter(Nbins)-histo.GetBinCenter(1)):
    minWidth = (histo.GetBinCenter(Nbins)-histo.GetBinCenter(1))
    bestTopEdge = histo.GetBinCenter(Nbins)
  valLow = bestTopEdge-minWidth



  return valLow,bestTopEdge


def GetMassWindow(sig, minRange=40, maxRange=1500):
  # Setup a gaussian fit
  #sig.Rebin(3)
  #if(sig.Integral() > 0): 
  #  sig.Scale(1. / sig.Integral(0, sig.GetNbinsX()+1), "width")
  integral = sig.Integral(0, sig.GetNbinsX()+1)
  gaussian_fit =  r.TF1("myFitMassWindow","gaus", minRange, maxRange)
  mean = sig.GetMean()
  maximum = sig.GetMaximum()
  if(mean > maxRange):
    mean = (maxRange + minRange) / 2.
  if(mean < minRange):
    mean = (maxRange + minRange) / 2.
  sigma = 30

  gRandom1 = r.TRandom(1000)
  gRandom = r.TRandom3(1000)
  gaussian_fit.SetParameter(1,mean)
  gaussian_fit.SetParameter(2,sigma)
  gaussian_fit.SetParLimits(1, minRange, maxRange)
  gaussian_fit.SetParLimits(2, 0, 100)
  gaussian_fit.SetRange(minRange, maxRange)
  sig.Fit("myFitMassWindow","RQ0", "", minRange, maxRange)
  #print  "range", max(mean-1.5*sigma, minRange), min(mean+2.0*sigma, maxRange), minRange, maxRange, mean
  #sig.Fit("myFitMassWindow","RQ0", "", mean-2*sigma, mean+2*sigma)
  #sig.Fit("myFitMassWindow","RQ0", "", mean-1.5*sigma, mean+1.5*sigma)

  #for i in range(2):
  for i in range(1):
    mean  = gaussian_fit.GetParameter(1)
    sigma = gaussian_fit.GetParameter(2)
    if sigma < 3:
      sigma = 30
      mean = sig.GetMean()
      i = i-1
    gaussian_fit.SetParameter(1, mean)
    gaussian_fit.SetParameter(2, sigma)
    gaussian_fit.SetParLimits(2, 0.2*sigma, 4*sigma)
    gaussian_fit.SetParLimits(1, mean-3.*sigma, mean+3.*sigma)
    gaussian_fit.SetRange(mean-0.6*sigma, mean+2.*sigma)
    sig.Fit("myFitMassWindow","RQ0", "", mean-0.6*sigma, mean+2.*sigma)

  mean  = gaussian_fit.GetParameter(1)
  sigma = gaussian_fit.GetParameter(2)
  meanError  = gaussian_fit.GetParError(1)
  sigmaError = gaussian_fit.GetParError(2)
  return gaussian_fit.GetParameter(0), mean, sigma, meanError, sigmaError, gaussian_fit.GetParError(0), gaussian_fit


def GetScalePoints(hist, width=0.68):
    max_chi2 = 100

    responseFit, _, _, _, _ = GetResponseFit(hist)

    mean       = responseFit.GetParameter(1)
    meanError  = responseFit.GetParError(1)

    #now we need to judge the quality o the fitted guassians for the response 
    if responseFit.GetNDF() == 0:
      chi2 = max_chi2 + 1
    else:
      chi2 = responseFit.GetChisquare() / responseFit.GetNDF()
    if chi2 > max_chi2:
      mean = hist.GetMean()
      meanError  = hist.GetMeanError()

    #JMR is defined as IQR/2/Median
    nq = 3
    a  = 0.5 - width/2.
    quantiles = array('d', [0.] * nq)
    xq = array('d', [a, 0.5, 1.0 - a])
    hist.GetQuantiles(3, quantiles, xq);
    IQR    = quantiles[2] - quantiles[0]
    median = quantiles[1]

    bin_size = hist.GetBinLowEdge(2) - hist.GetBinLowEdge(1)
    if hist.Integral() == 0:
      return mean, meanError, IQR / 2., median, 0, 0, 0
    f_16       = hist.GetBinContent( hist.FindBin( quantiles[0] ) )/bin_size/hist.Integral()
    f_84       = hist.GetBinContent( hist.FindBin( quantiles[2] ) )/bin_size/hist.Integral()
    sigmaError=0
    if f_16 != 0 and f_84 != 0:
      sigmaError = sqrt( a*(1-a)/hist.GetEffectiveEntries())*sqrt( pow(1./f_16,2)  + pow(1./f_84,2))
    norm = responseFit.GetParameter(0)
    resolution = responseFit.GetParameter(2)

    return mean, meanError, IQR/2., median, sigmaError, norm, resolution




def GetResponseFit(hist):
  #Fit with gaussian
  myFit =  r.TF1("myFit","gaus",-5,5)
  #myFit =  r.TF1("myFit","gaus",0,3.)
  myFit.SetParameter(1,1)
  myFit.SetParameter(2,0.2)

  #myFit.SetRange(mean-1.5*sigma, mean+1.5*sigma)
  hist.Fit("myFit","RQ0")
  mean  = myFit.GetParameter(1)
  sigma = myFit.GetParameter(2)
  meanError  = myFit.GetParError(1)
  sigmaError = myFit.GetParError(2)

  # extract the mean and one sigam 
  hist.Fit("myFit","RQ0", "", mean-2*sigma, mean+2*sigma)

  for i in range(2):
    mean  = myFit.GetParameter(1)
    sigma = myFit.GetParameter(2)
    myFit.SetParameter(1, mean)
    myFit.SetParameter(2, sigma)
    myFit.SetParLimits(1, mean-2*sigma, mean+2*sigma)
    myFit.SetParLimits(2, 0.2*sigma, 4*sigma)
    hist.Fit("myFit","RQ0", "", mean-1.5*sigma, mean+1.5*sigma)
    #hist.Fit("myFit","RQ0", "", mean-2.0*sigma, mean+2.0*sigma)
  mean  = myFit.GetParameter(1)
  sigma = myFit.GetParameter(2)
  meanError  = myFit.GetParError(1)
  sigmaError = myFit.GetParError(2)

  return myFit, mean, sigma, meanError, sigmaError
    


