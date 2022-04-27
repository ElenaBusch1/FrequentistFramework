#!/usr/bin/env python
import array
import subprocess, os, sys, argparse
from condor_handler import CondorHandler
from ROOT import *
sys.path.append("config/dijetTLA/")
from InitialParameters import initialParameters

gROOT.LoadMacro("atlasstyle-00-04-02/AtlasLabels.C")
gROOT.LoadMacro("atlasstyle-00-04-02/AtlasStyle.C")
gROOT.LoadMacro("atlasstyle-00-04-02/AtlasUtils.C")

SetAtlasStyle()

# First attempt of SWiFT fit:
# quickFit currently works on 1 GeV bins
# whw: referred to resolution bins
# Example: whw=3 means I will fit in a range starting from three resolution bins before 
# and extending for another three resolution bins after the resolution bin in which I want
# to evaluate the fit. This means that all 1 GeV bins in the resolution bin in which I want 
# to evaluate the fit, will correspond to the *same* fit.

# This code basically runs run_anaFit.py in different fitting ranges.
# we run PostFit extraction after that
# and we pick up results and stitch them together

# Specify spectrum edge strategy
# See page 71 https://cds.cern.ch/record/2226514/files/ATL-COM-PHYS-2016-1498.pdf

# fixLow: at the low end of the spectrum, we alway keep the same amount of bins.
# for example if WHW=3, the first 4 bins are evaluated from the same fit, because it is the 
# window. Only then does the window shift one bin to the right. If false, then the only constraint
# is to have at most WHW to the left of bin to evaluate, meaning that the actual size of the window
# gets smaller as we reach the bottom edge. 

# truncateRight: means that we don't consider bins beyond the analysis fitting range in the windows for 
# for the final bins. If we truncate, we can have fixHigh=0,1, considering the same edge effects as for 
# the bottom edge of the spectrum. If we don't truncate then that means that for the final bins in the 
# fitting range we consider bins beyond the fitting range inside the window.

################################# CHECK THIS ##########################

# Condor or local/lxplus?
useBatch = False
# Execute or printout commands?
quietMode = False

# Specs
trigger = "J100"
dataset = 'partialDataset'  # 'full', 'partialDataset', 'TLA2016'

# SWiFt specs:
WHW = 10 #22
fixLow = 1
truncateRight = 0
fixHigh = 0
# Use previous window to initialize nbkg parameter:
doReadPreviousFit = True

# Output folder -- where everything is stored:
# default in python/run_anaFit.py is run/
outFolder = "run/PartialDatasets/"+trigger+"/Swift_WHW{0}_fixLow{1}_TR{2}_fixHigh{3}_3par_halvedResBins_260422/".format(WHW,fixLow, truncateRight, fixHigh)

# whole fitting range:
analysisRange = [ 
  initialParameters[dataset][trigger]['low'],
  initialParameters[dataset][trigger]['high'] 
]

# Datafile:
datafile =  initialParameters[dataset][trigger]['datafile']
datahist =  initialParameters[dataset][trigger]['datahist']
nbkg	   = initialParameters[dataset][trigger]['nbkg']

# Provide resolution bins:
#resolutionBinsFile = "Input/data/dijetTLAnlo/binning2021/data_J100yStar06_range171_3217.root"
resolutionBinsFile = None
#resolutionBinsHisto = "data"

# halving resolution bins:
binEdges = [171.0, 180.0, 188.0, 197.0, 206.0, 215.0, 224.0, 234.0, 243.0, 253.0, 262.0, 272.0, 282.0, 292.0, 302.0, 313.0, 323.0, 334.0, 344.0, 355.0, 365.0, 376.0, 387.0, 399.0, 410.0, 422.0, 433.0, 445.0, 457.0, 469.0, 481.0, 494.0, 506.0, 519.0, 531.0, 544.0, 556.0, 569.0, 582.0, 595.0, 608.0, 622.0, 635.0, 649.0, 662.0, 676.0, 690.0, 705.0, 719.0, 734.0, 748.0, 763.0, 778.0, 793.0, 808.0, 824.0, 839.0, 855.0, 871.0, 887.0, 903.0, 920.0, 936.0, 953.0, 970.0, 987.0, 1004.0, 1022.0, 1039.0, 1057.0, 1075.0, 1093.0, 1111.0, 1130.0, 1148.0, 1167.0, 1186.0, 1206.0, 1225.0, 1245.0, 1264.0, 1284.0, 1304.0, 1325.0, 1345.0, 1366.0, 1387.0, 1408.0, 1429.0, 1451.0, 1472.0, 1494.0, 1516.0, 1539.0, 1561.0, 1584.0, 1607.0, 1631.0, 1654.0, 1678.0, 1701.0, 1725.0, 1749.0, 1774.0, 1798.0, 1823.0, 1848.0, 1874.0, 1899.0, 1925.0, 1951.0, 1978.0, 2004.0, 2031.0, 2058.0, 2086.0, 2113.0, 2141.0, 2169.0, 2198.0, 2226.0, 2255.0, 2284.0, 2314.0, 2343.0, 2373.0, 2403.0, 2434.0, 2464.0, 2495.0, 2526.0, 2558.0, 2590.0, 2623.0, 2655.0, 2688.0, 2721.0, 2755.0, 2788.0, 2822.0, 2856.0, 2891.0, 2926.0, 2962.0, 2997.0, 3033.0, 3069.0, 3106.0, 3142.0, 3180.0, 3217.0]

# xml template cards:
topfile 	= "config/dijetTLA/dijetTLA_J100yStar06_zprime.template"
categoryfile 	= "config/dijetTLA/category_dijetTLA_zprime.template"
backgroundfile 	= "config/dijetTLA/background_dijetTLA_J100yStar06_threePar.xml"

# brackets for fit number:
wsfile = "dijetTLA_combWS_swift_ibin{0}_{1}_{2}.root"
outputfile = "FitResult_threePar_J100yStar_bOnly_ibin{0}_{1}_{2}.root"

# Signal:
# dummy: it's a b-only fit, for now
sigmean = 1000
sigwidth = -999

##########################################################################

############ styling and setup
gStyle.SetOptStat(0)
gErrorIgnoreLevel = kWarning
# Always do batch mode!
gROOT.SetBatch(True)
gStyle.SetOptTitle(0)

############ Create output folder:

# local or Condor, everything will be stored here:
if not os.path.isdir(outFolder):
  subprocess.call("mkdir -p " + outFolder, shell=True)

############ Prepare Condor:

if useBatch:
  # Create location of .log, .sub and .sh files:
  batch_logs = outFolder + 'logs/'
  batch_scripts = outFolder +  'jobs/'
  if not os.path.isdir(batch_logs):
    subprocess.call("mkdir -p " + batch_logs, shell=True)
  if not os.path.isdir(batch_scripts):
    subprocess.call("mkdir -p " + batch_scripts, shell=True)

  # Prepare the handler:
  batchmanager = CondorHandler( batch_logs, batch_scripts)
  folder = 'output/'

else:
  
  folder = outFolder

##############################

wsfile = folder + wsfile
outputfile = folder + outputfile

###############################
#FIXME Este resiudals se podria sacar
def computeResiduals(data, fit, histoName="residuals"):
    h = fit.Clone(histoName)
    h.SetDirectory(0)
    h.Reset("M")
    
    for ibin in range(1, fit.GetNbinsX()+1):
        valueErrorData = data.GetBinError(ibin)
        valueData = data.GetBinContent(ibin)
        valueFit = fit.GetBinContent(ibin)

        binSig = 0.
        if valueErrorData > 0. and valueFit > 0.:
            binSig = (valueData - valueFit)/ valueErrorData
            h.SetBinContent(ibin, binSig)
            h.SetBinError(ibin, 0)
    
    return h

def update_nbkg(outputfile, i, low, high):
  paramsFileName = outputfile.format(i, low, high).replace("FitResult", "FitParameters")
  paramsFile = TFile(paramsFileName, 'read')
  paramsHisto = paramsFile.Get("postfit_params")
  for p in range(1,paramsHisto.GetNbinsX()+1):
    if paramsHisto.GetXaxis().GetBinLabel(p) == "nbkg":
      updated_Nbkg = str(round(paramsHisto.GetBinContent(p)))
      # print updated_Nbkg
      previous_Nbkg = nbkg.split(",")
      previous_Nbkg[0] = updated_Nbkg
      # print previous_Nbkg
      new_nbkg = ','.join(previous_Nbkg)
      print "Updated nbkg: {}".format(nbkg)
  paramsFile.Close()
  return new_nbkg


############# Prepare Commands:

# No BH, no rebinning

command = "python python/run_anaFit.py --datafile {0} --datahist {1} --topfile {2} --categoryfile {3} --wsfile {4} --outputfile {5} --nbkg {6} --rangelow {7} --rangehigh {8} --sigmean {9} --sigwidth {10} --folder {11} --backgroundfile {12} --notrebin --maskthreshold 1e-8"

# IMPORTANT: assuming resolution bins range is equal to or larger than data binning
# 1) Retrieve resolution bins:
if resolutionBinsFile:
  resFile = TFile(resolutionBinsFile, 'read')
  resHisto = resFile.Get(resolutionBinsHisto)
  binEdges = [ resHisto.GetBinLowEdge(i) for i in range(1, resHisto.GetNbinsX() + 2) ]
else:
  try:
    len(binEdges)
  except:
    print "Need to provide binEdges as a list"
    sys.exit()

resBins = array.array( 'd', binEdges )
# print "Resolution bins are:", resBins

binsToFit = []
for ibin, binEdge in enumerate(resBins):
  if binEdge >= analysisRange[0] and binEdge<= analysisRange[1]:
    binsToFit.append(ibin+1)
binsToFit.pop()

firstBinToFit = binsToFit[0]
lastBinToFit  = binsToFit[-1]

# 2) For plotting window cross check:
ybins = array.array('d',range(1, len(binsToFit)+2))
# Easier handling of bins and bin edges:
swiftCheck = TH2D("Swift_Range",";mjj [GeV];iteration;",len(resBins)-1,resBins,len(binsToFit), ybins)
# Nice plot for window visualization -- annoying to handle bins:
swiftPoly  = TH2Poly()
swiftPoly.SetNameTitle("swiftPoly",";mjj [GeV];iteration")
for ix in range(0, len(resBins)-1):
    xval1 = resBins[ix]
    xval2 = resBins[ix+1]
    for iy in range(1, len(binsToFit)+1):
        yval1 = iy
        yval2 = iy + 1
        swiftPoly.AddBin(xval1, yval1, xval2, yval2)

print "Analysis range requested:", analysisRange
print "Range determined by resolution bin edges: {0}-{1}".format( swiftCheck.GetXaxis().GetBinLowEdge(firstBinToFit), swiftCheck.GetXaxis().GetBinUpEdge(lastBinToFit))

# 3) Determine fit range from sliding window:

# for tomography plot
tomo_graph = TGraphAsymmErrors()
k = 0

# to first order it's one fit per resolution bin
# -- FIXME not really though, repeating fits :/ :

for i in range(firstBinToFit, lastBinToFit+1):
  
  j = i - firstBinToFit + 1
  
  # i is the bin to fit -- let's paint it with a 2
  swiftCheck.SetBinContent(i,j, 2)
  swiftPoly.Fill( swiftCheck.GetXaxis().GetBinCenter(i), swiftCheck.GetYaxis().GetBinCenter(j), 2)
  
  #
  # now let's decide the window:
  ##################################

  # 1) what happens low edge of spectrum:
  if ( (i-firstBinToFit + 1) - WHW ) <= 0 :
    # window starts at the bottom
    lowBin = firstBinToFit 
    if fixLow:
      # stable size
      upBin = 2*WHW + firstBinToFit
    else:
      # increasing size to full size
      upBin = i + WHW
  
  # center part of the spectrum:
  elif ( i + WHW ) <= lastBinToFit :
    lowBin = i - WHW
    upBin = i + WHW
    lastLowBin = lowBin
    lastUpBin = upBin
  else:
    # upper edge of the spectrum
    if truncateRight:
      # two options:
      if fixHigh:
        # keep same windows as the last one from the center:
        # stable window size
        upBin= lastUpBin
        lowBin = lastLowBin
      else:
        # window size gets smaller as we reach the end:
        upBin = lastUpBin
        lowBin = i-WHW
    else:
      # windows can extend beyond the analysis Range:
      lowBin = i-WHW
      # check that there are enough bins beyond the analysis
      # range to extend the window:
      bins_to_the_right = swiftCheck.GetXaxis().GetNbins() - i
      if abs(bins_to_the_right) < WHW:
        upBin = swiftCheck.GetXaxis().GetNbins()
      else:
          upBin = i + WHW
  for r in range(lowBin, upBin+1):
      if r != i:  
        swiftCheck.SetBinContent(r,j,1)
        swiftPoly.Fill( swiftCheck.GetXaxis().GetBinCenter(r), swiftCheck.GetYaxis().GetBinCenter(j), 1)
 
  # FIXME Assumes bin edges are INTs -- same as run_anaFit.py
  low =  int(swiftCheck.GetXaxis().GetBinLowEdge(lowBin))
  high = int(swiftCheck.GetXaxis().GetBinUpEdge(upBin)) 
  
  print "Preparing fit for window #{0} with fitting range ({1},{2})".format(i,low, high)
  thisCommand =  command.format(datafile, datahist, topfile, categoryfile, wsfile.format(i,low, high), outputfile.format(i,low,high), nbkg, low, high, sigmean, sigwidth, folder, backgroundfile) 
  print thisCommand
  
  # Submit the Jobs! -- al sequential for now
  if not quietMode:
    if not useBatch:
      subprocess.call(thisCommand, shell=True)
      # Fitting done, now let's retrieve nbkg estimation to
      if doReadPreviousFit:
	# initialize next window fit!
	nbkg = update_nbkg( outputfile, i, low, high)
      
      # retrieve window pvalue
      postfitFileName = outputfile.format(i,low,high).replace("FitResult","PostFit")
      postfitFile = TFile( postfitFileName, 'read')
      this_pvalue = postfitFile.Get("chi2").GetBinContent(6)
      postfitFile.Close()
      tomo_graph.SetPoint(k, swiftCheck.GetXaxis().GetBinCenter(i), this_pvalue)
      tomo_graph.SetPointEXlow(k, swiftCheck.GetXaxis().GetBinCenter(i) - low)
      tomo_graph.SetPointEXhigh(k,high - swiftCheck.GetXaxis().GetBinCenter(i))
      k+=1

  print " "

# Save cross check windows plot:
outputFile = TFile( outFolder + "/swiftCrossCheck.root",'recreate')
outputFile.cd()
swiftCheck.Write()
swiftPoly.Write()
tomo_graph.SetLineWidth(2)
tomo_graph.SetMarkerStyle(1)
tomo_graph.SetNameTitle("swift_tomography","SWiFt tomography; mjj [GeV]; window p-value")
tomo_graph.Write()
outputFile.Close()

canvas = TCanvas()
gStyle.SetPalette(kRainBow)
swiftPoly.GetXaxis().SetTitle("m_{jj} [GeV]")
swiftPoly.GetYaxis().SetTitle("SWiFt Iteration")
swiftPoly.Draw("COL0 L")
myText(0.2, 0.90, 1, "fixLow = {}".format(fixLow), 12)
myText(0.2, 0.85, 1, "truncateRight = {}".format(truncateRight), 12)
myText(0.2, 0.80, 1, "fixHigh = {}".format(fixHigh), 12)

canvas.Print( outFolder + "/swiftCrossCheck.png")

canvas.Clear()
canvas.SetLogy()
canvas.SetGrid()
tomo_graph.SetMinimum(0.001)
tomo_graph.Draw("AP")
line = TLine(457, 0.01, 2997, 0.01)
line.SetLineStyle(2)
line.SetLineWidth(2)
line.SetLineColor(kRed)
line.Draw("same")
canvas.Print( outFolder + "/swiftTomographyPlot.png")

