#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from array import array
from ROOT import *
from math import sqrt
from glob import glob

gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")


# sigmeans=[ 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1300, 1400, 1500, 1600, 1700, 1800, ]
# sigwidths=[ 5, 7, 10, 12, 15, ]
sigmeans=[ 700, 1000, 1400, 1800 ]
# sigmeans=[ 1000 ]
sigwidths=[ 5 ]
# sigamps=[ 10, 7, 5, 3, 0 ]
sigamps=[ 5, 4, 3, 2, 1, 0 ]

# sigamps=[ 0 ]

lumi = 130000

def main(args):
    SetAtlasStyle()
 
    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--infile', dest='infile', type=str, default='/data/scratch/users/bartels/FarmOutput/TLA/quickFit_injections_globalFit_fourpar_201122/quickFit_swift_J100_${MEAN}_${WIDTH}_${AMP}_sbFit/output.*/run/Limits_*.txt', help='Input FitResult paths')
    parser.add_argument('--outfile', dest='outfile', type=str, default='extractionGraphs.root', help='Output file name')
    
    args = parser.parse_args(args)

    path_limits = args.infile
    path_injection = path_limits.replace("Limits", "PD").replace(".txt", ".root")

    colors = [kBlue, kRed+1, kOrange-3]

    fout = TFile(args.outfile, "RECREATE")

    for i,sigwidth in enumerate(sigwidths):
        
        for j,sigmean in enumerate(sigmeans):
            
            g = TGraph()
            sqrtB = None

            for k,sigamp in enumerate(sigamps):
    
                #find number of injected events:
              
                if sigamp > 0:
                    tmp_path_injection = path_injection
                    tmp_path_injection = tmp_path_injection.replace("${MEAN}", str(sigmean))
                    tmp_path_injection = tmp_path_injection.replace("${WIDTH}", str(sigwidth))
                    tmp_path_injection = tmp_path_injection.replace("${AMP}", str(sigamp))
                    print tmp_path_injection 
                    tmp_path_injection = glob(tmp_path_injection)

                    if len(tmp_path_injection) == 0:
                        continue

                    f = TFile(tmp_path_injection[0])
                    h = f.Get("pseudodata_0_injection")
                    n_injected = h.Integral(0, h.GetNbinsX()+1)
                    f.Close()
                else:
                    n_injected = 0

                if sqrtB == None:
                    sqrtB = (n_injected / sigamp) if sigamp != 0 else 1
                    print "setting sqrtB to", sqrtB
                
                tmp_path_limits = path_limits
                tmp_path_limits = tmp_path_limits.replace("${MEAN}", str(sigmean))
                tmp_path_limits = tmp_path_limits.replace("${WIDTH}", str(sigwidth))
                tmp_path_limits = tmp_path_limits.replace("${AMP}", str(sigamp))
                print tmp_path_limits
                tmp_path_limits = glob(tmp_path_limits)
                if len(tmp_path_limits) == 0:
                    continue

                inj_limit = []
                nans = 0

                for path in tmp_path_limits:
                    with open(path) as f:
                        limit = float(f.readline().split()[0])
                        
                    # print n_injected, limit
                    inj_limit.append((n_injected, limit))
                    if math.isnan(limit):
                        nans += 1
                
                print "n_injected: %d,   NaNs: %d" % (n_injected, nans)
                # if float(nans) / len(inj_limit) < 0.02:
                for t in inj_limit:
                    g.SetPoint(g.GetN(), t[0]/sqrtB, t[1]/sqrtB)
                # else:
                #     print "skipping", inj_limit[0][0], "due to NaNs"

   
            fout.cd()
            g.SetTitle("%d GeV Gauss (%d%%)" % (sigmean, sigwidth))
            g.Write("g1_limit_gauss_%d_%d" % (sigmean, sigwidth))


    fout.Close()

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
