#!/usr/bin/env python

# This script does some checks of the pulls of the fit

import ROOT
import sys, re, os, math, argparse
import DrawingFunctions as df
import python.AtlasStyle as AS
import array
import config as config
import ExtractFitParameters as efp
from math import sqrt


ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
ROOT.gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")

def plotFits(infileName, infilePDName, outfile, rangelow, rangehigh, sigmean, sigwidth, sigamp, rebinedges=None, atlasLabel="Simulation Internal", residualhistName="residuals", datahistName="data", fithistName="postfit", suffix="_0", infileNameBkgOnly = ""):
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


    fitHist = inFile.Get("%s%s"%(fithistName, suffix))
    residualHist = inFile.Get("%s%s"%(residualhistName, suffix))
    chi2Hist = inFile.Get("chi2%s"%(suffix))
    chi2 = chi2Hist.GetBinContent(2)
    pval = chi2Hist.GetBinContent(6)
    fitHist.SetDirectory(0)
    residualHist.SetDirectory(0)


    inFilePD = ROOT.TFile(infilePDName, "READ")
    if not inFilePD:
      print "Did not find file ", infilePDName
    dataHist = inFilePD.Get("pseudodata%s"%(suffix))

    dataHist.SetDirectory(0)

    dataHist.SetName("%s_%s"%(dataHist.GetName(), infileName))
    fitHist.SetName("%s_%s"%(fitHist.GetName(), infileName))
    residualHist.SetName("%s_%s"%(residualHist.GetName(), infileName))


    dataHist.GetXaxis().SetRangeUser(rangelow, rangehigh)
    fitHist.GetXaxis().SetRangeUser(rangelow, rangehigh)
    residualHist.GetXaxis().SetRangeUser(rangelow, rangehigh)
    residualHist.SetFillColor(ROOT.kRed)

    if sigamp > 0:
      dataHistNoInjection = inFilePD.Get("pseudodata%s_beforeInjection"%(suffix))
      dataHistInjection = inFilePD.Get("pseudodata%s_injection"%(suffix))
      dataHistNoInjection.SetDirectory(0)
      dataHistInjection.SetDirectory(0)
      dataHistNoInjection.SetName("%s_%s"%(dataHistNoInjection.GetName(), infileName))
      dataHistInjection.SetName("%s_%s"%(dataHistInjection.GetName(), infileName))

      dataHistInjection.GetXaxis().SetRangeUser(rangelow, rangehigh)
      dataHistNoInjection.GetXaxis().SetRangeUser(rangelow, rangehigh)

  
    if rebinedges:
      print("Rebinning histogram based on list of bins")
      dataHist = dataHist.Rebin(len(rebinedges)-1, "postfit", array.array('d', rebinedges))
      if sigamp > 0:
        dataHistNoInjection = dataHistNoInjection.Rebin(len(rebinedges)-1, "postfitNoInjection", array.array('d', rebinedges))
        dataHistInjection = dataHistInjection.Rebin(len(rebinedges)-1, "postfitInjection", array.array('d', rebinedges))
      fitHist = fitHist.Rebin(len(rebinedges)-1, "fit", array.array('d', rebinedges))
      residualHist = residualHist.Rebin(len(rebinedges)-1, "residual", array.array('d', rebinedges))

    dataHists.append(dataHist)
    fitHists.append(fitHist)
    for i in range(fitHist.GetNbinsX()):
      residualHist.SetBinContent(i+1, (dataHists[0].GetBinContent(i+1)- fitHist.GetBinContent(i+1)) / sqrt(dataHists[0].GetBinContent(i+1)))

    residualHists.append(residualHist)

    plotHists.append(dataHist)
    plotHists.append(fitHist)
    if sigamp > 0:
      plotHists.append(dataHistNoInjection)
      plotHists.append(dataHistInjection)


    inFileBkgOnly = ROOT.TFile(infileNameBkgOnly, "READ")
    if not inFileBkgOnly:
      print "Did not find file ", infileName


    fitHistBkgOnly = inFileBkgOnly.Get("%s%s"%(fithistName, suffix))
    residualHistBkgOnly = inFileBkgOnly.Get("%s%s"%(residualhistName, suffix))
    chi2HistBkgOnly = inFileBkgOnly.Get("chi2%s"%(suffix))
    chi2BkgOnly = chi2HistBkgOnly.GetBinContent(2)
    pvalBkgOnly = chi2HistBkgOnly.GetBinContent(6)

    fitHistBkgOnly.SetDirectory(0)
    residualHistBkgOnly.SetDirectory(0)
    fitHistBkgOnly.SetName("%sBkgOnly_%s"%(fitHistBkgOnly.GetName(), infileName))
    residualHistBkgOnly.SetName("%sBkgOnly_%s"%(residualHistBkgOnly.GetName(), infileName))
    fitHistBkgOnly = fitHistBkgOnly.Rebin(len(rebinedges)-1, "fit", array.array('d', rebinedges))
    residualHistBkgOnly = residualHistBkgOnly.Rebin(len(rebinedges)-1, "residual", array.array('d', rebinedges))
    for i in range(residualHistBkgOnly.GetNbinsX()):
      residualHistBkgOnly.SetBinContent(i+1, (dataHists[0].GetBinContent(i+1) - fitHistBkgOnly.GetBinContent(i+1) )/ sqrt(dataHists[0].GetBinContent(i+1)))


    residualHists.append(residualHistBkgOnly)

    pathBkgOnly = infileNameBkgOnly.replace("PostFit", "FitParameters")
    fpeBkgOnly = efp.FitParameterExtractor(pathBkgOnly)
    fpeBkgOnly.suffix = suffix
    fpeBkgOnly.ExtractFromFile(suffix)
    paramsBkgOnly = fpeBkgOnly.GetH1Params()
    par2BkgOnly = paramsBkgOnly.GetBinContent(2)
    par3BkgOnly = paramsBkgOnly.GetBinContent(3)
    par4BkgOnly = paramsBkgOnly.GetBinContent(4)
    par5BkgOnly = paramsBkgOnly.GetBinContent(5)
    par2ErrBkgOnly = paramsBkgOnly.GetBinError(2)
    par3ErrBkgOnly = paramsBkgOnly.GetBinError(3)
    par4ErrBkgOnly = paramsBkgOnly.GetBinError(4)
    par5ErrBkgOnly = paramsBkgOnly.GetBinError(5)







    legNames.append("pseudo-data")
    legNames.append("fit")
    legNames.append("pseudo-data, no signal injection")
    legNames.append("signal injection")

    df.SetRange(plotHists, minMin=1e-3, maxMax=1e8, isLog=True)

    label = "#chi^2 / ndof = %.2f, p-value = %.1f %%"%(chi2, pval*100)
    labels.append(label)
    label = "Bkg only: #chi^2 / ndof = %.2f, p-value = %.1f %%"%(chi2BkgOnly, pvalBkgOnly*100)
    labels.append(label)
    labels.append("m_{Z'} = %d, width = %d%%, amplitude = %d"%(sigmean, sigwidth, sigamp) )

    path = infileName.replace("PostFit", "FitParameters")
    fpe = efp.FitParameterExtractor(path)
    fpe.suffix = suffix
    fpe.ExtractFromFile( suffix)
    nsig = fpe.GetNsig()
    params = fpe.GetH1Params()
    par0 = 1
    par1 = 8000
    par2 = params.GetBinContent(3)
    par3 = params.GetBinContent(4)
    par4 = params.GetBinContent(5)
    par5 = params.GetBinContent(6)

    #fitNoSignal = ROOT.TF1("testFit", "[0]*TMath::Power(1-x/[1],[2])/TMath::Power(x/[1], [3] + [4]*TMath::Log(x/[1]) )", 0, 2000)
    fitNoSignal = ROOT.TF1("testFit", "[0]*TMath::Power(1-x/[1],[2])/TMath::Power(x/[1], [3] + [4]*TMath::Log(x/[1]) + [5]*TMath::Power(TMath::Log(x/[1]), 2) )", 0, 2000)

    fitNoSignal.SetParameter(0, par0)
    fitNoSignal.SetParameter(1, par1)
    fitNoSignal.SetParameter(2, par2)
    fitNoSignal.SetParameter(3, par3)
    fitNoSignal.SetParameter(4, par4)
    fitNoSignal.SetParameter(5, par5)
    labels.append("p2 = %.2f, p3=%.2f, p4=%.2f, p5=%.2f"%(par2, par3, par4, par5))
    labels.append("BkgOnly: p2 = %.2f#pm%.2f, p3=%.2f#pm%.2f, p4=%.2f#pm%.2f, p5=%.2f#pm%.2f"%(par2BkgOnly, par2ErrBkgOnly, par3BkgOnly, par3ErrBkgOnly, par4BkgOnly, par4ErrBkgOnly, par5BkgOnly, par5ErrBkgOnly))

    par0 = params.GetBinContent(1) / fitNoSignal.Integral(rangelow, rangehigh)
    fitNoSignal.SetParameter(0, par0)

    fitHist2 = fitHists[0].Clone("fitHistNoSignal")
    residualHist2 = residualHists[0].Clone("residualHistNoSignal")
    fitHist2.SetDirectory(0)
    residualHist2.SetDirectory(0)
    for i in range(fitHist2.GetNbinsX()):
      fitHist2.SetBinContent(i+1, fitNoSignal.Integral(fitHist2.GetBinLowEdge(i+1), fitHist2.GetBinLowEdge(i+2)))
      residualHist2.SetBinContent(i+1, (dataHists[0].GetBinContent(i+1)- fitHist2.GetBinContent(i+1)) / sqrt(dataHists[0].GetBinContent(i+1)))

    fitHists.append(fitHist2)
    residualHists.append(residualHist2)


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
    labels.append("N_{sig, extracted} = %d"%(nsig))
    leg = df.DrawRatioHists(c, plotHists, residualHists, legNames, labels, "", drawOptions = ["HIST"], outName=outname, isLogX = False, ratioDrawOptions = ["HIST"])
    c.Print(outname + ".pdf")

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
