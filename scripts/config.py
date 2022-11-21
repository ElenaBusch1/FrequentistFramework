cdir="/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework"
nToys = 500
atlasLabel="Simulation Internal"

cSample = "fits_"
cPDFitName = "fivePar"
cFitName = "fourPar"
cSignal = "Gaussian"
cChannelNames = ["yxxjjjj_4j_alpha0", "yxxjjjj_4j_alpha1", "yxxjjjj_4j_alpha2", "yxxjjjj_4j_alpha3", "yxxjjjj_4j_alpha4", "yxxjjjj_4j_alpha5", "yxxjjjj_4j_alpha6", "yxxjjjj_4j_alpha7", "yxxjjjj_4j_alpha8", "yxxjjjj_4j_alpha9"]
cSignalMasses = [2000,3000,4000,5000,6000,7000,8000,9000]



#####################################################################################
# Input mjj distributions
#####################################################################################
samples = {}




samples["yxxjjjj_4j_inclusive"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_inclusive",
                 "lumi": 139000,
                 "alpha": 5,
                 "varName": "m_{4j}, 0.34 < #alpha",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.1 < #alpha",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_4j_alpha12"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_12",
                 "alpha": 12,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.34 < #alpha",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.34 < #alpha",
                 "rangelow" : 2000,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }


samples["yxxjjjj_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1700,
                 #"rangehigh" : 9000,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }



samples["yxxjjjj_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }


samples["yxxjjjj_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }




samples["sherpa_yxxjjjji_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "Sherpa AHADIC",
               }















samples["tenPercent_yxxjjjj_4j_alpha12"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_12",
                 "alpha": 12,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.34 < #alpha",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.34 < #alpha",
                 "rangelow" : 2000,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tenPercent_yxxjjjj_4j_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tenPercent_yxxjjjj_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }


samples["tenPercent_yxxjjjj_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tenPercent_yxxjjjj_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tenPercent_yxxjjjj_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tenPercent_yxxjjjj_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }



samples["tenPercent_yxxjjjj_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tenPercent_yxxjjjj_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tenPercent_yxxjjjj_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tenPercent_yxxjjjj_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tenPercent_yxxjjjj_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }


samples["tenPercent_yxxjjjj_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia_10percent.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "alpha": 1,
                 "lumi": 13900,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }






















samples["yxxjjjj_2javg_inclusive"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_inclusive",
                 "alpha": 5,
                 "lumi": 139000,
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
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_12",
                 "alpha": 12,
                 "lumi": 139000,
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
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 700,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_2javg_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 700,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }


samples["yxxjjjj_2javg_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 700,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_2javg_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 500,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_2javg_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 500,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_2javg_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 500,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }



samples["yxxjjjj_2javg_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 400,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_2javg_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 400,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_2javg_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 400,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }

samples["yxxjjjj_2javg_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 400,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }



samples["yxxjjjj_2javg_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 400,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }


samples["yxxjjjj_2javg_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 300,
                 "rangehigh" : 3500,
                 "legend": "PYTHIA8",
               }




samples["sherpa_yxxjjjji_2javg_alpha11"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 700,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 700,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_2javg_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 600,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 500,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 500,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 400,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 400,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 400,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }

samples["sherpa_yxxjjjj_2javg_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 300,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_2javg_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 300,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }



samples["sherpa_yxxjjjj_2javg_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 300,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }


samples["sherpa_yxxjjjj_2javg_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root",
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 139000,
                 "varName": "m_{#LT 2j #GT}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{#LT 2j #GT} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 300,
                 "rangehigh" : 3500,
                 "legend": "Sherpa AHADIC",
               }


samples["tile_4j_alpha12"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_12",
                 "alpha": 12,
                 "lumi": 139000,
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
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_11",
                 "alpha": 11,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.32 < #alpha < 0.34",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.32 < #alpha < 0.34",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha10"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_10",
                 "alpha": 10,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.30 < #alpha < 0.32",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.30 < #alpha < 0.32",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha9"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_9",
                 "alpha": 9,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.28 < #alpha < 0.30",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.28 < #alpha < 0.30",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha8"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_8",
                 "alpha": 8,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.26 < #alpha < 0.28",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.26 < #alpha < 0.28",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha7"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_7",
                 "alpha": 7,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.24 < #alpha < 0.26",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.24 < #alpha < 0.26",
                 "rangelow" : 1800,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }


samples["tile_4j_alpha6"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_6",
                 "alpha": 6,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.22 < #alpha < 0.24",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.22 < #alpha < 0.24",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }



samples["tile_4j_alpha5"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_5",
                 "alpha": 5,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.20 < #alpha < 0.22",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.20 < #alpha < 0.22",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha4"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_4",
                 "alpha": 4,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.18 < #alpha < 0.20",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.18 < #alpha < 0.20",
                 "rangelow" : 1700,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }


samples["tile_4j_alpha3"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_3",
                 "alpha": 3,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.16 < #alpha < 0.18",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.16 < #alpha < 0.18",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha2"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_2",
                 "alpha": 2,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.14 < #alpha < 0.16",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.14 < #alpha < 0.16",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }

samples["tile_4j_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_1",
                 "alpha": 1,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.12 < #alpha < 0.14",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.12 < #alpha < 0.14",
                 "rangelow" : 1600,
                 "rangehigh" : 11000,
                 "legend": "PYTHIA8",
               }


samples["tile_4j_alpha0"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "categoryfileSysts"  : "../config/category_backgroundWithSysts.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Pythia.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_alphaBin_0",
                 "alpha": 0,
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.10 < #alpha < 0.12",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.10 < #alpha < 0.12",
                 "rangelow" : 1600,
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
                 "templatefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/Signal_mX_MEAN_mY_MASSX.root",
                 "histname": "h2_resonance_jet_m4j_alpha_alphaBin_ALPHA_",
                 "systFile": "empty.txt",
                 #"histname": "Gaus_mX_3000_mY_870_alphaBin_ALPHA_ ",
               }

# Signal template (can include systematics)
signals["gausHist"] = {
                 "signalfile": "../config/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/SignalGaus_mX_MEAN_mY_MASSX.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/SignalGaus_mX_MEAN_mY_MASSX.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/systematics/gausSignals/gausSignal__mX_MEAN_mY_MASSX_alphaBin_ALPHA.root",
                 "histname": "Gaus_mX_MEAN_mY_MASSX_alphaBin_ALPHA_",
                 "systFile": "empty.txt",
               }


# Signal template (can include systematics)
signals["test"] = {
                 "signalfile": "../config/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/SignalGaus_mX_MEAN_mY_MASSX.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/SignalGaus_mX_MEAN_mY_MASSX.root",
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


def getBinning(rangelow, rangehigh, delta=25):
  bins = []
  for i in range(rangelow, rangehigh, delta):
    bins.append(i)
  bins.append(rangehigh)
  return bins
     


