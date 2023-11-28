#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from array import array
from ROOT import *
from math import sqrt
from math import isnan
from glob import glob
import config as config
import LocalFunctions as lf
import DrawingFunctions as df
import python.makeHepData as hepdata


#gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
#gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
#gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")


def get_theo_events(channelName="ajj_simpleTrig", masses=[250,350,450,550,650], lumi=1):
    input_file=TFile("../Input/data/dijetISR/sigHistMorphed_mjj_100_to_2000_"+channelName+"_yStar0p825.root","READ")
    g=TGraphErrors()
    theoryJJJ = [ 0.32222176*2.32, 0.32518957*1.9732, 0.28729875*1.8928, 0.25567026*2.04, 0.23259003*2.44]
    theoryJBB = [ 0.285*0.5478, 0.251*0.4518, 0.187*0.4130, 0.129*0.4361, 0.089*0.4973]


    for i, mass in enumerate(masses):
        if channelName == "FullRun2Data_NoNN_No21":
          g.SetPoint(g.GetN(), mass, theoryJJJ[i])
        else:
          g.SetPoint(g.GetN(), mass, theoryJBB[i])
        print theoryJJJ[i], theoryJBB[i], channelName == "FullRun2Data_NoNN_No21", channelName
    return g

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

def plotLimits(sigmeans, sigwidths, paths, lumis, outdir, cdir, channelName, rangelow, rangehigh, atlasLabel="Simulation Internal", signalfile="Gaussian", minY = 0.003, maxY = 2):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)
    SetAtlasStyle()

    # colors = [kBlue, kMagenta+2, kRed+1, kGreen+2]
    colors = [kBlue, kRed+1, kOrange-3, kPink, kGreen+2]
    #colors = ["#6B2C90", "#ED516F", "#F4BB4A",  "#339966", "#006699"]


    g_obs_datasets = []
    g_exp_datasets = []
    g_exp1_datasets = []
    g_exp2_datasets = []
    g_exp1u_datasets = []
    g_exp2u_datasets = []
    g_exp1d_datasets = []
    g_exp2d_datasets = []

    for dataset in range(len(paths)):

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
                # TODO need a better way of choosing a file. sometimes they don't get created, so making a second option.
                # Obviously this won't matter with real data, but it does for the tests
                tmp_path = paths[dataset]
                #tmp_path = config.getFileName(paths[dataset], cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + "0.root"
                tmp_path = config.getFileName(paths[dataset], cdir, channelName, rangelow, rangehigh, sigmean, sigwidth, 0) + ".root"

                h = lf.read_histogram(tmp_path,"limit")
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
                    print "It's nan, continuing"
                    continue

                g_obs[i].SetPoint(g_obs[i].GetN(), sigmean, obs)


            g_exp1.append( createFillBetweenGraphs(g_exp1d[-1], g_exp1u[-1]) )
            g_exp2.append( createFillBetweenGraphs(g_exp2d[-1], g_exp2u[-1]) )

            g_exp1[-1].SetFillColorAlpha(colors[i], 0.2)
            g_exp2[-1].SetFillColorAlpha(colors[i], 0.2)
            g_exp[-1].SetLineColor(colors[i])
            #g_exp1[-1].SetFillColorAlpha(ROOT.TColor.GetColor(colors[i]), 0.2)
            #g_exp2[-1].SetFillColorAlpha(ROOT.TColor.GetColor(colors[i]), 0.2)
            #g_exp[-1].SetLineColor(ROOT.TColor.GetColor(colors[i]))
            g_exp[-1].SetLineStyle(2)
            g_exp[-1].SetLineWidth(2)
            g_obs[-1].SetLineWidth(2)
            g_obs[-1].SetLineColor(colors[i])
            g_obs[-1].SetMarkerColor(colors[i])
            g_exp[-1].SetMarkerColor(colors[i])
            #g_obs[-1].SetLineColor(ROOT.TColor.GetColor(colors[i]))
            #g_obs[-1].SetMarkerColor(ROOT.TColor.GetColor(colors[i]))
            #g_exp[-1].SetMarkerColor(ROOT.TColor.GetColor(colors[i]))
            g_obs[-1].SetMarkerStyle(20+i)
            g_exp[-1].SetMarkerStyle(20+i)

            g_obs_datasets.append(g_obs)
            g_exp_datasets.append(g_exp)
            g_exp1_datasets.append(g_exp1)
            g_exp2_datasets.append(g_exp2)
            g_exp1u_datasets.append(g_exp1u)
            g_exp2u_datasets.append(g_exp2u)
            g_exp1d_datasets.append(g_exp1d)
            g_exp2d_datasets.append(g_exp2d)



    g_exp_datasets[0][0].GetXaxis().SetLimits(min(sigmeans)-49.9, max(sigmeans)+49.9)
    g_exp_datasets[0][0].GetHistogram().SetMinimum(minY)
    g_exp_datasets[0][0].GetHistogram().SetMaximum(maxY)

    if( len(g_exp_datasets)==1) and signalfile.find("template") >= 0:
      g_exp_datasets[0][0].GetXaxis().SetTitle("m_{Z'} [GeV]")
    else:
      g_exp_datasets[0][0].GetXaxis().SetTitle("m_{G} [GeV]")
    g_exp_datasets[0][0].GetYaxis().SetTitle("#sigma #times #it{A} #times #it{BR} [pb]")
    g_exp_datasets[0][0].GetYaxis().SetTitleOffset(1.0)



    c = TCanvas("c1_%s"%channelName, "c1", 800, 600)
    c.SetLogy()
    g_exp_datasets[0][0].Draw("af")

    c.Modified()

    if( len(g_exp_datasets)==1):
      leg_exp = TLegend(0.57,0.8,0.85,0.92)
      leg_exp.SetFillStyle(0)

      leg_type = TLegend(0.57,0.73,0.9,0.78)
      leg_type.SetNColumns(2)
      leg_type.SetFillStyle(0)

      leg_sig = TLegend(0.57,0.67,0.9,0.72)
      leg_sig.SetNColumns(2)
      leg_sig.SetFillStyle(0)



    else:
      leg_exp = TLegend(0.57,0.7,0.85,0.92)
      leg_exp.SetFillStyle(0)


      leg_type = TLegend(0.57,0.65,0.9,0.7)
      leg_type.SetNColumns(2)
      leg_type.SetFillStyle(0)

      leg_sig = TLegend(0.57,0.60,0.9,0.65)
      leg_sig.SetNColumns(2)


    test1sigma = g_exp1_datasets[0][0].Clone("test")
    #test1sigma.SetFillColorAlpha(ROOT.TColor.GetColor(colors[0]), 0.4)
    test1sigma.SetFillColorAlpha(colors[0], 0.4)
    leg_sig.AddEntry(test1sigma, "#pm 1 #sigma", "f")
    leg_sig.AddEntry(g_exp2_datasets[0][0], "#pm 2 #sigma", "f")

    testObs = g_obs_datasets[0][0].Clone("test_%s"%(g_obs_datasets[0][0].GetName()))
    testExp = g_exp_datasets[0][0].Clone("test_%s"%(g_exp_datasets[0][0].GetName()))
   
    if( len(g_exp_datasets)!=1):
      testObs.SetMarkerColor(ROOT.kBlack)
      testObs.SetLineColor(ROOT.kBlack)
      testExp.SetMarkerColor(ROOT.kBlack)
      testExp.SetLineColor(ROOT.kBlack)

    leg_type.AddEntry(testObs, "Observed", "lp")
    leg_type.AddEntry(testExp, "Expected", "l")

    #g_theo=None
    #if len(g_exp_datasets[0])==1: #add theory curve                                                                       
    #    g_theo=get_theo_events(channelName)
    #    g_theo.SetLineColor(kRed)
    #    g_theo.SetMarkerColor(kRed)
    #    g_theo.SetLineStyle(3)
    #    g_theo.Draw("l SAME")
    #    leg_exp.AddEntry(g_theo,"Theory (#it{g}_{#it{q}}=0.2)", "l")



    legNames = []

    for dataset in range(len(paths)):

        if dataset != len(paths)-1:
            l=TLine()
            l.DrawLineNDC(xToNDC(sigmeans[-1]), gPad.GetBottomMargin(), xToNDC(sigmeans[-1]), 0.72)

        g_exp2_datasets[dataset][0].Draw("f")
        g_exp1_datasets[dataset][0].Draw("f")

        for i,g in enumerate(g_exp_datasets[dataset]):
            g.Draw("l")
            if (dataset==0):
              if len(sigwidths)==1:
                #leg_exp.AddEntry(g, "#sigma_{Z'}/M_{Z'} = %.0f%%" % (sigwidths[i]), "lp")
                leg_exp.AddEntry(g, "Z'", "lp")
                legNames.append("Z'")
              else:
                leg_exp.AddEntry(g, "#sigma_{G}/M_{G} = %.0f%%" % (sigwidths[i]), "lp")
                legNames.append("#sigma_{G}/M_{G} = %.0f%%" % (sigwidths[i]))
        for i,g in enumerate(g_obs_datasets[dataset]):
            g.Draw("pl")
            #if (dataset==0):
            #    leg_obs.AddEntry(g, "#sigma_{Z'}/M_{Z'} = %.2f" % (sigwidths[i]/100.), "lp")


    ATLASLabel(0.20, 0.90, atlasLabel, 13)
    myText(0.2, 0.84, 1, "#sqrt{s}=13 TeV, %d fb^{-1}"%(int(lumis*0.001)), 13)
    myText(0.2, 0.78, 1, "%s" %(config.samples[channelName]["label"]), 13)
    myText(0.20, 0.72, 1, "95% CL_{s} upper limits", 13)

    leg_sig.Draw()
    leg_type.Draw()
    leg_exp.Draw()

    df.SaveCanvas(c, "%s/limitPlot_swift_fivepar_%s"%(outdir, signalfile))

    hepdata.makeLimitHepData(g_exp, g_obs, g_exp1d, g_exp1u, g_exp2d, g_exp2u, legNames, histName = "limits_%s_%s"%(channelName, signalfile))

    #print paths
    for dataset in range(len(paths)):
      for i,g in enumerate(g_exp_datasets[dataset]):

        g_exp_datasets[i][0].Draw("af")

        leg_exp = TLegend(0.57,0.8,0.85,0.92)
        leg_exp.SetFillStyle(0)

        leg_type = TLegend(0.57,0.73,0.9,0.78)
        leg_type.SetNColumns(2)
        leg_type.SetFillStyle(0)
  
        leg_sig = TLegend(0.57,0.67,0.9,0.72)
        leg_sig.SetNColumns(2)
        leg_sig.SetFillStyle(0)


        leg_type.AddEntry(testObs, "Observed", "lp")
        leg_type.AddEntry(testExp, "Expected", "l")

        test1sigma = g_exp1_datasets[dataset][i].Clone("test")
        test1sigma.SetFillColorAlpha(ROOT.TColor.GetColor(colors[i]), 0.4)
        leg_sig.AddEntry(test1sigma, "#pm 1 #sigma", "f")
        leg_sig.AddEntry(g_exp2_datasets[dataset][i], "#pm 2 #sigma", "f")





        if dataset != len(paths)-1:
            l=TLine()
            l.DrawLineNDC(xToNDC(sigmeans[-1]), gPad.GetBottomMargin(), xToNDC(sigmeans[-1]), 0.72)

        g_exp2_datasets[dataset][i].Draw("f")
        g_exp1_datasets[dataset][i].Draw("f")

        g.Draw("l")
        if len(sigwidths)==1:
          leg_exp.AddEntry(g, "Z'", "lp")
        else:
          leg_exp.AddEntry(g, "#sigma_{G}/M_{G} = %.0f%%" % (sigwidths[i]), "lp")
        g_obs_datasets[dataset][i].Draw("pl")

        ATLASLabel(0.20, 0.90, atlasLabel, 13)
        myText(0.2, 0.84, 1, "#sqrt{s}=13 TeV, %d fb^{-1}"%(int(lumis*0.001)), 13)
        myText(0.2, 0.78, 1, "%s" %(config.samples[channelName]["label"]), 13)
        myText(0.20, 0.72, 1, "95% CL_{s} upper limits", 13)

        leg_sig.Draw()
        leg_type.Draw()
        leg_exp.Draw()

        df.SaveCanvas(c, "%s/limitPlot_swift_fivepar_%s_sigwidth_%d"%(outdir, signalfile, sigwidths[i]))





def main(args):
  paths = [ "jjj/Limits_sigPlusBkg_Fit_300_1200_Sig_MEAN_width_WIDTH_amp_1_3.root",]
  sigmeans  =  [ 550, 650]
  sigwidths =  [ 7, ]
  lumis = [ 29300 ]
  plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=paths, lumis=lumis, outdir="jjj")
  


if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
