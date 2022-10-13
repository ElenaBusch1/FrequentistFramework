cdir="/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_forNatalie/FrequentistFramework"
nToys = 500
atlasLabel="Simulation Internal"

cSample = "bba"
cPDFitName = "fivePar"
cFitName = "fourPar"
cSignal = "Gaussian"
cChannelNames = ["bba",]
cSignalMasses = [350]



#####################################################################################
# Input mjj distributions
#####################################################################################
samples = {}

samples["bba"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/user/j/jroloff/public/forDavide/mc16e_outTree_mjj_169_to_10000_single_2b.root",
                 "histname": "mjj",
                 "lumi": 139000,
                 "varName": "mjj",
                 "varAxis": "m_{jj} [GeV]",
                 "varLabel": "bba",
                 "rangelow" : 200,
                 "rangehigh" : 1000,
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
     


