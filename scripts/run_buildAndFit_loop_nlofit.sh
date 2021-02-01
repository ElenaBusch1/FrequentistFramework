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

trap 'echo caught interrupt and exiting;exit' INT

# setting some default inputs if not given by env vars
if [[ -z $datafile ]]; then
    datafile=Input/data/dijetTLAnlo/PD_130ifb_GlobalFit_fivepar_resbinned_J100.root
fi
if [[ -z $datahist ]]; then
    datahist=pseudodata
fi
if [[ -z $categoryfile ]]; then
    categoryfile=config/dijetTLAnlo/category_dijetTLAnlo_J100yStar06.template
fi
if [[ -z $topfile ]]; then
    topfile=config/dijetTLAnlo/dijetTLAnlo_J100yStar06.template
fi
if [[ -z $wsfile ]]; then
    wsfile=run/dijetTLAnlo_combWS_nlofit.root
fi
if [[ -z $sigmean ]]; then
    sigmean=1000
fi
if [[ -z $sigwidth ]]; then
    sigwidth=7
fi
if [[ -z $sigamp ]]; then
    sigamp=7
fi
if [[ -z $sigfit ]]; then
    sigfit=true
fi
if [[ -z $nbkg ]]; then
    nbkg="9E8,0,15E8"
fi
if [[ -z $outputfile ]]; then
    outputfile=run/FitResult_nlofit_J100yStar06_mean${sigmean}_width${sigwidth}_amp${sigamp}.root
fi

tmpcategoryfile=run/category_dijetTLAnlo_fromTemplate.xml
tmptopfile=run/dijetTLAnlo_fromTemplate.xml

injecteddatafile=$datafile
# need to use bc for bash to understand floating points...
if (( $(echo "$sigamp > 0" | bc -l) )); then
    echo "Injecting signal of amplitude ${sigamp}sigma (FWHM)"

    injecteddatafile=`basename $datafile`
    injecteddatafile="run/${injecteddatafile/.root/_injected_mean${sigmean}_width${sigwidth}_amp${sigamp}.root}"
    echo "python python/InjectGaussian.py --infile $datafile --histname $datahist --sigmean $sigmean --sigwidth $sigwidth --sigamp $sigamp --outfile $injecteddatafile"
    python python/InjectGaussian.py --infile $datafile --histname $datahist --sigmean $sigmean --sigwidth $sigwidth --sigamp $sigamp --outfile $injecteddatafile
fi

templatebinning=Input/data/dijetTLAnlo/data_J100yStar06_range531_2079_fixedBins.root
if [[ $topfile == *"J75"* ]]; then
    templatebinning=Input/data/dijetTLAnlo/data_J75yStar03_range400_2079_fixedBins.root
fi

# apply uniform binning
injecteddatafileorigbinned=$injecteddatafile

if [[ $injecteddatafile != *"_fixedBins.root" ]]; then
    python python/unifyBinning.py $injecteddatafile
    injecteddatafilerebinned=${injecteddatafile/.root/_fixedBins.root}
    injecteddatafile=$injecteddatafilerebinned
fi

# generate the config files on the fly in run dir
if [ ! -f run/AnaWSBuilder.dtd ]; then
    ln -s ../config/dijetTLAnlo/AnaWSBuilder.dtd run/AnaWSBuilder.dtd
fi

for i in {0..49}
# for i in 0
do

    loopoutputfile=${outputfile/.root/_${i}.root}
    loopdatahist=${datahist}_${i}
    echo $loopoutputfile

    cp ${categoryfile} ${tmpcategoryfile}
    # cp config/dijetTLAnlo/category_dijetTLAnlo_J100yStar06.template ${categoryfile}
    sed -i "s@DATAFILE@${injecteddatafile}@g" ${tmpcategoryfile} #@ because datafile contains /
    sed -i "s@DATAHIST@${loopdatahist}@g" ${tmpcategoryfile}
    sed -i "s@RANGELOW@${rangelow}@g" ${tmpcategoryfile}
    sed -i "s@RANGEHIGH@${rangehigh}@g" ${tmpcategoryfile}
    sed -i "s@BINS@${bins}@g" ${tmpcategoryfile}
    sed -i "s@NBKG@${nbkg}@g" ${tmpcategoryfile}
    
    cp ${topfile} ${tmptopfile}
    # cp config/dijetTLAnlo/dijetTLAnlo_J100yStar06.template ${topfile}
    sed -i "s@CATEGORYFILE@${tmpcategoryfile}@g" ${tmptopfile}
    sed -i "s@OUTPUTFILE@${wsfile}@g" ${tmptopfile}

    xmlAnaWSBuilder/exe/XMLReader -x ${tmptopfile} -o "logy integral" -s 0 # minimizer strategy fast, binned data 
    if [[ $? != 0 ]]; then
	echo "Non-zero return code from XMLReader. Check if tolerable"
    fi

    # # need to pass POI first and fix all others to 0
    # PARS="nsig_mean450_width5=0,nsig_mean450_width7=0,nsig_mean450_width10=0,nsig_mean450_width12=0,nsig_mean450_width15=0,nsig_mean500_width5=0,nsig_mean500_width7=0,nsig_mean500_width10=0,nsig_mean500_width12=0,nsig_mean500_width15=0,nsig_mean550_width5=0,nsig_mean550_width7=0,nsig_mean550_width10=0,nsig_mean550_width12=0,nsig_mean550_width15=0,nsig_mean600_width5=0,nsig_mean600_width7=0,nsig_mean600_width10=0,nsig_mean600_width12=0,nsig_mean600_width15=0,nsig_mean650_width5=0,nsig_mean650_width7=0,nsig_mean650_width10=0,nsig_mean650_width12=0,nsig_mean650_width15=0,nsig_mean700_width5=0,nsig_mean700_width7=0,nsig_mean700_width10=0,nsig_mean700_width12=0,nsig_mean700_width15=0,nsig_mean750_width5=0,nsig_mean750_width7=0,nsig_mean750_width10=0,nsig_mean750_width12=0,nsig_mean750_width15=0,nsig_mean800_width5=0,nsig_mean800_width7=0,nsig_mean800_width10=0,nsig_mean800_width12=0,nsig_mean800_width15=0,nsig_mean850_width5=0,nsig_mean850_width7=0,nsig_mean850_width10=0,nsig_mean850_width12=0,nsig_mean850_width15=0,nsig_mean900_width5=0,nsig_mean900_width7=0,nsig_mean900_width10=0,nsig_mean900_width12=0,nsig_mean900_width15=0,nsig_mean950_width5=0,nsig_mean950_width7=0,nsig_mean950_width10=0,nsig_mean950_width12=0,nsig_mean950_width15=0,nsig_mean1000_width5=0,nsig_mean1000_width7=0,nsig_mean1000_width10=0,nsig_mean1000_width12=0,nsig_mean1000_width15=0,nsig_mean1050_width5=0,nsig_mean1050_width7=0,nsig_mean1050_width10=0,nsig_mean1050_width12=0,nsig_mean1050_width15=0,nsig_mean1100_width5=0,nsig_mean1100_width7=0,nsig_mean1100_width10=0,nsig_mean1100_width12=0,nsig_mean1100_width15=0,nsig_mean1150_width5=0,nsig_mean1150_width7=0,nsig_mean1150_width10=0,nsig_mean1150_width12=0,nsig_mean1150_width15=0,nsig_mean1200_width5=0,nsig_mean1200_width7=0,nsig_mean1200_width10=0,nsig_mean1200_width12=0,nsig_mean1200_width15=0,nsig_mean1300_width5=0,nsig_mean1300_width7=0,nsig_mean1300_width10=0,nsig_mean1300_width12=0,nsig_mean1300_width15=0,nsig_mean1400_width5=0,nsig_mean1400_width7=0,nsig_mean1400_width10=0,nsig_mean1400_width12=0,nsig_mean1400_width15=0,nsig_mean1500_width5=0,nsig_mean1500_width7=0,nsig_mean1500_width10=0,nsig_mean1500_width12=0,nsig_mean1500_width15=0,nsig_mean1600_width5=0,nsig_mean1600_width7=0,nsig_mean1600_width10=0,nsig_mean1600_width12=0,nsig_mean1600_width15=0,nsig_mean1700_width5=0,nsig_mean1700_width7=0,nsig_mean1700_width10=0,nsig_mean1700_width12=0,nsig_mean1700_width15=0,nsig_mean1800_width5=0,nsig_mean1800_width7=0,nsig_mean1800_width10=0,nsig_mean1800_width12=0,nsig_mean1800_width15=0"
    # PARS=${PARS/nsig_mean${sigmean}_width${sigwidth}=0/} # remove relevant fix to 0
    # PARS="nsig_mean${sigmean}_width${sigwidth},${PARS}"  # add to front
    # PARS=${PARS/,,/,} # remove double ,
    # PARS=${PARS%,}    # remove trailing ,

    # Don't need to set all POIs to 0, that is default behavior. Only specify the floating POI

    tol=1E-8

    if ! $sigfit; then


	echo "Now running bkg-only quickFit"
	quickFit -f ${wsfile} -d combData --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 --minTolerance $tol --minStrat 1 -o ${loopoutputfile}
	if [[ $? != 0 ]]; then
	    echo "Non-zero return code from quickFit. Check if tolerable"
	fi

	python python/ExtractPostfitFromWS.py --datafile $injecteddatafileorigbinned --datahist $loopdatahist --wsfile ${loopoutputfile}

    else

	PARS="nsig_mean${sigmean}_width${sigwidth}"

	echo "Now running s+b quickFit"
	quickFit -f ${wsfile} -d combData -p $PARS --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 --minTolerance $tol --minStrat 1 -o ${loopoutputfile}
	if [[ $? != 0 ]]; then
	    echo "Non-zero return code from quickFit. Check if tolerable"
	fi

	python python/ExtractPostfitFromWS.py --datafile $injecteddatafileorigbinned --datahist $loopdatahist --wsfile ${loopoutputfile}

	# tol=0.001
	# maxtol=0.002
	# tolfactor=3.16227766

	# while (( $(echo "$tol < $maxtol" | bc -l) )); do
	#     echo "Using minTolerance $tol"

	#     loopoutputfile2=${loopoutputfile/.root/_tol${tol}.root}
	    loopoutputfile2=${loopoutputfile/FitResult/Limits}

	    echo "Now running quickLimit"
	    timeout --foreground 600 quickLimit -f ${wsfile} -d combData -p $PARS --checkWS 1 --hesse 1 --initialGuess 100000 --minTolerance $tol --minStrat 1 --nllOffset 1 -o ${loopoutputfile2}
	    if [[ $? != 0 ]]; then
		echo "Non-zero return code from quickLimit. Check if tolerable"
	    fi
	    
	    # # if failing with NaN it can either crash and not produce an output or produce an output with NaN inside
	    # if [ ! -f ${loopoutputfile2/.root/.txt} ] || grep -iq "nan" ${loopoutputfile2/.root/.txt} ; then
	    # 	echo "NaN in limit output. Increasing minTolerance."
	    # 	tol=$(echo "$tol * $tolfactor" | bc -l)

	    # 	if (( $(echo "$tol < $maxtol" | bc -l) )); then
	    # 	    # if failed and one more loop to go, remove last result
	    # 	    rm $loopoutputfile2
	    # 	    rm ${loopoutputfile2/.root/.txt}
	    # 	fi
	    # else
	    # 	# successfully calculated limits, do not need to lower precision
	    # 	break
	    # fi
	# done
    fi	
done
