#!/usr/bin/env python
from __future__ import print_function
import ROOT
import sys, re, os, math, argparse
import color
import array
import json

ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")

ranges = [
   # (120,270),
   # (150,400),
   (150, 400),
   (230,500),
   (250,800),
   (300,1200),
   (1000,2500),
]

# initvals = [
#    [ 3.0012662, 1.6848446, 0.13985946, 1.4450655, 199.89222, 11.044677, 20.017046, 0.021577093 ],
#    # [ 7.8040569, 1.0000011, 0.10456439, 7.9604039, 352.15092, 63.412137, 15.153004, 0.0091604724 ],
#    [ 0.70569, 2.0000011, 1.456439, 7.9604039, 340, 30.412137, 25.153004, 0.01 ],
#    [ 0.39192768, 2.2778498, 20.000000, 1.00059705610, 583.40658, 42.075909, 32.534893, 0.0060055470 ],
#    [ 0.30000001, 2.5023781, 20.000000, 1.1490554, 977.45359, 51.578644, 44.893954, 0.0039386525 ],
#    # [ 0.30000079, 1.0000059, 0.54681755, 3.3431946e-09, 1725.4544, 6.7598213, 0.045557754, 0.0020283909 ],
#    [ 1.000079, 2.5000059, 5, 1, 1950.4544, 100, 70, 0.0025283909 ],
# ]

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
   # [0, 10],
   [0, 1000],
   [0, 20],
]

def doubleSidedCrystalBall(x, par):
   alpha_l = par[0] 
   alpha_h = par[1] 
   n_l     = par[2] 
   n_h     = par[3] 
   mean	= par[4] 
   sigma	= par[5]
   N	= par[6]
   t = (x[0]-mean)/sigma

   fact1TLessMinosAlphaL = alpha_l/n_l
   fact2TLessMinosAlphaL = (n_l/alpha_l) - alpha_l -t
   fact1THihgerAlphaH = alpha_h/n_h
   fact2THigherAlphaH = (n_h/alpha_h) - alpha_h +t
   
   if (-alpha_l <= t and alpha_h >= t):
       result = math.exp(-0.5*t*t)
   elif (t < -alpha_l):
       result = math.exp(-0.5*alpha_l*alpha_l)*math.pow(fact1TLessMinosAlphaL*fact2TLessMinosAlphaL, -n_l)
   elif (t > alpha_h):
       result = math.exp(-0.5*alpha_h*alpha_h)*math.pow(fact1THihgerAlphaH*fact2THigherAlphaH, -n_h)

   return N*result

def asymmDoubleSidedCrystalBall(x, par):
   alpha_l = par[0] 
   alpha_h = par[1] 
   n_l     = par[2] 
   n_h     = par[3] 
   mean	= par[4] 
   sigma_l	= par[5]
   sigma_h	= par[6]
   N	= par[7]

   if x[0] > mean:
      t = (x[0]-mean)/sigma_h
   else:
      t = (x[0]-mean)/sigma_l

   fact1TLessMinosAlphaL = alpha_l/n_l
   fact2TLessMinosAlphaL = (n_l/alpha_l) - alpha_l -t
   fact1THihgerAlphaH = alpha_h/n_h
   fact2THigherAlphaH = (n_h/alpha_h) - alpha_h +t
   
   if (-alpha_l <= t and alpha_h >= t):
       result = math.exp(-0.5*t*t)
   elif (t < -alpha_l):
       result = math.exp(-0.5*alpha_l*alpha_l)*math.pow(fact1TLessMinosAlphaL*fact2TLessMinosAlphaL, -n_l)
   elif (t > alpha_h):
       result = math.exp(-0.5*alpha_h*alpha_h)*math.pow(fact1THihgerAlphaH*fact2THigherAlphaH, -n_h)

   return N*result


def main(args):
    parser = argparse.ArgumentParser(description='%prog [options] INPUT')
    args, paths = parser.parse_known_args(args)

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

    # f1 = ROOT.TF1("dscb", doubleSidedCrystalBall, 0, 3000, 7)
    f1 = ROOT.TF1("adscb", asymmDoubleSidedCrystalBall, 0, 3000, 8)
    f1.SetNpx(1000)

    c = ROOT.TCanvas("c", "c", 800, 600)
    # c.SetLogy()
    c.Print("signalUncertainty.pdf[")

    parss = []
    out_dict = {}

    for i,hist in enumerate(hists):
        out_dict1 = {}
        for j,variation in enumerate(variations):
            hname = hist[0] + '_' + variation[0]
         
            h = f.Get(hname)
            h.SetDirectory(0)
            h.SetTitle(hname)
            
            mean = h.GetMean()
            rms  = h.GetRMS()

            print(hname, mean, rms)
         
            if j == 0:
               for k in range(8):
                  f1.ReleaseParameter(k)
                  f1.SetParLimits(k, limits[k][0], limits[k][1] )
                  f1.SetParameter(k, initvals[i][k])
            else:
               for k in [0,1,2,3]:
                  # only let width, mean, normalization float for variations
                  f1.FixParameter(k, f1.GetParameter(k))

            f1.SetLineColor(ROOT.kRed)

            h.Draw("hist")
            h.GetXaxis().SetRangeUser(ranges[i][0], ranges[i][1])
            ROOT.gPad.Update()

            fitresult = h.Fit(f1, "SQM")
            pars = list(fitresult.Parameters())
            pars.append(fitresult.Chi2())
            f1.Draw("same")

            parss.append(pars)
            out_dict1[variation[0]] = pars

            x_mean = pars[4]
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
            ROOT.myText(text_x1, text_y1-0.15, 1, "#mu = %.0f GeV" % pars[4], 13)
            ROOT.myText(text_x1, text_y1-0.20, 1, "#sigma_{l} = %.1f GeV, #sigma_{r} = %.1f GeV" % (pars[5], pars[6]), 13)

            ROOT.gPad.Update()
            c.Print("signalUncertainty.pdf")
            # raw_input("wait")

        out_dict[hist[0]] = out_dict1

    for p in parss:
        print(p)
     
    c.Print("signalUncertainty.pdf]")
   
    with open("signaluncertainty.json", 'w') as f:
       json.dump(out_dict, f)

if __name__ == "__main__":  
   # don't pass -b flag for root but keep -- flags for argparse
   args=[x for x in sys.argv[1:] if not (x.startswith("-") and not x.startswith("--"))]
   sys.exit(main(args))
