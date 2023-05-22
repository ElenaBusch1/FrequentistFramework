#!/usr/bin/env python
from __future__ import print_function
import ROOT
import sys, re, os, math, argparse
import color
import array
import json
from collections import OrderedDict

ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")

doSymmetric = True

ranges = [
   (150, 400),
   (230,500),
   (250,800),
   (300,1200),
   (1000,2500),
]

if doSymmetric:
   initvals = [
      [2.9372167648639036, 1.1356348224746515, 0.412734404647086, 2.0955121952384643, 204.72473418708194, 13.33035189862608, 0.023070508711273696, 369.0560059892184, 237],
      [0.46789135991762154, 2.2466404172388987, 3.4368144502830154, 1.0221802253469847, 339.24534119899147, 25.09445811068244, 0.010377201829036009, 305.8928700923177, 257],
      [0.26177873983500577, 1.6625568317060413, 99.99999985706762, 9.999999999433602, 584.9624282363235, 31.40628688100581, 0.00596640765057721, 878.9349385744961, 538],
      [0.2501367665876164, 2.221523567156397, 99.9999999845575, 1.4642260713620725, 977.9887879046056, 44.51162202377484, 0.003944127219711602, 1396.5295102603118, 877],
      [0.33581678879769594, 2.759942937571045, 2.5465275519325536, 0.35375819975254297, 1963.8558290951078, 71.63629000390421, 0.002358391908110491, 1407.4456288846188, 1296],
   ]
   
   limits = [
      [0, 10],
      [0, 10],
      [0, 200],
      [0, 20],
      [0, 3000],
      [0, 200],
      [0, 20],
   ]
else:
   initvals = [
      [3.001266302801475, 1.6848441928585505, 0.13986001064109632, 1.4450649582869357, 199.8922237481159, 11.04467711596765, 20.017052618555574, 0.021577096618038416],
      [0.5000000001239894, 2.1695448794067094, 2.7183810473807357, 1.0932687661733098, 338.7936140510232, 25.261499935090814, 25.286000799839226, 0.01046175209156952],
      [0.5000000011611061, 2.0152486179800992, 99.99999973648264, 2.4090384884032057, 588.4638802850174, 59.500079782779025, 29.90600549092226, 0.005702989962579341],
      [0.5000000000008564, 1.972077178626059, 33.221959320357506, 2.654685981404421, 984.3729282638158, 88.14898151480624, 40.962058961803216, 0.003770680820078809],
      [0.500000000490106, 2.7494289849286124, 3.0227360045314065, 3.1863400806741993e-13, 1968.7173072645935, 112.10773538171608, 70.0543800612753, 0.0022687715364200223],
   ]

   limits = [
      [0.5, 15],
      [0, 10],
      [0, 100],
      [0, 10],
      [0, 3000],
      [0, 200],
      [0, 1000],
      [0, 20],
   ]

def doubleSidedCrystalBall(x, par):
   alpha_l = par[0] 
   alpha_h = par[1] 
   n_l     = par[2] 
   n_h     = par[3] 
   mean	   = par[4] 
   sigma   =  par[5]
   N	   = par[6]
   try:
      t = (x[0]-mean)/sigma

      fact1TLessMinosAlphaL = alpha_l/n_l
      fact2TLessMinosAlphaL = (n_l/alpha_l) - alpha_l -t
      fact1THigherAlphaH = alpha_h/n_h
      fact2THigherAlphaH = (n_h/alpha_h) - alpha_h +t
      
      if (-alpha_l <= t and alpha_h >= t):
          result = math.exp(-0.5*t*t)
      elif (t < -alpha_l):
          result = math.exp(-0.5*alpha_l*alpha_l)*math.pow(fact1TLessMinosAlphaL*fact2TLessMinosAlphaL, -n_l)
      elif (t > alpha_h):
          result = math.exp(-0.5*alpha_h*alpha_h)*math.pow(fact1THigherAlphaH*fact2THigherAlphaH, -n_h)
    
      return N*result
   except:
      return 0

def asymmDoubleSidedCrystalBall(x, par):
   alpha_l = par[0] 
   alpha_h = par[1] 
   n_l     = par[2] 
   n_h     = par[3] 
   mean	   = par[4] 
   sigma_l = par[5]
   sigma_h = par[6]
   N	   = par[7]

   if x[0] > mean:
      t = (x[0]-mean)/sigma_h
   else:
      t = (x[0]-mean)/sigma_l

   fact1TLessMinosAlphaL = alpha_l/n_l
   fact2TLessMinosAlphaL = (n_l/alpha_l) - alpha_l -t
   fact1THigherAlphaH = alpha_h/n_h
   fact2THigherAlphaH = (n_h/alpha_h) - alpha_h +t
   
   if (-alpha_l <= t and alpha_h >= t):
       result = math.exp(-0.5*t*t)
   elif (t < -alpha_l):
       result = math.exp(-0.5*alpha_l*alpha_l)*math.pow(fact1TLessMinosAlphaL*fact2TLessMinosAlphaL, -n_l)
   elif (t > alpha_h):
       result = math.exp(-0.5*alpha_h*alpha_h)*math.pow(fact1THigherAlphaH*fact2THigherAlphaH, -n_h)

   return N*result


def main(args):
    parser = argparse.ArgumentParser(description='%prog [options] INPUT')
    args, paths = parser.parse_known_args(args)

    outname = "signalUncertainty_symmetric"

    ROOT.SetAtlasStyle()
    
    f = ROOT.TFile("../Input/model/dijetTLA/zprime/HLT_j0_perf_ds1_L1J100/SignalTemplates_th1s_gq0p1.root")

    hists = [
       ["mjj_mR200_gSM0p1"],
       ["mjj_mR350_gSM0p1"],
       ["mjj_mR600_gSM0p1"],
       ["mjj_mR1000_gSM0p1"],
       ["mjj_mR2000_gSM0p1"],
    ]

    variations = [
       ["nominal"],
       ["JET_Pileup_OffsetMu__1down"],
       ["JET_Pileup_RhoTopology__1down"],
       ["JET_Pileup_OffsetNPV__1down"],
       ["JET_Pileup_PtTerm__1down"],
       ["JET_JER_EffectiveNP_1__1down"],
       ["JET_JER_EffectiveNP_2__1down"],
       ["JET_JER_EffectiveNP_3__1down"],
       ["JET_JER_EffectiveNP_4__1down"],
       ["JET_JER_EffectiveNP_5__1down"],
       ["JET_JER_EffectiveNP_6__1down"],
       ["JET_JER_EffectiveNP_7__1down"],
       ["JET_JER_EffectiveNP_8__1down"],
       ["JET_JER_EffectiveNP_9__1down"],
       ["JET_JER_EffectiveNP_10__1down"],
       ["JET_JER_EffectiveNP_11__1down"],
       ["JET_JER_EffectiveNP_12restTerm__1down"],
       ["JET_JER_DataVsMC_MC16__1down"],
       ["JET_EffectiveNP_1__1down"],
       ["JET_EffectiveNP_2__1down"],
       ["JET_EffectiveNP_3__1down"],
       ["JET_EffectiveNP_4__1down"],
       ["JET_EffectiveNP_5__1down"],
       ["JET_EffectiveNP_6__1down"],
       ["JET_EffectiveNP_7__1down"],
       ["JET_EffectiveNP_8restTerm__1down"],
       ["JET_EtaIntercalibration_TotalStat__1down"],
       ["JET_EtaIntercalibration_NonClosure_negEta__1down"],
       ["JET_EtaIntercalibration_NonClosure_posEta__1down"],
       ["JET_EtaIntercalibration_Modelling__1down"],
       ["JET_EtaIntercalibration_NonClosure_2018data__1down"],
       ["JET_EtaIntercalibration_NonClosure_highE__1down"],
       ["JET_Flavor_Response__1down"],
       ["JET_Flavor_Composition__1down"],
       ["JET_SingleParticle_HighPt__1down"],
    ]

    if doSymmetric:
       f1 = ROOT.TF1("dscb", doubleSidedCrystalBall, 0, 3000, 7)
    else:
       f1 = ROOT.TF1("adscb", asymmDoubleSidedCrystalBall, 0, 3000, 8)
    f1.SetNpx(1000)

    c = ROOT.TCanvas("c", "c", 800, 600)
    # c.SetLogy()
    c.Print(outname + ".pdf[")

    parss = []
    out_dict = OrderedDict()

    for i,hist in enumerate(hists):
        out_dict1 = OrderedDict()
        diff_mean = []
        diff_width = []
        for j,variation in enumerate(variations):
            hname = hist[0] + '_' + variation[0]
         
            h = f.Get(hname)
            h.SetDirectory(0)
            h.SetTitle(hname)
            
            for k in range(len(limits)):
               f1.ReleaseParameter(k)
               f1.SetParLimits(k, limits[k][0], limits[k][1] )
               f1.SetParameter(k, initvals[i][k])
               
            f1.SetLineColor(ROOT.kRed)

            h.Draw("hist")
            h.GetXaxis().SetRangeUser(ranges[i][0], ranges[i][1])
            ROOT.gPad.Update()

            fitresult = h.Fit(f1, "SQM")
            pars = list(fitresult.Parameters())
            pars.append(fitresult.Chi2())
            # pars.append(fitresult.Ndf())
            pars.append(ranges[i][1] - ranges[i][0] - len(limits))
            f1.Draw("same")

            parss.append(pars)
            out_dict1[variation[0]] = pars

            x_mean = pars[4]
            if doSymmetric:
               x_alpha_low  = pars[4] - pars[0] * pars[5]
               x_alpha_high = pars[4] + pars[1] * pars[5]
            else:
               x_alpha_low  = pars[4] - pars[0] * pars[5]
               x_alpha_high = pars[4] + pars[1] * pars[6]

            l1 = ROOT.TLine(x_mean, 0, x_mean, ROOT.gPad.GetUymax())
            l1.SetLineColor(ROOT.kGray+1)
            l1.SetLineStyle(1)
            l2 = ROOT.TLine(x_alpha_low, 0, x_alpha_low, ROOT.gPad.GetUymax())
            l2.SetLineColor(ROOT.kGray+1)
            l2.SetLineStyle(2)
            l3 = ROOT.TLine(x_alpha_high, 0, x_alpha_high, ROOT.gPad.GetUymax())
            l3.SetLineColor(ROOT.kGray+1)
            l3.SetLineStyle(2)
            
            l1.Draw()
            l2.Draw()
            l3.Draw()

            text_x1 = 0.2
            text_y1 = 0.9
            if i == 0 or i == 1:
               text_x1 = 0.5
               text_y1 = 0.9
               
            ROOT.ATLASLabel(text_x1, text_y1, "Work in progress", 13)
            ROOT.myText(text_x1, text_y1-0.05, 1, hist[0], 13)
            ROOT.myText(text_x1, text_y1-0.10, 1, variation[0].replace("__1down", " #downarrow").replace("__1up", " #uparrow"), 13)
            if doSymmetric:
               ROOT.myText(text_x1, text_y1-0.15, 1, "#mu = %.0f GeV, #sigma = %.1f" % (pars[4], pars[5]), 13)
               ROOT.myText(text_x1, text_y1-0.20, 1, "#alpha_{l} = %.1f, #alpha_{r} = %.1f" % (pars[0], pars[1]), 13)
               ROOT.myText(text_x1, text_y1-0.25, 1, "#chi^{2}/n = %.1f/%d" % (pars[-2], pars[-1]), 13)
            else:
               ROOT.myText(text_x1, text_y1-0.15, 1, "#mu = %.0f GeV" % pars[4], 13)
               ROOT.myText(text_x1, text_y1-0.20, 1, "#sigma_{l} = %.1f GeV, #sigma_{r} = %.1f GeV" % (pars[5], pars[6]), 13)
               ROOT.myText(text_x1, text_y1-0.25, 1, "#alpha_{l} = %.1f, #alpha_{r} = %.1f" % (pars[0], pars[1]), 13)
               ROOT.myText(text_x1, text_y1-0.30, 1, "#chi^{2}/n = %.1f/%d" % (pars[-1], pars[-2]), 13)

            ROOT.gPad.Update()
            c.Print(outname+".pdf")
            # raw_input("wait")

        out_dict[hist[0]] = out_dict1
     
    c.Print(outname+".pdf]")
   
    with open(outname+".json", 'w') as f:
       json.dump(out_dict, f)

if __name__ == "__main__":  
   # don't pass -b flag for root but keep -- flags for argparse
   args=[x for x in sys.argv[1:] if not (x.startswith("-") and not x.startswith("--"))]
   sys.exit(main(args))
