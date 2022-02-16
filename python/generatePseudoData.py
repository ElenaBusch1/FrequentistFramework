#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse

gRand = ROOT.TRandom3()

def fluctuatePoisson(hist):
    global gRand

    result = hist.Clone("fluctuated hist");
    result.Reset("M")

    nBinsX = hist.GetNbinsX();
    nBinsY = hist.GetNbinsY();

    '''
    for i in range(0, nBinsX+2):
        for j in range(0, nBinsY+2):
            ibin = hist.GetBin(i, j);
            fluc = gRand.Poisson(hist.GetBinContent(ibin));
            print ibin, hist.GetBinContent(ibin), fluc
            if fluc >= 0:
                result.SetBinContent(ibin, fluc);
                result.SetBinError(ibin, math.sqrt(fluc));
    '''

    for ibin in range(0, nBinsX+2):
            fluc = gRand.Poisson(hist.GetBinContent(ibin));
            #print ibin, hist.GetBinContent(ibin), fluc
            if fluc >= 0:
                result.SetBinContent(ibin, fluc);
                result.SetBinError(ibin, math.sqrt(fluc));



    return result;

def generatePseudoData(infile, inhist, outfile, outhist, nreplicas, scaling):
    f_in = ROOT.TFile(infile, "READ")
    h_in = f_in.Get(inhist)
    h_in.SetDirectory(0)
    f_in.Close()

    h_in.Scale(scaling)

    f_out = ROOT.TFile(outfile, "RECREATE")
    f_out.cd()

    for i in range(0, nreplicas):
        if nreplicas > 20 and (i%(nreplicas/20) == 0):
            print i,"/",nreplicas

        gRand.SetSeed(i*h_in.GetNbinsX())
        h_out = fluctuatePoisson(h_in)
        h_out.Write("%s_%d" % (outhist, i))

    f_out.Close()


def main(args):
    global gRand

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--infile', dest='infile', type=str, default='', help='Input file name')
    parser.add_argument('--inhist', dest='inhist', type=str, default='', help='Input hist name')
    parser.add_argument('--outfile', dest='outfile', type=str, default='', help='Output file name')
    parser.add_argument('--outhist', dest='outhist', type=str, default='', help='Output hist name')
    parser.add_argument('--nreplicas', dest='nreplicas', type=int, default=50, help='Number of replicas to generate')
    parser.add_argument('--scaling', dest='scaling', type=float, default=1., help='factor to scale the lumi by')
    
    args = parser.parse_args(args)

    generatePseudoData(infile=args.infile, inhist=args.inhist, outhist=args.outhist, nreplicas=args.nreplicas, scaling=args.scaling)


if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
