#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse

def GetNsig(histbkg, histsig, sigamp):
    histsig.Scale(1./histsig.Integral())
    # determine FWHM
    binSigLow = histsig.FindFirstBinAbove(histsig.GetMaximum()/2);
    binSigHigh = histsig.FindLastBinAbove(histsig.GetMaximum()/2);

    #need to seperate binSig and binBkg because the histograms may not start at same x
    binBkgLow  = histbkg.FindBin(histsig.GetBinCenter(binSigLow))
    binBkgHigh = histbkg.FindBin(histsig.GetBinCenter(binSigHigh))

    nBkg = histbkg.Integral(binBkgLow, binBkgHigh)
    fSig = histsig.Integral(binSigLow, binSigHigh)

    if nBkg > 0.:
        nSig = int(sigamp * math.sqrt(nBkg) / fSig)
    else:
        nSig = 0

    return nSig

def InjectZprime(infile, histname, sigfile, sighist, sigamp, outfile, firsttoy=None, lasttoy=None):
    f_in = ROOT.TFile(infile, "READ")
    f_sig = ROOT.TFile(sigfile, "READ")

    h_sig = f_sig.Get(sighist)
    h_sig.SetDirectory(0)
    h_sig.Smooth(3)

    f_out = ROOT.TFile(outfile, "RECREATE")
    f_out.cd()

    gRand = ROOT.TRandom3()
    seed = 0

    for histKey in f_in.GetListOfKeys():
        histName = histKey.GetName()
        
        if not histname in histName:
            continue
        if firsttoy != None and lasttoy != None and re.search(r'.*_(\d+)', histName):
            #reduce size by omitting all other toys
            toy = int(re.search(r'.*_(\d+)', histName).group(1))
            if toy < firsttoy or toy > lasttoy:
                seed += 1
                continue

        hist = f_in.Get(histName).Clone()
        hinj = hist.Clone()
        hinjonly = hist.Clone("injectedSignal") 
        hinjonly.Reset("M")

        # define the parameters of the gaussian and fill it
        nSig = GetNsig(hist, h_sig, sigamp)
        if nSig > 0.:
            print 'Injecting Signal ', sighist, ' Number of events = ', nSig, 
            print ' (ntimes = ', sigamp, ')'

            gRand.SetSeed(seed)
            hinjonly.FillRandom(h_sig, nSig) 
            hinj.Add(hinjonly)

        hinj.Write(histName)
        hist.Write(histName+"_beforeInjection")
        hinjonly.Write(histName+"_injection")

        seed += 1
            
    f_out.Close()


def main(args):

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--infile', dest='infile', type=str, default='../Input/data/dijetTLAnlo/data_J75yStar03_range400_2079.root', help='original data file name')
    parser.add_argument('--histname', dest='histname', type=str, default='data', help='original data hist name')
    parser.add_argument('--sigfile', dest='sigfile', type=str, help='path to histogram of signal histogram')
    parser.add_argument('--sighist', dest='sighist', type=str, help='histogram name of input signal')
    parser.add_argument('--sigamp', dest='sigamp', type=float, default=5, help='number of injected events (in sigmas of central bin)')
    parser.add_argument('--outfile', dest='outfile', type=str, default='', help='Output file name')
    parser.add_argument('--firsttoy', dest='firsttoy', type=int, help='Only consider toys larger than this number')
    parser.add_argument('--lasttoy', dest='lasttoy', type=int, help='Only consider toys lower than this number')

    args = parser.parse_args(args)

    searchstring =r'mR(\d+)'
    res=re.search(searchstring, args.sighist)
    m=int(res.group(1))

    if args.outfile == "":
        args.outfile = os.path.split(args.infile)[-1].replace(".root", "_mR%d_amp%.0f.root" % (m, args.sigamp))

    InjectSignal(infile=args.infile,
                 histname=args.histname,
                 sigfile=args.sigfile,
                 sighist=args.sighist,
                 sigamp=args.sigamp,
                 outfile=args.outfile,
                 firsttoy=args.firsttoy,
                 lasttoy=args.lasttoy)
    
if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
