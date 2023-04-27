#!/usr/bin/env python
import ROOT as r
import sys, re, os, math, argparse


def findWindow(histo, windowFrac=0.72):
  
  minWidth = 1e5
  if not isinstance(histo, r.TH1):
    return 0, 0
  if histo.Integral()==0:
    return 0, 0

  integral = histo.Integral(1, histo.GetNbinsX()+1)
  Nbins = histo.GetNbinsX()
  bestTopEdge = 0

  tempFrac = 0.0
  for imax in range(0, Nbins+1):
     tempFrac += histo.GetBinContent(imax)

  # The i in this loop will be the starting bin for a scan over histo
  for i in range(Nbins):
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
  print(" Mass range: ", valLow, bestTopEdge)

  return valLow,bestTopEdge




def InjectTemplate(infile= "", histname= "", sigmean= "", sigwidth= "", sigamp= "", outfile= "", wsfile = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/Input/signal/HistFactory_dijetISR_mR550.root", wspdf = "SigLow_1_alpha200_SR1", firsttoy=None, lasttoy=None, writeFile = True):

    #print wsfile, wspdf
    inws = r.TFile.Open(wsfile)
    ws = inws.Get("combined")
    signalPDF = ws.pdf(wspdf + "_model")
    mjjVar = ws.var('obs_x_' + wspdf)
    print wsfile, histname, wspdf
    sigHistNom = signalPDF.createHistogram("test", mjjVar);

    f_in = r.TFile(infile, "READ")
    if writeFile:
      f_out = r.TFile(outfile, "RECREATE")
      f_out.cd()

    gRand = r.TRandom3()
    seed = 0

    nbkgs = []
    index = -1
    for histKey in f_in.GetListOfKeys():
        index+=1
        if index > lasttoy:
          break;
        histNameFile = histKey.GetName()
        
        if not histname in histNameFile:
            print "Did not find hist ", histname, "in ", histNameFile
            continue

        hist = f_in.Get(histNameFile).Clone()
        hinj = hist.Clone()
        hgaus = hist.Clone("injectedSignal") 
        hgaus.Reset("M")

        # define the parameters of the gaussian and fill it
        if sigmean > 0.0:

            # determine the gaussian amplitude (ntimes * sqrt(n) in FWHW range)
            rangeLow, rangeHigh = findWindow(sigHistNom)
            binLow = hist.FindBin(rangeLow)
            binHigh = hist.FindBin(rangeHigh)
            binLowSig = sigHistNom.FindBin(rangeLow)
            binHighSig = sigHistNom.FindBin(rangeHigh)
            nBkg = hist.Integral(binLow, binHigh)
            nbkgs.append(nBkg)
            print("number of background", binLow, binHigh, nBkg)

            sigma = (sigwidth*0.01) * sigmean 

            # TODO: Ideally the window size should be chosen from the template, not just arbitrary
            fSig = sigHistNom.Integral(binLowSig, binHighSig) #integral from -1.18 sigma to +1.18 sigma
            nSigNew = int(math.sqrt(nBkg)*sigamp / fSig)

            mctoy = signalPDF.generateBinned(r.RooArgSet(mjjVar), nSigNew)
            sigHist2 = mctoy.createHistogram("test_%s"%(histKey), mjjVar);
            hgaus = mctoy.fillHistogram(hgaus, r.RooArgList(mjjVar))

            hinj.Add(hgaus)

        if writeFile:
          hinj.Write(histNameFile )
          hist.Write(histNameFile+"_beforeInjection")
          hgaus.Write(histNameFile+"_injection")

        seed += 1
            
    if writeFile:
      f_out.Close()
    return nbkgs


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
