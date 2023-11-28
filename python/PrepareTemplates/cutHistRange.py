import ROOT
import sys, re, os, math, argparse
from array import array

def main(args):

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--rangeMin', dest='rangeMin', type=int, default=531, help='Start of range')
    parser.add_argument('--rangeMax', dest='rangeMax', type=int, default=2058, help='End of range')
    parser.add_argument('paths', type=str, nargs="+", help='Input files')
    args = parser.parse_args(args)

    for path in args.paths:

        f_in = ROOT.TFile(path, "READ")
        f_out = ROOT.TFile(path.replace(".root", "_range%d_%d.root" % (args.rangeMin, args.rangeMax)), "RECREATE")
        
        for histKey in f_in.GetListOfKeys():
            
            histName = histKey.GetName()
            
            h_in = f_in.Get(histName)
        
            if not isinstance(h_in, ROOT.TH1):
                continue
        
            binEdges = []
            
            for ibin in range(0, h_in.GetNbinsX()+2):
                binEdge = h_in.GetXaxis().GetBinLowEdge(ibin)
                if (binEdge >= args.rangeMin-0.001 and binEdge <= args.rangeMax+0.001): 
                    binEdges.append(binEdge)
        
            h_out = ROOT.TH1D(histName, h_in.GetTitle(), len(binEdges)-1, array('d', binEdges))

            for ibin in range(1, h_out.GetNbinsX()+1):
                x =  h_out.GetXaxis().GetBinCenter(ibin)
                oldBin = h_in.GetXaxis().FindBin(x)
                h_out.SetBinContent(ibin, h_in.GetBinContent(oldBin))
                h_out.SetBinError(ibin, h_in.GetBinError(oldBin))

            h_out.Write(histName)

        f_out.Close()

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
