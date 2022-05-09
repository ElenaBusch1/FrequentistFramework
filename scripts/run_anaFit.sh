#!/bin/bash

{
    . scripts/setup_buildAndFit.sh

    trig=J100
    pars=six

    signalfile=config/dijetTLA/signal/signal_dijetTLA.template
    backgroundfile=config/dijetTLA/background_dijetTLA_${trig/Comb/}yStar06_${pars}Par.xml
    categoryfile=config/dijetTLA/category_dijetTLA.template
    topfile=config/dijetTLA/dijetTLA_J100yStar06.template
    wsfile=run/dijetTLA_combWS_swift.root
    sigmean=1000
    sigwidth=7
    dosignal=1
    dolimit=1
    outputfile=run/FitResult_swift_${pars}Par_${trig}yStar06_mean${sigmean}_width${sigwidth}.root
    rangelow=457
    rangehigh=2997
    # rangelow=302
    # rangehigh=1516
    datafile=Input/data/dijetTLA/unblinding1_mjj_spectra.root
    datahist=L1${trig}/Mjj_1GeVbinning
    nbkg="2E8,0,3E8"
    # datafile=run/PD_Run2_GlobalFit_457_2997_sixPar_finebinned_J100.root
    # datahist=unfluctuated
    # nbkg="1.5E9,0,2E9"
    # datafile=Input/data/dijetTLA/PD_Run2_GlobalFit_302_1516_fivePar_finebinned_J50Comb.root
    # datahist=unfluctuated
    # nbkg="1E9,0,2E9"
    maskthreshold=-1

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
        $flags
}
