#!/bin/bash

dirname=${PWD##*/}

if [[ ! -d xmlAnaWSBuilder ]] || [[ ! -d quickFit ]]; then
    echo "Execute from FrequentistFramework directory!"
    return 1
fi

if [[ -z $_DIRXMLWSBUILDER ]]; then
    cd xmlAnaWSBuilder/
    source setup_lxplus.sh
    cd ..
fi

if [[ -z $_DIRFIT ]]; then
    cd quickFit/
    source setup_lxplus.sh
    cd ..
fi

mkdir -p run


# setting some default inputs if not given by env vars
if [[ -z $datafile ]]; then
    # datafile=Input/data/dijetTLAnlo/data_J75yStar03_range400_2079_fixedBins.root
    # datafile=Input/data/dijetTLAnlo/injections/pseudodata_J100yStar06_Juno100fb_range531_2079_mean600_width5_amp0_fixedBins.root
    datafile=Input/data/dijetTLAnlo/data_J100yStar06_range531_2079_fixedBins.root
fi
if [[ -z $datahist ]]; then
    # datahist=pseudodata_0
    datahist=data
fi
if [[ -z $categoryfile ]]; then
    # categoryfile=config/dijetTLAnlo/category_dijetTLAnlo_J75yStar03.template
    categoryfile=config/dijetTLAnlo/category_dijetTLAnlo_J100yStar06.template
fi
if [[ -z $topfile ]]; then
    # topfile=config/dijetTLAnlo/dijetTLAnlo_J75yStar03.template
    topfile=config/dijetTLAnlo/dijetTLAnlo_J100yStar06.template
fi
if [[ -z $wsfile ]]; then
    wsfile=run/dijetTLAnlo_combWS_testTemplate.root
fi
if [[ -z $sigmean ]]; then
    sigmean=550
fi
if [[ -z $sigwidth ]]; then
    sigwidth=5
fi
if [[ -z $outputfile ]]; then
    # outputfile=run/FitResult_J75yStar03_mean${sigmean}_width${sigwidth}.root
    outputfile=run/FitResult_J100yStar06_mean${sigmean}_width${sigwidth}.root
fi

tmpcategoryfile=run/category_dijetTLAnlo_fromTemplate.xml
tmptopfile=run/dijetTLAnlo_fromTemplate.xml

# generate the config files on the fly in run dir
if [ ! -f run/AnaWSBuilder.dtd ]; then
    ln -s ../config/dijetTLAnlo/AnaWSBuilder.dtd run/AnaWSBuilder.dtd
fi

cp ${categoryfile} ${tmpcategoryfile}
# cp config/dijetTLAnlo/category_dijetTLAnlo_J100yStar06.template ${categoryfile}
sed -i "s@DATAFILE@${datafile}@g" ${tmpcategoryfile} #@ because datafile contains /
sed -i "s@DATAHIST@${datahist}@g" ${tmpcategoryfile}
 
cp ${topfile} ${tmptopfile}
# cp config/dijetTLAnlo/dijetTLAnlo_J100yStar06.template ${topfile}
sed -i "s@CATEGORYFILE@${tmpcategoryfile}@g" ${tmptopfile}
sed -i "s@OUTPUTFILE@${wsfile}@g" ${tmptopfile}

xmlAnaWSBuilder/exe/XMLReader -x ${tmptopfile} -o "logy integral" -s 0 # minimizer strategy fast, binned data 
if [[ $? != 0 ]]; then
    echo "Non-zero return code from XMLReader. Check if tolerable"
fi


# need to pass POI first and fix all others to 0
# PARS="nsig_mean500_width5=0,nsig_mean500_width7=0,nsig_mean500_width10=0,nsig_mean500_width12=0,nsig_mean500_width15=0,nsig_mean600_width5=0,nsig_mean600_width7=0,nsig_mean600_width10=0,nsig_mean600_width12=0,nsig_mean600_width15=0,nsig_mean700_width5=0,nsig_mean700_width7=0,nsig_mean700_width10=0,nsig_mean700_width12=0,nsig_mean700_width15=0,nsig_mean800_width5=0,nsig_mean800_width7=0,nsig_mean800_width10=0,nsig_mean800_width12=0,nsig_mean800_width15=0,nsig_mean900_width5=0,nsig_mean900_width7=0,nsig_mean900_width10=0,nsig_mean900_width12=0,nsig_mean900_width15=0,nsig_mean1000_width5=0,nsig_mean1000_width7=0,nsig_mean1000_width10=0,nsig_mean1000_width12=0,nsig_mean1000_width15=0,nsig_mean1100_width5=0,nsig_mean1100_width7=0,nsig_mean1100_width10=0,nsig_mean1100_width12=0,nsig_mean1100_width15=0,nsig_mean1200_width5=0,nsig_mean1200_width7=0,nsig_mean1200_width10=0,nsig_mean1200_width12=0,nsig_mean1200_width15=0,nsig_mean1300_width5=0,nsig_mean1300_width7=0,nsig_mean1300_width10=0,nsig_mean1300_width12=0,nsig_mean1300_width15=0"
PARS="nsig_mean450_width5=0,nsig_mean450_width7=0,nsig_mean450_width10=0,nsig_mean450_width12=0,nsig_mean450_width15=0,nsig_mean500_width5=0,nsig_mean500_width7=0,nsig_mean500_width10=0,nsig_mean500_width12=0,nsig_mean500_width15=0,nsig_mean550_width5=0,nsig_mean550_width7=0,nsig_mean550_width10=0,nsig_mean550_width12=0,nsig_mean550_width15=0,nsig_mean600_width5=0,nsig_mean600_width7=0,nsig_mean600_width10=0,nsig_mean600_width12=0,nsig_mean600_width15=0,nsig_mean650_width5=0,nsig_mean650_width7=0,nsig_mean650_width10=0,nsig_mean650_width12=0,nsig_mean650_width15=0,nsig_mean700_width5=0,nsig_mean700_width7=0,nsig_mean700_width10=0,nsig_mean700_width12=0,nsig_mean700_width15=0,nsig_mean750_width5=0,nsig_mean750_width7=0,nsig_mean750_width10=0,nsig_mean750_width12=0,nsig_mean750_width15=0,nsig_mean800_width5=0,nsig_mean800_width7=0,nsig_mean800_width10=0,nsig_mean800_width12=0,nsig_mean800_width15=0,nsig_mean850_width5=0,nsig_mean850_width7=0,nsig_mean850_width10=0,nsig_mean850_width12=0,nsig_mean850_width15=0,nsig_mean900_width5=0,nsig_mean900_width7=0,nsig_mean900_width10=0,nsig_mean900_width12=0,nsig_mean900_width15=0,nsig_mean950_width5=0,nsig_mean950_width7=0,nsig_mean950_width10=0,nsig_mean950_width12=0,nsig_mean950_width15=0,nsig_mean1000_width5=0,nsig_mean1000_width7=0,nsig_mean1000_width10=0,nsig_mean1000_width12=0,nsig_mean1000_width15=0,nsig_mean1050_width5=0,nsig_mean1050_width7=0,nsig_mean1050_width10=0,nsig_mean1050_width12=0,nsig_mean1050_width15=0,nsig_mean1100_width5=0,nsig_mean1100_width7=0,nsig_mean1100_width10=0,nsig_mean1100_width12=0,nsig_mean1100_width15=0,nsig_mean1150_width5=0,nsig_mean1150_width7=0,nsig_mean1150_width10=0,nsig_mean1150_width12=0,nsig_mean1150_width15=0,nsig_mean1200_width5=0,nsig_mean1200_width7=0,nsig_mean1200_width10=0,nsig_mean1200_width12=0,nsig_mean1200_width15=0,nsig_mean1300_width5=0,nsig_mean1300_width7=0,nsig_mean1300_width10=0,nsig_mean1300_width12=0,nsig_mean1300_width15=0,nsig_mean1400_width5=0,nsig_mean1400_width7=0,nsig_mean1400_width10=0,nsig_mean1400_width12=0,nsig_mean1400_width15=0,nsig_mean1500_width5=0,nsig_mean1500_width7=0,nsig_mean1500_width10=0,nsig_mean1500_width12=0,nsig_mean1500_width15=0,nsig_mean1600_width5=0,nsig_mean1600_width7=0,nsig_mean1600_width10=0,nsig_mean1600_width12=0,nsig_mean1600_width15=0,nsig_mean1700_width5=0,nsig_mean1700_width7=0,nsig_mean1700_width10=0,nsig_mean1700_width12=0,nsig_mean1700_width15=0,nsig_mean1800_width5=0,nsig_mean1800_width7=0,nsig_mean1800_width10=0,nsig_mean1800_width12=0,nsig_mean1800_width15=0"
PARS=${PARS/nsig_mean${sigmean}_width${sigwidth}=0/} # remove relevant fix to 0
PARS="nsig_mean${sigmean}_width${sigwidth},${PARS}"  # add to front
PARS=${PARS/,,/,} # remove double ,
PARS=${PARS%,}    # remove trailing ,

quickFit -f ${wsfile} -d combData -p ${PARS} --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 -o ${outputfile}
if [[ $? != 0 ]]; then
    echo "Non-zero return code from quickFit. Check if tolerable"
fi

quickLimit -f ${wsfile} -d combData -p ${PARS} --checkWS 1 --hesse 1 --initialGuess 1000000 -o ${outputfile/FitResult/Limits}
if [[ $? != 0 ]]; then
    echo "Non-zero return code from quickLimit. Check if tolerable"
fi
