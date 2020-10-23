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
    datafile=Input/data/dijetTLA/lookInsideTheBoxWithUniformMjj.root
fi
if [[ -z $datahist ]]; then
    # datahist=Nominal/DSJ75yStar03_TriggerJets_J75_yStar03_mjj_finebinned_all_data
    datahist=Nominal/DSJ100yStar06_TriggerJets_J100_yStar06_mjj_finebinned_all_data
fi
if [[ -z $categoryfile ]]; then
    # categoryfile=config/dijetTLA/category_dijetTLA_J75yStar03.template
    categoryfile=config/dijetTLA/category_dijetTLA_J100yStar06.template
fi
if [[ -z $topfile ]]; then
    # topfile=config/dijetTLA/dijetTLA_J75yStar03.template
    topfile=config/dijetTLA/dijetTLA_J100yStar06.template
fi
if [[ -z $wsfile ]]; then
    wsfile=run/dijetTLAnlo_combWS_swift.root
fi
if [[ -z $sigmean ]]; then
    sigmean=1800
fi
if [[ -z $sigwidth ]]; then
    sigwidth=7
fi
if [[ -z $outputfile ]]; then
    # outputfile=run/FitResult_swift_J75yStar03_mean${sigmean}_width${sigwidth}.root
    outputfile=run/FitResult_swift_J100yStar06_mean${sigmean}_width${sigwidth}.root
fi

#window half width (full window = 2*whw+1)
whw=9
if [[ $topfile == *"J75"* ]]; then
    whw=13
fi

binedges=( 400 420 441 462 484 507 531 555 580 606 633 661 690 720 751 784 818 853 889 927 966 1007 1049 1093 1139 1186 1235 1286 1339 1394 1451 1511 1573 1637 1704 1773 1845 1920 1998 2079 2163 2251 2342 2437 2536 2639 2746 2857 2973 3094 3220 3351 3487 3629 3776 3929 4088 4254 )
nbinedges=${#binedges[@]}
binlow=0
binhigh=$((nbinedges - 1))

i=0
for edge in ${binedges[@]}; do
    if (($edge > $sigmean)); then
	if (($i < $whw + 1)); then
	    binlow=0
	else
	    binlow=$((i - whw - 1))
	fi
	if [[ $topfile == *"J100"* ]] && (( $binlow < 6 )); then
	    binlow=6
	fi
	binhigh=$((binlow + 2*whw))
	break
    fi
    i=$((i+1))
done

rangelow=${binedges[$binlow]}
rangehigh=${binedges[$((binhigh+1))]} 
bins=$((rangehigh - rangelow))

echo "Fitting $bins bins in range $rangelow - $rangehigh"

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
sed -i "s@RANGELOW@${rangelow}@g" ${tmpcategoryfile}
sed -i "s@RANGEHIGH@${rangehigh}@g" ${tmpcategoryfile}
sed -i "s@BINS@${bins}@g" ${tmpcategoryfile}
 
cp ${topfile} ${tmptopfile}
# cp config/dijetTLAnlo/dijetTLAnlo_J100yStar06.template ${topfile}
sed -i "s@CATEGORYFILE@${tmpcategoryfile}@g" ${tmptopfile}
sed -i "s@OUTPUTFILE@${wsfile}@g" ${tmptopfile}

xmlAnaWSBuilder/exe/XMLReader -x ${tmptopfile} -o "logy integral" -s 0 # minimizer strategy fast, binned data 
if [[ $? != 0 ]]; then
    echo "Non-zero return code from XMLReader. Check if tolerable"
fi

# need to pass POI first and fix all others to 0
PARS="nsig_mean450_width5=0,nsig_mean450_width7=0,nsig_mean450_width10=0,nsig_mean450_width12=0,nsig_mean450_width15=0,nsig_mean500_width5=0,nsig_mean500_width7=0,nsig_mean500_width10=0,nsig_mean500_width12=0,nsig_mean500_width15=0,nsig_mean550_width5=0,nsig_mean550_width7=0,nsig_mean550_width10=0,nsig_mean550_width12=0,nsig_mean550_width15=0,nsig_mean600_width5=0,nsig_mean600_width7=0,nsig_mean600_width10=0,nsig_mean600_width12=0,nsig_mean600_width15=0,nsig_mean650_width5=0,nsig_mean650_width7=0,nsig_mean650_width10=0,nsig_mean650_width12=0,nsig_mean650_width15=0,nsig_mean700_width5=0,nsig_mean700_width7=0,nsig_mean700_width10=0,nsig_mean700_width12=0,nsig_mean700_width15=0,nsig_mean750_width5=0,nsig_mean750_width7=0,nsig_mean750_width10=0,nsig_mean750_width12=0,nsig_mean750_width15=0,nsig_mean800_width5=0,nsig_mean800_width7=0,nsig_mean800_width10=0,nsig_mean800_width12=0,nsig_mean800_width15=0,nsig_mean850_width5=0,nsig_mean850_width7=0,nsig_mean850_width10=0,nsig_mean850_width12=0,nsig_mean850_width15=0,nsig_mean900_width5=0,nsig_mean900_width7=0,nsig_mean900_width10=0,nsig_mean900_width12=0,nsig_mean900_width15=0,nsig_mean950_width5=0,nsig_mean950_width7=0,nsig_mean950_width10=0,nsig_mean950_width12=0,nsig_mean950_width15=0,nsig_mean1000_width5=0,nsig_mean1000_width7=0,nsig_mean1000_width10=0,nsig_mean1000_width12=0,nsig_mean1000_width15=0,nsig_mean1050_width5=0,nsig_mean1050_width7=0,nsig_mean1050_width10=0,nsig_mean1050_width12=0,nsig_mean1050_width15=0,nsig_mean1100_width5=0,nsig_mean1100_width7=0,nsig_mean1100_width10=0,nsig_mean1100_width12=0,nsig_mean1100_width15=0,nsig_mean1150_width5=0,nsig_mean1150_width7=0,nsig_mean1150_width10=0,nsig_mean1150_width12=0,nsig_mean1150_width15=0,nsig_mean1200_width5=0,nsig_mean1200_width7=0,nsig_mean1200_width10=0,nsig_mean1200_width12=0,nsig_mean1200_width15=0,nsig_mean1300_width5=0,nsig_mean1300_width7=0,nsig_mean1300_width10=0,nsig_mean1300_width12=0,nsig_mean1300_width15=0,nsig_mean1400_width5=0,nsig_mean1400_width7=0,nsig_mean1400_width10=0,nsig_mean1400_width12=0,nsig_mean1400_width15=0,nsig_mean1500_width5=0,nsig_mean1500_width7=0,nsig_mean1500_width10=0,nsig_mean1500_width12=0,nsig_mean1500_width15=0,nsig_mean1600_width5=0,nsig_mean1600_width7=0,nsig_mean1600_width10=0,nsig_mean1600_width12=0,nsig_mean1600_width15=0,nsig_mean1700_width5=0,nsig_mean1700_width7=0,nsig_mean1700_width10=0,nsig_mean1700_width12=0,nsig_mean1700_width15=0,nsig_mean1800_width5=0,nsig_mean1800_width7=0,nsig_mean1800_width10=0,nsig_mean1800_width12=0,nsig_mean1800_width15=0"
PARS=${PARS/nsig_mean${sigmean}_width${sigwidth}=0/} # remove relevant fix to 0
PARS="nsig_mean${sigmean}_width${sigwidth},${PARS}"  # add to front
PARS=${PARS/,,/,} # remove double ,
PARS=${PARS%,}    # remove trailing ,

echo "Now running quickFit"
quickFit -f ${wsfile} -d combData -p $PARS --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 -o ${outputfile}
if [[ $? != 0 ]]; then
    echo "Non-zero return code from quickFit. Check if tolerable"
fi

echo "Now running quickLimit"
quickLimit -f ${wsfile} -d combData -p $PARS --checkWS 1 --hesse 1 --initialGuess 100000 -o ${outputfile/FitResult/Limits}
if [[ $? != 0 ]]; then
    echo "Non-zero return code from quickLimit. Check if tolerable"
fi
