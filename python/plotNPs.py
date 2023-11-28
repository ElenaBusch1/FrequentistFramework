#!/usr/bin/env python

# This script does some checks of the pulls of the fit

import ROOT
import sys, re, os, math, argparse
import LocalFunctions as lf
import DrawingFunctions as df
import python.AtlasStyle as AS
import array
import config as config
import ExtractFitParameters as efp

import numpy as np


def plotFits(infiles, outfile, minMjj, maxMjj, lumi, cdir, channelName, rebinedges=None, 
             atlasLabel="Simulation Internal", residualhistName="residuals", datahistName="data", 
             fithistName="postfit", suffix="", fitNames = None, sigamp=0, sigmean=0, sigwidth=0, toy=None, ntoys = 0):

    ROOT.gROOT.SetBatch(ROOT.kTRUE)
    AS.SetAtlasStyle()
    style = [1,2,3,4,5,6,7,8,9,10]
    colors  = [2,3,4,5,6,7,8,9,1]

    c = df.setup_canvas(outfile)
    c.SetLogy()

    dataHists = []
    fitHists = []
    residualHists = []
    plotHists = []
    legNames = []
    NPnames = []

    if not fitNames:
      fitNames = infiles

    labels = []
    all_pars = []
    g_obs = []
    g_obs.append( ROOT.TGraphErrors() )
    g_ref = []
    g_ref.append( ROOT.TGraphErrors() )


    for index, infileName, fitName in zip(range(len(infiles)), infiles, fitNames):
      for toy in range(ntoys):
        path = config.getFileName(infileName, cdir, channelName, minMjj, maxMjj, sigmean, sigwidth, sigamp) + ".root"
        suffix = "_%d"%(toy)

        postFit = path.replace("FitParameters", "PostFit")
        chi2Hist = lf.read_histogram(postFit, "chi2"+suffix)
        chi2 = chi2Hist.GetBinContent(2)
        pval = chi2Hist.GetBinContent(6)
        if pval < 0.05:
          continue


        fpe = efp.FitParameterExtractor(path)
        fpe.ExtractFromFile( suffix)
        params = fpe.GetH1Params()

        pars=[]
        for idx in range(0,params.GetNbinsX()):
          if "alpha" in params.GetXaxis().GetBinLabel(idx):
            pars.append([ params.GetXaxis().GetBinLabel(idx),  params.GetBinContent(idx),  params.GetBinError(idx)])
            if params.GetBinError(idx) > 2:
               print "bad: ",  params.GetXaxis().GetBinLabel(idx),  params.GetBinError(idx), pval
        all_pars.append(pars)

        restmp=[]
        if len(all_pars)==0:
          continue
        if len(all_pars[0])==0:
          continue

      for h, _ in enumerate(all_pars[0]):
        vec=[]
        vec2=[]
        for k, _ in enumerate(all_pars):
          vec.append(all_pars[k][h][1])
          vec2.append(all_pars[k][h][2])
        #vecmean=all_pars[0][h][1]
        #vecerr=all_pars[0][h][2]
        vecmean=np.mean(np.array(vec))
        #vecerr=np.std(np.array(vec))
        vecerr=np.mean(np.array(vec2))
        restmp.append([all_pars[0][h][0], vecmean, vecerr])

      for k, nuis in enumerate(restmp) :
        g_obs[0].SetPoint(g_obs[0].GetN(), float(nuis[1]), int(k))
        g_obs[0].SetPointError(g_obs[0].GetN()-1, float(nuis[2]), 0)
        if len(NPnames)<len(restmp):
          NPnames.append(nuis[0])
        g_ref[0].SetPoint(g_ref[0].GetN(), 0, len(restmp)/2.)
        g_ref[0].SetPointError(g_ref[0].GetN()-1, 1., len(restmp)/2.)

      g_obs[-1].SetLineColor(colors[0])
      g_obs[-1].SetMarkerColor(colors[0])


    #outname = outfile.replace(".root", "")

    c1 = ROOT.TCanvas("c1", "c1", 800, 600)
    c1.SetLeftMargin(0.2)

    #leg_obs = ROOT.TLegend(0.65,0.70,0.85,0.85)
    g_obs[0].GetXaxis().SetRangeUser(-2, 2)
    #g_obs[0].GetXaxis().SetRange(-2, 2)
    #g_obs[0].GetYaxis().SetRangeUser(0, a.GetXmax()*1.2)
    g_obs[0].Draw("ap0")

    a=g_obs[0].GetYaxis();
    a.Set(int(a.GetXmax()- a.GetXmin()), a.GetXmin(), a.GetXmax())
    for i in range(0,a.GetNbins()):
      if i < len(NPnames) :
        a.SetBinLabel(i+1, NPnames[i]);
      else:
        a.SetBinLabel(i+1 , "");
    a.SetLabelSize(a.GetLabelSize()*0.4)

    g_obs[0].Draw("ap0")
    g_ref[0].Draw("02same")
    g_ref[0].SetFillStyle(3010)
    g_ref[0].SetFillColor(ROOT.kCyan)
    g_ref[0].SetMarkerSize(0)

    g_obs[0].Draw("p0same")
    g_obs[0].GetXaxis().SetTitle("fit window")
    g_obs[0].GetYaxis().SetTitle("NP")

    #ATLASLabel(0.20, 0.90, "Internal", 13)
    #myText(0.20, 0.85, 1, "#sqrt{s}=13 TeV, "+str(lumi/1000)+" fb^{-1}", 13)

    #line f(x)=0                                                                                                                                                   
    func=ROOT.TF1("line","x*0 +0", 0, 1000)
    func.SetLineStyle(7)
    func.SetLineColor(ROOT.kGray)
    func.Draw("lsame")

    #leg_obs.Draw("same")
    c1.Print("test.pdf")




def main(args):
    ROOT.SetAtlasStyle()

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--infiles', dest='infiles', type=str, nargs="*", default=None, help='Input file names')
    parser.add_argument('--inResidualHist', dest='residualhist', type=str, default='residuals', help='Input residual hist name')
    parser.add_argument('--inDataName', dest='datahist', type=str, default='data', help='Data hist name')
    parser.add_argument('--outfile', dest='outfile', type=str, default='fits.root', help='Output file name')
    parser.add_argument('--minMjj', dest='minMjj', type=int, default=300, help='Minimum fit range')
    parser.add_argument('--maxMjj', dest='maxMjj', type=int, default=300, help='Maximum fit range')
    parser.add_argument('--rebinedges', dest='rebinedges', type=int, nargs="*", default=None, help='Name of template hist')
    args = parser.parse_args(args)

    plotFits(infiles=args.infiles, outfile=args.outfile, minMjj=args.minMjj, maxMjj=args.maxMjj, rebinedges=args.rebinedges, residualhistName=args.residualhist, datahistName=args.datahist)




if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
