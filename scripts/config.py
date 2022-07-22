cdir="/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework"
nToys = 500
atlasLabel="Simulation Internal"

cSample = "fitsNixon"
#cPDFitName = "fourPar"
#cFitName = "threePar"
cPDFitName = "fivePar"
cFitName = "fourPar"
cSignal = "Gaussian"
cChannelNames = ["nixon_4j_alpha0", "nixon_4j_alpha1", "nixon_4j_alpha2", "nixon_4j_alpha3", "nixon_4j_alpha4", "nixon_4j_alpha5", "nixon_4j_alpha6", "nixon_4j_alpha7", "nixon_4j_alpha8", "nixon_4j_alpha9"]
cSignalMasses = [2000,3000,4000,5000,6000,7000,8000,9000]



#####################################################################################
# Input mjj distributions
#####################################################################################
samples = {}

#samples["ambulance_4j_alpha0"] = {
#                 "categoryfile"  : "../config/category_background.template",
#                 "topfile": "../config/background.template",
#                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
#                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
#                 "lumi": 139000,
#                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
#                 "rangelow" : 1500,
#                 "rangehigh" : 9000,
#                 "legend": "PYTHIA8",
#               }


#samples["nixon_4j_alpha8_MCErr"] = {
#                 "categoryfile"  : "../config/category_background.template",
#                 "topfile": "../config/background.template",
#                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
#                 "histname": "h2_resonance_jet_m4j_alpha_nominal_MCErr_alphaBin_8",
#                 "lumi": 139000,
#                 "varName": "m_{4j}, 0.28 < #alpha",
#                 "rangelow" : 2000,
#                 "rangehigh" : 2200,
#                 "legend": "PYTHIA8",
#               }


samples["nixon_4j_alpha12"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_12",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.34 < #alpha",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.34 < #alpha",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["nixon_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["nixon_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }


samples["nixon_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["nixon_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["nixon_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["nixon_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }



samples["nixon_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }



samples["nixon_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }

samples["nixon_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }



samples["nixon_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }



samples["nixon_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }


samples["nixon_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "histname1": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "histname2": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }



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
                 "signalfile"  : "../config/signalGauss_meanM_widthW.xml",
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



def getFileName(prefix, directory, channelName, groupedName, sigmean=0, sigwidth=0, sigamp=0):
  if sigmean:
    if(channelName):
      return "%s/%s/%s_%s_Mean_%d_Width_%d_Amp_%d"%(directory, groupedName, prefix, channelName, sigmean, sigwidth, sigamp)
    else:
      return "%s/%s/%s_CHANNEL_Mean_%d_Width_%d_Amp_%d"%(directory, groupedName, prefix, sigmean, sigwidth, sigamp)
  else:
    if(channelName):
      return "%s/%s/%s_%s"%(directory, groupedName, prefix, channelName)
    else:
      return "%s/%s/%s_CHANNEL"%(directory, groupedName, prefix)


def getBinning(rangelow, rangehigh, delta=25):
  bins = []
  for i in range(rangelow, rangehigh, delta):
    bins.append(i)
  bins.append(rangehigh)
  return bins
     


