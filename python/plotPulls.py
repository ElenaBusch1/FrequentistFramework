#!/usr/bin/env python

# This script does some checks of the pulls of the fit

import ROOT
import sys, re, os, math, argparse
import python.DrawingFunctions as df
import AtlasStyle as AS

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")


def plotPulls(infiles, outfile, residualhist="residuals", datahist="data", atlasLabel="Simulation Internal", suffix=""):
  for infileName in infiles:
    inFile = ROOT.TFile(infileName, "READ")
        
    residualHist = inFile.Get(residualhist+suffix)
    dataHist = inFile.Get(datahist+suffix)
    fitHist = inFile.Get("postfit"+suffix)

    h_pulls = ROOT.TH1F("h_pulls", ";Pull;", 100, -5, 5)
    for i in range(residualHist.GetNbinsX()):
      h_pulls.Fill( residualHist.GetBinContent(i+1)*1.0 );
    f1 = ROOT.TF1("f1","[area] * ROOT::Math::normal_pdf(x, [sigma], [mean]) ", -5, 5);
    # TODO: need to figure out how to normalize this correctly
    f1.SetParameter("area", h_pulls.Integral("width"))
    f1.SetParameter("mean", 0.);
    f1.SetParameter("sigma",1.);


    c = df.setup_canvas()
    c.SetRightMargin(0.10)
    c.SetLeftMargin(0.10)
    h_pulls.Draw("HIST")
    h_pulls.Fit("gaus");
    f1.SetLineColor(ROOT.kBlue)
    f1.Draw("SAME")
    f2 = h_pulls.GetFunction("gaus")
    f2.SetLineColor(ROOT.kRed)
    f2.SetMarkerSize(0)
    f2.Draw("SAME")
    h_fit = f2.CreateHistogram()
    h_fit.SetMarkerColor(ROOT.kGreen)
    h_fit.Draw("P SAME")

    ks = h_pulls.KolmogorovTest(h_fit)

    ROOT.myText(0.15, 0.80, 1, "5-par fit", 13)
    ROOT.myText(0.15, 0.76, 1, "KS Test = %.2f"%(ks), 13)

    l=ROOT.TLegend(0.8, 0.75, 0.6, 0.85)
    l.AddEntry(h_pulls, "Pulls", "l")
    l.AddEntry(f1, "Normal gaussian distribution", "l")
    l.Draw()

    l2=ROOT.TLegend(0.60, 0.65, 0.80, 0.75)
    l2.AddEntry(f2, "#splitline{Gaussian fit}{mean = %.3f #pm %.3f}"%(f2.GetParameter(1), f2.GetParError(1)), "l")

    isProblematicFit = False
    if f2.GetParameter(1) > 0 and f2.GetParameter(1) - f2.GetParError(1) > 0:
      isProblematicFit = True
    if f2.GetParameter(1) < 0 and f2.GetParameter(1) + f2.GetParError(1) < 0:
      isProblematicFit = True

    # TODO: Need to run other tests too
    # Check if the mean is consistent with 0
    if isProblematicFit:
      l2.SetTextColor(ROOT.kRed)
    l2.Draw()
    AS.ATLASLabel(0.15, 0.9, 1, 0.15, 0.05, atlasLabel)

    c.Print(outfile + ".pdf")

    inFile.Close()


def main(args):
    ROOT.SetAtlasStyle()

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--infiles', dest='infiles', type=str, default='', help='Input file name')
    parser.add_argument('--inResidualHist', dest='residualhist', type=str, default='residuals', help='Input residual hist name')
    parser.add_argument('--inDataName', dest='datahist', type=str, default='data', help='Data hist name')
    parser.add_argument('--outfile', dest='outfile', type=str, default='pulls', help='Output file name')
    parser.add_argument('--atlasLabel', dest='atlasLabel', type=str, default='Simulation Internal', help='Output file name')

    args = parser.parse_args(args)
    plotPulls(infiles=args.infiles, outfile=args.outfile, residualhist=args.residualhist, datahist=args.datahist, atlasLabel=args.atlasLabel)



if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
