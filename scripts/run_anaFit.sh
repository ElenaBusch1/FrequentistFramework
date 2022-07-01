#!/bin/bash

{
    . scripts/setup_buildAndFit.sh

    # for pars in five six seven
    for pars in five
    do
	# for trig in J50Comb J100
	for trig in J100
	do
	    folder=run/outOfTheBoxFit
	    signalfile=config/dijetTLA/signal/signal_dijetTLA.template
	    backgroundfile=config/dijetTLA/background_dijetTLA_${trig/Comb/}yStar06_${pars}Par.template
	    categoryfile=config/dijetTLA/category_dijetTLA.template
	    topfile=config/dijetTLA/dijetTLA_J100yStar06.template
	    wsfile=${folder}/dijetTLA_combWS_${pars}Par_${trig}yStar06.root
	    sigmean=1000
	    sigwidth=7
	    dosignal=1
	    dolimit=1
	    outputfile=${folder}/FitResult_anaFit_${pars}Par_${trig}yStar06_mean${sigmean}_width${sigwidth}.root
	    rangelow=457
	    rangehigh=2997
	    datafile=Input/data/dijetTLA/unblinding1_mjj_spectra.root
	    datahist=L1${trig}/Mjj_1GeVbinning
	    nbkg="dummy" #overwritten by prefit
	    maskthreshold=0.01
	    doprefit=1

	    flags=""
	    if (( $dosignal )); then flags="$flags --dosignal"; fi
	    if (( $dolimit )); then flags="$flags --dolimit"; fi
	    if (( $doprefit )); then flags="$flags --doprefit"; fi

	    ./python/run_anaFit.py \
    		--datafile $datafile \
    		--datahist $datahist \
    		--backgroundfile $backgroundfile \
    		--sigfile $sigfile \
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
		--folder $folder \
		$flags
	done
    done
}
