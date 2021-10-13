import ROOT
import sys, re, os, math, argparse
from array import array

def main(args):

    for path in args:

        f_in = ROOT.TFile(path, "READ")
        f_out = ROOT.TFile(path.replace(".root", "_fixedBins.root"), "RECREATE")
        
        for histKey in f_in.GetListOfKeys():
            
            histName = histKey.GetName()
            
            h_in = f_in.Get(histName)
        
            if not isinstance(h_in, ROOT.TH1):
                continue
        
            h_out = ROOT.TH1D(histName, h_in.GetTitle(), h_in.GetNbinsX(), 0, h_in.GetNbinsX())

            for ibin in range(1, h_out.GetNbinsX()+1):
                h_out.SetBinContent(ibin, h_in.GetBinContent(ibin))
                h_out.SetBinError(ibin, h_in.GetBinError(ibin))

            h_out.Write(histName)
            
        f_out.Close()

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
