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




