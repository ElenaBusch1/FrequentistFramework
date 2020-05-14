import ROOT, sys

def getHistogram(datafilename,datahistname ):
    datafile = ROOT.TFile(datafilename,"READ")
    datahist = datafile.Get(datahistname)
    datahist.SetDirectory(0)

    datafile.Close()
    return datahist

def getJ75Histogram():
    datafilename = "../Input/data/dijetTLA/TLA2016_NominalUnblindedData.root"
    datahistname = "Nominal/DSJ75yStar03_TriggerJets_J75_yStar03_mjj_2016binning_TLArange_data"
    return getHistogram(datafilename, datahistname)

def getJ100Histogram():
    datafilename = "../Input/data/dijetTLA/TLA2016_NominalUnblindedData.root"
    datahistname = "Nominal/DSJ100yStar06_TriggerJets_J100_yStar06_mjj_2016binning_TLArange_data"
    return getHistogram(datafilename, datahistname)

def setBkfFunc_UA2(w):
    # fit parameters
    w.factory("p1[0.1, -0.5, 1.5]") 
    w.factory("p2[4.5, -10, 10]") 
    w.factory("p3[21, -30, 20]") 
    w.factory("p4[-28, -40, 10]") 
    # background function
    w.factory("EXPR::background('@1*TMath::Power(@0/13000.,-1*@2)*TMath::Exp( -1*(@3*@0/13000. + @4*TMath::Power(@0/13000.,2)))',{mass,p1,p2,p3,p4})")

def setBkfFunc_4param(w):
    # fit parameters
    w.factory("p1[0.25, -100, 100]") 
    w.factory("p2[9.15, -200, 200]") 
    w.factory("p3[-22.829, -200, 200]") 
    w.factory("p4[-6.9, -100, 100]") 
    # background function
    w.factory("EXPR::background('@1*TMath::Power(1-@0/13000.,1*@2)*1/TMath::Power( @0/13000., @3 + @4*TMath::Log(@0/13000.))',{mass,p1,p2,p3,p4})")



if __name__ == '__main__':

    # Construct model
    w = ROOT.RooWorkspace("w")

    #### Set input data & fit range ####
    #observable mass with fit range
    #w.factory("mass[400,2079]")
    #datahist = getJ75Histogram()
    #mytitle = "J75 Data"

    #For the 1400 GeV mass point we fit bins 22 through 40 which corresponds to a mass range of 927-1998 GeV.
    #for the 800 GeV Z' mass, we fit from bins 9  to 27 in our spectrum, which corresponds to a mass range of 531 GeV to 1186 GeV.


    w.factory("mass[ 1300,2079]")
    datahist = getJ100Histogram()
    mytitle = "J100 Data, fit range = [ 927,2079]"

    #### Set up bkg function ###########
    #setBkfFunc_UA2(w)
    setBkfFunc_4param(w)

    ####################################

    # put histogram into RooDataHist object
    data = ROOT.RooDataHist("data","data",ROOT.RooArgList(w.var('mass')),datahist);
    # workaround to call import function (import is a protected keyword in python)
    getattr(w,'import')(data, ROOT.RooFit.Rename("data"))

    # set up frame object
    frame = w.var('mass').frame(ROOT.RooFit.Title(mytitle)) ;

    # fitTo
    w.pdf("background").fitTo(data, ROOT.RooFit.Strategy(1),  ROOT.RooFit.SumW2Error(True), ROOT.RooFit.Minimizer("Minuit2","Migrad")) ;


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


