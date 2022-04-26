#!/usr/bin/env python
import ROOT
import sys, re, os, math, optparse
from color import getColorSteps
import DrawingFunctions as df
import LocalFunctions as lf
import python.AtlasStyle as AS
import config as config
import array


def calcFpF(chi2_nom, chi2_alt, npars_nom, npars_alt, nbins):
    F_num = (chi2_nom - chi2_alt) / (npars_alt - npars_nom)
    F_den = chi2_alt / (nbins - npars_alt)
    F = F_num / F_den
    pF = ROOT.Math.fdistribution_cdf_c( F, npars_alt-npars_nom, nbins-npars_alt)

    return (F, pF)


def runFTest(infiles, cdir, outfile, channelName, rangelow, rangehigh, lumi, atlasLabel="Simulation Internal", chi2bin=1, nbinsbin=3, nparsbin=4, ndofbin=5, usendof=0, rebinEdges=None):
    ROOT.gROOT.SetBatch(ROOT.kTRUE)
    l_pf = []
    l_res = []
    l_chi2 = []
    l_npars = []
    l_ndof = []
    nbins = -1
    l_constr=[]
    l_par=[]
    legNames = []

    for infile in infiles:
        tmp_path = config.getFileName(infile, cdir, channelName, rangelow, rangehigh) + ".root"

        h_chi2 = lf.read_histogram(tmp_path,"chi2")
        h_pf   = lf.read_histogram(tmp_path,"postfit")
        h_data   = lf.read_histogram(tmp_path,"data")
        h_res  = lf.read_histogram(tmp_path, "residuals")
        h_data.GetXaxis().SetTitle("m_{jj}")
        h_res.GetXaxis().SetTitle("m_{jj}")
        h_res.GetYaxis().SetTitle("Residual (#sigma)")

        if rebinEdges:
          h_res = h_res.Rebin(len(rebinEdges)-1, "postfit", array.array('d', rebinEdges))
          h_pf = h_pf.Rebin(len(rebinEdges)-1, "postfit", array.array('d', rebinEdges))
          h_data = h_data.Rebin(len(rebinEdges)-1, "postfit", array.array('d', rebinEdges))

          for ibin in range(1, h_data.GetNbinsX()+1):
            valueErrorData = h_data.GetBinError(ibin)
            valueData = h_data.GetBinContent(ibin)
            postFitValue = h_pf.GetBinContent(ibin)

            binSig = 0.
            if valueErrorData > 0. and postFitValue > 0.:
                binSig = (valueData - postFitValue)/valueErrorData

                h_res.SetBinContent(ibin, binSig)
                h_res.SetBinError(ibin, 0)

        chi2  = h_chi2.GetBinContent(chi2bin)
        _nbins = h_chi2.GetBinContent(nbinsbin)
        if nbins > 0 and _nbins != nbins:
            print "ERROR: Change of binning between files: %d, %d . Exiting" % (nbins, _nbins)
            return -1
        else:
            nbins = _nbins

        if not usendof:
            npars = h_chi2.GetBinContent(nparsbin)
        else:
            npars = h_chi2.GetBinContent(nbinsbin) - h_chi2.GetBinContent(ndofbin)

        ndof = h_chi2.GetBinContent(ndofbin)

        l_pf.append(h_pf)
        l_res.append(h_res)
        l_chi2.append(chi2)
        l_npars.append(npars)
        l_ndof.append(ndof)
        legtext = "%s (#chi^{2}/n = %.0f/%.0f)" % (infile, chi2, ndof)
        legNames.append(legtext)

    labels = []
    for i in range(len(l_chi2)-1):

        (F, pF) = calcFpF( chi2_nom=l_chi2[i],
                           chi2_alt=l_chi2[i+1],
                           npars_nom=l_npars[i],
                           npars_alt=l_npars[i+1],
                           nbins=nbins )

        print "\nF-Test between:", infiles[i], infiles[i+1]
        print "chi2 values:", l_chi2[i], l_chi2[i+1]
        print "npars:", l_npars[i], l_npars[i+1]
        print "nbins:", nbins
        print "pF:", pF

        labels.append("p(F_{^{%s #rightarrow %s par}}) = %.2f" % (infiles[i], infiles[i+1], pF))

    c = df.setup_canvas(outfile)
    df.SetRange(l_res, myMin=-5, myMax=5, isLog=False)
    outname = outfile.replace(".root", "")
    leg = df.DrawHists(c, l_res, legNames, labels, "", drawOptions = ["HIST", "HIST"], styleOptions = df.get_fit_style_opt, lumi=lumi, atlasLabel=atlasLabel)

    c.Print("%s/%s/FTest_%s.pdf"%(cdir, channelName, outfile))




def main(args):

    parser = optparse.OptionParser(description='%prog [options] INPUT')
    parser.add_option('--chi2bin', dest='chi2bin', type=int, default=1, help='bin of the chi2 value in the chi2 histogram')
    parser.add_option('--nbinsbin', dest='nbinsbin', type=int, default=3, help='bin of the nbins value in the chi2 histogram')
    parser.add_option('--nparsbin', dest='nparsbin', type=int, default=4, help='bin of the npars value in the chi2 histogram')
    parser.add_option('--ndofbin', dest='ndofbin', type=int, default=5, help='bin of the npars value in the chi2 histogram')
    parser.add_option('--usendof', dest='usendof', action='store_true', help='use npar=nbins-ndof instead of number in chi2 histogram')

    options, args = parser.parse_args(args)
    paths = args

    runFTest(options.chi2bin, options.nbinsbin, options.nparsbin, options.ndofbin, options.usendof)

        
if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))

