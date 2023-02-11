import ROOT as r 
import python.AtlasStyle as AS
from array import array
import math 
from math import sqrt

"""
    StyleOptions for a histogram not including the titles of the histogram, this allows the same style options to be used for histograms 
    showing data from the same source, but of a different type (e.g different MC generators showing different variables)

"""
class StyleOptions:
    def __init__(
        self,
        draw_options   = "",
        line_color     = r.kBlack,
        line_style     = 1,
        fill_color     = r.kWhite,
        fill_style     = 0,
        marker_color   = r.kBlack,
        marker_style   = 20,
        marker_size    = 0.045,
        line_width     = 4,
        legend_options = "l",
        y_divisions    = None,
        x_label_size   = 0.05,
        x_title_size   = 0.06,
        x_title_offset = 1.0,
        x_axis_label_offset = None,
        y_axis_label_offset = None,
        y_label_size   = 0.05,
        y_title_size   = 0.05,
        #y_title_offset = 0.5,
        y_title_offset = 1.3,
        z_label_size        = None,
        z_title_size        = None,
        z_title_offset      = None,
        z_axis_label_offset = None,
        ):

        self.draw_options = draw_options
        self.line_color   = line_color  
        self.line_style   = line_style  
        self.fill_color   = fill_color  
        self.fill_style   = fill_style 
        self.line_width   = line_width
        self.marker_color = marker_color
        self.marker_style = marker_style
        self.marker_size  = marker_size
        self.legend_options = legend_options
        self.y_divisions    = y_divisions
        self.x_label_size   = x_label_size
        self.y_label_size   = y_label_size
        self.x_title_size    = x_title_size
        self.x_title_offset = x_title_offset
        self.y_title_size   = y_title_size
        self.y_title_offset = y_title_offset
        self.x_axis_label_offset = x_axis_label_offset
        self.y_axis_label_offset = y_axis_label_offset
        self.z_label_size        = z_label_size        
        self.z_title_size        = z_title_size        
        self.z_title_offset      = z_title_offset      
        self.z_axis_label_offset = z_axis_label_offset 

def SetStyleOptions(hists, styleDef, height = 1.0):
  for hist in range(0, len(hists)):
    set_style_options(hists[hist], styleDef(hist), height)


def get_extraction_style_opt(count=0):
        markers = [34,20,24,21,25,22,26,23,32, 35, 20, 24, 21, 25]
        colors = ["#00CC99", "#CC3366", "#669933", "#3366CC", "#DD9933", "#9933CC"]
        lineStyles = [1, 1, 1, 1, 1, 1, 1]
        count = int(math.fmod(count, len(colors)))

        finalist_style_options= StyleOptions(
                             line_color   = colors[count],
                             line_style   = lineStyles[count],
                             marker_color = colors[count],
                             marker_style = markers[count],
                             marker_size = 1,
                             line_width = 4,
                             )
        return finalist_style_options

def get_fit_style_opt(count=0):
        markers = [24,20,24,21,25,22,26,23,32, 35, 20, 24, 21, 25]
        #colors = ['#000000','#3c3c3c','#5656d7','#D74061','#36bdbd', '#D69340', '#669900', "#2D2D70", "#CC6699", "#1518BD", "#33CC00", "#CC6600"]
        colors = ['#000000','#5656d7','#D74061','#36bdbd', '#D69340', '#669900', "#2D2D70", "#CC6699", "#1518BD", "#33CC00", "#CC6600"]
        #colors = ['#000000','#D74061']
        #colors = ['#000000','#5656d7','#D74061','#36bdbd']
        lineStyles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
        count = int(math.fmod(count, len(colors)))

        if count ==0:
          finalist_style_options= StyleOptions(
                             line_color   = colors[count],
                             line_style   = lineStyles[count],
                             marker_color = colors[count],
                             marker_style = markers[count],
                             marker_size = 1,
                             line_width = 0,
                             )
        if count >0:
          finalist_style_options= StyleOptions(
                             line_color   = colors[count],
                             line_style   = lineStyles[count],
                             marker_color = colors[count],
                             marker_style = markers[count],
                             marker_size = 1,
                             line_width = 4,
                             )
        return finalist_style_options


def get_finalist_style_opt(count=0):
        markers = [24,20,24,21,25,22,26,23,32, 35, 20, 24, 21, 25]
        #colors = ['#000000','#3c3c3c','#5656d7','#D74061','#36bdbd', '#D69340', '#669900', "#2D2D70", "#CC6699", "#1518BD", "#33CC00", "#CC6600"]
        colors = ['#000000','#5656d7','#D74061','#36bdbd', '#D69340', '#669900', "#2D2D70", "#CC6699", "#1518BD", "#33CC00", "#CC6600"]
        #colors = ['#000000','#D74061']
        #colors = ['#000000','#5656d7','#D74061','#36bdbd']
        lineStyles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
        count = int(math.fmod(count, len(colors)))

        finalist_style_options= StyleOptions(
                             line_color   = colors[count],
                             line_style   = lineStyles[count],
                             marker_color = colors[count],
                             fill_color = colors[count],
                             marker_style = markers[count],
                             marker_size = 1,
                             line_width = 4,
                             )
        return finalist_style_options

def get_fit_style_opt(count=0):
        markers = [20,20,24,21,25,22,26,23,32, 35, 20, 24, 21, 25]
        #colors = ['#000000','#3c3c3c','#5656d7','#D74061','#36bdbd', '#D69340', '#669900', "#2D2D70", "#CC6699", "#1518BD", "#33CC00", "#CC6600"]
        #colors = ['#000000','#FF0000','#D74061','#36bdbd', '#D69340', '#669900', "#2D2D70", "#CC6699", "#1518BD", "#33CC00", "#CC6600"]
        colors = ['#000000','#D74061','#D69340', '#669900', "#2D2D70", "#CC6699", "#1518BD", "#33CC00", "#CC6600"]
        #colors = ['#000000','#D74061','#36bdbd', '#D69340', '#669900', "#2D2D70", "#CC6699", "#1518BD", "#33CC00", "#CC6600"]
        #colors = ['#000000','#D74061']
        #colors = ['#000000','#5656d7','#D74061','#36bdbd']
        lineStyles = [1, 2, 4, 3, 5, 6, 7, 8, 9, 1, 2, 3, 4]
        count = int(math.fmod(count, len(colors)))

        finalist_style_options= StyleOptions(
                             line_color   = colors[count],
                             line_style   = lineStyles[count],
                             marker_color = colors[count],
                             fill_color = colors[count],
                             marker_size = 1,
                             marker_style = markers[count],
                             )
        return finalist_style_options


def get_rainbow_style_opt(count):
    colors = ["#3c3c3c", "#8A293E", "#D74061", "#BD4D37", "#D69340", "#BDA637",
              "#FFFF66", "#B6D640", "#36BDBD", "#5656D7", "#000099", "#49288A", "#9900CC"]

    #colors = ["#3c3c3c", "#8A293E", "#D74061", "#BD4D37", "#D69340", "#BDA637",
    #          "#3A4213", "#B6D640", "#36BDBD", "#5656D7", "#2D2D70", "#49288A"]
    lineStyles = [1, 2, 3, 4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    markers = [34,20,24,21,25,22,26,23,32, 35, 20, 24, 21, 25]
    if count >= len(colors):
        count = int(math.fmod(count, len(colors)))

    markers = [34,20,24,21,25,22,26,23,32, 34, 20, 24, 21]
    lineStyles = [1, 2, 3, 4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    rainbow_style_options= StyleOptions(
        line_style   = lineStyles[count],
        line_color = colors[count],
        marker_style = markers[count],
        marker_size = 1,
        marker_color = colors[count],
    )
    return rainbow_style_options


def draw_text(x, y, color, tsize, text, angle,set_NDC = False):
    l = r.TLatex()

    if set_NDC:
        l.SetNDC()

    l.SetTextAngle(angle)
    l.SetTextColor(color)
    l.SetTextSize(tsize)
    l.DrawLatex(x,y,text)

def setup_canvas(name=""):
  AS.SetAtlasStyle()
  r.gROOT.SetBatch(r.kTRUE)

  canvas = r.TCanvas("Canvas_%s"%(name),"",800,600)

  # give ourselves lots of room for groomer type
  canvas.SetLeftMargin(0.15)
  canvas.SetRightMargin(0.05)
  canvas.SetBottomMargin(0.15)
  canvas.SetTopMargin(0.05)
  r.gStyle.SetLegendBorderSize(0)
  #r.gStyle.SetLegendTextSize(0.025)
  r.gStyle.SetLegendFont(42)

  return canvas

def set_style_options(hist,style_options, height):

    hist.SetMarkerStyle(style_options.marker_style )
    hist.SetLineStyle(style_options.line_style  )
    #hist.SetFillStyle(1001)
    #hist.SetFillColorAlpha(r.TColor.GetColor(style_options.fill_color), 0.3)
    hist.SetMarkerColor(r.TColor.GetColor(style_options.marker_color))
    hist.SetLineColor(r.TColor.GetColor(style_options.line_color))
    hist.SetLineWidth(style_options.line_width)

    hist .GetXaxis().SetLabelSize(style_options.x_label_size / height)
    hist .GetXaxis().SetTitleSize(style_options.x_title_size / height)

    hist.GetXaxis().SetTitleOffset(style_options.x_title_offset )
    hist.GetYaxis().SetLabelSize(style_options.y_label_size / height)
    #hist.GetYaxis().SetTitleOffset(style_options.y_title_offset )
    #hist.GetYaxis().SetTitleOffset(style_options.y_title_offset / height )
    #hist.GetYaxis().SetTitleOffset(style_options.y_title_offset)
    hist.GetYaxis().SetTitleOffset(style_options.y_title_offset*height)
    hist.GetYaxis().SetTitleSize(style_options.y_title_size / height)

    hist.SetMarkerSize((style_options.marker_size))

    return hist


 
def get_mass_plot_style(is_signal = 0):
        #set the drawing style options options to be nice 
        colors = ['#5656d7','#D74061','#36bdbd']
        return StyleOptions(
                             draw_options = "HIST",
                             line_style   = 1 if is_signal else 2,
                             line_width   = 4,
                             line_color   = colors[is_signal],
                             fill_color   = r.kWhite,
                             fill_style   = 0,
                             marker_color = r.kBlack,
                             marker_style = 0,
                             marker_size  = 0,
                             y_title_offset = 1.5,
                             )


def draw_atlas_details(labels=[],x_pos= 0.18,y_pos = 0.88, dy = 0.055, text_size = 0.05, sampleName="", atlasLabel = "Simulation Internal", height = 1.0, lumi=139):
    text_size = text_size / height
    dy = dy / height
    if sampleName != "":
          sampleName = ", " + sampleName
    AS.ATLASLabel(x_pos, y_pos, 1, 0.13, text_size, atlasLabel)

    y_pos -= dy
    AS.myText(  x_pos, y_pos,1,text_size,"#sqrt{s} = 13 TeV, %.1f fb^{-1}  %s"%(lumi, sampleName))
    y_pos -= dy

    for label in labels:
        AS.myText( x_pos, y_pos, 1, text_size, "%s"%label)
        y_pos -= dy
    return


def SetRange(hists, minMin=-1e6, maxMax=1e6, myMin=-123456, myMax=-123456, isLog=False, isZeroed=True, minMjj=0, maxMjj=10000000):
  if myMin != myMax: 
    for hist in hists:
      hist.GetYaxis().SetRangeUser(myMin, myMax)
    return
  maximum = minMin
  minimum = maxMax
  for hist in hists:
    if(hist.GetBinContent( hist.GetMaximumBin()) > maximum):
      maximum = hist.GetBinContent( hist.GetMaximumBin())

    if(hist.GetBinContent( hist.GetMinimumBin()) < minimum):
      minimum = hist.GetBinContent( hist.GetMinimumBin())

  delta = maximum-minimum

  if isLog:
    if maximum > minimum:
      if minimum == 0:
        minimum = maxMax
        for cbin in range(hist.GetNbinsX()):
          if hist.GetBinCenter(cbin+1) < minMjj: 
             continue
          if hist.GetBinCenter(cbin+1) > maxMjj: 
             continue
          if hist.GetBinContent(cbin+1) > 0 and hist.GetBinContent(cbin+1) < minimum:
            minimum = hist.GetBinContent( cbin+1)
          
      maximum = math.pow(10, math.log10(maximum) + math.log10(maximum/minimum)*0.6  )
    #minimum = pow(10, math.floor(math.log10(minimum)))*0.2
    minimum = pow(10, math.floor(math.log10(minimum)))*0.5
  else:
    #maximum = maximum + delta*1.
    maximum = maximum + delta*0.25
    minimum = minimum - delta*0.2
    if minimum < minMin:
      minimum = minMin
    if maximum > maxMax:
      maximum = maxMax
    if myMin != -123456:
      minimum = myMin
    if myMax != -123456:
      maximum = myMax
    if isZeroed:
      minimum = 0

  if minimum < minMin:
    minimum = minMin
  if maximum > maxMax:
    maximum = maxMax
  

  for hist in hists:
    hist.GetYaxis().SetRangeUser(minimum, maximum)

def DrawHists(canvas, hists, legendNames, labels, sampleName = "", drawOptions = ["HIST"], styleOptions=get_finalist_style_opt, isLogX=0, lumi=0, atlasLabel="Simulation Internal"):
  canvas.cd()

  if len(hists) ==0:
    return
  legend = r.TLegend(0.65,0.9-(len(hists))*0.05,.94,0.90)
  legend.SetFillStyle(0)
  SetStyleOptions(hists, styleOptions)

  canvas.SetLogx(isLogX)
  if(isLogX):
    hists[0].GetXaxis().SetMoreLogLabels()

  hists[0].Draw("AXIS")

  for hist in range(len(hists)):
    hists[hist].Draw("%s SAME"%(drawOptions[hist%len(drawOptions)]))
    legend.AddEntry(hists[hist], legendNames[hist] , "lp")

  legend.Draw()

  draw_atlas_details(labels=labels, sampleName=sampleName, atlasLabel=atlasLabel, text_size = 0.04)

  return legend


def DrawRatioHists(canvas, hists, Ratios, legendNames, labels, sampleName, drawOptions = ["HIST"], styleOptions=get_finalist_style_opt, outName="Test", isLogX = False, isLogY=True, lumi=0, atlasLabel="Simulation Internal", ratioDrawOptions = ["B", "HIST"], ratioHeight = 0.35):
  canvas.cd()
  style = AS.SetAtlasStyle()

  upperPad = r.TPad("pad1%s"%outName, "pad1",0.0,ratioHeight,1.0,1.0)
  upperPad.SetTopMargin(0.05)
  upperPad.SetBottomMargin(0.0)
  upperPad.SetLeftMargin(0.15)
  upperPad.SetRightMargin(0.05)
  upperPad.Draw()
  upperPad.SetLogx(isLogX)
  upperPad.SetLogy(isLogY)
  upperPad.cd()
  r.SetOwnership(upperPad, False)

  canvas.cd();
  lowerPad = r.TPad("pad2%s"%outName, "pad2", 0.0,0.0,1.0,ratioHeight)
  lowerPad.SetBottomMargin(0.4)
  lowerPad.SetTopMargin(0.00)
  lowerPad.SetLeftMargin(0.15)
  lowerPad.SetRightMargin(0.05)
  lowerPad.Draw()
  lowerPad.SetLogx(isLogX)
  r.SetOwnership(lowerPad, False)

  if len(hists) ==0:
    return
  upperPad.cd()
  deltaHists=0.11
  if len(hists) > 5:
    deltaHists = 0.06
  legend = r.TLegend(0.56,0.95-(len(hists))*deltaHists,.91,0.95)
  legend.SetFillStyle(0)
  SetStyleOptions(hists, styleOptions,1.0-ratioHeight)
  SetStyleOptions(Ratios, styleOptions, ratioHeight)
  #hists[0].SetFillColor(r.kBlack)
  #hists[0].SetFillStyle(1001)

  #if(isLogX):
  #  hists[0].SetLineWidth(1)

  hists[0].Draw("%s"%(drawOptions[0]))
  for hist in range(len(hists)):
    if hist > 0:
      hists[hist].Draw("%s SAME"%(drawOptions[1]))
    index = (hist > 0)
    if( drawOptions[index]=="HIST" or drawOptions[index]=="hist" or drawOptions[index]=="l"):
      legend.AddEntry(hists[hist], legendNames[hist] , "l")
    else:
      legend.AddEntry(hists[hist], legendNames[hist] , "px0")
  if drawOptions[0] != "AP":
    hists[0].Draw("%s SAME"%(drawOptions[0]))
  #hists[0].Draw("%s SAME"%(drawOptions[0]))

  legend.Draw()

  draw_atlas_details(labels=labels, sampleName=sampleName, height=0.9-0.35, y_pos=0.85, atlasLabel=atlasLabel, text_size = 0.04)
  lowerPad.cd()

  if(isLogX):
    Ratios[0].GetXaxis().SetMoreLogLabels()
  Ratios[0].Draw("%s"%(ratioDrawOptions[0]))
  for hist in range(len(Ratios)):
    if hist > 0:
      Ratios[hist].Draw("%s SAME"%(ratioDrawOptions[1]))

  return legend, upperPad, lowerPad



def DrawResponseArrows(multigraph):
  arrow1 = r.TArrow()
  arrow1.SetLineWidth(2)
  arrow1.SetLineColor(r.kBlack)
  arrow1.SetLineStyle(1)
  arrow1.DrawArrow(multigraph.GetXaxis().GetXmin() ,1.0,multigraph.GetXaxis().GetXmax(),1.0,0.5,"same")

  arrow2 = r.TArrow()
  arrow2.SetLineWidth(2)
  arrow2.SetLineColor(r.kBlack)
  arrow2.SetLineStyle(7)
  arrow2.DrawArrow(multigraph.GetXaxis().GetXmin() ,1.03,multigraph.GetXaxis().GetXmax(),1.03,0.5,"same")

  arrow3 = r.TArrow()
  arrow3.SetLineWidth(2)
  arrow3.SetLineColor(r.kBlack)
  arrow3.SetLineStyle(7)
  arrow3.DrawArrow(multigraph.GetXaxis().GetXmin() ,0.97,multigraph.GetXaxis().GetXmax(),0.97,0.5,"same")

def SaveCanvas(canvas,name):
    #if savePDF:
        canvas.SaveAs(name+".pdf")
    #if saveEPS:
    #    canvas.SaveAs(name+".eps")


def SetColorWheel():
    NRGBs = 6
    NCont = 99
    stops = [ 0.00, 0.10, 0.48, 0.52, 0.90, 1.00 ]
    red   = [ 0.00, 0.00, 1.00, 1.00, 1.00, 1.00 ]
    green = [ 0.20, 0.50, 1.00, 1.00, 0.50, 0.20 ]
    blue  = [ 1.00, 1.00, 1.00, 1.00, 0.00, 0.00 ]
    stopsArray = array('d', stops)
    redArray   = array('d', red)
    greenArray = array('d', green)
    blueArray  = array('d', blue)
    r.TColor.CreateGradientColorTable(NRGBs, stopsArray, redArray, greenArray, blueArray, NCont)
    r.gStyle.SetNumberContours(NCont)


