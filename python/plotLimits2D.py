#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from array import array
from ROOT import *
from math import sqrt
from math import isnan
from glob import glob
import config as config

ROOT.gROOT.SetBatch(ROOT.kTRUE)

gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")


def xToNDC(x):
    gPad.Update()
    lm = gPad.GetLeftMargin()
    rm = 1.-gPad.GetRightMargin()
    xndc = (rm-lm)*((gPad.XtoPad(x)-gPad.GetUxmin())/(gPad.GetUxmax()-gPad.GetUxmin()))+lm
    return xndc

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

def plotLimits(sigmeans, sigwidths, paths, lumis, outdir, cdir, channelNames, atlasLabel="Simulation Internal", deltaMassAboveFit=0, sigamp=0, ntoy=0, alphaBins = [], meansCentered = [1500, 2500, 3500, 5000, 7000, 9000, 11000]):
    SetAtlasStyle()

    # colors = [kBlue, kMagenta+2, kRed+1, kGreen+2]
    colors = [kBlue, kRed+1, kOrange-3]

    #limits2D = TGraph2D()

  
    limits2D = TH2D("limits2D", ";m_{Y} [GeV];#alpha;#sigma #times #it{A} #times #it{BR} [pb]", len(sigmeans), array('d', meansCentered), len(alphaBins)-1, array('d', alphaBins))

    for alphaBin, channelName in enumerate(channelNames):
        g_obs_datasets = []
        g_exp_datasets = []
        g_exp1_datasets = []
        g_exp2_datasets = []
        g_exp1u_datasets = []
        g_exp2u_datasets = []
        g_exp1d_datasets = []
        g_exp2d_datasets = []
  

        #for dataset in range(len(paths)):

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
                rangelow = config.samples[channelNames[alphaBin]]["rangelow"]
                if sigmean < (rangelow + deltaMassAboveFit) :
                   continue

                # TODO need a better way of choosing a file. sometimes they don't get created, so making a second option.
                # Obviously this won't matter with real data, but it does for the tests
                tmp_path = paths[alphaBin]
                tmp_path = config.getFileName(paths[alphaBin], cdir, None, outdir + channelNames[alphaBin], sigmean, sigwidth, sigamp) + "_%s.root"%(ntoy)
                f = TFile(tmp_path, "READ")

                if f.IsZombie():
                    if f.IsZombie():
                      continue
                h = f.Get("limit")
                obs = h.GetBinContent(h.GetXaxis().FindBin("Observed")) / lumis
                exp = h.GetBinContent(h.GetXaxis().FindBin("Expected")) / lumis
                exp1u = h.GetBinContent(h.GetXaxis().FindBin("+1sigma")) / lumis
                exp2u = h.GetBinContent(h.GetXaxis().FindBin("+2sigma")) / lumis
                exp1d = h.GetBinContent(h.GetXaxis().FindBin("-1sigma")) / lumis
                exp2d = h.GetBinContent(h.GetXaxis().FindBin("-2sigma")) / lumis

                g_exp[i].SetPoint(g_exp[i].GetN(), sigmean, exp)
                g_exp1u[i].SetPoint(g_exp1u[i].GetN(), sigmean, exp1u)
                g_exp2u[i].SetPoint(g_exp2u[i].GetN(), sigmean, exp2u)
                g_exp1d[i].SetPoint(g_exp1d[i].GetN(), sigmean, exp1d)
                g_exp2d[i].SetPoint(g_exp2d[i].GetN(), sigmean, exp2d)

                if isnan(obs):
                    continue

                g_obs[i].SetPoint(g_obs[i].GetN(), sigmean, obs)
                #limits2D.SetPoint(limits2D.GetN(), sigmean, alphaBin, obs)
                limits2D.Fill(sigmean, alphaBins[alphaBin], obs)
                print sigmean, alphaBins[alphaBin], exp


            #g_exp1.append( createFillBetweenGraphs(g_exp1d[-1], g_exp1u[-1]) )
            #g_exp2.append( createFillBetweenGraphs(g_exp2d[-1], g_exp2u[-1]) )

            #g_exp1[-1].SetFillColorAlpha(colors[i], 0.2)
            #g_exp2[-1].SetFillColorAlpha(colors[i], 0.2)
            #g_exp[-1].SetLineColor(colors[i])
            #g_exp[-1].SetLineStyle(2)
            #g_exp[-1].SetLineWidth(2)
            #g_obs[-1].SetLineWidth(2)
            #g_obs[-1].SetLineColor(colors[i])
            #g_obs[-1].SetMarkerColor(colors[i])

        g_obs_datasets.append(g_obs)
        g_exp_datasets.append(g_exp)
        g_exp1_datasets.append(g_exp1)
        g_exp2_datasets.append(g_exp2)
        g_exp1u_datasets.append(g_exp1u)
        g_exp2u_datasets.append(g_exp2u)
        g_exp1d_datasets.append(g_exp1d)
        g_exp2d_datasets.append(g_exp2d)

  
        leg_obs = TLegend(0.65,0.76,0.85,0.86)
        leg_exp = TLegend(0.65,0.6,0.85,0.7)
  
        minY = 0.00001
        maxY = 0.7
  
        '''
        g_exp_datasets[0][0].Draw("af")
        g_exp_datasets[0][0].GetXaxis().SetTitle("M_{G} [GeV]")
        g_exp_datasets[0][0].GetYaxis().SetTitle("#sigma #times #it{A} #times #it{BR} [pb]")
        g_exp_datasets[0][0].GetYaxis().SetTitleOffset(1.0)
        g_exp_datasets[0][0].GetHistogram().SetMinimum(minY)
        g_exp_datasets[0][0].GetHistogram().SetMaximum(maxY)
        g_exp_datasets[0][0].GetXaxis().SetLimits(min(sigmeans)-49.9, max(sigmeans)+49.9)
  
        c.Modified()
  
        for dataset in range(len(paths)):
          if dataset != len(paths)-1:

            l=TLine()
            l.DrawLineNDC(xToNDC(sigmeans[-1]), gPad.GetBottomMargin(), xToNDC(sigmeans[-1]), 0.72)

          g_exp2_datasets[dataset][0].Draw("f")
          g_exp1_datasets[dataset][0].Draw("f")

          for i,g in enumerate(g_exp_datasets[dataset]):
            g.Draw("l")
            if (dataset==0):
                leg_exp.AddEntry(g, "#sigma_{G}/M_{G} = %.2f" % (sigwidths[i]/100.), "l")
          for i,g in enumerate(g_obs_datasets[dataset]):
            g.Draw("pl")
            if (dataset==0):
                leg_obs.AddEntry(g, "#sigma_{G}/M_{G} = %.2f" % (sigwidths[i]/100.), "lp")


        ATLASLabel(0.20, 0.90, atlasLabel, 13)
        myText(0.20, 0.84, 1, "95% CL_{s} upper limits", 13)
        myText(0.2, 0.78, 1, "#sqrt{s}=13 TeV", 13)
        myText(0.2, 0.72, 1, "%.1f fb^{-1}" % (lumis*0.001), 13)
  
        myText(0.65, 0.92, 1, "Observed:", 13)
        myText(0.65, 0.76, 1, "Expected:", 13)
        leg_exp.Draw()
        leg_obs.Draw()

        c.Print("%s/limitPlot_swift_fivepar_%s.pdf"%(outdir, channelNames[alphaBin]))
        '''


    c = TCanvas("c1_%s"%(outdir), "c1", 800, 600)
    c.SetRightMargin(0.2)
    c.SetLogz()
    limits2D.Draw("COLZ")
    c.Print("%s/limits2D.pdf"%(outdir))


def main(args):
  paths = [ "jjj/Limits_sigPlusBkg_Fit_300_1200_Sig_MEAN_width_WIDTH_amp_1_3.root",]
  sigmeans  =  [ 550, 650]
  sigwidths =  [ 7, ]
  lumis = [ 29300 ]
  plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=paths, lumis=lumis, outdir="jjj")
  


if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
