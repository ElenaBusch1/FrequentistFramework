#!/bin/bash

#  Mass grid defined as in morphing:
mR=( 250 350 450 550 650 750 850 )
#mR=( 250 )



for mass in ${mR[@]}
do
  echo "Processing mass point $mass"
  FILE_TEMPLATES="/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/massSpectraFullTrain_decorr2_SRAlpha_200_BkgAlpha_200_dimVars_pt_cutVal_6_${mass}.root"
  OUT_FILE="/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/Input/signal/HistFactory_dijetISR_mR${mass}.root"
  echo ../python/PrepareTemplates/dijetTLA_genJJJSignals.py --infile ${FILE_TEMPLATES} --mass ${mass} --outfile ${OUT_FILE}
  python ../python/PrepareTemplates/dijetTLA_genJJJSignals.py --infile ${FILE_TEMPLATES} --mass ${mass} --outfile ${OUT_FILE}
done

