#!/usr/bin/env python
import ROOT
import array
import subprocess, os, sys, argparse
from condor_handler import CondorHandler

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
useBatch = True
# Execute or printout commands?
quiteMode = True
# None: submit all fits sequentially, or doNJobs fits per submission
doNJobs = 10 # not implemented yet

WHW = 3
fixLow = 1
truncateRight = 0
fixHigh = 0

# Datafile:
datafile = "Input/data/dijetTLA/lookInsideTheBoxWithUniformMjj.root"
datahist = "Nominal/DSJ100yStar06_TriggerJets_J100_yStar06_mjj_finebinned_all_data"
nbkg = "2E8,0,3E8"

# whole fitting range:
analysisRange = [ 531, 2997 ]

# Provide resolution bins:
resolutionBinsFile = "/home/mariana/Nube/TLA/FrequentistFramework/Input/data/dijetTLAnlo/data_J100yStar06_range171_3217.root"
resolutionBinsHisto = "data"

# xml template cards:
topfile = "config/dijetTLA/dijetTLA_J100yStar06_zprime.template"
# reminder: category file points to which bkg fitting function!
categoryfile = "config/dijetTLA/category_dijetTLA_J100yStar06_fivePar_zprime.template"

# Output folder -- where everything is stored:
# default in python/run_anaFit.py is run/
outFolder = "run/SWiFt_14022022/"

# brackets for fit number:
wsfile = "dijetTLA_combWS_swift_{}.root"
outputfile = "FitResult_fivePar_J100yStar_bOnly_{}.root"

# Signal:
# dummy: it's a b-only fit, for now
sigmean = 'bOnly'
sigwidth = -999

##########################################################################

############ styling and setup
ROOT.gStyle.SetOptStat(0)
ROOT.gErrorIgnoreLevel = ROOT.kWarning
# Always do batch mode!
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptTitle(0)

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

############# Prepare Commands:
command = "python python/run_anaFit.py --datafile {0} --datahist {1} --topfile {2} --categoryfile {3} --wsfile {4} --outputfile {5} --nbkg {6} --rangelow {7} --rangehigh {8} --sigmean {9} --sigwidth {10} --folder {11}"

# IMPORTANT: assuming resolution bins range is equal to or larger than data binning
# 1) Retrieve resolution bins:
resFile = ROOT.TFile(resolutionBinsFile, 'read')
resHisto = resFile.Get(resolutionBinsHisto)
resBins = array.array('d',[ resHisto.GetBinLowEdge(i) for i in range(1, resHisto.GetNbinsX() + 2) ])
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
swiftCheck = ROOT.TH2D("Swift_Range","",len(resBins)-1,resBins,len(binsToFit), ybins)
# Nice plot for window visualization -- annoying to handle bins:
swiftPoly  = ROOT.TH2Poly()
swiftPoly.SetName("swiftPoly")
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

# to first order it's one fit per resolution bin
# -- FIXME not really though:
for i in range(firstBinToFit, lastBinToFit+1):
  j = i - firstBinToFit + 1
  
  # i is the bin to fit -- let's paint it with a 2
  outputfile.format(i)
  wsfile.format(i)
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
      bins_to_the_right = swiftCheck.GetXaxis().GetNbins() - lastBinToFit
      if abs(bins_to_the_right) < WHW:
        upBin = swiftCheck.GetXaxis().GetNbins()
      else:
          upBin = i + WHW
  for r in range(lowBin, upBin+1):
      if r != i:  
        swiftCheck.SetBinContent(r,j,1)
        swiftPoly.Fill( swiftCheck.GetXaxis().GetBinCenter(r), swiftCheck.GetYaxis().GetBinCenter(j), 1)
 
  low = swiftCheck.GetXaxis().GetBinLowEdge(lowBin)
  high = swiftCheck.GetXaxis().GetBinUpEdge(upBin) 
  
  print "Submitting fit for window #{0} with fitting range ({1},{2})".format(j,low, high)
  thisCommand =  command.format(datafile, datahist, topfile, categoryfile, wsfile, outputfile, nbkg, low, high, sigmean, sigwidth, folder) 
  commands.append( thisCommand )
  print thisCommand


# Save cross check windows plot:
outputFile = ROOT.TFile( outFolder + "/swiftCrossCheck.root",'recreate')
outputFile.cd()
swiftCheck.Write()
swiftPoly.Write()
outputFile.Close()

canvas = ROOT.TCanvas()
canvas.SetGrayScale()
swiftPoly.GetXaxis().SetTitle("m_{jj} [GeV]")
swiftPoly.GetYaxis().SetTitle("SWiFt Iteration")
swiftPoly.Draw("COL0 L")
canvas.Print( outFolder + "/swiftCrossCheck.png")

# Submit the Jobs! -- al sequential for now
if not quietMode:
  if not useBatch:
    for c in commands:
      subprocess.call(c, shell=True)
  else:
    run_command = '\n'.join(commands) + '\n'
    batchmanager.send_job( run_command, outFolder )

# We got some stitching up to do now:


