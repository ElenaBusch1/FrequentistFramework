#!/usr/bin/env python

initialParameters = {
  'partialDataset' : { # Partial dataset (1st unblinding)
	
	'J100' : {  	
	  
	  'nbkg' 	: "4E7,0,1E8",
	  'dataset'	: "Input/data/dijetTLA/unblinding1_mjj_spectra.root",
	  'datahist'	: "L1J100/Mjj_1GeVbinning",
	  # Analysis range		
	  'low'  :457 ,
	  'high' : 2997,
	},
	
	'J40'  : {  
	  
	  'nbkg'	: "1E7,0,2E7",
	  'dataset'	: "Input/data/dijetTLA/unblinding1_mjj_spectra.root",
	  'datahist'	: "L1J40/Mjj_1GeVbinning",                      	  
	  'low'  : 302,
	  'high' : 1516, 
	},
	
	'J50'  : {	
	  
	  'nbkg' : "1E7,0,2E7",
	  'dataset'	: "Input/data/dijetTLA/unblinding1_mjj_spectra.root",
	  'datahist'	: "L1J50/Mjj_1GeVbinning",
	  'low'  : 302,
	  'high' : 1516, 
	},

    },

    'full' : {  # Full lumi: total dataset

	'J100' : {  	
	  
	  'nbkg' 	: "9E8,0,15E8",
	  'dataset'	: "",
	  'datahist'	: "",
	  'low'  :457 ,
	  'high' : 2997,
	},
	
	'J40'  : {  
	  
	  'nbkg'	: "1E7,0,2E7",
	  'dataset'	: "",
	  'datahist'	: "",                      	  
	  'low'  : 302,
	  'high' : 1516, 
	},
	
	'J50'  : {	
	  
	  'nbkg' : "1E7,0,2E7",
	  'dataset'	: "",
	  'datahist'	: "",
	  'low'  : 302,
	  'high' : 1516, 
	},
    },
}
