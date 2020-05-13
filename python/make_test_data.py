import ROOT

#Declare observable x
x= ROOT.RooRealVar("x","x",0,2000) ;
frame = x.frame(ROOT.RooFit.Title("Gaussian p.d.f.")) ;

#Define a Gaussian p.d.f for the signal
mean = ROOT.RooRealVar("mean","mean",800,0,2000) ;
sigma = ROOT.RooRealVar("sigma","sigma",30,0,60) ;
gx = ROOT.RooGaussian("gauss","gauss",x,mean,sigma) ;

# Construct background pdf
a0 = ROOT.RooRealVar("a0", "a0", -0.1, -1, 1)
a1 = ROOT.RooRealVar("a1", "a1", 0.004, -1, 1)
px = ROOT.RooChebychev("px", "px", x, ROOT.RooArgList(a0, a1))

# Construct composite pdf
f = ROOT.RooRealVar("f", "f", 0.2, 0., 1.)
model = ROOT.RooAddPdf("model", "model", ROOT.RooArgList(gx, px), ROOT.RooArgList(f))

# Generate 1000 events in x from model
data = model.generate(ROOT.RooArgSet(x), 1000)

h = data.createHistogram(x)

data.plotOn(frame) ;
model.plotOn(frame) ;
frame.Draw()

f = ROOT.TFile("testdata.root","RECREATE")
h.Write("testhist")
f.Close()

raw_input("Press Enter...")


