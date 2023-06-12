#!/usr/bin/env python
import ROOT
from math import log10
from math import floor
import sys, re, os, math, argparse
from array import array
from ROOT import *
from math import sqrt
from math import isnan
from glob import glob
import config as config
import LocalFunctions as lf

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

def plotLimits(sigmeans, sigwidths, paths, lumis, outdir, cdir, channelName, atlasLabel="Simulation Internal", deltaMassAboveFit=0, sigamp=0, ntoy=0, signalType="Gaussian", isMx = False, alphaBin = 0, signalName = "Y"):
    SetAtlasStyle()

    massString = "mY"
    #if isMx:
    #  massString = "mX"
    fileName = "limitFiles/h2_eff_alpha_%s_forJen.root"%(massString)
    histName = "h2_eff_alpha_%s"%(massString)
    alpha = config.alphaBins[alphaBin] 
    #+ 0.01
    h_eff = lf.read_histogram(fileName, histName)
    h_xsTmp = lf.read_histogram("limitFiles/h2_xs_alpha_%s_forJen.root"%(massString), "h2_xs_alpha_%s"%(massString))
    h_xs = h_xsTmp.Clone("hXs")
    for xBin in range(h_xs.GetNbinsX()):
      for yBin in range(h_xs.GetNbinsY()):
        if h_xsTmp.GetBinContent(xBin+1, yBin+1):
          h_xs.SetBinContent(xBin+1, yBin+1, log10(h_xsTmp.GetBinContent(xBin+1, yBin+1)))

    myMeans = [2000, 3000, 4000, 6000, 8000, 10000]
    gEff = TGraph2D()
    test = TGraph()
    for i, myMean in enumerate(myMeans):
      test.SetPoint(i+1, myMean, h_xs.GetBinContent(i+1, 12))
      print h_xs.GetBinContent(i+1, 12)
      for j in range(h_eff.GetNbinsY()):
        gEff.SetPoint(gEff.GetN()+1, myMean, h_eff.GetYaxis().GetBinCenter(j+1), h_eff.GetBinContent(i+1, j+1))




    # colors = [kBlue, kMagenta+2, kRed+1, kGreen+2]
    colors = [kBlue, kRed+1, kOrange-3]

    g_model_datasets = []

    g_obs_datasets = []
    g_exp_datasets = []
    g_exp1_datasets = []
    g_exp2_datasets = []
    g_exp1u_datasets = []
    g_exp2u_datasets = []
    g_exp1d_datasets = []
    g_exp2d_datasets = []

    g_obs_datasets_model = []
    g_exp_datasets_model = []
    g_exp1_datasets_model = []
    g_exp2_datasets_model = []
    g_exp1u_datasets_model = []
    g_exp2u_datasets_model = []
    g_exp1d_datasets_model = []
    g_exp2d_datasets_model = []


    for dataset in range(len(paths)):

        g_model = []
        g_obs = []
        g_exp = []
        g_exp1 = []
        g_exp2 = []
        g_exp1u = []
        g_exp2u = []
        g_exp1d = []
        g_exp2d = []

        g_obs_model = []
        g_exp_model = []
        g_exp1_model = []
        g_exp2_model = []
        g_exp1u_model = []
        g_exp2u_model = []
        g_exp1d_model = []
        g_exp2d_model = []

        for i,sigwidth in enumerate(sigwidths):

            g_model.append( TGraph() )

            g_obs.append( TGraph() )
            g_exp.append( TGraph() )
            g_exp1u.append( TGraph() )
            g_exp2u.append( TGraph() )
            g_exp1d.append( TGraph() )
            g_exp2d.append( TGraph() )

            g_obs_model.append( TGraph() )
            g_exp_model.append( TGraph() )
            g_exp1u_model.append( TGraph() )
            g_exp2u_model.append( TGraph() )
            g_exp1d_model.append( TGraph() )
            g_exp2d_model.append( TGraph() )

            for j,sigmean in enumerate(sigmeans):
                if isMx:
                  alpha = config.alphaBins[alphaBin]
                  mY = round(sigmean / alpha / 10) * 10
                  #if sigmean < 500:
                  #  continue
                  #if mY < 3000:
                  #  continue
                  #if mY > 10000:
                  #  continue
                  #print sigmean, mY, alpha
                else:
                  mYTest = floor(sigmean/1000) * 1000 
                  mX = round(mYTest * alpha / 10) * 10
                  #print sigmean, mYTest, mX
                  #if mYTest < 2000:
                  #  continue
                  #if mX < 500:
                  #  continue
                  

                rangelow = config.samples[channelName[0]]["rangelow"]

                if sigmean < (rangelow + deltaMassAboveFit) :
                   continue


                # TODO need a better way of choosing a file. sometimes they don't get created, so making a second option.
                # Obviously this won't matter with real data, but it does for the tests
                tmp_path = paths[dataset]
                
                tmp_path = config.getFileName(paths[dataset], cdir, None, outdir, sigmean, sigwidth, sigamp) + ".root"
                f = TFile(tmp_path, "READ")

                if f.IsZombie():
                  tmp_path = config.getFileName(paths[dataset], cdir, None, outdir, sigmean, sigwidth, sigamp) + "_%s.root"%(ntoy)
                  print "zombie"
                  f = TFile(tmp_path, "READ")
                  if f.IsZombie():
                    print "still zombie"
                    continue
                #print f

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

                xs = pow(10, test.Eval(sigmean))*1000.
                #eff = h_eff.Interpolate(sigmean, alpha)
                #eff = gEff.Eval(sigmean, alpha)
                eff = gEff.Interpolate(sigmean, alpha)

                g_exp_model[i].SetPoint(g_exp_model[i].GetN(), sigmean, exp*xs*eff)
                g_exp1u_model[i].SetPoint(g_exp1u_model[i].GetN(), sigmean, exp1u*xs*eff)
                g_exp2u_model[i].SetPoint(g_exp2u_model[i].GetN(), sigmean, exp2u*xs*eff)
                g_exp1d_model[i].SetPoint(g_exp1d_model[i].GetN(), sigmean, exp1d*xs*eff)
                g_exp2d_model[i].SetPoint(g_exp2d_model[i].GetN(), sigmean, exp2d*xs*eff)

                if isnan(obs):
                    continue

                print sigmean, eff, h_eff.Interpolate(sigmean, alpha)
                g_model[i].SetPoint(g_model[i].GetN(), sigmean, xs*eff)
                #g_model[i].SetPoint(g_model[i].GetN(), sigmean, xs)

                g_obs[i].SetPoint(g_obs[i].GetN(), sigmean, obs)
                g_obs_model[i].SetPoint(g_obs_model[i].GetN(), sigmean, obs*xs*eff)


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

           
            g_exp1_model.append( createFillBetweenGraphs(g_exp1d_model[-1], g_exp1u_model[-1]) )
            g_exp2_model.append( createFillBetweenGraphs(g_exp2d_model[-1], g_exp2u_model[-1]) )
            g_exp1_model[-1].SetFillColorAlpha(colors[i], 0.2)
            g_exp2_model[-1].SetFillColorAlpha(colors[i], 0.2)
            g_exp_model[-1].SetLineColor(colors[i])
            g_exp_model[-1].SetLineStyle(2)
            g_exp_model[-1].SetLineWidth(2)
            g_obs_model[-1].SetLineWidth(2)
            g_obs_model[-1].SetLineColor(colors[i])
            g_obs_model[-1].SetMarkerColor(colors[i])

        g_model_datasets.append(g_model)
        g_obs_datasets.append(g_obs)
        g_exp_datasets.append(g_exp)
        g_exp1_datasets.append(g_exp1)
        g_exp2_datasets.append(g_exp2)
        g_exp1u_datasets.append(g_exp1u)
        g_exp2u_datasets.append(g_exp2u)
        g_exp1d_datasets.append(g_exp1d)
        g_exp2d_datasets.append(g_exp2d)

        g_obs_datasets_model.append(g_obs_model)
        g_exp_datasets_model.append(g_exp_model)
        g_exp1_datasets_model.append(g_exp1_model)
        g_exp2_datasets_model.append(g_exp2_model)
        g_exp1u_datasets_model.append(g_exp1u_model)
        g_exp2u_datasets_model.append(g_exp2u_model)
        g_exp1d_datasets_model.append(g_exp1d_model)
        g_exp2d_datasets_model.append(g_exp2d_model)

    c = TCanvas("c1_%s"%(outdir), "c1", 800, 600)
    c.SetLogy()

    leg_obs = TLegend(0.65,0.72,0.85,0.87)
    leg_exp = TLegend(0.65,0.5,0.85,0.65)

    #minY = 0.005
    minY = 0.000003
    maxY = 0.5

    g_exp_datasets[0][0].Draw("af")
    g_exp_datasets[0][0].GetXaxis().SetTitle("M_{%s} [GeV]"%(signalName))
    g_exp_datasets[0][0].GetYaxis().SetTitle("#sigma #times #it{A} #times #it{BR} [pb]")
    g_exp_datasets[0][0].GetYaxis().SetTitleOffset(1.1)
    g_exp_datasets[0][0].GetHistogram().SetMinimum(minY)
    g_exp_datasets[0][0].GetHistogram().SetMaximum(maxY)
    g_exp_datasets[0][0].GetXaxis().SetLimits(min(sigmeans)-49.9, max(sigmeans)+49.9)

    #g_model_datasets[0][0].SetLineColor(ROOT.kRed)
    #g_model_datasets[0][0].Draw("l")

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
                leg_exp.AddEntry(g, "#sigma_{G}/M_{%s} = %.2f" % (signalName, sigwidths[i]/100.), "l")
        for i,g in enumerate(g_obs_datasets[dataset]):
            g.Draw("pl")
            if (dataset==0):
                leg_obs.AddEntry(g, "#sigma_{G}/M_{%s} = %.2f" % (signalName, sigwidths[i]/100.), "lp")


    ATLASLabel(0.20, 0.90, atlasLabel, 13)
    myText(0.20, 0.84, 1, "95% CL_{s} upper limits", 13)
    myText(0.2, 0.78, 1, "#sqrt{s}=13 TeV, %.0f fb^{-1}"%(lumis*0.001), 13)
    myText(0.2, 0.72, 1, config.samples[channelName[0]]["varLabel"], 13)


    myText(0.65, 0.92, 1, "Observed:", 13)
    myText(0.65, 0.70, 1, "Expected:", 13)
    leg_exp.Draw()
    leg_obs.Draw()

    c.Print("%s/limitPlot_%s_%s.pdf"%(outdir, channelName[0], signalType))


    '''
    minY = 1e-20
    maxY = 1e-8
    g_exp_datasets_model[0][0].Draw("af")
    g_exp_datasets_model[0][0].GetXaxis().SetTitle("M_{%s} [GeV]"%(signalName))
    g_exp_datasets_model[0][0].GetYaxis().SetTitle("#sigma #times #it{BR} [pb]")
    g_exp_datasets_model[0][0].GetYaxis().SetTitleOffset(1.0)
    g_exp_datasets_model[0][0].GetHistogram().SetMinimum(minY)
    g_exp_datasets_model[0][0].GetHistogram().SetMaximum(maxY)
    g_exp_datasets_model[0][0].GetXaxis().SetLimits(min(sigmeans)-49.9, max(sigmeans)+49.9)

    c.Modified()


    for dataset in range(len(paths)):
        if dataset != len(paths)-1:

            l=TLine()
            l.DrawLineNDC(xToNDC(sigmeans[-1]), gPad.GetBottomMargin(), xToNDC(sigmeans[-1]), 0.72)

        g_exp2_datasets_model[dataset][0].Draw("f")
        g_exp1_datasets_model[dataset][0].Draw("f")

        for i,g in enumerate(g_exp_datasets_model[dataset]):
            g.Draw("l")
            if (dataset==0):
                leg_exp.AddEntry(g, "#sigma_{G}/M_{G} = %.2f" % (sigwidths[i]/100.), "l")
        for i,g in enumerate(g_obs_datasets_model[dataset]):
            g.Draw("pl")
            if (dataset==0):
                leg_obs.AddEntry(g, "#sigma_{G}/M_{G} = %.2f" % (sigwidths[i]/100.), "lp")


    
    

    ATLASLabel(0.20, 0.90, atlasLabel, 13)
    myText(0.20, 0.84, 1, "95% CL_{s} upper limits", 13)
    myText(0.2, 0.78, 1, "#sqrt{s}=13 TeV, %.1f fb^{-1}"%(lumis*0.001), 13)
    myText(0.2, 0.72, 1, config.samples[channelName[0]]["varLabel"], 13)


    myText(0.65, 0.92, 1, "Observed:", 13)
    myText(0.65, 0.76, 1, "Expected:", 13)
    leg_exp.Draw()
    leg_obs.Draw()
    c.Print("%s/limitPlot_modelDependent_%s_%s.pdf"%(outdir, channelName[0], signalType))

    '''




def main(args):
  paths = [ "jjj/Limits_sigPlusBkg_Fit_300_1200_Sig_MEAN_width_WIDTH_amp_1_3.root",]
  sigmeans  =  [ 550, 650]
  sigwidths =  [ 7, ]
  lumis = [ 29300 ]
  plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=paths, lumis=lumis, outdir="jjj")
  


if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
