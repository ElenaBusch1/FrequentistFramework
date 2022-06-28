#!/bin/bash

generatePD=true

{
    . scripts/setup_buildAndFit.sh

    for pars in five six seven
    do
	# for trig in J50Comb J100
	for trig in J100
	do
	    signalfile=config/dijetTLA/signal/signal_dijetTLA.template
	    backgroundfile=config/dijetTLA/background_dijetTLA_${trig/Comb/}yStar06_${pars}Par.template
	    categoryfile=config/dijetTLA/category_dijetTLA.template
	    topfile=config/dijetTLA/dijetTLA_J100yStar06.template
	    wsfile=run/dijetTLA_combWS_anaFit_${pars}Par_${trig}yStar06_bkgonly.root
	    sigmean=1000
	    sigwidth=5
	    dosignal=0
	    dolimit=0
	    maskthreshold=-1
	    outputfile=run/FitResult_anaFit_${pars}Par_${trig}yStar06_bkgonly.root
	    rangelow=302
	    rangehigh=1516
	    nbkg="1E7,0,2.5E7"
	    if [[ $trig == "J100" ]]
	    then
		rangelow=457
		rangehigh=2997
		nbkg="4E7,0,1E8"
	    fi
	    datafile=Input/data/dijetTLA/unblinding1_mjj_spectra.root
	    datahist=L1${trig}/Mjj_1GeVbinning
	    if [[ $trig == "J50Topo" ]]
	    then
		datahist="L1J50_DETA20-J50J(noHLT_j0_perf_ds1_L1J50)/Mjj_1GeVbinning"
	    fi
	    folder=generatePD_531_defaultScale
	    flags=""
	    if (( $dosignal )); then flags="$flags --dosignal"; fi
	    if (( $dolimit )); then flags="$flags --dolimit"; fi

	    ./python/run_anaFit.py \
    		--datafile $datafile \
    		--datahist $datahist \
    		--signalfile $signalfile \
    		--backgroundfile $backgroundfile \
    		--categoryfile $categoryfile \
    		--topfile $topfile \
    		--wsfile $wsfile \
    		--sigmean $sigmean \
    		--sigwidth $sigwidth \
    		--nbkg $nbkg \
    		--rangelow $rangelow \
    		--rangehigh $rangehigh \
    		--outputfile $outputfile \
		--maskthreshold $maskthreshold \
		--doprefit \
		--folder $folder \
		$flags

	    if [[ $generatePD == true ]]
	    then

		if [[ $trig == "J40" ]]
		then
		    scalefactor=$( bc <<< 'scale=2; 3.3/0.342' )
		fi
		if [[ $trig == "J50" ]]
		then
		    scalefactor=$(  bc <<< 'scale=2; 5.77/0.114' )
		fi
		if [[ $trig == "J50Topo" ]]
		then
		    scalefactor=$( bc <<< 'scale=2; 9.22/0.185' )
		fi
		if [[ $trig == "J50Comb" ]]
		then
		    scalefactor=$( bc <<< 'scale=2; 14.5/0.299' )
		fi
		if [[ $trig == "J100" ]]
		then
		    scalefactor=$( bc <<< 'scale=2; 133.2/3.630' )
		fi

		toys=1000
		
		echo python python/generatePseudoData.py --infile ${outputfile/FitResult/PostFit} --inhist J100yStar06/postfit --outhist pseudodata --outfile run/PD_Run2_GlobalFit_${rangelow}_${rangehigh}_${pars}Par_finebinned_${trig}.root --nreplicas $toys --scaling $scalefactor

		python python/generatePseudoData.py --infile ${outputfile/FitResult/PostFit} --inhist J100yStar06/postfit --outhist pseudodata --outfile run/PD_Run2_GlobalFit_${rangelow}_${rangehigh}_${pars}Par_finebinned_${trig}.root --nreplicas $toys --scaling $scalefactor

	    fi
	done
    done
}
