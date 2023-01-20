#!/usr/bin/env python
from __future__ import print_function
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
    parser.add_option('--notoys', dest='notoys', action='store_true', help='Use one fit instead of many toys')
    
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
    sigamps.sort(reverse=True)

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
                    print("WARNING: No fitresult file for", sigmean, sigwidth, sigamp)
                    continue

                #find number of injected events:
                if sigamp > 0:
                    # tmp_path_injection = tmp_path_fitresult[0].replace("FitResult", "PD")
                    try:
                        tmp_path_injection = glob(os.path.join(os.path.dirname(tmp_path_fitresult[0]),"*_injected_mean*_width*_amp*.root"))[0]
                        print(tmp_path_injection)
                        f = TFile(tmp_path_injection)
                        # for obj in f.GetListOfKeys():
                        #     h=f.Get(obj.
                        h = f.Get("unfluctuated_injection")
                        n_injected = h.Integral(0, h.GetNbinsX()+1)
                        f.Close()
                    except:
                        print("WARNING: Could not find injection file for tmp_path_limits. Using n_injected=0 now.")
#                        return
                        n_injected = 0
                else:
                    n_injected = 0
                
                inj_extr = []
                nans = 0
                
                parNames = {}
                parLists = {}
                parErrs = {}
                parHists = {}
                parHists2 = {}
        
                for path in tmp_path_fitresult:
                    try:
                        f = TFile(path)
                        h = f.Get("postfit_params")
                        for i in range(1, h.GetNbinsX()+1):
                            p = h.GetBinContent(i)
                            if not i in parNames:
                                parNames[i] = h.GetXaxis().GetBinLabel(i)
                                parLists[i] = []
                                parErrs[i] = []
                            parLists[i].append(p)
                            parErrs[i].append(h.GetBinError(i))
                    except:
                        print("Couldn't read fit parameters from", path)
                        continue

                for i in parNames:
                    par = parNames[i]
                    l = parLists[i]
                    h = TH1D("mean%d_width%d_amp%d/%s" % (sigmean, sigwidth, sigamp, par), par, 100, min(l), max(l))
                    perc_1 = numpy.percentile(l,1)
                    perc_99 = numpy.percentile(l,99)
                    delta = perc_99-perc_1
                    _min = max([min(l), perc_1 - 0.2*delta])
                    _max = min([max(l), perc_99 + 0.2*delta])
                    h2 = TH1D("mean%d_width%d_amp%d_1to99_percentile/%s" % (sigmean, sigwidth, sigamp, par), par, 100, _min, _max)
                    
                    for e in l:
                        h.Fill(e)
                        h2.Fill(e)

                    parHists[i] = h
                    parHists2[i] = h2
                    
                    if "nsig" in par:
                        # print n_injected, nsig
                        print(l)
                        for e in l:
                            inj_extr.append((n_injected, e))
                            if math.isnan(e):
                                nans += 1
                    
                print("n_injected: %d,   NaNs: %d" % (n_injected, nans))
                # if float(nans) / len(inj_extr) < 0.02:
                for t in inj_extr:
                    g_allPoints.SetPoint(g_allPoints.GetN(), t[0], t[1])
   
                if sqrtB == None:
                    try:
                        sqrtB = (n_injected / sigamp) if sigamp != 0 else 1
                    except:
                        sqrtB = 1
                    
                if not options.notoys:
                    arr = numpy.array([x[1] for x in inj_extr])
                    nFit = numpy.mean(arr)
                    nFitErr = numpy.std(arr, ddof=1) #1/N-1 corrected
                                        
                    g_profile.SetPoint(g_profile.GetN(), sigamp, nFit / sqrtB)
                    g_profile.SetPointError(g_profile.GetN()-1, 0, nFitErr / sqrtB)
    
                    d = fout.mkdir("hists_mean%d_width%d_amp%d" % (sigmean, sigwidth, sigamp))
                    d.cd()
                    for h in parHists.values():
                        h.Write(h.GetName().split('/')[-1])
                    d.Close()

                    d = fout.mkdir("hists_mean%d_width%d_amp%d_1to99_percentile" % (sigmean, sigwidth, sigamp))
                    d.cd()
                    for h in parHists2.values():
                        h.Write(h.GetName().split('/')[-1])
                    d.Close()
                    # print "Setting point at", sigamp, nFit / sqrtB
                else:
                    for i in parNames:
                        par = parNames[i]
                        if "nsig" in par:
                            l = parLists[i][0]
                            e = parErrs[i][0]
                            
                            g_profile.SetPoint(g_profile.GetN(), sigamp, l / sqrtB)
                            g_profile.SetPointError(g_profile.GetN()-1, 0, e / sqrtB)
                        
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
    # if "lumi" in dict_file.values()[0]:
    if "lumi" in list(next(iter(dict_file.items())))[0]:
        try:
            # lumi=int(dict_file.values()[0].split("lumi")[-1].split("_")[0])
            lumi=int(list(next(iter(dict_file.items())))[0].split("lumi")[-1].split("_")[0])
        except:
            pass
    text1 = "Pseudodata %d fb^{-1}" % lumi

    text2 = "global fit"
    # if "four" in  dict_file.values()[0]:
    #     text2 += " 4 par"
    # if "five" in  dict_file.values()[0]:
    #     text2 += " 5 par"
    # if "nloFit" in dict_file.values()[0]:
    #     text2 = "NLOFit"
    text2="NLOFit"

    text = text1 + ", " + text2

    ATLASLabel(0.2, 0.9, "   Work in progress", 13)
    myText(0.2, 0.82, 1, text)

    # raw_input("enter")

    c.Print(options.outfile.replace(".root", ".png"))
    
if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   

