#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse

gRand = ROOT.TRandom3()

def fluctuatePoisson(hist):
    global gRand

    result = hist.Clone("fluctuated hist");
    result.Reset("M")

    nBinsX = hist.GetNbinsX();
    for ibin in range(0, nBinsX+2):
      fluc = gRand.Poisson(hist.GetBinContent(ibin));
      if fluc >= 0:
          result.SetBinContent(ibin, fluc);
          result.SetBinError(ibin, math.sqrt(fluc));

    return result;

def generatePseudoData(infile, inhist, infit, outfile, outhist, nreplicas, scaling, rangelow):
    f_in = ROOT.TFile(infile, "READ")
    h_in = f_in.Get(inhist)
    h_fit = f_in.Get(infit)
    print (infile, inhist)
    h_in.SetDirectory(0)
    h_fit.SetDirectory(0)
    f_in.Close()

    h_in.Scale(scaling)
    h_fit.Scale(scaling)

    f_out = ROOT.TFile(outfile, "RECREATE")
    f_out.cd()

    h_out = ROOT.TH1D(h_fit.Clone("fluctuated hist"));
    h_out.Reset()
    h_out.SetDirectory(0)

    nBinsX = h_out.GetNbinsX();
    for ibin in range(0, nBinsX+2):
      dataErr = math.sqrt(h_in.GetBinContent(ibin+rangelow))
      mcErr = h_in.GetBinError(ibin+rangelow)
      if dataErr < mcErr:
        h_out.SetBinContent(ibin, h_fit.GetBinContent(ibin))
      else:
        h_out.SetBinContent(ibin, h_in.GetBinContent(ibin+rangelow))

    f_out = ROOT.TFile(infile, "UPDATE")
    #f_out = ROOT.TFile("test.root", "RECREATE")
    h_out.Write(outhist)
    #h_out.Write()
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

    generatePseudoData(infile=args.infile, inhist=args.inhist, outfile=args.outfile,  outhist=args.outhist, nreplicas=args.nreplicas, scaling=args.scaling)


if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
