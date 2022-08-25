#!/usr/bin/env python

from __future__ import print_function
import os,sys,re,argparse,subprocess,shutil
import json
from ExtractPostfitFromWS import PostfitExtractor
from ExtractFitParameters import FitParameterExtractor
from PreFit import PreFitter
import ROOT

def execute(cmd):  
    print("EXECUTE:", cmd)
    sys.stdout.flush() # keeps print and subprocess output in sync
    rtv = subprocess.call(cmd, shell=True)
    return rtv

def replaceinfile(f, old_new_list):
    with open(f, 'r') as file :
        filedata = file.read()

    try:
        for tup in old_new_list:
            filedata = re.sub(tup[0], tup[1], filedata)
    except:
        print("ERROR: replaceinfile expects a list of tuples of strings [(old1,new1),...] as input")
        print(old_new_list)
        sys.exit(-1)

    with open(f, 'w') as file:
        file.write(filedata)

def build_fit_extract(topfile, datafile, datahist, rangelow, wsfile, fitresultfile, poi=None, maskrange=None):
    rtv=execute('XMLReader -x %s -o "logy integral" --minimizerStrategy 0' % topfile) # minimizer strategy fast
    if rtv != 0:
        print("WARNING: Non-zero return code from XMLReader. Check if tolerable")

    if poi:
        print("Now running s+b quickFit")
        _poi="-p %s" % poi
    else:
        print("Now running bkg-only quickFit")
        _poi=""

    if maskrange:
        _range="--range SBLo,SBHi"
        maskmin=maskrange[0]
        maskmax=maskrange[1]
    else:
        _range=""
        maskmin=-1
        maskmax=-1

    rtv=execute("quickFit -f %s -d combData %s --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 --minStrat 2 --nllOffset 0 --optConst 2 --GKIntegrator 1 --minTolerance 1E-10 %s -o %s" % (wsfile, _poi, _range, fitresultfile))
    if rtv != 0:
        print("WARNING: Non-zero return code from quickFit. Check if tolerable")

    postfitfile=fitresultfile.replace("FitResult","PostFit")
    parameterfile=fitresultfile.replace("FitResult","FitParameters")

    f=ROOT.TFile(datafile)
    d=f.Get(datahist)
    datafirstbin=d.FindBin(rangelow)-1
    f.Close()

    pfe = PostfitExtractor(
        datafile=datafile,
        datahist=datahist,
        datafirstbin=datafirstbin,
        wsfile=fitresultfile,
        rebinfile="Input/data/dijetTLAnlo/binning2021/data_J100yStar06_range171_3217.root",
        rebinhist="data",
        maskmin=maskmin,
        maskmax=maskmax,
        bkgonly=True
    )
    pval = pfe.GetPval("J100yStar06_rebinned")
    pfe.WriteRoot(postfitfile, dirPerCategory=True)
    # pfe.WriteRoot(postfitfile)

    fpe = FitParameterExtractor(wsfile=fitresultfile)
    fpe.WriteRoot(parameterfile)

    return (pval, postfitfile, parameterfile)

def run_anaFit(datafile,
               datahist,
               topfile,
               categoryfile,
               wsfile,
               outputfile,
               nbkg,
               nsig,
               rangelow,
               rangehigh,
               signame,
               backgroundfile=None,
               signalfile=None,
               dosignal=False,
               dolimit=False,
               sigmean=1000,
               sigwidth=7,
               maskthreshold=0.01,
               doprefit=False,
               folder="run/"):

    nbins=rangehigh - rangelow

    print("Fitting", nbins, "bins in range", rangelow, "-", rangehigh)

    # generate the config files on the fly in run dir
    if not os.path.isfile("{}/AnaWSBuilder.dtd".format(folder)):
      execute("ln -sf $PWD/config/dijetTLA/AnaWSBuilder.dtd $PWD/{}/AnaWSBuilder.dtd".format(folder))
    if sigwidth == -999: # running on zprime samples:
      print("Running in Zprime samples")
      tmpcategoryfile="{0}/category_dijetTLA_fromTemplate_mR{1}.xml".format(folder, sigmean)
      tmptopfile="{0}/dijetTLA_fromTemplate_mR{1}.xml".format(folder, sigmean)
    else:
      tmpcategoryfile="{}/category_dijetTLA_fromTemplate.xml".format(folder)
      tmptopfile="{}/dijetTLA_fromTemplate.xml".format(folder)  
    tmpsignalfile="{}/signal_dijetTLA_fromTemplate.xml".format(folder)
    tmpbackgroundfile="{}/background_dijetTLA_fromTemplate.xml".format(folder)
    
    shutil.copy2(topfile, tmptopfile) 
    shutil.copy2(categoryfile, tmpcategoryfile) 
    if signalfile:
        shutil.copy2(signalfile, tmpsignalfile) 
    
    replaceinfile(tmptopfile, 
                  [("CATEGORYFILE", tmpcategoryfile),
                   ("OUTPUTFILE", wsfile),
                   ("SIGNAME", signame),
               ])

    if backgroundfile:
        shutil.copy2(backgroundfile, tmpbackgroundfile) 
        replaceinfile(tmpcategoryfile, 
                      [("BACKGROUNDFILE", tmpbackgroundfile)])
        
        if doprefit:
            nPars = 5

            if "four" in  backgroundfile:
                nPars = 4
            elif "five" in  backgroundfile:
                nPars = 5
            elif "six" in  backgroundfile:
                nPars = 6
            elif "seven" in  backgroundfile:
                nPars = 7
            # [1, -30, -30, -30, ...]
            parRangeLow = [1]+[-30]*(nPars-1)
            parRangeHigh = [1]+[30]*(nPars-1)
            
            # get prefit ranges from background file
            with open(tmpbackgroundfile) as f:
                lines = f.readlines()
                for line in lines:
                    if not "<!--" in line and "<ModelItem" in line:
                        matches = re.findall('\[PAR(\d+),[ ]*([+-]?[0-9]+(?:[.][0-9]*)?),[ ]*([+-]?[0-9]+(?:[.][0-9]*)?)[ ]*\]', line)
                        for m in matches:
                            #m[0] is parN
                            #m[1] is rangeLow
                            #m[2] is rangeHigh
                            parRangeLow[int(m[0])-1] = float(m[1])
                            parRangeHigh[int(m[0])-1] = float(m[2])

            print("Starting PreFit in parameter ranges:")
            print(parRangeLow)
            print(parRangeHigh)
                            
            pf = PreFitter(
                datafile = datafile,
                datahist = datahist,
                xMin = rangelow,
                xMax = rangehigh,
                nPars = nPars,
                nRetries1 = 2000*nPars,
                nRetries2 = 2*nPars,
                fitLog = True,
                parRangeLow = parRangeLow,
                parRangeHigh = parRangeHigh,
            )
            
            initPars,_nbkg = pf.Fit()
            nbkg="%.1E, 0, %.1E" % (_nbkg, 2*_nbkg)
            
            print("Starting fit with initial pars", initPars)

            for i in range(nPars):
                replaceinfile(tmpbackgroundfile, 
                              [("PAR%d" % (i+1), str(initPars[i]))
                           ])

    replaceinfile(tmpcategoryfile, [
        ("DATAFILE", datafile),
        ("DATAHIST", datahist),
        ("RANGELOW", str(rangelow)),
        ("RANGEHIGH", str(rangehigh)),
        ("BINS", str(nbins)),
        ("NBKG", nbkg),
	("NSIG", nsig),
	("SIGNAME", signame),
	("SIGNALFILE", tmpsignalfile)
    ])    

    if signalfile:
        replaceinfile(tmpsignalfile, 
                      [("SIGMEAN", str(sigmean)),
                       ("SIGWIDTH", str(sigwidth)),
                   ])
            

    if dosignal:
        poi="nsig_%s" % signame
        if sigwidth == -999:
    	    poi="nsig_mR{}_gq0p1".format(sigmean)
    else:
        poi=None

    pval_global, postfitfile, parameterfile = build_fit_extract(topfile=tmptopfile,
                                                                datafile=datafile, 
                                                                datahist=datahist, 
                                                                rangelow=rangelow, 
                                                                wsfile=wsfile, 
                                                                fitresultfile=outputfile, 
                                                                poi=poi,
							                                )

    print ("Global fit p(chi2)=%.3f" % pval_global)

    if pval_global > maskthreshold:
        print("p(chi2) threshold passed. Exiting with succesful fit.")
    else:
        print("p(chi2) threshold not passed.")
        print("Now running BH for masking.")

        tmpcategoryfilemasked=tmpcategoryfile.replace(".xml","_masked.xml")

        # need to unset pythonpath in order to not use cvmfs numpy
        execute("source pyBumpHunter/pyBH_env/bin/activate; env PYTHONPATH=\"\" python3 python/FindBHWindow.py --inputfile %s --bkghist %s --datahist %s --outputjson %s; deactivate" % (postfitfile, "J100yStar06_rebinned/postfit", "J100yStar06_rebinned/data", "{}/BHresults.json".format(folder)))

        # pass results of pyBH via this json file
        with open("{}/BHresults.json".format(folder)) as f:
            BHresults=json.load(f)

        tmptopfilemasked=tmptopfile.replace(".xml","_masked.xml")
        wsfilemasked=wsfile.replace(".root","_masked.root")
        outfilemasked=outputfile.replace(".root","_masked.root")

        shutil.copy2(tmptopfile, tmptopfilemasked) 
        shutil.copy2(tmpcategoryfile, tmpcategoryfilemasked) 

        replaceinfile(tmptopfilemasked, 
                      [(tmpcategoryfile,tmpcategoryfilemasked),
                       (r'(OutputFile="[A-Za-z0-9_/.-]*")',r'\1 Blind="true"'),
                       (wsfile, wsfilemasked),])
        replaceinfile(tmpcategoryfilemasked, 
                      [(r'(Binning="\d+")', r'\1 BlindRange="%s"' % BHresults["BlindRange"])])

        pval_masked,_,_ = build_fit_extract(tmptopfilemasked,
                                            datafile=datafile, 
                                            datahist=datahist, 
                                            rangelow=rangelow, 
                                            wsfile=wsfilemasked, 
                                            fitresultfile=outfilemasked, 
                                            poi=poi, 
                                            maskrange=(int(BHresults["MaskMin"]), int(BHresults["MaskMax"])))

        print("Masked fit p(chi2)=%.3f" % pval_masked)

        if pval_masked > maskthreshold:
            print("p(chi2) threshold passed. Continuing with successful (window-excluded) fit.")
            wsfile=wsfilemasked
        else:
            print("p(chi2) threshold still not passed.")
            print("Exiting with failed fit status.")
            return -1
            
    # blindrange not yet implemented with quickLimit
    if dolimit and dosignal and pval_global > maskthreshold:
        print("Now running quickLimit")
        #rtv=execute("timeout --foreground 1800 quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 100000 --minTolerance 1E-8 --muScanPoints 20 --minStrat 1 --nllOffset 1 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits")))
        rtv=execute("quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 100000 --minTolerance 1E-10 --muScanPoints 20 --minStrat 2 --nllOffset 0 --GKIntegrator 1 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits")))
        if rtv != 0:
            print("WARNING: Non-zero return code from quickLimit. Check if tolerable")
    
    return 0

def main(args):
    
    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--datafile', dest='datafile', type=str, required=True, help='Input data file')
    parser.add_argument('--datahist', dest='datahist', type=str, required=True, help='Input finebinned data histogram name')
    parser.add_argument('--topfile', dest='topfile', type=str, required=True, help='Input top-level xml card')
    parser.add_argument('--categoryfile', dest='categoryfile', type=str, required=True, help='Input category xml card')
    parser.add_argument('--backgroundfile', dest='backgroundfile', type=str, help='Input background xml card')
    parser.add_argument('--signalfile', dest='signalfile', default= None, type=str, help='Input signal xml card')
    parser.add_argument('--wsfile', dest='wsfile', type=str, required=True, help='Output workspace file')
    parser.add_argument('--outputfile', dest='outputfile', type=str, required=True, help='Output fitresult file')
    parser.add_argument('--nbkg', dest='nbkg', type=str, required=True, help='Initial value and range of nbkg par (e.g. "2E8,0,3E8")')
    parser.add_argument('--nsig', dest='nsig', type=str, default='0,-1E6,1E6', help='Initial value and range of nsig par (e.g. "0,-1E6,1E6")')
    parser.add_argument('--rangelow', dest='rangelow', type=int, help='Start of fit range (in GeV)')
    parser.add_argument('--rangehigh', dest='rangehigh', type=int, help='End Start of fit range (in GeV)')
    parser.add_argument('--dosignal', dest='dosignal', action="store_true", help='Perform s+b fit (default: bkg-only)')
    parser.add_argument('--dolimit', dest='dolimit', action="store_true", help='Perform limit setting')
    parser.add_argument('--signame', dest='signame', type=str, help='Name of the signal parameter')
    parser.add_argument('--sigmean', dest='sigmean', type=int, default=1000, help='Mean of signal Gaussian for s+b fit (in GeV)')
    parser.add_argument('--sigwidth', dest='sigwidth', type=int, default=7, help='Width of signal Gaussian for s+b fit (in %). If -999 dealing with Zprime samples.')
    parser.add_argument('--maskthreshold', dest='maskthreshold', type=float, default=0.01, help='Threshold of p(chi2) below which to run BH and mask the most significant window')
    parser.add_argument('--doprefit', dest='doprefit', action="store_true", help='Perform ROOT prefit before quickFit')
    parser.add_argument('--folder', dest='folder', type=str, default='run', help='Output folder to store configs and results (default: run)')

    args = parser.parse_args(args)
    if not args.signame:
        if args.sigwidth == -999:
            args.signame="mR%s" % (args.sigmean)
        else:
            args.signame="mean%s_width%s" % (args.sigmean, args.sigwidth)

    # create dir if not exists: https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
    try: 
        os.makedirs(args.folder)
    except OSError:
        if not os.path.isdir(args.folder):
            raise

    run_anaFit(datafile=args.datafile,
               datahist=args.datahist,
               topfile=args.topfile,
               categoryfile=args.categoryfile,
               backgroundfile=args.backgroundfile,
               signalfile=args.signalfile,
               wsfile=args.wsfile,
               outputfile=args.outputfile,
               nbkg=args.nbkg,
               nsig=args.nsig,
               rangelow=args.rangelow,
               rangehigh=args.rangehigh,
               dosignal=args.dosignal,
               dolimit=args.dolimit,
               sigmean=args.sigmean,
               sigwidth=args.sigwidth,
               folder=args.folder,	       
               signame=args.signame,
               maskthreshold=args.maskthreshold,
               doprefit=args.doprefit)



if __name__ == "__main__":  
    sys.exit(main(sys.argv[1:]))
