#!/usr/bin/env python

from __future__ import print_function
import os,sys,re,argparse,subprocess,shutil
import json
from ExtractPostfitFromWS import PostfitExtractor
from ExtractFitParameters import FitParameterExtractor
import config as config

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

def build_fit_extract(topfile, datafile, datahist, datafirstbin, wsfile, fitresultfile, poi=None, maskrange=None, rebinFile=None, rebinHist=None, rebinEdges=None):
    print("starting fit extractor")
    #rtv=execute('XMLReader -x %s -o "logy integral" -s 0 -v 0 -m Minuit2 -n 1 -p 0 -b 1' % topfile) # minimizer strategy fast
    rtv=execute('XMLReader -x %s -o "logy integral" -s 0' % topfile) # minimizer strategy fast
    #XMLReader -x ${tmptopfile} -o "logy integral" -s 0 -v 0 -m Minuit2 -t $tolXML -n 1 -p 0 -b 1

    print("done with xml")
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

    print("running quickfit")
    rtv=execute("quickFit -f %s -d combData %s --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 --minTolerance 1E-4 --minStrat 1 %s -o %s" % (wsfile, _poi, _range, fitresultfile))
    if rtv != 0:
        print("WARNING: Non-zero return code from quickFit. Check if tolerable")

    if maskrange:
      postfitfile=fitresultfile.replace("FitResult","PostFit_masked")
      parameterfile=fitresultfile.replace("FitResult","FitParameters_masked")
    else:
      postfitfile=fitresultfile.replace("FitResult","PostFit")
      parameterfile=fitresultfile.replace("FitResult","FitParameters")

    print("actual postfit extractor")
    # TODO please fix the datafirstbin if not already fixed
    pfe = PostfitExtractor(
        datafile=datafile,
        datahist=datahist,
        datafirstbin=datafirstbin,
        wsfile=fitresultfile,
        rebinfile=rebinFile,
        rebinhist=rebinHist,
        binEdges=rebinEdges,
        maskmin=maskmin,
        maskmax=maskmax
    )
    pval = pfe.GetPval()
    pfe.WriteRoot(postfitfile)

    fpe = FitParameterExtractor(wsfile=fitresultfile)
    fpe.WriteRoot(parameterfile)

    return (pval, postfitfile, parameterfile)

def run_anaFit(datafile,
               datahist,
               topfile,
               categoryfile,
               wsfile,
               outputfile,
               outputstring,
               cdir,
               nbkg,
               rangelow,
               rangehigh,
               outdir,
               signalfile,
               dosignal=False,
               dolimit=False,
               sigmean=1000,
               sigwidth=7,
               maskthreshold=0.01,
               nsig="0,0,1e6",
               rebinFile=None,
               rebinHist=None,
               rebinEdges=None,
               fitFunction=None,
              ):

    nbins=rangehigh - rangelow

    print("Fitting", nbins, "bins in range", rangelow, "-", rangehigh)

    # generate the config files on the fly in run dir
    if not os.path.isfile("%s/run/AnaWSBuilder.dtd"%(cdir)):
        execute("ln -s ../config/dijetTLA/AnaWSBuilder.dtd %s/run/AnaWSBuilder.dtd"%(cdir))

    tmpcategoryfile="%s/run/category_dijet_fromTemplate_%s.xml"%(cdir, outputstring)
    tmptopfile="%s/run/dijet_fromTemplate_%s.xml"%(cdir, outputstring)
    tmpsignalfile="%s/run/dijetTLACat_signal_%d_%d_%s.xml"%(cdir, sigmean, sigwidth, outputstring)

    signalWSName = config.signals[signalfile]["workspacefile"]
    signalfile = config.signals[signalfile]["signalfile"]

    print(topfile, categoryfile, tmpcategoryfile)
    shutil.copy2(topfile, tmptopfile)
    shutil.copy2(categoryfile, tmpcategoryfile)
    shutil.copy2(signalfile, tmpsignalfile)
    tmpsignalfile.replace("MEAN", str(sigmean))


    tmpfitfile="%s/run/dijetFit_signal_%d_%d_%s.xml"%(cdir, sigmean, sigwidth, outputstring)
    fitfile = cdir + "/" + config.fitFunctions[fitFunction]["Config"]
    shutil.copy2(fitfile, tmpfitfile)


    replaceinfile(tmpfitfile,
                  [
                   ("CDIR", cdir),
                  ])

    replaceinfile(tmptopfile,
                  [("CATEGORYFILE", tmpcategoryfile),
                   ("CDIR", cdir),
                   ("MEAN", str(sigmean)),
                   ("WIDTH", str(sigwidth)),
                   ("SIGNALFILE", tmpsignalfile),
                   ("OUTPUTFILE", wsfile),
                  ])

    replaceinfile(tmpsignalfile,
                  [
                   ("WORKSPACEFILE", signalWSName),
                   ("CDIR", cdir),
                   ("MEAN", str(sigmean)),
                   ("WPERCENT", str(sigwidth/100.)),
                   ("WIDTH", str(sigwidth)),
                   ("OUTPUTFILE", wsfile),
                  ])



    print ("Running with datafile ", datafile)
    replaceinfile(tmpcategoryfile, [
        ("DATAFILE", datafile),
        ("DATAHIST", datahist),
        ("RANGELOW", str(rangelow)),
        ("FITFUNC", tmpfitfile),
        ("SIGNALFILE", tmpsignalfile),
        ("CDIR", cdir),
        ("RANGEHIGH", str(rangehigh)),
        ("BINS", str(nbins)),
        ("NBKG", nbkg),
        ("NSIG", nsig),
        ("MEAN", str(sigmean)),
        ("WIDTH", str(sigwidth)),
    ])    

    if dosignal:
        poi="nsig_mean%s_width%s" % (sigmean, sigwidth)
    else:
        poi=None

    print("running fit extractor")
    # TODO: Need to dynamically set datafirstbin based on the histogram -- they might not always start at 0, and the bin width might not always be 1
    pval_global, postfitfile, parameterfile = build_fit_extract(topfile=tmptopfile,
                                                                datafile=datafile, 
                                                                datahist=datahist, 
                                                                datafirstbin=rangelow, 
                                                                wsfile=wsfile, 
                                                                fitresultfile=outputfile, 
                                                                poi=poi,
                                                                rebinFile=rebinFile,
                                                                rebinHist=rebinHist,
                                                                rebinEdges=rebinEdges,
                                                                )

    print("Finished fit extractor")
    print ("Global fit p(chi2)=%.3f" % pval_global)

    if pval_global > maskthreshold:
        print("p(chi2) threshold passed. Exiting with succesful fit.")
        #execute("source ../pyBumpHunter/pyBH_env/bin/activate; env PYTHONPATH=\"\" python3 ../python/FindBHWindow.py --inputfile %s  --outputjson run/BHresults.json; deactivate" % (postfitfile))
    else:
        print("p(chi2) threshold not passed.")
        print("Now running BH for masking.")



        # TODO: Need to use the actual path, since this will only run if working in the correct directory
        # need to unset pythonpath in order to not use cvmfs numpy
        #execute("source ../pyBumpHunter/pyBH_env/bin/activate; env PYTHONPATH=\"\" python3 ../python/FindBHWindow.py --inputfile %s --outputjson %s; deactivate" % (postfitfile, "run/BHresults.json"))
        execute("source ../pyBumpHunter/pyBH_env/bin/activate; env PYTHONPATH=\"\" python3 ../python/FindBHWindow.py --inputfile %s  --outputjson %s/scripts/%s/BHresults.json; deactivate" % (postfitfile, cdir, outdir))

        # pass results of pyBH via this json file
        with open(cdir + "/scripts/" + outdir + "/BHresults.json") as f:
            BHresults=json.load(f)

        tmptopfilemasked=tmptopfile.replace(".xml","_masked.xml")
        tmpcategoryfilemasked=tmpcategoryfile.replace(".xml","_masked.xml")
        # We don't make a new file, and this seems to behave correctly, so I think this is ok to comment out
        #wsfilemasked=wsfile.replace(".root","_masked.root")
        #outfilemasked=outputfile.replace(".root","_masked.root")

        #tmptopfilemasked=tmptopfile
        outfilemasked=outputfile
        wsfilemasked=wsfile

        shutil.copy2(tmptopfile, tmptopfilemasked) 
        shutil.copy2(tmpcategoryfile, tmpcategoryfilemasked) 

        # TODO there is probably a better way of doing this
        replaceinfile(tmptopfilemasked, 
                      [(tmpcategoryfile,tmpcategoryfilemasked),
                       (r'(OutputFile="[A-Za-z0-9_/.-]*")',r'\1'),
                       ('Blind="false"','Blind="true"'),
                       (wsfile, wsfilemasked),])
        replaceinfile(tmpcategoryfilemasked, 
                      [(r'(Binning="\d+")', r'\1 BlindRange="%s"' % BHresults["BlindRange"])])

        pval_masked,_,_ = build_fit_extract(tmptopfilemasked,
                                            datafile=datafile, 
                                            datahist=datahist, 
                                            datafirstbin=rangelow, 
                                            wsfile=wsfilemasked, 
                                            fitresultfile=outfilemasked, 
                                            poi=poi, 
                                            rebinFile=rebinFile,
                                            rebinHist=rebinHist,
                                            rebinEdges=rebinEdges,
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
    #if dolimit and dosignal:
        rtv=execute("timeout --foreground 1800 quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 100000 --minTolerance 1E-8 --muScanPoints 20 --minStrat 1 --nllOffset 1 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits")))
        if rtv != 0:
            print("WARNING: Non-zero return code from quickLimit. Check if tolerable")
    
    return 0

def main(args):
    
    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--datafile', dest='datafile', type=str, required=True, help='Input data file')
    parser.add_argument('--datahist', dest='datahist', type=str, required=True, help='Input finebinned data histogram name')
    parser.add_argument('--topfile', dest='topfile', type=str, required=True, help='Input top-level xml card')
    parser.add_argument('--categoryfile', dest='categoryfile', type=str, required=True, help='Input category xml card')
    parser.add_argument('--fitFunction', dest='fitFunction', type=str, default=None, help='Name of the file with the fit function information')
    parser.add_argument('--cdir', dest='cdir', type=str, default=None, help='Full path to current directory')
    parser.add_argument('--wsfile', dest='wsfile', type=str, required=True, help='Output workspace file')
    parser.add_argument('--outputfile', dest='outputfile', type=str, required=True, help='Output fitresult file')
    parser.add_argument('--outputdir', dest='outputdir', type=str, required=True, help='Output fitresult file')
    parser.add_argument('--nbkg', dest='nbkg', type=str, required=True, help='Initial value and range of nbkg par (e.g. "2E8,0,3E8")')
    parser.add_argument('--rangelow', dest='rangelow', type=int, help='Start of fit range (in GeV)')
    parser.add_argument('--rangehigh', dest='rangehigh', type=int, help='End Start of fit range (in GeV)')
    parser.add_argument('--dosignal', dest='dosignal', action="store_true", help='Perform s+b fit (default: bkg-only)')
    parser.add_argument('--dolimit', dest='dolimit', action="store_true", help='Perform limit setting')
    parser.add_argument('--sigmean', dest='sigmean', type=int, default=1000, help='Mean of signal Gaussian for s+b fit (in GeV)')
    parser.add_argument('--sigwidth', dest='sigwidth', type=int, default=7, help='Width of signal Gaussian for s+b fit (in %)')
    parser.add_argument('--rebinfile', dest='rebinfile', type=str, required=False, help='File containing histogram with template histogram for rebinning result')
    parser.add_argument('--rebinhist', dest='rebinhist', type=str, required=False, help='Name of template histogram for rebinning result')
    parser.add_argument('--rebinedges', dest='rebinedges', type=int, nargs="*", default=None, help='Name of template hist')
    parser.add_argument('--maskthreshold', dest='maskthreshold', type=float, default=0.01, help='Threshold of p(chi2) below which to run BH and mask the most significant window')

    args = parser.parse_args(args)
    print(args.datafile)

    if not os.path.exists(args.outputdir):
        os.makedirs(args.outputdir)

    run_anaFit(datafile=args.datafile,
               datahist=args.datahist,
               topfile=args.topfile,
               categoryfile=args.categoryfile,
               wsfile=args.outputdir + "/" + args.wsfile,
               outputfile=args.outputdir + "/" + args.outputfile,
               cdir=args.cdir,
               nbkg=args.nbkg,
               rangelow=args.rangelow,
               rangehigh=args.rangehigh,
               dosignal=args.dosignal,
               dolimit=args.dolimit,
               sigmean=args.sigmean,
               sigwidth=args.sigwidth,
               rebinFile=args.rebinfile,
               rebinHist=args.rebinhist,
               rebinEdges=args.rebinedges,
               maskthreshold=args.maskthreshold,
               fitFunction=args.fitFunction)


if __name__ == "__main__":  
    sys.exit(main(sys.argv[1:]))
