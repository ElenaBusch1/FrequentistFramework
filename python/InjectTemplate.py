#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse

def InjectTemplate(infile= "", histname= "", sigmean= "", sigwidth= "", sigamp= "", outfile= "", wsfile = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/ff_latest/config/dijetISR/Input/signal/HistFactory_dijetISR_mR550.root", wspdf = "SigLow_1_alpha200_SR1", firsttoy=None, lasttoy=None):

    #print wsfile, wspdf
    inws = ROOT.TFile.Open(wsfile)
    ws = inws.Get("combined")
    signalPDF = ws.pdf(wspdf + "_model")
    mjjVar = ws.var('obs_x_' + wspdf)
    sigHistNom = signalPDF.createHistogram("test", mjjVar);

    f_in = ROOT.TFile(infile, "READ")
    f_out = ROOT.TFile(outfile, "RECREATE")
    f_out.cd()

    gRand = ROOT.TRandom3()
    seed = 0

    for histKey in f_in.GetListOfKeys():
        histNameFile = histKey.GetName()
        
        if not histname in histNameFile:
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
            rangeLow = sigmean  - 1.18*(sigwidth*0.01) * sigmean
            rangeHigh = sigmean + 1.18*(sigwidth*0.01) * sigmean
            binLow = hist.FindBin(rangeLow)
            binHigh = hist.FindBin(rangeHigh)
            binLowSig = sigHistNom.FindBin(rangeLow)
            binHighSig = sigHistNom.FindBin(rangeHigh)
            nBkg = hist.Integral(binLow, binHigh)

            sigma = (sigwidth*0.01) * sigmean 

            # TODO: Ideally the window size should be chosen from the template, not just arbitrary
            fSig = sigHistNom.Integral(binLowSig, binHighSig) #integral from -1.18 sigma to +1.18 sigma
            nSigNew = int(math.sqrt(nBkg)*sigamp / fSig)

            mctoy = signalPDF.generateBinned(ROOT.RooArgSet(mjjVar), nSigNew)
            sigHist2 = mctoy.createHistogram("test_%s"%(histKey), mjjVar);
            hgaus = mctoy.fillHistogram(hgaus, ROOT.RooArgList(mjjVar))

            #hinj.Add(sigHist2)
            hinj.Add(hgaus)

        hinj.Write(histNameFile )
        hist.Write(histNameFile+"_beforeInjection")
        #sigHist2.Write(histNameFile+"_injection")
        hgaus.Write(histNameFile+"_injection")

        seed += 1
            
    f_out.Close()
    return [nBkg]


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
