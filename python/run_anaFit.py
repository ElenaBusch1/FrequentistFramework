#!/usr/bin/env python

from __future__ import print_function
import os,sys,re,argparse,subprocess,shutil
import json
from python.ExtractPostfitFromWS import PostfitExtractor
from python.ExtractFitParameters import FitParameterExtractor
import config as config
import ROOT as r
from scipy.stats.distributions import chi2
import python.LocalFunctions as lf
import getSystematics as gs

def execute(cmd):  
    print("EXECUTE:", cmd)
    sys.stdout.flush() # keeps print and subprocess output in sync
    rtv = subprocess.call(cmd, shell=True, close_fds=True)
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

def build_fit_extract(topfile, datafiles, channels, datahist, datafirstbin, wsfile, fitresultfile, toy=0, toyString = "",  poi=None, maskrange=None, rebinFile=None, rebinHist=None, rebinEdges=None, nbkgWindow=[]):
    
    print("starting fit extractor")
    rtv=execute('XMLReader -x %s -o "logy integral" -s 0 -v 0 -m Minuit2 -n 1 -p 0 -b 1' % topfile) # minimizer strategy fast
    #rtv=execute('XMLReader -x %s -o "logy integral" -s 0 -t 100' % topfile) # minimizer strategy fast

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
    #rtv=execute("quickFit -f %s -d combData %s --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 --minStrat 2 %s --minTolerance 1e-8 -o %s" % (wsfile, _poi, _range, fitresultfile))
    #rtv=execute("quickFit -f %s -d combData %s --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 --minStrat 2 %s --minTolerance 1e-5 -o %s" % (wsfile, _poi, _range, fitresultfile))
    #rtv=execute("quickFit -f %s -d combData %s --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 --minStrat 2 %s --minTolerance 1e-8 -o %s" % (wsfile, _poi, _range, fitresultfile))
    rtv=execute("quickFit -f %s -d combData %s --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 --minStrat 2 %s --minTolerance 1e-8 -o %s" % (wsfile, _poi, _range, fitresultfile))
    if rtv != 0:
        #rtv=execute("quickFit -f %s -d combData %s --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 --minStrat 2 %s --minTolerance 10 -o %s" % (wsfile, _poi, _range, fitresultfile))
        print("WARNING: Non-zero return code from quickFit. Check if tolerable")


    print("actual postfit extractor")
    pfe = PostfitExtractor(
        datafile=datafiles,
        datahist=datahist,
        datafirstbin=datafirstbin,
        wsfile=fitresultfile,
        rebinfile=rebinFile,
        rebinhist=rebinHist,
        binEdges=rebinEdges,
        maskmin=maskmin,
        maskmax=maskmax,
        channels=channels,
    )
    isPass = pfe.Extract()
    doRecreate = (toy==0)
    pvals = []
    chi2s = []
    ndofs = []

    for index, histName, channel, rangelow, datafile in zip(range(len(datahist)), datahist, channels, datafirstbin, datafiles):
      if maskrange:
        postfitfile=fitresultfile.replace("FitResult","PostFit_masked")
        parameterfile=fitresultfile.replace("FitResult","FitParameters_masked")
      else:
        postfitfile=fitresultfile.replace("FitResult","PostFit")
        parameterfile=fitresultfile.replace("FitResult","FitParameters")

      pval = pfe.GetPval(channelname=channel)
      pvals.append(pval)
      chi2val = pfe.GetChi2(channelname=channel)
      chi2s.append(chi2val)
      ndof = pfe.GetNdof(channelname=channel)
      ndofs.append(ndof)

      postfitfile=postfitfile.replace("CHANNEL", channel)
      parameterfile=parameterfile.replace("CHANNEL", channel)

      pfe.WriteRoot(postfitfile, doRecreate=doRecreate, suffix=channel + "_" +toyString, dirPerCategory=True, channelNames =[channel])

      if len(nbkgWindow) > index:
        print( index, nbkgWindow)
        if toy > 0:
          print ("Number of bkg: ", nbkgWindow[index][toy], "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        fpe = FitParameterExtractor(wsfile=fitresultfile, nbkg=nbkgWindow[index][toy])
      else:
        fpe = FitParameterExtractor(wsfile=fitresultfile, nbkg=0)
      fpe.WriteRoot(parameterfile,  doRecreate=doRecreate, suffix=channel + "_" +toyString)
      print("Done with loop")

    for chi2val,pval, ndof in zip(chi2s, pvals, ndofs):
      print(chi2val, (1- chi2.cdf(chi2val, ndof)), pval)

    fitnsig = fpe.GetNsig()
    fitnbkg = fpe.GetNbkgFit()

    return (pvals, postfitfile, parameterfile, fitnsig, fitnbkg, isPass)

def run_anaFit(datahist,
               topfile,
               signalfile,
               wsfile,
               outputfile,
               outputstring,
               cdir,
               nbkg,
               outdir,
               dosignal=False,
               dolimit=False,
               sigmean=0,
               sigwidth=7,
               ntoys=10,
               maskthreshold=0.01,
               nsig="0,0,1e6",
               nbkgWindow = [],
               rebinFile=None,
               rebinHist=None,
               rebinEdges=None,
               fitFunction=None,
               datafiles = None,
               histnames = None,
               doRemake = False,
               useSysts = False,
               alphaBin = 0,
              ):


    alphaBins = [0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33, 0.35]
    # generate the config files on the fly in run dir
    if not os.path.isfile("%s/run/AnaWSBuilder.dtd"%(cdir)):
        execute("ln -s ../config/dijetTLA/AnaWSBuilder.dtd %s/run/AnaWSBuilder.dtd"%(cdir))

    tmptopfile="%s/run/dijetTLA_fromTemplate_%s.xml"%(cdir, outputstring)
    tmpsignalfile="%s/run/dijetTLACat_signal_%d_%d_%s.xml"%(cdir, sigmean, sigwidth, outputstring)
    alpha          = config.samples[datahist[0]]["alpha"]
    sigmeanX = round( (alphaBins[int(alpha)] * sigmean)/10)*10

    signalWSName   = config.signals[signalfile]["workspacefile"]
    signalfileName = config.signals[signalfile]["signalfile"]
    sigwsfile      = config.signals[signalfile]["workspacefile"]
    sighist        = config.signals[signalfile]["histname"]

    #print( "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" , str(alpha), str(alphaBins[alpha]), sigmeanX)
    sighist = sighist.replace("ALPHA", "%d"%alpha)
    sighist = sighist.replace("MEAN", "%d"%sigmean)
    sighist = sighist.replace("MASSX", "%d"%sigmeanX)

    sigwsfile = sigwsfile.replace("MEAN", "%d"%(sigmean))

    signalWSName = signalWSName.replace("MASSX", "%d"%(sigmeanX))
    signalfileName = signalfileName.replace("MASSX", "%d"%(sigmeanX))
    sigwsfile = sigwsfile.replace("MASSX", "%d"%(sigmeanX))

    shutil.copy2(topfile, tmptopfile) 
    shutil.copy2(signalfileName, tmpsignalfile) 
    tmpsignalfile.replace("MEAN", str(sigmean))
    tmpsignalfile.replace("MASSX", str(sigmeanX))
    
    # Make a list of all of the distributions that should be fit
    newName = ""
    newSignal = "  <POI>"
    newSignalZero = ""
    for index, histName in enumerate(datahist):
         tmpcategoryfile="%s/run/category_dijet_fromTemplate_%s_%s.xml"%(cdir, outputstring, histName)
         tmpfitfile="%s/run/dijetFit_signal_%d_%d_%s_%s.xml"%(cdir, sigmean, sigwidth, outputstring, histName)
         fitfile = cdir + "/" + config.fitFunctions[fitFunction]["Config"]
         shutil.copy2(fitfile, tmpfitfile)

         replaceinfile(tmpfitfile,
                  [
                   ("CDIR", cdir),
                   ("CATEGORY", histName),
                  ])
         newName = newName + "  <Input>%s</Input>\n"%(tmpcategoryfile)
         if index >0:
           newSignal = newSignal + ",nsig_mean%d_%s"%(sigmean,histName)
           newSignalZero = newSignalZero + ",nsig_mean%d_%s=0"%(sigmean,histName)
         else:
           newSignal = newSignal + "nsig_mean%d_%s"%(sigmean,histName)
           newSignalZero = newSignalZero + "nsig_mean%d_%s=0"%(sigmean,histName)
    newSignal = newSignal + "</POI>\n"
    systFileName = config.signals[signalfile]["systFile"]
    systFileName = systFileName.replace("ALPHA", "%d"%alpha)
    systFileName = systFileName.replace("MEAN", "%.0f"%sigmean)
    systFileName = systFileName.replace("MASSX", "%.0f"%sigmeanX)
    systematics = gs.writeSystematics("systematics", sigmean, alpha, systFileName)
    
    replaceinfile(tmptopfile, 
                  [
                   ("  <Input>CATEGORYFILE</Input>", newName),
                   ("  <POI>nsig_meanMEAN_DATAHIST</POI>", newSignal),
                   ("nsig_meanMEAN_DATAHIST=0", newSignalZero),
                   ("CDIR", cdir),
                   ("MEAN", str(sigmean)),
                   ("MASSX", str(sigmeanX)),
                   ("WIDTH", str(sigwidth)),
                   ("SIGNALFILE", tmpsignalfile),
                   ("SYSTEMATICS", systematics),
                   ("OUTPUTFILE", wsfile),
                  ])

    replaceinfile(tmpsignalfile,
                  [
                   ("WORKSPACEFILE", signalWSName),
                   ("CDIR", cdir),
                   ("MEAN", str(sigmean)),
                   ("MEANX", str(sigmeanX)),
                   ("WPERCENT", str(sigwidth/100.)),
                   ("WIDTH", str(sigwidth)),
                   ("SIGHIST", str(sighist)),
                   ("SIGFILE", str(sigwsfile)),
                   ("OUTPUTFILE", wsfile),
                   ("SYSTEMATICS", systematics),
                  ])



    nsigOld = -10
    nbkgOld = 0
    for toy in range(max(ntoys, 1)):
      if not doRemake:
        postfitfile=outputfile.replace("FitResult","PostFit")
        postfitfile=postfitfile.replace("CHANNEL", histName)
        print(postfitfile)
        if lf.read_histogram(postfitfile, "data%s__%d"%(histName, toy)):
          print( "Already found toy for ", toy)
          continue


      print ("Running toy ", toy)
      if ntoys == 0:
        toyString = ""
      else:
        toyString = "_%d"%(toy)
      
      # Make a category file for each signal region
      tmpDataHists = []
      rangesLow = []
      hasFiles = True
      if not datafiles:
        datafiles = []
        hasFiles = False
      poi=""
      for index, histName in enumerate(datahist):
        rangelow = config.samples[histName]["rangelow"]
        rangehigh = config.samples[histName]["rangehigh"]
        nbins = rangehigh - rangelow
        rangesLow.append(rangelow)
        if not hasFiles:
          datafile = config.samples[histName]["inputFile"]
          datafiles.append(datafile)
          actualHistName = config.samples[histName]["histname"]
        else:
          datafile = datafiles[index]
          actualHistName = histnames[index]

        topfile=config.samples[histName]["topfile"]
        categoryfile=config.samples[histName]["categoryfile"]
        if useSysts:
          categoryfile=config.samples[histName]["categoryfileSysts"]
        if index > 0:
          poi=poi + ",nsig_mean%s_%s" % (sigmean, histName)
        else:
          poi=poi + "nsig_mean%s_%s" % (sigmean, histName)



        tmpDataHists.append("%s%s"%(actualHistName, toyString))
        tmpcategoryfile="%s/run/category_dijet_fromTemplate_%s_%s.xml"%(cdir, outputstring, histName)
        shutil.copy2(categoryfile, tmpcategoryfile) 
        tmpfitfile="%s/run/dijetFit_signal_%d_%d_%s_%s.xml"%(cdir, sigmean, sigwidth, outputstring, histName)
        replaceinfile(tmpcategoryfile, [
          ("DATAFILE", datafile),
          ("CHANNEL", histName),
          ("DATAHIST", actualHistName + "%s"%(toyString)) ,
          ("FITFUNC", tmpfitfile),
          ("CDIR", cdir),
          ("SIGNALFILE", tmpsignalfile),
          ("RANGELOW", str(rangelow)),
          ("RANGEHIGH", str(rangehigh)),
          ("SYSTEMATICS", systematics),
          ("BINS", str(nbins)),
          ("NBKG", str(nbkg)),
          ("NSIG", str(nsig)),
          ("MEAN", str(sigmean)),
          ("MASSX", str(sigmeanX)),
          ("WIDTH", str(sigwidth)),
        ])

      if dosignal:
          poi=poi
      else:
          poi=None

      print("running fit extractor")
      # TODO: Need to dynamically set datafirstbin based on the histogram -- they might not always start at 0, and the bin width might not always be 1
      pvals_global, postfitfile, parameterfile, fitnsig, fitnbkg, isPass = build_fit_extract(topfile=tmptopfile,
                                                                datafiles=datafiles, 
                                                                channels=datahist,
                                                                datahist=tmpDataHists,
                                                                datafirstbin=rangesLow, 
                                                                wsfile=wsfile, 
                                                                fitresultfile=outputfile, 
                                                                poi=poi,
                                                                rebinFile=rebinFile,
                                                                rebinHist=rebinHist,
                                                                rebinEdges=rebinEdges,
                                                                toy=toy,
                                                                toyString=toyString,
                                                                nbkgWindow=nbkgWindow,
                                                                )

      
      #if isPass == 1 and fitnsig == -10:
      if dosignal and (abs(fitnsig +5) < 1e-3 or abs(fitnsig +10) < 1e-2  or abs(fitnsig+100) < 1e-2):
        print ("Rerunning")
        if abs(fitnsig +10) < 1e-3 :
          replaceinfile(tmpcategoryfile, [(str(nsig), "0,0,10"), ])
        if abs(fitnsig +5) < 1e-3 :
          replaceinfile(tmpcategoryfile, [(str(nsig), "0,0,5"), ])
        if abs(fitnsig +100) < 1e-3 :
          replaceinfile(tmpcategoryfile, [(str(nsig), "0,0,100"), ])
        pvals_global, postfitfile, parameterfile, fitnsig, fitnbkg, isPass = build_fit_extract(topfile=tmptopfile,
                                                                datafiles=datafiles,
                                                                channels=datahist,
                                                                datahist=tmpDataHists,
                                                                datafirstbin=rangesLow,
                                                                wsfile=wsfile,
                                                                fitresultfile=outputfile,
                                                                poi=poi,
                                                                rebinFile=rebinFile,
                                                                rebinHist=rebinHist,
                                                                rebinEdges=rebinEdges,
                                                                toy=toy,
                                                                toyString=toyString,
                                                                nbkgWindow=nbkgWindow,
                                                                )


      if sigmean and dosignal:
        if abs(fitnsig - nsigOld)< 0.0001 and abs(fitnbkg - nbkgOld) < 0.0001:
          print( "Fitting seems to be stuck?", fitnsig, nsigOld, fitnbkg, nbkgOld)
          return -1
        nsigOld = fitnsig
        fitnbkg = nbkgOld



      print("Finished fit extractor")
      print ("Global fit p(chi2)=%.3f" % pvals_global[0])

      if pvals_global[0] > maskthreshold:
        print("p(chi2) threshold passed. Exiting with succesful fit.")
        #execute("source ../pyBumpHunter/pyBH_env/bin/activate; env PYTHONPATH=\"\" python3 ../python/FindBHWindow.py --inputfile %s  --outputjson run/BHresults.json; deactivate" % (postfitfile))
      else:
        print("p(chi2) threshold not passed.")
        print("Now running BH for masking.")

        # TODO: Need to use the actual path, since this will only run if working in the correct directory
        # need to unset pythonpath in order to not use cvmfs numpy
        execute("source ../pyBumpHunter/pyBH_env/bin/activate; env PYTHONPATH=\"\" python3 ../python/FindBHWindow.py --inputfile %s  --outputjson %s/scripts/%s/BHresults.json; deactivate" % (postfitfile, cdir, outdir))

        # pass results of pyBH via this json file
        with open(cdir + "/scripts/" + outdir + "/BHresults.json") as f:
            BHresults=json.load(f)

        tmptopfilemasked=tmptopfile.replace(".xml","_masked.xml")
        tmpcategoryfilemasked=tmpcategoryfile.replace(".xml","_masked.xml")

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

        pvals_masked,_,_ = build_fit_extract(tmptopfilemasked,
                                            datafiles=datafiles, 
                                            channels=datahist,
                                            datahist=tmpDataHists,
                                            datafirstbin=rangelow, 
                                            wsfile=wsfilemasked, 
                                            fitresultfile=outfilemasked, 
                                            poi=poi, 
                                            rebinFile=rebinFile,
                                            rebinHist=rebinHist,
                                            rebinEdges=rebinEdges,
                                            toy=toy,
                                            toyString=toyString,
                                            maskrange=(int(BHresults["MaskMin"]), int(BHresults["MaskMax"])))

        print("Masked fit p(chi2)=%.3f" % pvals_masked[0])

        if pvals_masked[0] > maskthreshold:
            print("p(chi2) threshold passed. Continuing with successful (window-excluded) fit.")
            wsfile=wsfilemasked
        else:
            print("p(chi2) threshold still not passed.")
            print("Exiting with failed fit status.")
            return -1
            
 
      
      # blindrange not yet implemented with quickLimit
      if dolimit and dosignal and pvals_global[0] > maskthreshold:
          #rtv=execute("timeout --foreground 1800 quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 10000 --minTolerance 1E-8 --muScanPoints 0 --minStrat 1 --nllOffset 1 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits").replace(".root","%s.root"%(toyString))))
          #rtv=execute("timeout --foreground 6000 quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 10000 --minTolerance 1E-5  --minStrat 1 --muScanPoints 0 --nllOffset 1 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits").replace(".root","%s.root"%(toyString))))
          #rtv=execute("timeout --foreground 6000 quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 10000 --minTolerance 1E-5  --minStrat 1  --nllOffset 1 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits").replace(".root","%s.root"%(toyString))))
          rtv=execute("quickLimit -f %s -d combData -p %s --checkWS 1 --initialGuess 10000 --minTolerance 1E-5  --minStrat 1  --nllOffset 1 -o %s" % (wsfile, poi, outputfile.replace("FitResult","Limits").replace(".root","%s.root"%(toyString))))
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
    parser.add_argument('--sigmean', dest='sigmean', type=int, default=0, help='Mean of signal Gaussian for s+b fit (in GeV)')
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
