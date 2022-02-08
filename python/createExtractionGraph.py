#!/usr/bin/env python
import ROOT
import sys, re, os, math, optparse
from array import array
from ROOT import *
from math import sqrt
from glob import glob
import ExtractFitParameters as efp
import numpy
from color import getColorSteps

gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")



def main(args):
    SetAtlasStyle()

    parser = optparse.OptionParser(description='%prog [options] INPUT')
    parser.add_option('--outfile', dest='outfile', type=str, default='extractionGraphs.root', help='Output file name')
    
    options, args = parser.parse_args(args)

    paths = args
    sigmeans = set()
    sigwidths = set()
    sigamps = set()
    dict_file = {}

    for p in paths:
        res=re.search(r'mean(\d+)_width(\d+)(:?_amp\d+)?', p)
        m=int(res.group(1))
        w=int(res.group(2))
        
        sigmeans.add(m)
        sigwidths.add(w)

        try:
            a=int(res.group(3)[4:])
        except:
            a=0
        sigamps.add(a)
            
        if (m, w, a) in dict_file:
            dict_file[(m, w, a)].append(p)
        else:
            dict_file[(m, w, a)]=[p]
            
    sigmeans = list(sigmeans)
    sigwidths = list(sigwidths)
    sigamps = list(sigamps)

    sigmeans.sort()
    sigwidths.sort()
    sigamps.sort()

    colors = getColorSteps(len(sigmeans)*len(sigwidths))

    fout = TFile(options.outfile, "RECREATE")

    profile_list = []
    allPoints_list = []

    for j,sigmean in enumerate(sigmeans):
        
        for i,sigwidth in enumerate(sigwidths):

            g_allPoints = TGraph()
            g_profile   = TGraphErrors()
            sqrtB = None

            for k,sigamp in enumerate(sigamps):
    
                try:
                    tmp_path_fitresult = dict_file[(sigmean, sigwidth, sigamp)]
                except:
                    print "WARNING: No fitresult file for", sigmean, sigwidth, sigamp
                    continue

                #find number of injected events:
                if sigamp > 0:
                    tmp_path_injection = tmp_path_fitresult.replace("FitResult", "PD")

                    try:
                        f = TFile(tmp_path_injection[0])
                        h = f.Get("pseudodata_0_injection")
                        n_injected = h.Integral(0, h.GetNbinsX()+1)
                        f.Close()
                    except:
                        print "WARNING: Could not find injection file for tmp_path_limits. Using n_injected=0 now."
                        n_injected = 0
                else:
                    n_injected = 0
                
                inj_extr = []
                nans = 0
                
                parNames = {}
                parLists = {}
                parHists = {}
        
                for path in tmp_path_fitresult:
                    try:
                        f = TFile(path)
                        h = f.Get("postfit_params")
                        for i in range(1, h.GetNbinsX()+1):
                            p = h.GetBinContent(i)
                            if not i in parNames:
                                parNames[i] = h.GetXaxis().GetBinLabel(i)
                                parLists[i] = []
                            parLists[i].append(p)
                    except:
                        print "Couldn't read fit parameters from", path
                        continue

                for i in parNames:
                    par = parNames[i]
                    l = parLists[i]
                    h = TH1D(par, par, 100, min(l), max(l))
                    
                    for e in l:
                        h.Fill(e)

                    parHists[i] = h
                    
                    if "nsig" in par:
                        # print n_injected, nsig
                        for e in l:
                            inj_extr.append((n_injected, e))
                            if math.isnan(e):
                                nans += 1
                    
                print "n_injected: %d,   NaNs: %d" % (n_injected, nans)
                # if float(nans) / len(inj_extr) < 0.02:
                for t in inj_extr:
                    g_allPoints.SetPoint(g_allPoints.GetN(), t[0], t[1])
   
                arr = numpy.array([x[1] for x in inj_extr])
                nFit = numpy.mean(arr)
                nFitErr = numpy.std(arr, ddof=1) #1/N-1 corrected
                
                if sqrtB == None:
                    sqrtB = (n_injected / sigamp) if sigamp != 0 else 1
                
                g_profile.SetPoint(g_profile.GetN(), sigamp, nFit / sqrtB)
                g_profile.SetPointError(g_profile.GetN()-1, 0, nFitErr / sqrtB)

                d = fout.mkdir("hists_mean%d_width%d_amp%d" % (sigmean, sigwidth, sigamp))
                d.cd()
                for h in parHists.values():
                    h.Write()
                d.Close()
                # print "Setting point at", sigamp, nFit / sqrtB

            fout.cd()
            g_allPoints.SetTitle("%d GeV Gauss (%d%%)" % (sigmean, sigwidth))
            g_allPoints.Write("g1_extraction_gauss_%d_%d" % (sigmean, sigwidth))
            
            g_profile.SetTitle("%d GeV Gauss (%d%%)" % (sigmean, sigwidth))
            g_profile.Write("g1_profile_gauss_%d_%d" % (sigmean, sigwidth))

            allPoints_list.append(g_allPoints)
            profile_list.append(g_profile)

    fout.Close()

    # Plotting:
    c = TCanvas()
    mg = TMultiGraph()

    for i,g in enumerate(profile_list):
        g.SetLineWidth(2)
        g.SetLineColor(colors[i])
        g.SetMarkerColor(colors[i])
        mg.Add(g, "")

    mg.Draw("APL")
    mg.GetXaxis().SetTitle("Injected N_{sig} / #sqrt{N_{bkg}}")
    mg.GetYaxis().SetTitle("Extracted N_{sig} / #sqrt{N_{bkg}}")
    mg.GetXaxis().SetLimits(-0.5, 6)
    # mg.GetYaxis().SetLimits(-0.5, 15)
    mg.SetMinimum(-0.5)
    mg.SetMaximum(8)
    c.Update()

    c.BuildLegend(0.2,0.54,0.5,0.78)

    l = TLine(-0.5,-0.5,6,6)
    l.SetLineColor(kGray+2)
    l.SetLineStyle(7)
    l.Draw()

    lumi = 29
    if "lumi" in dict_file.values()[0]:
        try:
            lumi=int(dict_file.values()[0].split("lumi")[-1].split("_")[0])
        except:
            pass
    text1 = "Pseudodata %d fb^{-1}" % lumi

    text2 = "global fit"
    if "four" in  dict_file.values()[0]:
        text2 += " 4 par"
    if "five" in  dict_file.values()[0]:
        text2 += " 5 par"
    if "nloFit" in dict_file.values()[0]:
        text2 = "NLOFit"

    text = text1 + ", " + text2

    ATLASLabel(0.2, 0.9, "   Work in progress", 13)
    myText(0.2, 0.82, 1, text)

    raw_input("enter")

    c.Print(options.outfile.replace(".root", ".png"))
    
if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   

