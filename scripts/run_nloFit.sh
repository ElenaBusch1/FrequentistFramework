#!/bin/bash

{
    . scripts/setup_buildCombineFit.sh

    modelfile=Input/model/dijetTLAnlo/templates2021/LO_CT14nnlo_reducedNPs_scaledOnly_reweightedNLO/HistFactory_dijetTLAnlo_J100yStar06_bkg_ws.root
    bkgfile=config/dijetTLAnlo/templates2021/background_dijetTLAnlo_J100yStar06_CT14nnlo.template
    sigfile=config/dijetTLAnlo/templates2021/signal/signal_dijetTLAnlo_J100yStar06.template
    categoryfile=config/dijetTLAnlo/templates2021/category_dijetTLAnlo_J100yStar06.template
    topfile=config/dijetTLAnlo/templates2021/dijetTLAnlo_J100yStar06.template
    combinefile=config/dijetTLAnlo/Inflation_CT14.template
    wsfile=run/dijetTLAnlo_combWS_nloFit.root
    sigmean=1000
    sigwidth=7
    rangelow=302
    rangehigh=1516
    # rangelow=457
    # rangehigh=2997
    constr=5
    signalmodelfile=Input/model/dijetTLAnlo/templates2021/signal/HistFactory_dijetTLAnlo_J100yStar06_sig_mean${sigmean}_width${sigwidth}_ws.root
    outputfile=run/FitResult_nloFit_J50CombyStar06_templates2021_CT14nnlo_scaledOnly_constr${constr}_mean${sigmean}_width${sigwidth}.root
    externalchi2file=Input/model/dijetTLAnlo/templates2021/LO_CT14nnlo_reducedNPs_scaledOnly_reweightedNLO/chi2/chi2_PD_lumi130_scaledOnly_constr${constr}_fit_scaledOnly_constr${constr}_531_2997.root
    externalchi2fct=fit
    externalchi2bins=55
    datafile=Input/data/dijetTLAnlo/binning2021/data_J100yStar06_range171_3217_fixedBins.root
    datahist=data
    nbkg="2E8,0,3E8"
    # datafile=Input/data/dijetTLAnlo/binning2021/PD_Run2_nloFit_CT14nnlo_constr10_${rangelow}_${rangehigh}_J50Comb_range171_3217_fixedBins.root
    # datafile=Input/data/dijetTLAnlo/binning2021/PD_Run2_nloFit_CT14nnlo_constr10_${rangelow}_${rangehigh}_J50Comb_range171_3217.root
    # datahist=unfluctuated
    # nbkg="1E9,0,2E9"
    # datafile=Input/data/dijetTLAnlo/binning2021/unblinding1_mjj_spectra_range171_3217_fixedBins.root
    # datahist=L1J50Comb/Mjj_TLA2022binning
    # datahist="L1J50_DETA20-J50J(noHLT_j0_perf_ds1_L1J50)/Mjj_TLA2022binning"
    # nbkg="1E7,0,2E7"
    maskthreshold=-1
    doinitialpars=1
    dosignal=1
    dolimit=1

    flags=""
    if (( $doinitialpars )); then flags="$flags --doinitialpars"; fi
    if (( $dosignal )); then flags="$flags --dosignal"; fi
    if (( $dolimit )); then flags="$flags --dolimit"; fi
    
    ./python/run_nloFit.py \
    	--datafile $datafile \
    	--datahist $datahist \
    	--modelfile $modelfile \
    	--signalmodelfile $signalmodelfile \
    	--bkgfile $bkgfile \
    	--sigfile $sigfile \
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
}
