import sys, ROOT, math, glob, os, re
from array import array
from color import getColorSteps
import DrawingFunctions as df
import config as config



def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


def plotFalseExclusionCandles(inpath, masses, widths, rangelow, rangehigh, channelName, cdir, lumi, atlasLabel):
  ROOT.gROOT.SetBatch(ROOT.kTRUE)
  ROOT.gROOT.SetStyle("ATLAS")

  infile = ROOT.TFile(config.getFileName(inpath, cdir, channelName, rangelow, rangehigh) +".root")

  graphs_lim = {}
  for k in infile.GetListOfKeys():
    name = k.GetName()
    g = infile.Get(name)
    if name.find("g1_limit")< 0:
       continue
    print name
    if not isinstance(g, ROOT.TGraph):
        continue

    graphs_lim[g.GetTitle()] = g

  ################################################

  x_min = 0
  x_max = 0

  graphs_frac_above = {}
  graphs_frac_below = {}
  h2_all_points = {}
  bin_edges = []

  masses = natural_sort(graphs_lim.keys())
  existMasses = []

  for mass, index in zip(masses, range(len(masses))):
    graph = graphs_lim[mass]
    # Number of toys where # of extracted signal is above # of injected signal
    above = {}
    # Number of toys
    total = {}
    
    ninj_list = []
    graphs_frac_below[mass] = ROOT.TGraphErrors();

    for n in range(graph.GetN()):
        ninj = graph.GetX()[n]
        ulim = graph.GetY()[n]
        if math.isnan(ulim):
            ulim = 0.

        if ninj not in ninj_list: ninj_list.append(ninj)
        if ninj not in above: above[ninj] = 0
        if ninj not in total: total[ninj] = 0
        total[ninj] += 1
        if ulim > ninj:
            above[ninj] += 1

    ninj_list.sort()
    for n in ninj_list:
        below = total[n] - above[n]
        valueBelow = below*1./total[n]
        errorBelow = math.sqrt( (below+1.)*(below+2.)/(total[n]+2.)/(total[n]+3.) - (below+1.)**2/(total[n]+2.)**2 )
        graphs_frac_below[mass].SetPoint(graphs_frac_below[mass].GetN(), n, valueBelow )
        graphs_frac_below[mass].SetPointError(graphs_frac_below[mass].GetN()-1, 0, errorBelow)
        #graphs_frac_below[mass].SetPointError(graphs_frac_below[mass].GetN()-1, 0.2, errorBelow)
        graphs_frac_below[mass].GetYaxis().SetTitle("False exclusion rate")
        graphs_frac_below[mass].GetXaxis().SetTitle("N_{inj} / #sqrt{N_{bkg}}")
        graphs_frac_below[mass].GetYaxis().SetRangeUser(-0.0,0.2999)
        graphs_frac_below[mass].GetXaxis().SetLimits(-0.0,max(ninj_list)+1)
        
        if n > x_max:
            x_max = 1.1*n
        if n < x_min:
            x_min = 1.1*n

    # for candle plot:
    try:
      bin_width = 0.1
    except:
      continue

    if bin_edges == []:
        #only set it once so all histograms have same binning. Necessary for the THStack later
        for n in range(int((max(ninj_list)+2))):
            bin_edges.append(n)
        
        bin_edges = array('d', bin_edges)


    existMasses.append(mass)
    h2_all_points[mass] = ROOT.TH2D("h2_"+str(mass), "", len(bin_edges)-1, bin_edges, 1000, 0.0001, 5*bin_edges[-1]);
    h2_all_points[mass].GetXaxis().SetTitle("N_{inj} / #sqrt{N_{bkg}}")
    h2_all_points[mass].GetYaxis().SetTitle("95% limit / #sqrt{N_{bkg}}")

    for n in range(graph.GetN()):
        ninj = graph.GetX()[n] + bin_width*index
        ulim = graph.GetY()[n]
        if math.isnan(ulim):
            ulim = 0.
        h2_all_points[mass].Fill(ninj, ulim)
        h2_all_points[mass].SetBarWidth(bin_width)
        h2_all_points[mass].SetBarOffset((index+1)*bin_width - 0.5)
    
    
  graphs = []
  ratios = []
  legendNames = []
  for mass in existMasses:
    graphs.append(h2_all_points[mass])
    ratios.append(graphs_frac_below[mass])
    legendNames.append(mass)

  canvas3 = df.setup_canvas("Canvas3")
  outfile = config.getFileName(inpath + "_candleplot", cdir, channelName, rangelow, rangehigh) +".pdf"
  ratios[0].GetYaxis().SetTitle("#splitline{False}{Excl. Rate}")
  leg, upperPad, lowerPad = df.DrawRatioHists(canvas3, graphs, ratios, legendNames, [], sampleName = "", drawOptions = ["CANDLEX"], styleOptions=df.get_extraction_style_opt, isLogX=0, isLogY=0, ratioDrawOptions = ["APEL", "PEL", "PEL", "PEL", "PEL"])

  upperPad.cd()
  line = ROOT.TLine(0, 0, bin_edges[-1], bin_edges[-1])
  line.SetLineWidth(2)
  line.SetLineStyle(7)
  line.SetLineColor(ROOT.kGray+1)
  line.Draw()

  lowerPad.cd()
  line2 = ROOT.TLine(0, 0.05, bin_edges[-1], 0.05)
  line2.SetLineWidth(2)
  line2.SetLineStyle(7)
  line2.SetLineColor(ROOT.kGray+1)
  line2.Draw()


  canvas3.Print(outfile)

    


