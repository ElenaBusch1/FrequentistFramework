# Directory where the code is installed
cdir="/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework"

# Directory where the input histograms are
# This isn't strictly needed, but it makes the samples section slightly easier to handle
baseDir = "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/"

nToys = 50
atlasLabel="Simulation Internal"


cSample = "fits_"
cPDFitName = "fivePar"
cFitName = "fourPar"
cSignal = "Gaussian"
alphaBins = [0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33]




#####################################################################################
# Input mjj distributions
#####################################################################################
samples = {}




samples["yxxjjjj_4j_inclusive"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_inclusive",
                 "lumi": 140000,
                 "alpha": 5,
                 "varName": "m_{4j}, 0.34 < #alpha",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.1 < #alpha",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_0.txt",
               }

samples["yxxjjjj_4j_alpha12"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_12",
                 "alpha": 12,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.34 < #alpha",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.34 < #alpha",
                 "rangelow" : 2000,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_12.txt",
               }

samples["yxxjjjj_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 2175,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_11.txt",
               }

samples["yxxjjjj_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_10.txt",
               }


samples["yxxjjjj_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_9.txt",
               }

samples["yxxjjjj_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1925,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_8.txt",
               }

samples["yxxjjjj_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_7.txt",
               }

samples["yxxjjjj_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1875,
                 #"rangehigh" : 9000,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_6.txt",
               }



samples["yxxjjjj_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_5.txt",
               }

samples["yxxjjjj_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_4.txt",
               }

samples["yxxjjjj_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1825,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_3.txt",
               }

samples["yxxjjjj_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1725,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_2.txt",
               }

samples["yxxjjjj_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_1.txt",
               }


samples["yxxjjjj_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_0.txt",
               }




samples["sherpa_yxxjjjji_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 2175,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1925,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1825,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1725,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }











samples["tenPercentData_yxxjjjj_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 2175,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_11.txt",
               }

samples["tenPercentData_yxxjjjj_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_10.txt",
               }


samples["tenPercentData_yxxjjjj_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_9.txt",
               }

samples["tenPercentData_yxxjjjj_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1925,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_8.txt",
               }

samples["tenPercentData_yxxjjjj_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_7.txt",
               }

samples["tenPercentData_yxxjjjj_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_6.txt",
               }

samples["tenPercentData_yxxjjjj_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_5.txt",
               }

samples["tenPercentData_yxxjjjj_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_4.txt",
               }

samples["tenPercentData_yxxjjjj_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1825,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_3.txt",
               }
samples["tenPercentData_yxxjjjj_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1725,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_2.txt",
               }

samples["tenPercentData_yxxjjjj_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_1.txt",
               }


samples["tenPercentData_yxxjjjj_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "alpha": 1,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_0.txt",
               }








samples["Data_yxxjjjj_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 2175,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_11.txt",
               }

samples["Data_yxxjjjj_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_10.txt",
               }


samples["Data_yxxjjjj_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_9.txt",
               }

samples["Data_yxxjjjj_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1925,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_8.txt",
               }

samples["Data_yxxjjjj_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_7.txt",
               }

samples["Data_yxxjjjj_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_6.txt",
               }

samples["Data_yxxjjjj_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_5.txt",
               }

samples["Data_yxxjjjj_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_4.txt",
               }

samples["Data_yxxjjjj_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1825,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_3.txt",
               }
samples["Data_yxxjjjj_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1725,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_2.txt",
               }

samples["Data_yxxjjjj_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_1.txt",
               }


samples["Data_yxxjjjj_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "alpha": 1,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_0.txt",
               }





















samples["hybrid10_yxxjjjj_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 2175,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_11.txt",
               }

samples["hybrid10_yxxjjjj_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_10.txt",
               }


samples["hybrid10_yxxjjjj_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_9.txt",
               }
samples["hybrid10_yxxjjjj_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1925,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_8.txt",
               }

samples["hybrid10_yxxjjjj_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_7.txt",
               }

samples["hybrid10_yxxjjjj_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_6.txt",
               }

samples["hybrid10_yxxjjjj_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_5.txt",
               }

samples["hybrid10_yxxjjjj_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_4.txt",
               }

samples["hybrid10_yxxjjjj_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1825,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_3.txt",
               }
samples["hybrid10_yxxjjjj_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1725,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_2.txt",
               }

samples["hybrid10_yxxjjjj_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_1.txt",
               }


samples["hybrid10_yxxjjjj_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "alpha": 1,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "Hybrid",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_0.txt",
               }




















samples["tenPercent_yxxjjjj_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 2175,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_11.txt",
               }

samples["tenPercent_yxxjjjj_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_10.txt",
               }


samples["tenPercent_yxxjjjj_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_9.txt",
               }

samples["tenPercent_yxxjjjj_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1925,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_8.txt",
               }

samples["tenPercent_yxxjjjj_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_7.txt",
               }

samples["tenPercent_yxxjjjj_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_6.txt",
               }



samples["tenPercent_yxxjjjj_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_5.txt",
               }

samples["tenPercent_yxxjjjj_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_4.txt",
               }

samples["tenPercent_yxxjjjj_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1825,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_3.txt",
               }

samples["tenPercent_yxxjjjj_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1725,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_2.txt",
               }

samples["tenPercent_yxxjjjj_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_1.txt",
               }


samples["tenPercent_yxxjjjj_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "alpha": 1,
                 "lumi": 14000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m4j_m4jresp_0.txt",
               }
















samples["hybrid10_2javg_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 730,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_11.txt",
               }

samples["hybrid10_2javg_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 630,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_10.txt",
               }


samples["hybrid10_2javg_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 570,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_9.txt",
               }

samples["hybrid10_2javg_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 510,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_8.txt",
               }

samples["hybrid10_2javg_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 490,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_7.txt",
               }

samples["hybrid10_2javg_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 430,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_6.txt",
               }


samples["hybrid10_2javg_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 430,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_5.txt",
               }

samples["hybrid10_2javg_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 370,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_4.txt",
               }

samples["hybrid10_2javg_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 330,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_3.txt",
               }

samples["hybrid10_2javg_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 270,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_2.txt",
               }



samples["hybrid10_2javg_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 250,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_1.txt",
               }


samples["hybrid10_2javg_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/hybrid_tenPercent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 230,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_0.txt",
               }




























samples["tenPercentData_2javg_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 749,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_11.txt",
               }

samples["tenPercentData_2javg_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 630,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_10.txt",
               }


samples["tenPercentData_2javg_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 570,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_9.txt",
               }

samples["tenPercentData_2javg_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 510,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_8.txt",
               }

samples["tenPercentData_2javg_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 490,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_7.txt",
               }

samples["tenPercentData_2javg_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 430,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_6.txt",
               }

samples["tenPercentData_2javg_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 430,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_5.txt",
               }

samples["tenPercentData_2javg_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 370,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_4.txt",
               }

samples["tenPercentData_2javg_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 330,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_3.txt",
               }

samples["tenPercentData_2javg_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 270,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_2.txt",
               }



samples["tenPercentData_2javg_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 250,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_1.txt",
               }


samples["tenPercentData_2javg_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_DataRun2_10percent.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 14000,
                 "varName": "m_{#LT 2j #GT}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 230,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_0.txt",
               }












samples["Data_2javg_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 730,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_11.txt",
               }

samples["Data_2javg_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 630,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_10.txt",
               }


samples["Data_2javg_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 570,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_9.txt",
               }

samples["Data_2javg_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 510,
                 #"rangelow" : 527,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_8.txt",
               }

samples["Data_2javg_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 490,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_7.txt",
               }

samples["Data_2javg_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 430,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_6.txt",
               }

samples["Data_2javg_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 430,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_5.txt",
               }

samples["Data_2javg_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 370,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_4.txt",
               }

samples["Data_2javg_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 330,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_3.txt",
               }

samples["Data_2javg_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 270,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_2.txt",
               }



samples["Data_2javg_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 250,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_1.txt",
               }


samples["Data_2javg_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Data.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 230,
                 "rangehigh" : 3500,
                 "legend": "Data",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_0.txt",
               }




























samples["yxxjjjj_2javg_inclusive"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_inclusive",
                 "alpha": 5,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.34 < #alpha",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.1 < #alpha",
                 "rangelow" : 700,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }



samples["yxxjjjj_2javg_alpha12"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_12",
                 "alpha": 12,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.34 < #alpha",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.34 < #alpha",
                 "rangelow" : 700,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_2javg_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 730,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_11.txt",
               }

samples["yxxjjjj_2javg_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 630,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_10.txt",
               }


samples["yxxjjjj_2javg_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 570,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_9.txt",
               }

samples["yxxjjjj_2javg_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 510,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_8.txt",
               }

samples["yxxjjjj_2javg_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 490,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_7.txt",
               }

samples["yxxjjjj_2javg_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 430,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_6.txt",
               }



samples["yxxjjjj_2javg_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 430,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_5.txt",
               }

samples["yxxjjjj_2javg_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 370,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_4.txt",
               }

samples["yxxjjjj_2javg_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 330,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_3.txt",
               }

samples["yxxjjjj_2javg_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 270,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_2.txt",
               }



samples["yxxjjjj_2javg_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 250,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_1.txt",
               }


samples["yxxjjjj_2javg_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 230,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
                 "binFile": "massResolutionBins/binFile_h2_resonance_jet_m2javg_m2javgresp_0.txt",
               }




samples["sherpa_yxxjjjji_2javg_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 730,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 630,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_2javg_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 570,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 510,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 490,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 430,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 430,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 370,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 330,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_2javg_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 270,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }



samples["sherpa_yxxjjjj_2javg_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 250,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_2javg_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Sherpa.root"%(baseDir),
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 140000,
                 "varName": "m_{#LT 2j #GT}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }


samples["tile_4j_alpha12"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_12",
                 "alpha": 12,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.34 < #alpha",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.34 < #alpha",
                 "rangelow" : 2000,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_11",
                 "alpha": 11,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 2175,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_10",
                 "alpha": 10,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_9",
                 "alpha": 9,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1975,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_8",
                 "alpha": 8,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1925,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_7",
                 "alpha": 7,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }


samples["tile_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_6",
                 "alpha": 6,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }



samples["tile_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_5",
                 "alpha": 5,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_4",
                 "alpha": 4,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1875,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }


samples["tile_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_3",
                 "alpha": 3,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1675,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_2",
                 "alpha": 2,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1725,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_1",
                 "alpha": 1,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }


samples["tile_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "%s/yxxjjjj_Pythia.root"%(baseDir),
                 "histname": "h2_resonance_jet_m4j_alpha_TILE_CORE_alphaBin_0",
                 "alpha": 0,
                 "lumi": 140000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1775,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }












#####################################################################################
# Signals
#####################################################################################
signals = {}

# Signal template (can include systematics)
signals["template"] = {
                 "signalfile": "../config/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/Signal_mX_MEAN_mY_MASSX.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/Signal_mX_MEAN_mY_MASSX.root",
                 "histname": "h2_resonance_jet_m4j_alpha_alphaBin_ALPHA_",
                 "systFile": "empty.txt",
                 #"histname": "Gaus_mX_3000_mY_870_alphaBin_ALPHA_ ",
               }


signals["crystalBallHist"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/config/signalGauss_meanM_template.xml",
                 "workspacefile": "%s/scripts/signalTemplates/TAGNAMESignalCB_mX_MEAN_mY_MASSX.root"%(cdir),
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/systematics/gausSignals/gausCB__mX_MEAN_mY_MASSX_alphaBin_ALPHA.root",
                 #"histname": "Gaus_mX_MEAN_mY_MASSX_alphaBin_ALPHA_",
                 "histname": "h2_resonance_jet_m4j_alpha_",
                 "histnameMX": "h2_resonance_jet_m2javg_alpha_",
                 #"histname": "",
                 #"systFile": "empty.txt",
                 "systFile": "uncertaintySets/systematics",
               }

signals["crystalBallHistNoSyst"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/config/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/TAGNAMESignalCBNoSyst_mX_MEAN_mY_MASSX.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/systematics/gausSignals/gausCB__mX_MEAN_mY_MASSX_alphaBin_ALPHA.root",
                 "histname": "h2_resonance_jet_m4j_alpha_",
                 "histnameMX": "h2_resonance_jet_m2javg_alpha_",
                 "systFile": "empty.txt",
               }

signals["gausHist"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/config/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/TAGNAMESignalGaus_mX_MEAN_mY_MASSX_width_WIDTH.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/systematics/gausSignals/gausCB__mX_MEAN_mY_MASSX_alphaBin_ALPHA.root",
                 "histname": "h2_resonance_jet_m4j_alpha_",
                 "histnameMX": "h2_resonance_jet_m2javg_alpha_",
                 "systFile": "uncertaintySets/systematics",
               }

signals["gausHistNoSyst"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/config/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/TAGNAMESignalGausNoSyst_mX_MEAN_mY_MASSX_width_WIDTH.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/systematics/gausSignals/gausCB__mX_MEAN_mY_MASSX_alphaBin_ALPHA.root",
                 "histname": "h2_resonance_jet_m4j_alpha_",
                 "histnameMX": "h2_resonance_jet_m2javg_alpha_",
                 "systFile": "empty.txt",
               }






# Signal template (can include systematics)
signals["test"] = {
                 "signalfile": "../config/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/SignalGaus_mX_MEAN_mY_MASSX.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/systematics/gausSignals/gausSignal__mX_MEAN_mY_MASSX_alphaBin_ALPHA.root",
                 "systFile": "/afs/cern.ch/work/j/jroloff/nixon/systematics/test/Systematics_h2_resonance_jet_m4j_alpha_mX_MEAN_mY_MASSX_alphaBin_ALPHA_systematics_mean",
                 "histname": "Gaus_mX_MEAN_mY_MASSX_alphaBin_ALPHA_",
               }


# Generic gaussian distribution
signals["Gaussian"] = {
                 "signalfile"  : "../config/signalGauss_meanM_widthW.xml",
                 "workspacefile": "",
                 "templatefile"  : "",
                 "systFile": "empty.txt",
                 "histname": "",
               }






#####################################################################################
# Fit functions
#####################################################################################
fitFunctions = {}

fitFunctions["threeParM2j"] = {
                            "Name" : "3-par fit",
                            "Config" : "config/background_threePar_m2j.xml",
                          }

fitFunctions["fourParM2j"] = {
                            "Name" : "4-par fit",
                            "Config" : "config/background_fourPar_m2j.xml",
                          }

fitFunctions["fiveParM2j"] = {
                            "Name" : "5-par fit",
                            "Config" : "config/background_fivePar_m2j.xml",
                          }

fitFunctions["sixParM2j"] = {
                            "Name" : "6-par fit",
                            "Config" : "config/background_sixPar_m2j.xml",
                          }

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

def getBinningFromFile(channelName):
   binFile = samples[channelName]["binFile"]
   bins = []
   
   try:
     fp = open(binFile )
   except:
     print "Could not find the binning file"
     return None

   inputFileLines = fp.readlines()

   for line in inputFileLines:
     bins.append(int(line))
 
   #print bins
   return bins


def getBinning(rangelow, rangehigh, delta=25):
  bins = []
  for i in range(rangelow, rangehigh, delta):
    bins.append(i)
  bins.append(rangehigh)
  return bins
     


