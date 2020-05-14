import ROOT, sys

# Construct model
w = ROOT.RooWorkspace("w")

#observable mass
w.factory("mass[400,2079]")

# fit parameters
w.factory("p1[0.1, -0.5, 1.5]") 
w.factory("p2[4.5, -10, 10]") 
w.factory("p3[21, -30, 20]") 
w.factory("p4[-28, -40, 10]") 
# background function
w.factory("EXPR::background('@1*TMath::Power(@0/13000.,-1*@2)*TMath::Exp( -1*(@3*@0/13000. + @4*TMath::Power(@0/13000.,2)))',{mass,p1,p2,p3,p4})")

# set up frame object
frame = w.var('mass').frame(ROOT.RooFit.Title("J75 Data")) ;

#import J75 data
datafilename = "../Input/data/dijetTLA/TLA2016_NominalUnblindedData.root"
# DSJ100yStar06_TriggerJets_J100_yStar06_mjj_2016binning_TLArange_data
datahistname = "Nominal/DSJ75yStar03_TriggerJets_J75_yStar03_mjj_2016binning_TLArange_data"
datafile = ROOT.TFile(datafilename,"READ")
datahist = datafile.Get(datahistname)

# put histogram into RooDataHist object
data = ROOT.RooDataHist("data","data",ROOT.RooArgList(w.var('mass')),datahist);
#w.Import(datahist, ROOT.RooFit.Rename("data"))
# workaround to call import function (import is a protected keyword in python)
getattr(w,'import')(data, ROOT.RooFit.Rename("data"))


w.pdf("background").fitTo(data) ;

w.data("data").plotOn(frame) ;
w.pdf("background").plotOn(frame) ;
w.pdf("background").paramOn(frame,ROOT.RooFit.Layout(0.55)) ;


#Construct a histogram with the residuals of the data w.r.t. the curve
hresid = frame.residHist() 

#Construct a histogram with the pulls of the data w.r.t the curve
hpull = frame.pullHist() 

#Create a new frame to draw the residual distribution and add the distribution to the frame
frame2 = w.var('mass').frame(ROOT.RooFit.Title("Residual Distribution")) ;
frame2.addPlotable(hresid,"P") ;

#Create a new frame to draw the pull distribution and add the distribution to the frame
frame3 = w.var('mass').frame(ROOT.RooFit.Title("Pull Distribution")) ;
frame3.addPlotable(hpull,"P") ;

c = ROOT.TCanvas("c1","c1",900,300)
c.Divide(3) 
#c.cd(1)

c.cd(1)
ROOT.gPad.SetLeftMargin(0.15)
frame.GetYaxis().SetTitleOffset(1.6)
frame.Draw()
ROOT.gPad.SetLogy()

c.cd(2)
ROOT.gPad.SetLeftMargin(0.15)
frame2.GetYaxis().SetTitleOffset(1.6)
frame2.Draw()

c.cd(3)
ROOT.gPad.SetLeftMargin(0.15)
frame3.GetYaxis().SetTitleOffset(1.6)
frame3.Draw()

w.Print()

raw_input("Press Enter...")


