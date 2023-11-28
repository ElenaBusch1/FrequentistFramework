#!/usr/bin/env python

from __future__ import print_function
import os,sys,re,argparse
from InjectGaussian import InjectGaussian
from InjectTemplate import InjectTemplate
from run_anaFit import run_anaFit
import config as config

def run_injections_anaFit(datafile, 
                          datahist, 
                          topfile, 
                          categoryfile, 
                          signalfile, 
                          wsfile, 
                          outputfile, 
                          outputstring,
                          nbkg, 
                          nsig,
                          rangelow, 
                          rangehigh, 
                          dosignal, 
                          dolimit, 
                          sigmean, 
                          sigwidth, 
                          maskthreshold, 
                          sigamp, 
                          rebinfile, 
                          rebinhist,
                          rebinedges, 
                          loopstart, 
                          loopend, 
                          fitFunction, 
                          cdir,
                          outdir,
                          useSysts = False,
                          systematicNameFile = "uncertaintySets/systematics.txt",
                          systematicAllNameFile = "uncertaintySets/systematics.txt",
                          histName = "",
                          biasMagnitude=0,
                          inDirSysts = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/test",
                          initialGuess = "1000",
                         ):

    print("Injecting signal of amplitude %.1f sigma (FWHM)" % sigamp)
    injecteddatafile=datafile
    injecteddatafile=injecteddatafile.replace(".root","_Mean_%d_Width_%d_Amp_%.0f_Sig_%s.root" % (sigmean, sigwidth, sigamp, signalfile))
    print (injecteddatafile)


    print (loopstart, loopend)
    if config.signals[signalfile]["histname"] == "":
      print ("Running gaussian injection")
      nbkgWindow = InjectGaussian(infile=datafile,
                       histname=datahist,
                       sigmean=sigmean,
                       sigwidth=sigwidth,
                       sigamp=sigamp,
                       outfile=injecteddatafile,
                       firsttoy=loopstart,
                       lasttoy=loopend-1)
    else:
      print ("Running template injection")
      nbkgWindow = InjectTemplate(infile=datafile,
                       histname=datahist,
                       sigmean=sigmean,
                       sigwidth=sigwidth,
                       sigamp=sigamp,
                       outfile=injecteddatafile,
                       firsttoy=loopstart,
                       lasttoy=loopend-1,
                       wsfile = config.signals[signalfile]["templatefile"].replace("MEAN", "%d"%sigmean).replace("WIDTH", "%d"%sigwidth),
                       wspdf = config.signals[signalfile]["histname"].replace("MEAN", "%d"%(sigmean)),
                       minMass = rangelow,
                       maxMass = rangehigh,
                       )

    if loopstart==None or loopend==None:
       ntoys=1
    else:
       ntoys = loopend

    
    #print("Running run_anaFit with datahist %s" % datahistName)
    run_anaFit(datafile=injecteddatafile,
               datahist=datahist,
               topfile=topfile,
               categoryfile=categoryfile,
               wsfile=wsfile,
               outputfile=outputfile,
               outputstring=outputstring,
               fitFunction=fitFunction,
               cdir=cdir,
               nbkg=nbkg,
               outdir=outdir,
               rangelow=rangelow,
               rangehigh=rangehigh,
               dosignal=dosignal,
               signalfile = signalfile, 
               nsig=nsig,
               nbkgWindow=nbkgWindow,
               ntoys=ntoys,
               dolimit=dolimit,
               sigmean=sigmean,
               sigwidth=sigwidth,
               rebinFile=rebinfile,
               rebinHist=rebinhist,
               rebinEdges=rebinedges,
               maskthreshold=maskthreshold,
               useSysts = useSysts,
               systematicNameFile = systematicNameFile,
               systematicAllNameFile = systematicAllNameFile,
               histName = histName,
               biasMagnitude= biasMagnitude,
               inDirSysts = inDirSysts,
               initialGuess = initialGuess,
              )




def main(args):
    
    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--datafile', dest='datafile', type=str, required=True, help='Input data file')
    parser.add_argument('--datahist', dest='datahist', type=str, required=True, help='Input finebinned data histogram name')
    parser.add_argument('--topfile', dest='topfile', type=str, required=True, help='Input top-level xml card')
    parser.add_argument('--categoryfile', dest='categoryfile', type=str, required=True, help='Input category xml card')
    parser.add_argument('--wsfile', dest='wsfile', type=str, required=True, help='Output workspace file')
    parser.add_argument('--outputfile', dest='outputfile', type=str, required=True, help='Output fitresult file')
    parser.add_argument('--nbkg', dest='nbkg', type=str, required=True, help='Initial value and range of nbkg par (e.g. "2E8,0,3E8")')
    parser.add_argument('--rangelow', dest='rangelow', type=int, required=True, help='Start of fit range (in GeV)')
    parser.add_argument('--rangehigh', dest='rangehigh', type=int, required=True, help='End Start of fit range (in GeV)')
    parser.add_argument('--dosignal', dest='dosignal', action="store_true", help='Perform s+b fit (default: bkg-only)')
    parser.add_argument('--dolimit', dest='dolimit', action="store_true", help='Perform limit setting')
    parser.add_argument('--sigmean', dest='sigmean', type=int, default=1000, help='Mean of signal Gaussian for s+b fit (in GeV)')
    parser.add_argument('--sigwidth', dest='sigwidth', type=int, default=7, help='Width of signal Gaussian for s+b fit (in %)')
    parser.add_argument('--maskthreshold', dest='maskthreshold', type=float, default=0.01, help='Threshold of p(chi2) below which to run BH and mask the most significant window')
    parser.add_argument('--sigamp', dest='sigamp', type=float, default=0, help='Amplitude of Gaussian to inject (in sigma)')
    parser.add_argument('--rebinfile', dest='rebinfile', type=str, required=False, help='File containing histogram with template histogram for rebinning result')
    parser.add_argument('--rebinhist', dest='rebinhist', type=str, required=False, help='Name of template histogram for rebinning result')
    parser.add_argument('--rebinedges', dest='rebinedges', type=int, nargs="*", default=None, help='Name of template hist')
    parser.add_argument('--loopstart', dest='loopstart', type=int, help='First toy to fit')
    parser.add_argument('--loopend', dest='loopend', type=int, help='Last toy to fit')
    parser.add_argument('--fitFunction', dest='fitFunction', type=str, default=None, help='Name of the file with the fit function information')
    parser.add_argument('--cdir', dest='cdir', type=str, default=None, help='Full path to current directory')
    parser.add_argument('--outdir', dest='outdir', type=str, default=None, help='Full path to current directory')

    args = parser.parse_args(args)


    run_injections_anaFit(datafile=args.datafile, datahist=args.datahist, topfile=args.topfile, categoryfile=args.categoryfile, wsfile=args.wsfile, outputfile=args.outputfile, nbkg=args.nbkg, rangelow=args.rangelow, rangehigh=args.rangehigh, dosignal=args.dosignal, dolimit=args.dolimit, sigmean=args.sigmean, sigwidth=args.sigwidth, maskthreshold=args.maskthreshold, sigamp=args.sigamp, rebinfile=args.rebinfile, rebinedges=args.rebinedges, loopstart=args.loopstart, loopend=args.loopend, fitFunction=args.fitFunction, cdir=args.cdir, rebinhist=args.rebinhist, outdir=args.outdir)



if __name__ == "__main__":  
    sys.exit(main(sys.argv[1:]))
