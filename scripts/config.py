cdir="/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest"
nToys = 20
atlasLabel="Simulation Internal"

samples = {}

samples["BkgLow_3_alpha0_SR1_tagged"] = { 
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_3_alpha0_SR1_tagged",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_ptOrdered_vars_pt_cutVal_6.root",
               }

fitFunctions = {}
fitFunctions["fivePar"] = {
                            "Name" : "5-par fit",
                            "Config" : "dijetISR/background_ajj_simpleTrig_yStar0p825_fivePar.xml",
                          }

fitFunctions["fourPar"] = { 
                            "Name" : "4-par fit",
                            "Config" : "dijetISR/background_ajj_simpleTrig_yStar0p825_fourPar.xml",
                          }


def getFileName(prefix, directory, channelName, rangelow, rangehigh, sigmean=0, sigwidth=0, sigamp=0):
  if sigamp:
    return "%s/%s/%s_Fit_%d_%d_Mean_%d_Width_%d_Amp_%d"%(directory, channelName, prefix, rangelow, rangehigh, sigmean, sigwidth, sigamp)
  else:
    return "%s/%s/%s_Fit_%d_%d"%(directory, channelName, prefix, rangelow, rangehigh)


def getBinning(rangelow, rangehigh, delta=25):
  bins = []
  for i in range(rangelow, rangehigh, delta):
    bins.append(i)
  bins.append(rangehigh)
  return bins
     


