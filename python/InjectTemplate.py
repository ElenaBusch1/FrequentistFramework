#!/usr/bin/env python
import ROOT as r
import sys, re, os, math, argparse
from math import sqrt


def findWindow(histo, windowFrac=0.762, minMass = 200, maxMass = 1000):

  minWidth = 1e5
  if not isinstance(histo, r.TH1):
    return 0, 0
  if histo.Integral()==0:
    return 0, 0

  #integral = histo.Integral(0, histo.GetNbinsX()+1)
  integral = histo.Integral(histo.FindBin(minMass), histo.FindBin(maxMass))
  Nbins = histo.GetNbinsX()
  bestTopEdge = 0

  tempFrac = 0.0
  #for imax in range(0, Nbins+1):
  for imax in range(histo.FindBin(minMass), histo.FindBin(maxMass)):
     tempFrac += histo.GetBinContent(imax)

  # The i in this loop will be the starting bin for a scan over histo
  for i in range(histo.FindBin(minMass), histo.FindBin(maxMass)):
  #for i in range(Nbins):
       tempFrac = 0.0
       imax = i

       # Scan over histo, starting at bin i until it contains a fraction of events > frac or it reaches the end of the histogram
       while tempFrac<float(windowFrac) and imax != Nbins:
          tempFrac += histo.GetBinContent(imax)/integral
          imax += 1

       # Width of the window found by the scan above
       width = histo.GetBinCenter(imax) - histo.GetBinCenter(i)
       # Bin center where the scan ended
       top_edge = histo.GetBinCenter(imax)

       # We want to find the smallest window containing fraction of signal ~= frac
       # So we check that our new width is smaller than the previous one (minwidth) and the scan didn't reach the end of the histo
       if imax != Nbins and width<minWidth:
          minWidth = width
          bestTopEdge = top_edge

  if minWidth > (histo.GetBinCenter(Nbins)-histo.GetBinCenter(1)):
    minWidth = (histo.GetBinCenter(Nbins)-histo.GetBinCenter(1))
    bestTopEdge = histo.GetBinCenter(Nbins)
  valLow = bestTopEdge-minWidth

  print integral, valLow, bestTopEdge, histo.FindBin(minMass), histo.FindBin(maxMass), minMass, maxMass

  return valLow,bestTopEdge



def InjectTemplate(infile= "", histname= "", sigmean= "", sigwidth= "", sigamp= "", outfile= "", wsfile = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/Input/signal/HistFactory_dijetISR_mR550.root", wspdf = "SigLow_1_alpha200_SR1", firsttoy=None, lasttoy=None, minMass = 200, maxMass = 1000):

    inws = r.TFile.Open(wsfile)
    ws = inws.Get("combined")
    signalPDF = ws.pdf(wspdf + "_model")
    print wspdf

    mjjVar = ws.var('obs_x_' + wspdf)
    ws.Print()
    #print wsfile, wspdf + "_model"
    print wsfile, wspdf + "_model"
    #print signalPDF
    sigHistNom = signalPDF.createHistogram("test", mjjVar);

    f_in = r.TFile(infile, "READ")
    f_out = r.TFile(outfile, "RECREATE")
    f_out.cd()
    print "Writing to ", outfile

    gRand = r.TRandom3()
    seed = 0
    nBkgs = []

    for index, histKey in enumerate(f_in.GetListOfKeys()):
        print histKey.GetName(), histname
        #if (lasttoy or lasttoy==0) and index > lasttoy:
        #  continue
        histNameFile = histKey.GetName()
        
        if not histname in histNameFile:
        #if not histname == histNameFile:
            continue

        hist = f_in.Get(histNameFile).Clone()
        hinj = hist.Clone()
        hgaus = hist.Clone("injectedSignal") 
        hgaus.Reset("M")

        #sigHist2.GetXaxis().Set(hist.GetNbinsX(), hist.GetBinLowEdge(1), hist.GetBinLowEdge(hist.GetNbinsX()+1))
        #sigHist2.GetXaxis().SetLimits(hist.GetBinLowEdge(1), hist.GetBinLowEdge(hist.GetNbinsX()+1))
        #sigHist2.GetXaxis().SetMinimum(hist.GetBinLowEdge(1))
        #sigHist2.GetXaxis().SetMaximum(hist.GetBinLowEdge(hist.GetNbinsX()+1))
        # define the parameters of the gaussian and fill it
        if sigmean > 0.0:
            # determine the gaussian amplitude (ntimes * sqrt(n) in FWHW range)
            rangeLow, rangeHigh = findWindow(sigHistNom, minMass = minMass, maxMass = maxMass)
            binLow = hist.FindBin(rangeLow)
            binHigh = hist.FindBin(rangeHigh)
            nBkg = hist.Integral(binLow, binHigh)
            nBkgs.append(nBkg)

            # TODO: Ideally the window size should be chosen from the template, not just arbitrary
            binLowSig = sigHistNom.FindBin(rangeLow)
            binHighSig = sigHistNom.FindBin(rangeHigh)
            fSig = sigHistNom.Integral(binLowSig, binHighSig) / sigHistNom.Integral(1,sigHistNom.GetNbinsX())#integral from -1.18 sigma to +1.18 sigma
            nSigNew = int(math.sqrt(nBkg)*sigamp / fSig)

            mctoy = signalPDF.generateBinned(r.RooArgSet(mjjVar), nSigNew)
            sigHist2 = mctoy.createHistogram("test_%s"%(histKey), mjjVar);
            hgaus = mctoy.fillHistogram(hgaus, r.RooArgList(mjjVar))

            print(nSigNew, sigHistNom.Integral(), sigHistNom.Integral(binLowSig, binHighSig), sigHistNom.Integral(sigHistNom.FindBin(minMass), sigHistNom.FindBin(maxMass)))
            print(nBkg, sqrt(nBkg), binLow, binHigh, rangeLow, rangeHigh, nSigNew, hgaus.Integral(hgaus.FindBin(minMass), hgaus.FindBin(maxMass)))


            hinj.Add(hgaus)
            nBkgs.append(nBkg)

        print "Wrote files"
        print "test", histNameFile
        hinj.Write(histNameFile )
        hist.Write(histNameFile+"_beforeInjection")
        #sigHist2.Write(histNameFile+"_injection")
        hgaus.Write(histNameFile+"_injection")

        seed += 1
            
    f_out.Close()
    return nBkgs


def main(args):

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--infile', dest='infile', type=str, default='../Input/data/dijetTLAnlo/data_J75yStar03_range400_2079.root', help='original data file name')
    parser.add_argument('--histname', dest='histname', type=str, default='data', help='original data hist name')
    parser.add_argument('--sigmean', dest='sigmean', type=float, default=600, help='mean of injected Gaussian')
    parser.add_argument('--sigwidth', dest='sigwidth', type=float, default=5, help='width of injected Gaussian (in %)')
    parser.add_argument('--sigamp', dest='sigamp', type=float, default=5, help='number of injected events (in sigmas of central bin)')
    parser.add_argument('--outfile', dest='outfile', type=str, default='', help='Output file name')
    parser.add_argument('--firsttoy', dest='firsttoy', type=str, help='Only consider toys larger than this number')
    parser.add_argument('--lasttoy', dest='lasttoy', type=str, help='Only consider toys lower than this number')

    args = parser.parse_args(args)

    if args.outfile == "":
        args.outfile = os.path.split(args.infile)[-1].replace(".root", "_mean%.0f_width%.0f_amp%.0f.root" % (args.sigmean, args.sigwidth, args.sigamp))

    InjectGaussian(infile=args.infile,
                   histname=args.histname,
                   sigmean=args.sigmean,
                   sigwidth=args.sigwidth,
                   sigamp=args.sigamp,
                   outfile=args.outfile,
                   firsttoy=args.firsttoy,
                   lasttoy=args.lasttoy)

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
