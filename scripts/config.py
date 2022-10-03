cdir="/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_forNatalie/FrequentistFramework"
nToys = 500
atlasLabel="Simulation Internal"

cSample = "fitsYXXjjjj"
cPDFitName = "fivePar"
cFitName = "fourPar"
cSignal = "Gaussian"
cChannelNames = ["yxxjjjj_4j_inclusive",]
cSignalMasses = [2000,3000,4000,5000,6000,7000,8000,9000]



#####################################################################################
# Input mjj distributions
#####################################################################################
samples = {}

samples["yxxjjjj_4j_inclusive"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "testOutputAutomatic.root",
                 "histname": "h2_resonance_jet_m4j_alpha_nominal_inclusive",
                 "lumi": 139000,
                 "varName": "m_{4j}, 0.34 < #alpha",
                 "varAxis": "m_{4j} [GeV]",
                 "varLabel": "0.1 < #alpha",
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
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/FrequentistFramework/scripts/signalTemplates/Signal_mX_3000_mY_630.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/FrequentistFramework/scripts/signalTemplates/Signal_mX_3000_mY_630.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/FrequentistFramework/scripts/signalTemplates/Signal_mX_3000_mY_630.root",
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

fitFunctions["UA2"] = { 
                            "Name" : "UA2 fit",
                            "Config" : "config/background_UA2.xml",
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
     


