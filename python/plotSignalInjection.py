#!/usr/bin/env python

# This script does some checks of the pulls of the fit

import ROOT
import sys, re, os, math, argparse
import DrawingFunctions as df
import python.AtlasStyle as AS
import array
import config as config

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")

def plotFits(infileName, infilePDName, outfile, rangelow, rangehigh, sigmean, sigwidth, sigamp, rebinedges=None, atlasLabel="Simulation Internal", residualhistName="residuals", datahistName="data", fithistName="postfit"):
    AS.SetAtlasStyle()

    c = df.setup_canvas()
    c.SetLogy()

    dataHists = []
    fitHists = []
    residualHists = []
    plotHists = []
    legNames = []

    labels = []

    inFile = ROOT.TFile(infileName, "READ")
    if not inFile:
      print "Did not find file ", infileName


    fitHist = inFile.Get(fithistName)
    residualHist = inFile.Get(residualhistName)
    chi2Hist = inFile.Get("chi2")
    chi2 = chi2Hist.GetBinContent(2)
    pval = chi2Hist.GetBinContent(6)
    fitHist.SetDirectory(0)
    residualHist.SetDirectory(0)


    inFilePD = ROOT.TFile(infilePDName, "READ")
    if not inFilePD:
      print "Did not find file ", infilePDName
    dataHist = inFilePD.Get("pseudodata_0")
    dataHistNoInjection = inFilePD.Get("pseudodata_0_beforeInjection")
    dataHistInjection = inFilePD.Get("pseudodata_0_injection")

    dataHist.SetDirectory(0)
    dataHistNoInjection.SetDirectory(0)
    dataHistInjection.SetDirectory(0)

    dataHist.SetName("%s_%s"%(dataHist.GetName(), infileName))
    dataHistNoInjection.SetName("%s_%s"%(dataHistNoInjection.GetName(), infileName))
    dataHistInjection.SetName("%s_%s"%(dataHistInjection.GetName(), infileName))
    fitHist.SetName("%s_%s"%(fitHist.GetName(), infileName))
    residualHist.SetName("%s_%s"%(residualHist.GetName(), infileName))


    dataHist.GetXaxis().SetRangeUser(rangelow, rangehigh)
    dataHistInjection.GetXaxis().SetRangeUser(rangelow, rangehigh)
    dataHistNoInjection.GetXaxis().SetRangeUser(rangelow, rangehigh)
    fitHist.GetXaxis().SetRangeUser(rangelow, rangehigh)
    residualHist.GetXaxis().SetRangeUser(rangelow, rangehigh)
    residualHist.SetFillColor(ROOT.kRed)

  
    if rebinedges:
      print("Rebinning histogram based on list of bins")
      dataHist = dataHist.Rebin(len(rebinedges)-1, "postfit", array.array('d', rebinedges))
      dataHistNoInjection = dataHistNoInjection.Rebin(len(rebinedges)-1, "postfitNoInjection", array.array('d', rebinedges))
      dataHistInjection = dataHistInjection.Rebin(len(rebinedges)-1, "postfitInjection", array.array('d', rebinedges))
      fitHist = fitHist.Rebin(len(rebinedges)-1, "fit", array.array('d', rebinedges))
      residualHist = residualHist.Rebin(len(rebinedges)-1, "residual", array.array('d', rebinedges))

    dataHists.append(dataHist)
    fitHists.append(fitHist)
    residualHists.append(residualHist)

    plotHists.append(dataHist)
    plotHists.append(fitHist)
    plotHists.append(dataHistNoInjection)
    plotHists.append(dataHistInjection)


    legNames.append("pseudo-data")
    legNames.append("fit")
    legNames.append("pseudo-data, no signal injection")
    legNames.append("signal injection")

    df.SetRange(plotHists, minMin=1e-3, maxMax=1e8, isLog=True)

    label = "#chi^2 / ndof = %.2f, p-value = %.1f %%"%(chi2, pval)
    labels.append(label)
    labels.append("m_{Z'} = %d, width = %d%%, amplitude = %d"%(sigmean, sigwidth, sigamp) )

    '''
    const Int_t n = 20;
    Double_t x[n], y[n],ymin[n], ymax[n];
    Int_t i;
    for (i=0;i<n;i++) {
    x[i] = 0.1+i0.1;
    ymax[i] = 10sin(x[i]+0.2);
    ymin[i] = 8sin(x[i]+0.1);
    y[i] = 9sin(x[i]+0.15);
    }
    TGraph *grmin = new TGraph(n,x,ymin);
    TGraph *grmax = new TGraph(n,x,ymax);
    TGraph *gr = new TGraph(n,x,y);
    TGraph grshade = new TGraph(2n);
    for (i=0;i<n;i++) {
    grshade->SetPoint(i,x[i],ymax[i]);
    grshade->SetPoint(n+i,x[n-i-1],ymin[n-i-1]);
    }
    grshade->SetFillStyle(3013);
    grshade->SetFillColor(16);
    grshade->Draw("f");
    grmin->Draw("l");
    grmax->Draw("l");
    gr->SetLineWidth(4);
    gr->SetMarkerColor(4);
    gr->SetMarkerStyle(21);
    gr->Draw("CP");
    }

    '''

    outname = outfile.replace(".root", "")
    leg = df.DrawRatioHists(c, plotHists, residualHists, legNames, labels, "", drawOptions = "HIST", outName=outname, isLogX = False)

    inFile.Close()



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
