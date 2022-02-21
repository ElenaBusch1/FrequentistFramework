cdir="/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest"
nToys = 1000
atlasLabel="Simulation Internal"

cSample = "PtOrdered6"
cRangeLow = 200
cRangeHigh = 900
cPDFitName = "fivePar"
cFitName = "fourPar"
#cPDFitName = "sixPar"
#cFitName = "fivePar"
cSignal = "Gaussian"
#cSignal = "PtOrdered6"


#####################################################################################
# Input mjj distributions
#####################################################################################
samples = {}

samples["PtOrdered"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_2_alpha100_SR1",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_test_SRAlpha_100_BkgAlpha_100_dimVars_pt_cutVal_7.root",
                 "lumi": 139000,
               }

samples["PtOrdered5"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_SR1",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_decorr2_SRAlpha_200_BkgAlpha_200_dimVars_pt_cutVal_5.root",
                 "lumi": 139000,
               }



samples["PtOrdered5Tagged"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_2_SR1_tagged",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_decorr2_SRAlpha_200_BkgAlpha_200_dimVars_pt_cutVal_5.root",
                 "lumi": 139000,
               }

samples["PtOrdered6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "histname": "BkgLow_SR1",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_decorr2_SRAlpha_200_BkgAlpha_200_dimVars_pt_cutVal_6.root",
                 "lumi": 139000,
               }



#####################################################################################
# Signals
#####################################################################################
signals = {}

# Signal template (can include systematics)
signals["PtOrdered6"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/Input/signal/HistFactory_dijetISR_mRMEAN.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_decorr2_SRAlpha_200_BkgAlpha_200_dimVars_pt_cutVal_6_MEAN.root",
                 "histname": "SigLow_1_alpha200_SR1",
               }

# Generic gaussian distribution
signals["Gaussian"] = {
                 "signalfile"  : "../config/dijetISR/signalGauss_meanM_widthW.xml",
                 "workspacefile": "",
                 "templatefile"  : "",
                 "histname": "",
               }






#####################################################################################
# Fit functions
#####################################################################################
fitFunctions = {}
fitFunctions["sixPar"] = {
                            "Name" : "6-par fit",
                            "Config" : "config/background_sixPar.xml",
                          }
fitFunctions["fivePar"] = {
                            "Name" : "5-par fit",
                            "Config" : "config/background_fivePar.xml",
                          }


fitFunctions["fiveParV2"] = {
                            "Name" : "5-par fit",
                            "Config" : "dijetISR/background_ajj_simpleTrig_yStar0p825_fiveParV2.xml",
                          }

fitFunctions["fiveParV3"] = {
                            "Name" : "5-par fit",
                            "Config" : "dijetISR/background_ajj_simpleTrig_yStar0p825_fiveParV3.xml",
                          }

fitFunctions["fourPar"] = { 
                            "Name" : "4-par fit",
                            "Config" : "config/background_fourPar.xml",
                          }


def getFileName(prefix, directory, channelName, rangelow, rangehigh, sigmean=0, sigwidth=0, sigamp=0):
  if sigmean:
    return "%s/%s/%s_Fit_%d_%d_Mean_%d_Width_%d_Amp_%d"%(directory, channelName, prefix, rangelow, rangehigh, sigmean, sigwidth, sigamp)
  else:
    return "%s/%s/%s_Fit_%d_%d"%(directory, channelName, prefix, rangelow, rangehigh)


def getBinning(rangelow, rangehigh, delta=25):
  bins = []
  for i in range(rangelow, rangehigh, delta):
    bins.append(i)
  bins.append(rangehigh)
  return bins
     


