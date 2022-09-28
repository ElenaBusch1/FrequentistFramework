cdir="/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework"
nToys = 500
atlasLabel="Simulation Internal"

cSample = "fitsNixon"
cPDFitName = "fivePar"
cFitName = "fourPar"
cSignal = "Gaussian"
cChannelNames = ["nixon_4j_alpha0", "nixon_4j_alpha1", "nixon_4j_alpha2", "nixon_4j_alpha3", "nixon_4j_alpha4", "nixon_4j_alpha5", "nixon_4j_alpha6", "nixon_4j_alpha7", "nixon_4j_alpha8", "nixon_4j_alpha9"]
cSignalMasses = [2000,3000,4000,5000,6000,7000,8000,9000]



#####################################################################################
# Input mjj distributions
#####################################################################################
samples = {}

samples["nixon_4j_inclusive"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_inclusive",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.34 < #alpha",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.1 < #alpha",
                 "rangelow" : 1500,
                 "rangehigh" : 9000,
                 "legend": "PYTHIA8",
               }



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



#####################################################################################
# Signals
#####################################################################################
signals = {}

# Signal template (can include systematics)
signals["template"] = {
                 "signalfile": "../config/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/Signal_mX_3000_mY_630.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/Signal_mX_3000_mY_630.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/Signal_mX_3000_mY_630.root",
                 "histname": "h2_resonance_jet_m4j_alpha_alphaBin_5_",
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
     


