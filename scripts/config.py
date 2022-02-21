cdir="/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest"
nToys = 1000
atlasLabel="Simulation Internal"

samples = {}

samples["BkgLow_3_alpha0_SR1_tagged"] = { 
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_3_alpha0_SR1_tagged",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_ptOrdered_vars_pt_cutVal_6.root",
                 "lumi": 139000,
               }


samples["SR1_cutval7"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_3_alpha0_SR1_tagged",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_ptOrdered_vars_pt_cutVal_7.root",
                 "lumi": 139000,
               }



samples["BkgLow_4_alpha0_SR1_tagged"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_4_alpha0_SR1_tagged",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_ptOrdered_vars_pt_cutVal_6.root",
                 "lumi": 139000,
               }

samples["BkgLow_5_alpha0_SR1_tagged"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_5_alpha0_SR1_tagged",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_ptOrdered_vars_pt_cutVal_6.root",
                 "lumi": 139000,
               }

samples["BkgLow_2_alpha0_SR1_tagged"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_2_alpha0_SR1_tagged",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_ptOrdered_vars_pt_cutVal_6.root",
                 "lumi": 139000,
               }

samples["BkgLow_2_alpha0_SR1_tagged"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_1_alpha0_SR1_tagged",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_ptOrdered_vars_pt_cutVal_6.root",
                 "lumi": 139000,
               }

samples["BkgMid_2_alpha0_SR2_tagged"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgMid_2_alpha0_SR2_tagged",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_ptOrdered_vars_pt_cutVal_6.root",
                 "lumi": 139000,
               }


samples["MassOrdered_2"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_1_alpha0_SR1",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectra_test_SRAlpha_100_BkgAlpha_0_dimVars_pt_cutVal_6.root",
                 "lumi": 139000,
               }


samples["PtOrdered"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_2_alpha100_SR1",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_test_SRAlpha_100_BkgAlpha_100_dimVars_pt_cutVal_7.root",
                 "lumi": 139000,
               }


samples["PtOrdered2"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_3_alpha100_SR1",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_test_SRAlpha_100_BkgAlpha_100_dimVars_pt_cutVal_7.root",
                 "lumi": 139000,
               }

samples["PtOrderedSR1_tagged"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_3_alpha100_SR1_tagged",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_test_SRAlpha_100_BkgAlpha_100_dimVars_pt_cutVal_7.root",
                 "lumi": 139000,
               }

samples["PtOrderedSR2_tagged"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgMid_3_alpha100_SR2",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_test_SRAlpha_100_BkgAlpha_100_dimVars_pt_cutVal_7.root",
                 "lumi": 139000,
               }

samples["PtOrdered3"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_3_alpha100_SR1",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_test_SRAlpha_100_BkgAlpha_100_dimVars_pt_cutVal_5.root",
                 "lumi": 139000,
               }

samples["PtOrdered4"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
                 "topfile": "../config/dijetISR/jjj_SR1.template",
                 "histname": "BkgLow_3_alpha100_SR1",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_test_SRAlpha_100_BkgAlpha_100_dimVars_pt_cutVal_6.root",
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


#samples["PtOrdered6"] = {
#                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1.template",
#                 "topfile": "../config/dijetISR/jjj_SR1.template",
#                 "histname": "BkgLow_SR1",
#                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_decorr2_SRAlpha_200_BkgAlpha_200_dimVars_pt_cutVal_6.root",
#                 "lumi": 139000,
#               }



#samples["PtOrdered6"] = {
#                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1_signalTest.template",
#                 "topfile": "../config/dijetISR/jjj_SR1_signalTest.template",
#                 "histname": "BkgLow_SR1",
#                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_decorr2_SRAlpha_200_BkgAlpha_200_dimVars_pt_cutVal_6.root",
#                 "lumi": 139000,
#               }

samples["PtOrdered6"] = {
                 "categoryfile"  : "../config/dijetISR/category_jjj_SR1_signalTemplate.template",
                 "topfile": "../config/dijetISR/jjj_SR1_signalTemplate.template",
                 "histname": "BkgLow_SR1",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_decorr2_SRAlpha_200_BkgAlpha_200_dimVars_pt_cutVal_6.root",
                 "lumi": 139000,
               }






signals = {}
signals["PtOrdered6"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/Input/signal/HistFactory_dijetISR_mRMEAN.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_decorr2_SRAlpha_200_BkgAlpha_200_dimVars_pt_cutVal_6_MEAN.root",
                 "histname": "SigLow_1_alpha200_SR1",
               }


signals["Gaussian"] = {
                 "signalfile"  : "../config/dijetISR/signalGauss_meanM_widthW.xml",
                 "workspacefile": "",
                 "templatefile"  : "",
                 "histname": "",
               }









fitFunctions = {}
fitFunctions["sixPar"] = {
                            "Name" : "6-par fit",
                            "Config" : "dijetISR/background_ajj_simpleTrig_yStar0p825_sixPar.xml",
                          }
fitFunctions["fivePar"] = {
                            "Name" : "5-par fit",
                            "Config" : "dijetISR/background_ajj_simpleTrig_yStar0p825_fivePar.xml",
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
                            "Config" : "dijetISR/background_ajj_simpleTrig_yStar0p825_fourPar.xml",
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
     


