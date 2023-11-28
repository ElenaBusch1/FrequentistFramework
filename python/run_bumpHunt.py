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
               ntoys=0,
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
               rebinOnlyBH = False,
               rangelow = 225,
               rangehigh = 1000,
              ):

    myRebinEdges = rebinEdges

    # generate the config files on the fly in run dir
    if not os.path.isfile("%s/run/AnaWSBuilder.dtd"%(cdir)):
        execute("ln -s ../config/dijetTLA/AnaWSBuilder.dtd %s/run/AnaWSBuilder.dtd"%(cdir))

    tmptopfile="%s/run/dijetTLA_fromTemplate_%s.xml"%(cdir, outputstring)
    tmpsignalfile="%s/run/dijetTLACat_signal_%d_%d_%s.xml"%(cdir, sigmean, sigwidth, outputstring)

    signalWSName   = config.signals[signalfile]["workspacefile"]
    signalfileName = config.signals[signalfile]["signalfile"]
    sigwsfile      = config.signals[signalfile]["workspacefile"]
    sighist        = config.signals[signalfile]["histname"]

    sighist = sighist.replace("MEAN", "%d"%sigmean)
    sigwsfile = sigwsfile.replace("MEAN", "%d"%(sigmean))


    shutil.copy2(topfile, tmptopfile) 
    shutil.copy2(signalfileName, tmpsignalfile) 
    tmpsignalfile.replace("MEAN", str(sigmean))
    
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
    #systFileName = config.signals[signalfile]["systFile"]
    #systFileName = systFileName.replace("MEAN", "%.0f"%sigmean)
    #systematics = gs.writeSystematics("systematics", sigmean, systFileName)
    systematics = ""
    
    replaceinfile(tmptopfile, 
                  [
                   ("  <Input>CATEGORYFILE</Input>", newName),
                   ("  <POI>nsig_meanMEAN_DATAHIST</POI>", newSignal),
                   ("nsig_meanMEAN_DATAHIST=0", newSignalZero),
                   ("CDIR", cdir),
                   ("MEAN", str(sigmean)),
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
                   ("WPERCENT", str(sigwidth/100.)),
                   ("WIDTH", str(sigwidth)),
                   ("SIGHIST", str(sighist)),
                   ("SIGFILE", str(sigwsfile)),
                   ("OUTPUTFILE", wsfile),
                   ("SYSTEMATICS", systematics),
                  ])



    for toy in range(max(ntoys, 1)):
      postfitfile=outputfile.replace("FitResult","PostFit")
      postfitfile=postfitfile.replace("CHANNEL", histName)


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
        #rangelow = config.samples[histName]["rangelow"]
        #rangehigh = config.samples[histName]["rangehigh"]
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
        #if useSysts:
        #  categoryfile=config.samples[histName]["categoryfileSysts"]
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
          ("WIDTH", str(sigwidth)),
        ])

      if dosignal:
          poi=poi
      else:
          poi=None


      print("Finished fit extractor")
      #print ("Global fit p(chi2)=%.3f" % pvals_global[0])


      pfe = PostfitExtractor(
        datafile=datafiles[0],
        datahist=tmpDataHists[0],
        datafirstbin=rangelow,
        wsfile=outputfile,
        rebinfile=rebinFile,
        rebinhist=rebinHist,
        binEdges=rebinEdges,
      )



      print (datafiles, datahist, tmpDataHists)
      print ("Running rebinning", myRebinEdges)
      pfe.SetRebinEdges(myRebinEdges)
      postfitfileName=postfitfile.replace("CHANNEL", datahist[0])
      pfe.WriteRoot(postfitfileName, doRecreate=False, suffix=datahist[0] + "_" +toyString, dirPerCategory=True)


      # TODO: Need to use the actual path, since this will only run if working in the correct directory
      # need to unset pythonpath in order to not use cvmfs numpy
      bkghist = "postfit%s_%s"%(histName, toyString)
      datahistName = "data%s_%s"%(histName, toyString)
      outname = datahist[0]
      execute("source ../pyBumpHunter/pyBH_env/bin/activate; env PYTHONPATH=\"\" python3 ../python/FindBHWindow.py --inputfile %s  --outputjson %s/scripts/%s/BHresults.json --bkghist %s --datahist %s --outname %s; deactivate" % (postfitfile, cdir, outdir, bkghist, datahistName, outname))
      #execute("source ../pyBumpHunter/pyBH_env/bin/activate; env PYTHONPATH=\"\" python3 ../python/FindBHWindow.py --inputfile %s  --outputjson %s/scripts/%s/BHresults.json  --outname %s; deactivate" % (postfitfile, cdir, outdir, outname))

      # pass results of pyBH via this json file
      #with open(cdir + "/scripts/" + outdir + "/BHresults.json") as f:
      #    BHresults=json.load(f)

      #print("Bump hunter", BHresults)

      
    
    return 0
