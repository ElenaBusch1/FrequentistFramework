#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from array import array
from ROOT import *
from math import sqrt
from glob import glob

gROOT.LoadMacro("../../TLASpectraFit/atlasstyle-00-04-02/AtlasLabels.C")
gROOT.LoadMacro("../../TLASpectraFit/atlasstyle-00-04-02/AtlasStyle.C")
gROOT.LoadMacro("../../TLASpectraFit/atlasstyle-00-04-02/AtlasUtils.C")

# path = "/data/barn01/bartels/TLA/quickFit/run/Limits_J75yStar03_mean${MEAN}_width${WIDTH}.root"
path = "../run/Limits/Limits_J75yStar03_mean${MEAN}_width${WIDTH}.root"

sigmeans=[ 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1300, 1400, 1500, 1600, 1700, 1800, ]
# sigwidths=[ 5, 7, 10, 12, 15, ]
sigwidths=[ 5, 7, 10 ]

# lumi = 3600
lumi = 29300

def createFillBetweenGraphs(g1, g2):
  g_fill = TGraph()
  
  for i in range(g1.GetN()):
      x=ROOT.Double()
      y=ROOT.Double()
    
      g1.GetPoint(i, x, y)
    
      g_fill.SetPoint(g_fill.GetN(), x, y)

  for i in range(g2.GetN()-1, -1, -1):
      x=ROOT.Double()
      y=ROOT.Double()
    
      g2.GetPoint(i, x, y)
    
      g_fill.SetPoint(g_fill.GetN(), x, y)

  return g_fill


def main(args):
    SetAtlasStyle()
 
    # colors = [kBlue, kMagenta+2, kRed+1, kGreen+2]
    colors = [kBlue, kRed+1, kOrange-3]

    g_obs = []
    g_exp = []
    g_exp1 = []
    g_exp2 = []
    g_exp1u = []
    g_exp2u = []
    g_exp1d = []
    g_exp2d = []

    for i,sigwidth in enumerate(sigwidths):

        g_obs.append( TGraph() )
        g_exp.append( TGraph() )
        g_exp1u.append( TGraph() )
        g_exp2u.append( TGraph() )
        g_exp1d.append( TGraph() )
        g_exp2d.append( TGraph() )
        
        for j,sigmean in enumerate(sigmeans):
            
            tmp_path = path
            tmp_path = tmp_path.replace("${MEAN}", str(sigmean))
            tmp_path = tmp_path.replace("${WIDTH}", str(sigwidth))
        
            f = TFile(tmp_path, "READ")
            if f.IsZombie():
                continue
            h = f.Get("limit")
            
            obs = h.GetBinContent(h.GetXaxis().FindBin("Observed")) / lumi
            exp = h.GetBinContent(h.GetXaxis().FindBin("Expected")) / lumi
            exp1u = h.GetBinContent(h.GetXaxis().FindBin("+1sigma")) / lumi
            exp2u = h.GetBinContent(h.GetXaxis().FindBin("+2sigma")) / lumi
            exp1d = h.GetBinContent(h.GetXaxis().FindBin("-1sigma")) / lumi
            exp2d = h.GetBinContent(h.GetXaxis().FindBin("-2sigma")) / lumi
            
            g_obs[i].SetPoint(g_obs[i].GetN(), sigmean, obs)
            g_exp[i].SetPoint(g_exp[i].GetN(), sigmean, exp)
            g_exp1u[i].SetPoint(g_exp1u[i].GetN(), sigmean, exp1u)
            g_exp2u[i].SetPoint(g_exp2u[i].GetN(), sigmean, exp2u)
            g_exp1d[i].SetPoint(g_exp1d[i].GetN(), sigmean, exp1d)
            g_exp2d[i].SetPoint(g_exp2d[i].GetN(), sigmean, exp2d)


        g_exp1.append( createFillBetweenGraphs(g_exp1d[-1], g_exp1u[-1]) )
        g_exp2.append( createFillBetweenGraphs(g_exp2d[-1], g_exp2u[-1]) )

        g_exp1[-1].SetFillColorAlpha(colors[i], 0.2)
        g_exp2[-1].SetFillColorAlpha(colors[i], 0.2)
        g_exp[-1].SetLineColor(colors[i])
        g_exp[-1].SetLineStyle(2)
        g_exp[-1].SetLineWidth(2)
        g_obs[-1].SetLineWidth(2)
        g_obs[-1].SetLineColor(colors[i])
        g_obs[-1].SetMarkerColor(colors[i])


    c = TCanvas("c1", "c1", 800, 600)
    c.SetLogy()

    leg_obs = TLegend(0.65,0.70,0.85,0.85)
    leg_exp = TLegend(0.65,0.49,0.85,0.64)

    g_exp2[0].Draw("af")
    g_exp2[0].GetXaxis().SetTitle("M_{G} [GeV]")
    g_exp2[0].GetYaxis().SetTitle("#sigma #times #it{A} #times #it{BR} [pb]")
    g_exp2[0].GetHistogram().SetMaximum(50.)
    g_exp2[0].GetXaxis().SetLimits(min(sigmeans), max(sigmeans))

    g_exp2[0].Draw("af")
    c.Modified()

    g_exp1[0].Draw("f")

    for i,g in enumerate(g_exp):
        g.Draw("l")
        leg_exp.AddEntry(g, "#sigma_{G}/M_{G} = %.2f" % (sigwidths[i]/100.), "l")
    for i,g in enumerate(g_obs):
        g.Draw("pl")
        leg_obs.AddEntry(g, "#sigma_{G}/M_{G} = %.2f" % (sigwidths[i]/100.), "lp")
        
    ATLASLabel(0.20, 0.90, "Work in progress", 13)
    myText(0.20, 0.85, 1, "95% CL_{s} upper limts", 13)
    # myText(0.20, 0.80, 1, "#sqrt{s}=13 TeV, 3.6 fb^{-1}", 13)
    myText(0.20, 0.80, 1, "#sqrt{s}=13 TeV, 29.3 fb^{-1}", 13)

    myText(0.65, 0.90, 1, "Observed:", 13)
    myText(0.65, 0.69, 1, "Expected:", 13)
    leg_exp.Draw()
    leg_obs.Draw()

    c1.Print("../run/limitPlot.png")

    # raw_input("Press enter to continue...")

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
