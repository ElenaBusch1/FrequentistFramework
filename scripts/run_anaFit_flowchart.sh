#!/bin/bash

{
    . scripts/setup_buildAndFit.sh

    for pars in four five six
    do
	# for trig in J40 J50Comb J100
	for trig in J50Comb
	do
	    categoryfile=config/dijetTLA/category_dijetTLA_J100yStar06_${pars}Par.template
	    topfile=config/dijetTLA/dijetTLA_J100yStar06.template
	    wsfile=run/dijetTLA_combWS_swift.root
	    sigmean=1000
	    sigwidth=5
	    dosignal=0
	    dolimit=0
	    maskthreshold=-1
	    outputfile=run/FitResult_anaFit_${pars}Par_${trig}yStar06_bkgonly.root
	    rangelow=302
	    rangehigh=1516
	    nbkg="1E7,0,2E7"
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

	    flags=""
	    if (( $dosignal )); then flags="$flags --dosignal"; fi
	    if (( $dolimit )); then flags="$flags --dolimit"; fi

	    ./python/run_anaFit.py \
    		--datafile $datafile \
    		--datahist $datahist \
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
		$flags

	    if [[ $trig == "J40" ]]
	    then
		scalefactor=$( bc <<< '3.3/0.342' )
	    fi
	    if [[ $trig == "J50" ]]
	    then
		scalefactor=$(  bc <<< '5.77/0.114' )
	    fi
	    if [[ $trig == "J50Topo" ]]
	    then
		scalefactor=$( bc <<< '9.22/0.185' )
	    fi
	    if [[ $trig == "J50Comb" ]]
	    then
		scalefactor=$( bc <<< '14.5/0.299' )
	    fi
	    if [[ $trig == "J100" ]]
	    then
		scalefactor=$( bc <<< '133.2/3.630' )
	    fi
	    
	    echo python python/generatePseudoData.py --infile ${outputfile/FitResult/PostFit} --inhist J100yStar06/postfit --outhist pseudodata --outfile run/PD_Run2_GlobalFit_${rangelow}_${rangehigh}_${pars}Par_finebinned_${trig}.root --nreplicas 1000 --scaling $scalefactor

	    python python/generatePseudoData.py --infile ${outputfile/FitResult/PostFit} --inhist J100yStar06/postfit --outhist pseudodata --outfile run/PD_Run2_GlobalFit_${rangelow}_${rangehigh}_${pars}Par_finebinned_${trig}.root --nreplicas 1000 --scaling $scalefactor
	done
    done
}
