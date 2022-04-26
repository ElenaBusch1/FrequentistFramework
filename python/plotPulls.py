#!/usr/bin/env python

# This script does some checks of the pulls of the fit

import ROOT
import sys, re, os, math, argparse
import python.DrawingFunctions as df
import AtlasStyle as AS
import config as config

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")


def plotPulls(infiles, fitNames, outfile, lumi, minMjj, maxMjj, cdir, channelName, residualhist="residuals", datahist="data", atlasLabel="Simulation Internal", suffix=""):
  for infileName, fitName in zip(infiles, fitNames):
    path = config.getFileName(infileName, cdir, channelName, minMjj, maxMjj) + ".root"

    #inFile = ROOT.TFile(infileName, "READ")
    inFile = ROOT.TFile(path, "READ")
        
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

    labels = []
    try:
        tmpName = config.fitFunctions[fitName]["Name"]
    except:
        tmpName = fitName
    labels.append(tmpName)
    labels.append("KS Test = %.2f"%(ks))

    l=ROOT.TLegend(0.65, 0.75, 0.9, 0.9)
    l.AddEntry(h_pulls, "Pulls", "l")
    l.AddEntry(f1, "Normal gaussian distribution", "l")
    l.Draw()

    l2=ROOT.TLegend(0.65, 0.65, 0.9, 0.75)
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
    #AS.ATLASLabel(0.17, 0.9, 1, 0.15, 0.05, atlasLabel)
    df.draw_atlas_details(labels=labels,x_pos= 0.18,y_pos = 0.9, dy = 0.04, text_size = 0.035, atlasLabel = atlasLabel, lumi=lumi/1000.)


    outpath = config.getFileName(outfile + "_%s"%(fitName), cdir, channelName, minMjj, maxMjj) + ".pdf"
    c.Print(outpath)

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
