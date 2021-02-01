#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from ROOT import *

def main(args):

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--infile', dest='infile', type=str, default='../Input/data/dijetTLAnlo/data_J75yStar03_range400_2079.root', help='original data file name')
    parser.add_argument('--histname', dest='histname', type=str, default='data', help='original data hist name')
    parser.add_argument('--sigmean', dest='sigmean', type=float, default=600, help='mean of injected Gaussian')
    parser.add_argument('--sigwidth', dest='sigwidth', type=float, default=5, help='width of injected Gaussian (in %)')
    parser.add_argument('--sigamp', dest='sigamp', type=float, default=5, help='number of injected events (in sigmas of central bin)')
    parser.add_argument('--outfile', dest='outfile', type=str, default='', help='Output file name')

    args = parser.parse_args(args)

    if args.outfile == "":
        args.outfile = os.path.split(args.infile)[-1].replace(".root", "_mean%.0f_width%.0f_amp%.0f.root" % (args.sigmean, args.sigwidth, args.sigamp))

    f_in = ROOT.TFile(args.infile, "READ")
    f_out = ROOT.TFile(args.outfile, "RECREATE")
    f_out.cd()

    gRand = ROOT.TRandom3()
    seed = 0

    for histKey in f_in.GetListOfKeys():
        histName = histKey.GetName()
        
        if not args.histname in histName:
            # copy all histograms except data
            # hist.Write("histName")
            pass
        else:
            
            hist = f_in.Get(histName).Clone()
            hinj = hist.Clone()
            hgaus = hist.Clone("injectedSignal") 
            hgaus.Reset("M")

            # define the parameters of the gaussian and fill it
            if args.sigmean > 0.0:

                # determine the gaussian amplitude (ntimes * sqrt(n) in FWHW range)
                rangeLow = args.sigmean  - 1.18*(args.sigwidth*0.01) * args.sigmean
                rangeHigh = args.sigmean + 1.18*(args.sigwidth*0.01) * args.sigmean
                binLow = hist.FindBin(rangeLow)
                binHigh = hist.FindBin(rangeHigh)
                nBkg = hist.Integral(binLow, binHigh)

                if nBkg > 0.0:
                    sigma = (args.sigwidth*0.01) * args.sigmean 
                    mygaus = TF1( 'mygaus', 'gaus', 0, 10000) 
                    mygaus.SetParameters(1.0, args.sigmean, sigma) 

                    fSig = 0.762 #integral from -1.18 sigma to +1.18 sigma
                    nSig = int(math.sqrt(nBkg)*args.sigamp / fSig)

                    print 'Injecting Signal with mean = ', args.sigmean, ' Number of events = ', nSig, 
                    print ' (ntimes = ', args.sigamp, ') Width = ', args.sigwidth

                    gRand.SetSeed(seed)
                    hgaus.FillRandom('mygaus', nSig) 
                    hinj.Add(hgaus)

            hinj.Write(histName)
            hist.Write(histName+"_beforeInjection")
            hgaus.Write(histName+"_injection")

            seed += 1
            
    f_out.Close()


if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
