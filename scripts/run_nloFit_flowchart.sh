#!/bin/bash

{
    . scripts/setup_buildCombineFit.sh

    for constr in 1 2 5 10 20 50 100
    # for constr in 100 200
    do
	# for trig in J40 J50Comb J100
	for trig in J50Comb J100
	do
	    modelfile=Input/model/dijetTLAnlo/templates2021/LO_CT14nnlo_reducedNPs_scaledOnly_reweightedNLO/HistFactory_dijetTLAnlo_J100yStar06_bkg_ws.root
	    bkgfile=config/dijetTLAnlo/templates2021/background_dijetTLAnlo_J100yStar06_CT14nnlo.template
	    categoryfile=config/dijetTLAnlo/templates2021/category_dijetTLAnlo_J100yStar06.template
	    topfile=config/dijetTLAnlo/templates2021/dijetTLAnlo_J100yStar06.template
	    combinefile=config/dijetTLAnlo/Inflation_CT14.template
	    wsfile=run/dijetTLAnlo_combWS_nloFit.root
	    sigmean=1000
	    sigwidth=5

	    rangelow=302
	    rangehigh=1516
	    nbkg="1E7,0,3E7"
	    if [[ $trig == "J100" ]]
	    then
		rangelow=457
		rangehigh=2997
		nbkg="4E7,0,1E8"
	    fi

	    outputfile=run/FitResult_nloFit_${trig}yStar06_templates2021_CT14nnlo_scaledOnly_constr${constr}_bkgonly.root
	    externalchi2fct=fit
	    
	    # externalchi2file=Input/model/dijetTLAnlo/templates2021/LO_CT14nnlo_reducedNPs_scaledOnly_reweightedNLO/chi2/chi2_PD_lumi130_scaledOnly_constr${constr}_fit_scaledOnly_constr${constr}_531_2997.root
	    # externalchi2bins=55
	    externalchi2file=Input/model/dijetTLAnlo/templates2021/LO_CT14nnlo_reducedNPs_scaledOnly_reweightedNLO/chi2/chi2_range_457_2997_J100_constr${constr}.root
	    externalchi2bins=58
	    if [[ $trig =~ "J50" || $trig =~ "J40" ]]
	    then
		externalchi2file=Input/model/dijetTLAnlo/templates2021/LO_CT14nnlo_reducedNPs_scaledOnly_reweightedNLO/chi2/chi2_range_302_1516_J50Comb_constr${constr}.root
		externalchi2bins=39
	    fi

	    datafile=Input/data/dijetTLAnlo/binning2021/unblinding1_mjj_spectra_range171_3217_fixedBins.root
	    datahist=L1${trig}/Mjj_TLA2022binning
	    if [[ $trig == "J50Topo" ]]
	    then
		datahist="L1J50_DETA20-J50J(noHLT_j0_perf_ds1_L1J50)/Mjj_TLA2022binning"
	    fi
	    maskthreshold=-1
	    doinitialpars=1
	    dosignal=0
	    dolimit=0

	    flags=""
	    if (( $doinitialpars )); then flags="$flags --doinitialpars"; fi
	    if (( $dosignal )); then flags="$flags --dosignal"; fi
	    if (( $dolimit )); then flags="$flags --dolimit"; fi
	    
	    ./python/run_nloFit.py \
    		--datafile $datafile \
    		--datahist $datahist \
    		--modelfile $modelfile \
    		--bkgfile $bkgfile \
    		--categoryfile $categoryfile \
    		--topfile $topfile \
    		--combinefile $combinefile \
    		--wsfile $wsfile \
    		--sigmean $sigmean \
    		--sigwidth $sigwidth \
    		--nbkg $nbkg \
    		--rangelow $rangelow \
    		--rangehigh $rangehigh \
    		--outputfile $outputfile \
		--constr $constr \
		--externalchi2file $externalchi2file \
		--externalchi2fct $externalchi2fct \
		--externalchi2bins $externalchi2bins \
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
	    
	    # echo python python/generatePseudoData.py --infile ${outputfile/FitResult/PostFit} --inhist postfit --outhist pseudodata --outfile run/PD_Run2_nloFit_CT14nnlo_constr${constr}_${rangelow}_${rangehigh}_${trig}.root --nreplicas 10000 --scaling $scalefactor
	    # python python/generatePseudoData.py --infile ${outputfile/FitResult/PostFit} --inhist postfit --outhist pseudodata --outfile run/PD_Run2_nloFit_CT14nnlo_constr${constr}_${rangelow}_${rangehigh}_${trig}.root --nreplicas 10000 --scaling $scalefactor
	done
    done
}
