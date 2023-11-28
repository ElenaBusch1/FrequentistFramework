cdir="/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest"
nToys = 1000
atlasLabel="Simulation Internal"

cSample = "sherpaReweight"
cRangeLow = 200
cRangeHigh = 1000
cPDFitName = "sixPar"
cFitName = "fivePar"
cSignal = "Gaussian"
cSignalMasses = [250, 350, 450, 550, 650, 750, 850]



#####################################################################################
# Input mjj distributions
#####################################################################################
samples = {}



samples["test3New_15_MCEffOnData"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/plots/massSpectraMCwithDataEfficiency.root",
                 "histname": "BkgLow_15_SR1_DataWithMC",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }



samples["test3New_15_dataEff"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/plots/massSpectraMCwithDataEfficiency.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }

samples["test3New_15_dataErf"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/plots/massSpectraMCwithDataEfficiency.root",
                 "histname": "BkgLow_15_SR1_DataErf",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }

samples["test3New_15_dataErf_350"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/plots/massSpectraMCwithDataEfficiency_350.root",
                 "histname": "BkgLow_15_SR1_DataErf",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["test3New_15_dataErf_425"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/plots/massSpectraMCwithDataEfficiency_425.root",
                 "histname": "BkgLow_15_SR1_DataErf",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["test3New_15_dataErf_550"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/plots/massSpectraMCwithDataEfficiency_550.root",
                 "histname": "BkgLow_15_SR1_DataErf",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }



samples["test3New_15_MCwithMC"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/plots/massSpectraMCwithDataEfficiency.root",
                 "histname": "BkgLow_15_SR1_MCwithMC",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }

samples["test3New_15_data_mcEff"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/plots/massSpectraMCwithDataEfficiency.root",
                 "histname": "BkgLow_15_SR1_Data",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["Data17_500_25"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_sigpick2_10_SRAlpha_20_dimVarsDphi_cutVal_7_Data17_dphiLow_ptCuts_500_25.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 0,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 500 GeV, p_{T,j2} > 25 GeV, p_{T,j3} > 25 GeV",
               }


samples["Data16_500_25"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_sigpick2_10_SRAlpha_20_dimVarsDphi_cutVal_7_Data16_dphiLow_ptCuts_500_25.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 0,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 500 GeV, p_{T,j2} > 25 GeV, p_{T,j3} > 25 GeV",
               }

samples["Data_500_60"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/unblinded_500_60.root",
                 "histname": "BkgLow",
                 "lumi": 0,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 500, p_{T,j2,j3} > 60",
               }

samples["Data_475_60"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/unblinded_475_60.root",
                 "histname": "BkgLow",
                 "lumi": 0,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475, p_{T,j2,j3} > 60",
               }

samples["Data_550_25"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/unblinded_550_25.root",
                 "histname": "BkgLow",
                 "lumi": 0,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 550, p_{T,j2,j3} > 25",
               }



samples["Data16_500_40"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_sigpick2_10_SRAlpha_20_dimVarsDphi_cutVal_7_Data16_dphiLow_ptCuts_500_25.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 0,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 500, p_{T,j2,j3} > 40",
               }


samples["Data16_massAnd"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/unblindedData.root",
                 "histname": "BkgLow_m3231",
                 "lumi": 0,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV, p_{T,j2} > 40 GeV, p_{T,j3} > 40 GeV",
               }



samples["btagFinal"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/btagStudies/plots/massSpectraQCD_DL1r_77_dphiLow.root",
                 "histname": "BkgLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "#it{jbb}, Pythia",
                 "label": "p_{T,j1} > 475 GeV, 2 #it{b}-tag",
               }


samples["btag_32"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/btagStudies/plots/massSpectraQCD_DL1r_77_32.root",
                 "histname": "BkgLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Pythia, yjj",
                 "label": "p_{T,j1} > 475 GeV, 2 #it{b}-tag",
               }



samples["yjj"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/fromDavide/originalMC.root",
                 "histname": "h_orig_ajj",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Sherpa, yjj",
               }

samples["yjjPD"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/fromDavide/PseudoFromSWIFTajj_DataStat.root",
                 "histname": "h_pseudo3",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Sherpa, yjj",
               }

samples["yjjPD2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/d/dmelini/public/toJennifer/PseudoFromSWIFT_Wlarge_ajj_DataStat.root",
                 "histname": "h_pseudo3",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Sherpa, yjj",
               }


samples["FullRun2Data_NoNN"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/unblindedData.root",
                 #"inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7_Data17.root",
                 "histname": "BkgLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "#it{jjj}, p_{T,j1} > 475 GeV",
               }

samples["FullRun2Data_NoNN_No21"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/unblindedData.root",
                 #"inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7_Data17.root",
                 "histname": "BkgLow_m3231",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Data",
                 "label": "#it{jjj}, p_{T}^{j1} > 475 GeV",
               }


samples["FullRun2Data"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/unblindedData.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["FullRun2Data_cut9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/unblindedData.root",
                 "histname": "BkgLow_9_SR1",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["Data18"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/dataCrossChecks_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7_Data18_test.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               }

samples["Data17"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7_Data17_dphiLow.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["Data16"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7_Data16_test.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["Data16MCJES"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_sigpick2_10_SRAlpha_20_dimVarsDphi_cutVal_7_Data16_dphiLow_ptCuts_475_25_jet_MCJES.root",
                 "histname": "BkgLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["DataNoInsitu"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_jet_noInsitu.root",
                 "histname": "BkgLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               } 

samples["DataMCJES"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_jet_MCJES.root",
                 "histname": "BkgLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               }

samples["DataAllJES"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_jet.root",
                 "histname": "BkgLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               }




samples["Data_m32"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/unblinded_m32.root",
                 "histname": "BkgLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["Data_minMass"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/unblinded_minMass.root",
                 "histname": "BkgLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Run-2 Data",
                 "label": "p_{T,j1} > 475 GeV",
               }








samples["Data15"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7_Data15.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 3200,
                 "varName": "m_{jj}",
                 "legend": "Data 15",
                 "label": "p_{T,j1} > 475 GeV",
               }



samples["Data18Partial"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/data/massSpectraData_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7_Data18.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 3000,
                 "varName": "m_{jj}",
                 "legend": "Data 18 Period??",
                 "label": "p_{T,j1} > 475 GeV",
               }

samples["bbj_Data18Partial"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/btagStudies/massSpectra/massSpectra_Data18.root",
                 "histname": "SigMj2j3",
                 "lumi": 3000,
                 "varName": "m_{jj}",
                 "legend": "Data 18 Period??",
                 "label": "p_{T,j1} > 475 GeV, 2 #it{b}-tag",
               }

samples["bbj_Data15Partial"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/btagStudies/massSpectra/massSpectra_Data15.root",
                 "histname": "SigMj2j3",
                 "lumi": 3200,
                 "varName": "m_{jj}",
                 "legend": "Data 15",
                 "label": "p_{T,j1} > 475 GeV, 2 #it{b}-tag",
               }


samples["bbj_Data"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/btagStudies/massSpectra/unblindedData.root",
                 "histname": "SigMj2j3_3231",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Data",
                 "label": "#it{jbb}, p_{T}^{j1} > 475 GeV",
               }



samples["test3New_15"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/plots/massSpectra_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["test3New_NoCut_no21"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/plots/massSpectra_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi.root",
                 "histname": "BkgLow_3231",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "#it{jjj}, p_{T,j1} > 475 GeV",
               }




samples["testSherpa_NoCut"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/sherpa/massSpectra_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7.root",
                 "histname": "BkgLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Sherpa",
                 "label": "p_{T,j1} > 475 GeV",
               }

samples["testSherpa"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/sherpa/massSpectra_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7.root",
                 "histname": "BkgLow_12_SR1",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Sherpa",
               }

samples["testSherpa_15"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/sherpa/massSpectra_sigpick2_10_SRAlpha_20_BkgAlpha_20_dimVarsDphi_cutVal_7.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Sherpa",
                 "label": "p_{T,j1} > 475 GeV",
               }

samples["finalSherpa"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/sherpa/massSpectra_sherpa_bkg.root",
                 "histname": "BkgLow_15_SR1",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Sherpa",
                 "label": "p_{T,j1} > 475 GeV",
               }




samples["sherpaReweight"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/sherpaTest.root",
                 "histname": "SigLow_SR2_reweighted_scaled_cut_15",
                 #"histname": "SigLow_SR2_reweighted_scaled_cut_12",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "Sherpa, reweighted and rescaled",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["mj2j3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/backgroundValidation_Basic.root",
                 "histname": "mjj_32",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }

samples["mjjmin"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/backgroundValidation_Basic.root",
                 "histname": "mjj_low",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["mjjmindphi"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/backgroundValidation_Basic.root",
                 "histname": "mjj_dphiLow",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
                 "label": "p_{T,j1} > 475 GeV",
               }


samples["Btagged70_23_ystar"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "histname": "Bkg_mj2j3_ystar",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_btagging_70.root",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
               }


samples["Btagged70_jj_ystar"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "histname": "Bkg_mjj_ystar",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_pullvar_btagging_70.root",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
               }


samples["Btagged70_23"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "histname": "Bkg_mj2j3",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_btagging_70.root",
                 "lumi": 140000,
                 "varName": "m_{jj}",
                 "legend": "PYTHIA8",
               }


samples["Btagged70_jj"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "histname": "Bkg_mjj",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_pullvar_btagging_70.root",
                 "lumi": 140000,
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

signals["template"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/config/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/Signal_mX_MEAN_mY_580.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/Signal_mX_MEAN_mY_580.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/Signal_mX_MEAN_mY_580.root",
                 "histname": "h2_resonance_jet_m4j_alpha_alphaBin_9_",
               }

signals["jbbNoSysts"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template_noSysts.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/NoSystsSignal_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/scripts/NoSystsSignal_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/NoSystsSignal_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histname": "SigLowNorm_15_SR1_tagged_",
               }


signals["test3_15NoSysts"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template_noSysts.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/NoSystsSignal_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/scripts/NoSystsSignal_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/NoSystsSignal_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histname": "Morphed_m_250_",
               }

signals["test3_15"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/massSpectraWithSysts_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN_mR_histFactoryWS.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/scripts/massSpectraWithSysts_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN_mR_histFactoryWS.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/massSpectraWithSysts_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN_mR_histFactoryWS.root",
                 "histname": "SigLowNorm_15_SR1_tagged_",
                 #"histname": "SigLowAllNorm_15_SR1_tagged_",
               }


signals["test3_NoCut"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_nocut_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_sigpick2_10_BkgAlpha_20_dimVarsDphi_MEAN.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/Signal_nocut_sigpick2_10_BkgAlpha_20_dimVarsDphi_Mean_MEAN.root",
                 "histname": "SigLowAllNorm_0_SR1_tagged",
               }

signals["gausHistBBJ"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalGaus_bbj_mZ_MEAN_width_WIDTH.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalGaus_bbj_mZ_MEAN_width_WIDTH.root",
                 "histname": "btagFinal_",
               }

signals["gausHist"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalGaus_trijet_mZ_MEAN_width_WIDTH.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalGaus_trijet_mZ_MEAN_width_WIDTH.root",
                 "histname": "test3New_15_",
               }

signals["gausHistNoSyst"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalGausNoSyst_trijet_mZ_MEAN_width_WIDTH.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalGausNoSyst_trijet_mZ_MEAN_width_WIDTH.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/systematics/gausSignals/gausCB__mX_MEAN_mY_MASSX_alphaBin_ALPHA.root",
                 "histname": "test3New_15_",
               }

signals["templateHist"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalTemplate_trijet_mZ_MEAN_width_WIDTH.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalTemplate_trijet_mZ_MEAN_width_WIDTH.root",
                 "histname": "Morphed_m_MEAN_",
               }

signals["templateHistNoSyst"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalTemplateNoSyst_trijet_mZ_MEAN_width_WIDTH.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalTemplateNoSyst_trijet_mZ_MEAN_width_WIDTH.root",
                 "histname": "Morphed_m_MEAN_",
               }


signals["templateHistBBJNoSyst"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalTemplateNoSyst_bbj_mZ_MEAN_width_WIDTH.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalTemplateNoSyst_bbj_mZ_MEAN_width_WIDTH.root",
                 "histname": "Morphed_m_MEAN_",
               }

signals["templateHistBBJ"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalTemplate_bbj_mZ_MEAN_width_WIDTH.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/scripts/signalTemplates/SignalTemplate_bbj_mZ_MEAN_width_WIDTH.root",
                 "histname": "Morphed_m_MEAN_",
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


def getBinning(rangelow, rangehigh, delta=0):
  bins = []
  if delta > 0:
    for i in range(rangelow, rangehigh, delta):
      bins.append(i)
    bins.append(rangehigh)
  else:
    bins.append(rangelow)
    #cbinning = {200, 218, 237, 257, 278, 300, 323, 347, 372, 397, 423, 450, 478, 506, 535, 565, 595, 626, 657, 689, 721, 754, 787, 821, 855, 890, 925, 995, 1031, 1067, 1103, 1139, 1175, 1212, 1249, 1286, 1323}
    #cbinning = [225, 237, 257, 278, 300, 323, 347, 372, 397, 423, 450, 478, 506, 535, 565, 595, 626, 657, 689, 721, 754, 787, 821, 855, 890, 925, 1000]
    cbinning = [225, 239, 253, 268, 284, 300, 317, 335, 353, 372, 392, 413, 435, 458, 482, 507, 533, 560, 588, 618, 649, 681, 715, 750, 787, 826, 866, 908, 952, 1000]
    if rangehigh == 700:
      cbinning = [160, 171, 183, 195, 207, 220, 234, 248, 263, 278, 294, 311, 328, 346, 365, 385, 406, 427, 449, 472, 496, 521, 548, 576, 605, 635, 667, 700]
    #cbinning = [200, 220, 240, 260, 280, 300, 325, 350, 375, 400, 425, 450, 475, 500, 535, 565, 595, 625, 660, 690, 720, 750, 785, 820, 855, 890, 925, 960, 1000]
    #for cbin in cbinning:
    #  if cbin > rangelow and cbin < rangehigh:
    #    bins.append(cbin)
    #bins.append(rangehigh)
    return cbinning
  return bins
     


