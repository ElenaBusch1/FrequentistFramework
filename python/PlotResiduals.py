#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from array import array
from ROOT import *
from math import sqrt
from glob import glob
from color import getColorSteps

gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")

def main(args):
    SetAtlasStyle()
 

    paths = args[0:]

    colors = getColorSteps(len(paths))
    # fillstyles = [3245, 3254, 3295, 3205]
    fillstyles = [3245, 3245, 3245, 3245]

    hists = []

    for p in paths:
        f = TFile(p)
        h = f.Get("postFitSigma")
        h.SetDirectory(0)
        f.Close()
        hists.append(h)

    c = TCanvas("c1", "c1", 800, 600)
        
    for i, h in enumerate(hists):
        h.SetFillStyle(fillstyles[i])
        h.SetLineColor(colors[i])
        h.SetFillColor(colors[i])
        h.SetMarkerColor(colors[i])
        h.SetMinimum(min(-3.2, h.GetMinimum()))
        h.SetMaximum(max( 4.2, h.GetMaximum()))
        h.GetXaxis().SetTitle("m_{jj} [GeV]")
        h.GetYaxis().SetTitle("Residuals [#sigma]")

        h.Draw("same hist")

    leg = TLegend(0.70,0.70,0.85,0.90)
    # leg.AddEntry(hists[0], "quickFit", "f")
    # leg.AddEntry(hists[1], "custom RooFit", "f")
    leg.AddEntry(hists[0], "CT14")
    leg.AddEntry(hists[1], "MMHT")
    leg.AddEntry(hists[2], "ABMP")
    leg.AddEntry(hists[3], "ABMP, rew.")
    leg.Draw()


    ATLASLabel(0.20, 0.90, "Work in progress", 13)
    myText(0.20, 0.85, 1, "#sqrt{s}=13 TeV, 29 fb^{-1}", 13)

    c1.Print("residuals_J100.svg")

    raw_input("Press enter to continue...")


if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   

