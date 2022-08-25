#!/usr/bin/env python

initialParameters = {
    'TLA2016' : { 
	
	'J100' : {  	
	  
	  'nbkg' 	: "2E8,0,3E8",
	  'datafile'	: "Input/data/dijetTLA/lookInsideTheBoxWithUniformMjj.root",
	  'datahist'	: "Nominal/DSJ100yStar06_TriggerJets_J100_yStar06_mjj_finebinned_all_data",
	  # Analysis range		
	  'low'  : 531 ,
	  'high' : 2997,
	  'lumi' : 29.3,
	},
    },
    'partialDataset' : { # Partial datafile (1st unblinding)
	
	'J100' : {  	
	  
	  'nbkg' 	: "4E7,0,1E8",
	  'datafile'	: "Input/data/dijetTLA/unblinding1_mjj_spectra.root",
	  'datahist'	: "L1J100/Mjj_1GeVbinning",
	  # Analysis range		
	  'low'  : 457,
	  'high' : 2997,
	  'lumi' : 3.6,
	},
	
	'J40'  : {  
	  
	  'nbkg'	: "1E7,0,2E7",
	  'datafile'	: "Input/data/dijetTLA/unblinding1_mjj_spectra.root",
	  'datahist'	: "L1J40/Mjj_1GeVbinning",                      	  
	  'low'  : 302,
	  'high' : 1516, 
	},
	
	'J50'  : {	
	  
	  'nbkg' : "1E7,0,2E7",
	  'datafile'	: "Input/data/dijetTLA/unblinding1_mjj_spectra.root",
	  'datahist'	: "L1J50/Mjj_1GeVbinning",
	  'low'  : 302,
	  'high' : 1516, 
	  'lumi'  : 0.11,
	},

    },
    
    'partialDataset2' : { # Partial datafile (2nd unblinding)
	
	'J100' : {  	
	  
	  'nbkg' 	: "4E7,0,1E8",
	  'datafile'	: "Input/data/dijetTLA/unblinding2_mjj_spectra_J100_no2017.root",
	  'datahist'	: "L1J100/Mjj_1GeVbinning",
	  # Analysis range		
	  'low'  : 457,  # 481 -- trying one less bin, because of the mjj turnon threshold is now a bit higher.
	  'high' : 2997,
	  'lumi' : 19.6,  #29.5 - 9.869 (2017)
	},
	
	'J50'  : {	
	  
	  'nbkg' : "1E7,0,2E7",
	  'datafile'	: "Input/data/dijetTLA/unblinding2_mjj_spectra_all.root",
	  'datahist'	: "L1J50/Mjj_1GeVbinning",
	  'lumi'	: 1.5,
	  'low'  : 282,  # 282 --trying one more bin, close to the mjj 99.9 threshold, but below, DIDN'T WORK
	  'high' : 1516, 
	},
    },

    'partialDataset2_PD' : { # PD based on partialDataset2

	'J100' : {
	  'four' 	: "Input/data/dijetTLA/PD_Run2_GlobalFit_457_2997_fivePar_finebinned_J100_scale6.78.root", 
	  'five'	: "Input/data/dijetTLA/PD_Run2_GlobalFit_457_2997_sixPar_finebinned_J100_scale6.78.root", 
	  'six' 	: "Input/data/dijetTLA/PD_Run2_GlobalFit_457_2997_sevenPar_finebinned_J100_scale6.78.root",
	  
	  #'four'	: "Input/data/dijetTLA/PD_Run2_GlobalFit_481_2997_fivePar_finebinned_J100_scale6.78.root", 
	  #'five'	: "Input/data/dijetTLA/PD_Run2_GlobalFit_481_2997_sixPar_finebinned_J100_scale6.78.root", 
	  #'six'  	: "Input/data/dijetTLA/PD_Run2_GlobalFit_481_2997_sevenPar_finebinned_J100_scale6.78.root",
	  },

	'J50'  : {
	  'four' 	: "Input/data/dijetTLA/PD_Run2_GlobalFit_302_1516_fivePar_finebinned_J50Comb_scale9.77.root",
	  'five'	: "Input/data/dijetTLA/PD_Run2_GlobalFit_302_1516_sixPar_finebinned_J50Comb_scale9.77.root",	
	  'six' 	: "Input/data/dijetTLA/PD_Run2_GlobalFit_302_1516_sevenPar_finebinned_J50Comb_scale9.77.root",
	  },
    },

    'full' : {  # Full lumi: total datafile

	'J100' : {  	
	  
	  'nbkg' 	: "9E8,0,2E9",
	  'datafile'	: "",
	  'datahist'	: "",
	  'low'  :457 ,
	  'high' : 2997,
	  'lumi' : 133.2,
	},
	
	'J40'  : {  
	  
	  'nbkg'	: "1E7,0,2E7",
	  'datafile'	: "",
	  'datahist'	: "",                      	  
	  'low'  : 302,
	  'high' : 1516, 
	},
	
	'J50'  : {	
	  
	  'nbkg' : "1E7,0,2E7",
	  'datafile'	: "",
	  'datahist'	: "",
	  'lumi'	: 18.9,
	  'low'  : 302,
	  'high' : 1516, 
	},
    },
}
