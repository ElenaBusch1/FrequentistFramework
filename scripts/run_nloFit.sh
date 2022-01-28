#!/bin/bash

{
    . scripts/setup_buildCombineFit.sh

    modelfile=Input/model/dijetTLAnlo/templates2021/LO_CT14nnlo_reducedNPs_scaledOnly_reweightedNLO/HistFactory_dijetTLAnlo_J100yStar06_bkg_ws.root
    bkgfile=config/dijetTLAnlo/templates2021/background_dijetTLAnlo_J100yStar06_CT14nnlo.template
    categoryfile=config/dijetTLAnlo/templates2021/category_dijetTLAnlo_J100yStar06.template
    topfile=config/dijetTLAnlo/templates2021/dijetTLAnlo_J100yStar06.template
    combinefile=config/dijetTLAnlo/Inflation_CT14.template
    wsfile=run/dijetTLAnlo_combWS_nloFit.root
    sigmean=1000
    sigwidth=7
    rangelow=531
    rangehigh=2997
    constr=10
    outputfile=run/FitResult_nloFit_J100yStar06_templates2021_CT14nnlo_scaledOnly_constr${constr}_bkgonly.root
    externalchi2file=Input/model/dijetTLAnlo/templates2021/LO_CT14nnlo_reducedNPs_scaledOnly_reweightedNLO/chi2/chi2_PD_lumi130_scaledOnly_constr${constr}_fit_scaledOnly_constr${constr}_531_2997.root
    externalchi2fct=fit
    externalchi2bins=55
    datafile=Input/data/dijetTLAnlo/binning2021/data_J100yStar06_range171_3217_fixedBins.root
    datahist=data
    nbkg="2E8,0,3E8"
    maskthreshold=0.01
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
}
