#!/usr/bin/env python
#import ROOT
import sys, re, os, math, argparse
from array import array
from ROOT import *
from math import sqrt
from glob import glob
import numpy as np


def main(args):
  parser = argparse.ArgumentParser(description='%prog [options]')
  parser.add_argument('--filedir', dest='filedir', type=str, default='/eos/user/d/dmelini/ISRZprime/dijetgamma/FrequentistFramework/condor_outputs/', help='Directory where input file(s) is (are)')
  parser.add_argument('--filepath', dest='filepath', type=str, default='FitResult_ajj_simpleTrig_yStar0p825_1GeVBin_WindowFit${WINDOWFITSTR}_SigM${MEAN}W${WIDTH}_${PSEUDO}.root', help='Input file name')
  parser.add_argument('--maindir', dest='maindir', type=str, default='/afs/cern.ch/work/d/dmelini/ISR_Dijet/Fitting_ZprimeISR/FrequentistFramework', help='Input file name')
  parser.add_argument('--outdir', dest='outdir', type=str, default='/afs/cern.ch/work/d/dmelini/ISR_Dijet/Fitting_ZprimeISR/FrequentistFramework/run/runAll/plots', help='Output directory')
  parser.add_argument('--uncpseudo', dest='douncpseudo', type=bool, default=False, help="Get uncertainty from pseudodata rather than from RooFit single-fit")
  parser.add_argument('--fitwindowchoice', dest='fitwindowchoice', type=str, nargs="*", default=["2"], help='Fit Width choice')
  parser.add_argument('--lumi', dest='lumi', type=float, default=140, help='Luminosity')
  parser.add_argument('--sigmeans',dest='sigmeans', type=int, nargs='*', default=[250])
  parser.add_argument('--sigwidths',dest='sigwidths', type=int, nargs='*', default=[5])  
  parser.add_argument('--ntoys',dest='ntoys', type=int, default=100, help="Number of toys from which computing the unc")

  args = parser.parse_args(args)
  if args.outdir:
    gROOT.SetBatch(True)

  sigmeans=args.sigmeans
  sigwidths=args.sigwidths
  maindir=args.maindir
  path=args.filepath
  douncpseudo=args.douncpseudo
  lumi=args.lumi if args.lumi > 1000 else 1000*args.lumi #check lumi is given in correct units


  SetAtlasStyle()
    
  style = [1,2,3,4,5,6,7,8,9,10]
  colors  = [2,3,4,5,6,7,8,9,1]

  g_obs = []
  NPnames=[]
  g_ref=[]
  hist_name="nsig_pseudo_M${MEAN}W${WIDTH}"

  failedfit_counter=0
  fit_counter=0
  #for saving histograms where the mean of nsig is extracted from toys
  for i,sigwidth in enumerate(sigwidths):

    g_obs.append( TGraphErrors() )
    g_ref.append( TGraphErrors() )
    for j,sigmean in enumerate(sigmeans):
    
      tmp_path = path
      if len(args.fitwindowchoice)==1:
        tmp_path = tmp_path.replace("${WINDOWFITSTR}", "M${MEAN}W${WIDTHGEV}" if int(args.fitwindowchoice[0])<int(sigmean) else str("0to"+str(int(args.fitwindowchoice[0]))) )
        tmp_path = tmp_path.replace("${WIDTHGEV}", str(int(int(args.fitwindowchoice[0])*sigwidth*sigmean/100.)))
      else:
        limits=(args.fitwindowchoice[j]).split()
        if len(limits)!=2:
          print("Incorrect input of fitwindowchoice. If providing multiple arguments, give something like:")
          print("'window1Low window1High' 'window2Low window2High' 'window3Low window3High' ... ")
          return
        tmp_path = tmp_path.replace("${WINDOWFITSTR}", "{}to{}".format(limits[0],limits[1]) )
  
      tmp_path = tmp_path.replace("${MEAN}", str(sigmean))
      tmp_path = tmp_path.replace("${WIDTH}", str(sigwidth))
      
      
      #save each toy to check ditribution
      hist_name_tmp= hist_name 
      hist_name_tmp = hist_name_tmp.replace("${MEAN}", str(sigmean))
      hist_name_tmp = hist_name_tmp.replace("${WIDTH}", str(sigwidth))
      print("Running on: ", tmp_path)
      all_pars=[]

      for count in range(0,args.ntoys if douncpseudo else 1):
        tmp_pseudo_path = tmp_path
        tmp_pseudo_path = tmp_pseudo_path.replace("${PSEUDO}", str(count if douncpseudo else args.ntoys))
        tmp_pseudo_path2 = tmp_pseudo_path.replace("FitResult", "PostFit")
        try:
          f = TFile(args.filedir+tmp_pseudo_path, "READ")
          f2 = TFile(args.filedir+tmp_pseudo_path2, "READ")
        except:
          print("Can't open \n", args.filedir+tmp_pseudo_path, " or \n", args.filedir+tmp_pseudo_path2)
          continue
        #print("doing toy", count)
        try:
          #if True:
          fitRes=f.Get("fitResult")
          chi2_plots =f2.Get("chi2")
          if not fitRes: 
            failedfit_counter+=1
            continue
          if not chi2_plots: 
            failedfit_counter+=1
            continue

          if fitRes.status()>1 or chi2_plots.GetBinContent(5)<0.05: #chi2 p-val <5%
            print("fit did not converge (status "+str(fitRes.status()),", chi2 p-val", chi2_plots.GetBinContent(5)," ). Skipping")
            failedfit_counter+=1
            continue
          else:
            fake_convergence=False
            for idx in range(0,len(fitRes.floatParsFinal())): #extra conditions for which fit should be considered as failed                                                                
              if "nsig" in fitRes.floatParsFinal()[idx].GetName() and fitRes.floatParsFinal()[idx].getValV()<-9000.: #too low value. Sometime fit doesn't get out of that                   
                fake_convergence=True
                print("fit did not converge (nsig= ",fitRes.floatParsFinal()[idx].getValV(), "). Skipping")
              if "nsig" in fitRes.floatParsFinal()[idx].GetName() and fitRes.floatParsFinal()[idx].getError()>10000.: #too high unc. Sometime fit doesn't get POI right and has unreasaonable fit unc                                                                                                                                                                                   
                fake_convergence=True
                print("fit did not converge (nsigErr= ",fitRes.floatParsFinal()[idx].getError(), "). Skipping")
              if "p2" == fitRes.floatParsFinal()[idx].GetName() and fitRes.floatParsFinal()[idx].getValV()<16.: #too low value. Sometime fit doesn't get out of that                                                                                                                                          
                fake_convergence=True
                print("fit did not converge (p2= ",fitRes.floatParsFinal()[idx].getValV(), "). Skipping")
            if fake_convergence:
              failedfit_counter+=1
              continue
          fit_counter+=1
        except:
          print("Can't get fitResult from ", tmp_pseudo_path)
          print("Can't get chi2 from ", tmp_pseudo_path2)
          f.Close()
          f2.Close()
          continue
          
        pars=[]
        for idx in range(0,len(fitRes.floatParsFinal())):
          if "alpha" in fitRes.floatParsFinal()[idx].GetName():
            pars.append([fitRes.floatParsFinal()[idx].GetName(), fitRes.floatParsFinal()[idx].getValV()])
        all_pars.append(pars)
        f.Close()

      restmp=[]
      if len(all_pars)==0:
        continue
      if len(all_pars[0])==0:
        continue
        
      for h, _ in enumerate(all_pars[0]):
        vec=[]
        for k, _ in enumerate(all_pars):
          vec.append(all_pars[k][h][1])
        vecmean=np.mean(np.array(vec))
        vecerr=np.std(np.array(vec))
        restmp.append([all_pars[0][h][0], vecmean, vecerr])

      for k, nuis in enumerate(restmp) :
        g_obs[i].SetPoint(g_obs[i].GetN(), float(nuis[1]) +3*int(j)+1, int(k))
        g_obs[i].SetPointError(g_obs[i].GetN()-1, float(nuis[2]), 0)
        if len(NPnames)<len(restmp):
          NPnames.append(nuis[0])
        g_ref[i].SetPoint(g_ref[i].GetN(), 3*int(j)+1, len(restmp)/2.)
        g_ref[i].SetPointError(g_ref[i].GetN()-1, 1., len(restmp)/2.)
      
      g_obs[-1].SetLineColor(colors[i])
      g_obs[-1].SetMarkerColor(colors[i])
      
  #print("Performed "+str(fit_counter+failedfit_counter)+", of which "+str(round(float(fit_counter)/float(fit_counter+failedfit_counter)*100,3))+"% converged")

  c1 = TCanvas("c1", "c1", 800, 600)
  
  leg_obs = TLegend(0.65,0.70,0.85,0.85)
  g_obs[0].Draw("ap0")
  
  x=g_obs[0].GetXaxis();
  x.Set(len(sigmeans), x.GetXmin(), x.GetXmax())
  for i in range(0, x.GetNbins()):
      x.SetBinLabel(i+1, str(sigmeans[i]));
    
  a=g_obs[0].GetYaxis();
  a.Set(int(a.GetXmax()- a.GetXmin()), a.GetXmin(), a.GetXmax())
  for i in range(0,a.GetNbins()):
    if i < len(NPnames) :
      print(i, NPnames[i])
      a.SetBinLabel(i+1, NPnames[i]);
    else:
      a.SetBinLabel(i+1 , "");
  a.SetLabelSize(a.GetLabelSize()*0.4)

  g_obs[0].Draw("ap0")
  g_ref[0].Draw("02same")
  g_ref[0].SetFillStyle(3010)
  g_ref[0].SetFillColor(kCyan)
  g_ref[0].SetMarkerSize(0)

  g_obs[0].Draw("p0same")
  g_obs[0].GetXaxis().SetTitle("fit window")
  g_obs[0].GetYaxis().SetTitle("NP")
  g_obs[0].GetXaxis().SetRangeUser(0, 3*len(sigmeans))
  g_obs[0].GetYaxis().SetRangeUser(0, a.GetXmax()*1.2)
  gPad.SetLeftMargin(3.)
  c1.Modified()

  for i,g in enumerate(g_obs):
    g.Draw("p0")
    #leg_obs.AddEntry(g, "#sigma_{Z'}/M_{Z'} = %.2f" % (sigwidths[i]/100.), "l")
        
  ATLASLabel(0.20, 0.90, "Internal", 13)
  myText(0.20, 0.85, 1, "#sqrt{s}=13 TeV, "+str(lumi/1000)+" fb^{-1}", 13)
  
  #line f(x)=0                                                                                                                                                   
  func=TF1("line","x*0 +0", 0, 1000)
  func.SetLineStyle(7)
  func.SetLineColor(kGray)
  func.Draw("lsame")

  leg_obs.Draw("same")

  if args.outdir:
    c1.Print(args.outdir+"NpPlot_lumi"+str(int(lumi))+"_fitwindowchoice"+str(int(args.fitwindowchoice[0]) if len(args.fitwindowchoice)==1 else "SWIFT")+("_UncPseudo" if douncpseudo else "")+".pdf")    
  else:
    raw_input("Press enter to continue...")                

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))

