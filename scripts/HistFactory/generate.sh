#!/bin/bash

SIGMEANS=( 450 500 550 600 650 700 750 800 850 900 950 1000 1050 1100 1150 1200 1300 1400 1500 1600 1700 1800 ) 
SIGWIDTHS=( 5 7 10 12 15 )

FILE_BKG="Input/model/dijetTLAnlo/HistFactoryInput/templates2021/bkg/dijet_HTystar_00_06_R04_P2_ScaleMjj_standTheoryUncert_rebin4_LO_CT14nnlo_reducedNPs_DataIsJ100_scaledOnly_reweightedNLO_range531_2058_fixedBins_normalized.root"

python python/PrepareTemplates/dijetTLAnlo_genBkg.py --infile $FILE_BKG --outfile "Input/model/dijetTLAnlo/templates2021/LO_CT14nnlo_reducedNPs_scaledOnly_reweightedNLO/HistFactory_dijetTLAnlo_J100yStar06_bkg_ws.root"

mkdir -p Input/model/dijetTLAnlo/HistFactoryInput/templates2021/signal
mkdir -p Input/model/dijetTLAnlo/templates2021/signal

for SIGMEAN in "${SIGMEANS[@]}"
do
    for SIGWIDTH in "${SIGWIDTHS[@]}"
    do
	TMPFILE="Input/model/dijetTLAnlo/HistFactoryInput/templates2021/signal/sigshape_J100yStar06_mean${SIGMEAN}_width${SIGWIDTH}_range531_2058.root"
	OUTFILE="Input/model/dijetTLAnlo/templates2021/signal/HistFactory_dijetTLAnlo_J100yStar06_sig_mean${SIGMEAN}_width${SIGWIDTH}_ws.root"

	python python/PrepareTemplates/createGaussHist.py --infile ${FILE_BKG//_fixedBins_normalized/} --histname "nominal" --sigMean ${SIGMEAN} --sigWidth ${SIGWIDTH} --outfile ${TMPFILE}
	python python/PrepareTemplates/unifyBinning.py ${TMPFILE}

	python python/PrepareTemplates/dijetTLAnlo_genSig.py --infile ${TMPFILE//.root/_fixedBins.root} --outfile ${OUTFILE}
    done
done
