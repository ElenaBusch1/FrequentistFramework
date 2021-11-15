#!/bin/bash

{
    . scripts/setup_buildAndFit.sh

    categoryfile=config/dijetTLA/category_dijetTLA_J100yStar06_fivePar.template
    topfile=config/dijetTLA/dijetTLA_J100yStar06.template
    wsfile=run/dijetTLA_combWS_swift.root
    sigmean=1000
    sigwidth=7
    dosignal=1
    dolimit=1
    outputfile=run/FitResult_swift_fivePar_J100yStar06_bkgonly.root
    rangelow=531
    rangehigh=2058
    datafile=Input/data/dijetTLA/lookInsideTheBoxWithUniformMjj.root
    datahist=Nominal/DSJ100yStar06_TriggerJets_J100_yStar06_mjj_finebinned_all_data
    nbkg="2E8,0,3E8"

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
        $flags

#     datafile=Input/data/dijetTLA/PD_130ifb_GlobalFit_531_2079_fivepar_finebinned_J100.root
#     datahist=pseudodata
#     nbkg="9E8,0,15E8"
#     sigamp=1
#     loopstart=0
#     loopend=5

#     flags=""
#     if (( $dosignal )); then flags="$flags --dosignal"; fi
#     if (( $dolimit )); then flags="$flags --dolimit"; fi

#     ./python/run_injections_anaFit.py \
#     	--datafile $datafile \
#     	--datahist $datahist \
#     	--categoryfile $categoryfile \
#     	--topfile $topfile \
#     	--wsfile $wsfile \
#     	--sigmean $sigmean \
#     	--sigwidth $sigwidth \
#     	--nbkg $nbkg \
#     	--rangelow $rangelow \
#     	--rangehigh $rangehigh \
#     	--outputfile $outputfile \
#       --sigamp $sigamp \
# 	--loopstart $loopstart \
# 	--loopend $loopend \
#       $flags
}
