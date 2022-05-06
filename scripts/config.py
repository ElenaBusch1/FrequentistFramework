cdir="/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest"
nToys = 500
atlasLabel="Simulation Internal"

cSample = "testSherpa"
cRangeLow = 200
cRangeHigh = 1200
cPDFitName = "sixPar"
cFitName = "fivePar"
#cSignal = "test3_NoCut"
#cSignal = "test3_inverted"
#cSignal = "test3_inverted_some"
#cSignal = "test3"
#cSignal = "test3_some"
#cSignal = "test3_NoCut_some"
cSignal = "Gaussian"
cSignalMasses = [250, 350, 450, 550, 650]


ambulanceSample = "ambulance_4j"
ambulanceRangeLow = 2000
ambulanceRangeHigh = 9000
ambulancePDFitName = "fiveParAmb"
ambulanceFitName = "fourParAmb"
ambulanceSignal = "Gaussian"


#####################################################################################
# Input mjj distributions
#####################################################################################
samples = {}


samples["test3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7.root",
                 "histname": "BkgLow_12_SR1",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "rangelow" : 200,
                 "rangehigh" : 1200,
               }



samples["test_cut15"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "rangelow" : 200,
                 "rangehigh" : 1200,
               }

samples["testSherpa"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/sherpaTest.root",
                 "histname": "SigLow_SR2_reweighted_cut_12",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "Sherpa",
                 "rangelow" : 200,
                 "rangehigh" : 1200,
               }



samples["mj2j3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/backgroundValidation_Basic.root",
                 "histname": "mjj_32",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "rangelow" : 200,
                 "rangehigh" : 1200,
               }

samples["mjjmin"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/backgroundValidation_Basic.root",
                 "histname": "mjj_low",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "rangelow" : 200,
                 "rangehigh" : 1200,
               }


samples["mjjmindphi"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/backgroundValidation_Basic.root",
                 "histname": "mjj_dphiLow",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "rangelow" : 200,
                 "rangehigh" : 1200,
               }





samples["test3_DNN"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7_JZ4_0.root",
                 "histname": "BkgLow_12_SR2",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
               }


samples["ambulance_4j"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h1_resonance_rjet_m4j_nominal",
                 "lumi": 139000,
                 "varName": "m_{4j}",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["ambulance_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["ambulance_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["ambulance_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["ambulance_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["ambulance_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["ambulance_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["ambulance_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }


samples["ambulance_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["ambulance_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["ambulance_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["ambulance_2javg"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/ambulances/testOutputAutomatic.root",
                 "histname": "h1_resonance_rjet_m2javg_nominal",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "rangelow" : 500,
                 "rangehigh" : 3000,
                 "legend": "PYTHIA8",
               }






samples["Btagged70_23_ystar"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "histname": "Bkg_mj2j3_ystar",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_pullvar_btagging_70.root",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
               }


samples["Btagged70_jj_ystar"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "histname": "Bkg_mjj_ystar",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_pullvar_btagging_70.root",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
               }


samples["Btagged70_23"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "histname": "Bkg_mj2j3",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_pullvar_btagging_70.root",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
               }


samples["Btagged70_jj"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "histname": "Bkg_mjj",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_pullvar_btagging_70.root",
                 "lumi": 139000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
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

signals["test3_15"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal15_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/scripts/massSpectraWithSysts_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN_mR_histFactoryWS.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal15_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histname": "SigLowAllNorm_15_SR1_tagged",
               }

signals["test3_some"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_some_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/scripts/massSpectraWithSysts_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN_mR_histFactoryWS.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_some_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histname": "SigLowNorm_12_SR1_tagged",
               }


signals["test3_NoCut_some"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_nocut_some_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_nocut_some_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histname": "SigLowNorm_0_SR1_tagged",
               }



signals["test3_NoCut"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_nocut_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_nocut_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histname": "SigLowAllNorm_0_SR1_tagged",
               }

signals["test3_inverted"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_inverted_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_inverted_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histname": "SigLowAllNorm_12_SR2_tagged",
               }


signals["test3_inverted_some"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_inverted_some_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_inverted_some_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histname": "SigLowNorm_12_SR2_tagged",
               }


# Generic gaussian distribution
signals["Gaussian"] = {
                 "signalfile"  : "../config/dijetISR/signalGauss_meanM_widthW.xml",
                 "workspacefile": "",
                 "templatefile"  : "",
                 "histname": "",
               }



# Generic gaussian distribution
signals["Poisson"] = {
                 "signalfile"  : "../config/dijetISR/signalPoisson_meanM_widthW.xml",
                 "workspacefile": "",
                 "templatefile"  : "",
                 "histname": "",
               }






#####################################################################################
# Fit functions
#####################################################################################
fitFunctions = {}

fitFunctions["threePar"] = { 
                            "Name" : "3-par fit",
                            "Config" : "config/background_threePar.xml",
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

fitFunctions["threeParAmb"] = {
                            "Name" : "3-par fit",
                            "Config" : "config/background_threeParAmb.xml",
                          }

fitFunctions["fourParAmb"] = {
                            "Name" : "4-par fit",
                            "Config" : "config/background_fourParAmb.xml",
                          }

fitFunctions["fiveParAmb"] = {
                            "Name" : "5-par fit",
                            "Config" : "config/background_fiveParAmb.xml",
                          }

fitFunctions["fiveParAmbMod"] = {
                            "Name" : "5-par fit",
                            "Config" : "config/background_fiveParAmbMod.xml",
                          }
fitFunctions["fiveParAmbPow"] = {
                            "Name" : "5-par fit",
                            "Config" : "config/background_fiveParAmbPow.xml",
                          }

fitFunctions["sixParAmb"] = {
                            "Name" : "6-par fit",
                            "Config" : "config/background_sixParAmb.xml",
                          }


fitFunctions["sevenPar"] = {
                            "Name" : "7-par fit",
                            "Config" : "config/background_sevenPar.xml",
                          }

fitFunctions["UA2"] = { 
                            "Name" : "UA2 fit",
                            "Config" : "config/background_UA2.xml",
                          }

fitFunctions["fiveParV2"] = {
                            "Name" : "5-par fit, v2",
                            "Config" : "config/background_fiveParV2.xml",
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
     


