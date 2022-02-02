#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from ROOT import *


class FitParameterExtractor:

    def __init__(self, wsfile):
        self.wsfile = wsfile
        self.h1_params = None
        self.h2_cov = None
        self.h2_cor = None
        self.nsig = None
        self.nsigErr = None
        self.suffix = ""

    def ExtractFromFile(self, suffix):
        f_in = ROOT.TFile(self.wsfile, "READ")

        self.h1_params = f_in.Get("postfit_params%s"%(suffix))
        self.h2_cov    = f_in.Get("h2_cov%s"%(suffix))
        self.h2_cor    = f_in.Get("h2_cor%s"%(suffix))

        self.h1_params.SetDirectory(0)
        self.h2_cov.SetDirectory(0)
        self.h2_cor.SetDirectory(0)


        for i in range(self.h1_params.GetNbinsX()):
            name = self.h1_params.GetXaxis().GetBinLabel(i)

            if "nsig" in name:
                self.nsig = self.h1_params.GetBinContent(i)
                self.nsigErr = self.h1_params.GetBinError(i)

        f_in.Close()


    def Extract(self):
        f_in = ROOT.TFile(self.wsfile, "READ")
        r = f_in.Get("fitResult%s"%(self.suffix))

        # r.Print()

        mat_cov = r.covarianceMatrix()
        mat_cor = r.correlationMatrix()
    
        argset = r.floatParsFinal()
    
        self.h1_params = TH1D("postfit_params", "postfit parameters", len(argset), 0, len(argset))
        self.h2_cov    = TH2D("h2_cov", "covariance matrix", len(argset), 0, len(argset), len(argset), 0, len(argset))
        self.h2_cor    = TH2D("h2_cor", "correlation matrix", len(argset), 0, len(argset), len(argset), 0, len(argset))
    
        self.h1_params.SetDirectory(0)
        self.h2_cov.SetDirectory(0)
        self.h2_cor.SetDirectory(0)

        for i,arg in enumerate(argset):
            name = arg.namePtr().GetName() 
    
            self.h1_params.GetXaxis().SetBinLabel(i+1, name)
            self.h1_params.SetBinContent(i+1, arg.getVal())
            self.h1_params.SetBinError(i+1, arg.getError())
    
            if "nsig" in name:
                self.nsig = arg.getVal()
                self.nsigErr = arg.getError()
    
            self.h2_cov.GetXaxis().SetBinLabel(i+1, name)
            self.h2_cov.GetYaxis().SetBinLabel(i+1, name)
            self.h2_cor.GetXaxis().SetBinLabel(i+1, name)
            self.h2_cor.GetYaxis().SetBinLabel(i+1, name)
    
        for i in range(len(argset)):
            for j in range(len(argset)):
                ibin = self.h2_cov.GetBin(i+1, j+1)
                self.h2_cov.SetBinContent(ibin, mat_cov[i][j])
                self.h2_cor.SetBinContent(ibin, mat_cor[i][j])

        f_in.Close()
    
    def GetH1Params(self):
        if not self.h1_params:
            self.Extract()
        return self.h1_params

    def GetH2Cov(self):
        if not self.h2_cov:
            self.Extract()
        return self.h2_cov

    def GetH2Cor(self):
        if not self.h2_cor:
            self.Extract()
        return self.h2_cor

    def GetNsig(self):
        if not self.nsig:
            self.Extract()
        return self.nsig

    def GetNsigErr(self):
        if not self.nsigErr:
            self.Extract()
        return self.nsigErr

    def WriteRoot(self, outfile, doRecreate=True, suffix=""):
        if not self.h1_params:
            self.Extract()

        if doRecreate:
          f_out = ROOT.TFile(outfile, "RECREATE")
        else:
          f_out = ROOT.TFile(outfile, "UPDATE")

        self.h1_params.Write("%s%s"%(self.h1_params.GetName(), suffix))
        self.h2_cov.Write("%s%s"%(self.h2_cov.GetName(), suffix))
        self.h2_cor.Write("%s%s"%(self.h2_cor.GetName(), suffix))

        f_out.Close()

def main(args):
    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--wsfile', dest='wsfile', type=str, default='../run/FitResult.root', help='Input workspace file name')
    parser.add_argument('--outfile', dest='outfile', type=str, default='../run/ParsedFitResult.root', help='Output file name')
    
    args = parser.parse_args(args)
    
    fpe = FitParameterExtractor(args.wsfile)
    fpe.WriteRoot(args.outfile)

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
