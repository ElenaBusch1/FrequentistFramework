cdir="/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest"
nToys = 500
atlasLabel="Simulation Internal"

cSample = "test3"
cRangeLow = 200
cRangeHigh = 1200
cPDFitName = "sixPar"
cFitName = "fivePar"
cSignal = "Gaussian"


#####################################################################################
# Input mjj distributions
#####################################################################################
samples = {}


samples["Example"] = {
                 "categoryfile"  : "../config/category_background.template", # Config files for the background
                 "topfile": "../config/background.template",                 # Config files for the background
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7.root", # The root file with the bkg distribution
                 "histname": "BkgLow_12_SR1", # The name of the histogram with the background distribution
                 "lumi": 139000,      # The luminosity (in pb), used for plot labels
                 "varName": "m_{jj}", # The x-axis name, just for plotting
                 "legend": "PYTHIA8", # This way, we don't write that everything is data, even when it's simulation
                 "rangelow" : 200,  # Note: these should be set after running generic_anaFit.py, and determining the fit range you want to use.
                 "rangehigh" : 1200,
               }


#####################################################################################
# Signals
#####################################################################################
signals = {}

# Signal template (can include systematics)
signals["test3"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/scripts/massSpectraWithSysts_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN_mR_histFactoryWS.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histname": "SigLowAllNorm_12_SR1_tagged",
               }


# Generic gaussian distribution
signals["Gaussian"] = {
                 "signalfile"  : "../config/dijetISR/signalGauss_meanM_widthW.xml",
                 "workspacefile": "", # These are left empty, since we generate the gaussian distribution.
                 "templatefile"  : "", # These are left empty, since we generate the gaussian distribution.
                 "histname": "", # These are left empty, since we generate the gaussian distribution.
               }




#####################################################################################
# Fit functions
#####################################################################################
fitFunctions = {}

fitFunctions["threePar"] = { 
                            "Name" : "3-par fit", # A human readable name, drawn on plots
                            "Config" : "config/background_threePar.xml", # The xml file with the fit function
                          }

fitFunctions["fourPar"] = { 
                            "Name" : "4-par fit",
                            "Config" : "config/background_fourPar.xml",
                          }

fitFunctions["fivePar"] = {
                            "Name" : "5-par fit",
                            "Config" : "config/background_fivePar.xml",
                          }

fitFunctions["sixPar"] = {
                            "Name" : "6-par fit",
                            "Config" : "config/background_sixPar.xml",
                          }

fitFunctions["UA2"] = { 
                            "Name" : "UA2 fit",
                            "Config" : "config/background_UA2.xml",
                          }


# A generic function 
def getFileName(prefix, directory, channelName, rangelow, rangehigh, sigmean=0, sigwidth=0, sigamp=0):
  if sigmean:
    return "%s/%s/%s_Fit_%d_%d_Mean_%d_Width_%d_Amp_%d"%(directory, channelName, prefix, rangelow, rangehigh, sigmean, sigwidth, sigamp)
  else:
    return "%s/%s/%s_Fit_%d_%d"%(directory, channelName, prefix, rangelow, rangehigh)


# This is a placeholder until we have resolution binning, but this is used in a few places
# You can change it to return the binning you want
def getBinning(rangelow, rangehigh, delta=25):
  bins = []
  for i in range(rangelow, rangehigh, delta):
    bins.append(i)
  bins.append(rangehigh)
  return bins
     


