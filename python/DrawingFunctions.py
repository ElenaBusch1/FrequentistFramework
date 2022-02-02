import ROOT as r 
import AtlasStyle as AS
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
        x_label_size   = 0.04,
        x_title_size   = 0.05,
        x_title_offset = 1.0,
        x_axis_label_offset = None,
        y_axis_label_offset = None,
        y_label_size   = 0.04,
        y_title_size   = 0.05,
        #y_title_offset = 0.5,
        y_title_offset = 1.25,
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


def get_finalist_style_opt(count=0):
        markers = [34,20,24,21,25,22,26,23,32, 35, 20, 24, 21, 25]
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
                             marker_style = markers[count],
                             )
        return finalist_style_options

def get_fit_style_opt(count=0):
        markers = [34,20,24,21,25,22,26,23,32, 35, 20, 24, 21, 25]
        #colors = ['#000000','#3c3c3c','#5656d7','#D74061','#36bdbd', '#D69340', '#669900', "#2D2D70", "#CC6699", "#1518BD", "#33CC00", "#CC6600"]
        colors = ['#000000','#FF0000','#D74061','#36bdbd', '#D69340', '#669900', "#2D2D70", "#CC6699", "#1518BD", "#33CC00", "#CC6600"]
        #colors = ['#000000','#D74061']
        #colors = ['#000000','#5656d7','#D74061','#36bdbd']
        lineStyles = [1, 1, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
        count = int(math.fmod(count, len(colors)))

        finalist_style_options= StyleOptions(
                             line_color   = colors[count],
                             line_style   = lineStyles[count],
                             marker_color = colors[count],
                             marker_size = 1,
                             marker_style = markers[count],
                             )
        return finalist_style_options


def get_rainbow_style_opt(count):
    colors = ["#3c3c3c", "#8A293E", "#D74061", "#BD4D37", "#D69340", "#BDA637",
              "#3A4213", "#B6D640", "#36BDBD", "#5656D7", "#2D2D70", "#49288A"]
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
  #AS.SetAtlasStyle()
  r.gROOT.SetBatch(r.kTRUE)

  canvas = r.TCanvas("Canvas_%s"%(name),"",800,600)

  # give ourselves lots of room for groomer type
  canvas.SetLeftMargin(0.15)
  canvas.SetRightMargin(0.05)
  canvas.SetBottomMargin(0.15)
  canvas.SetTopMargin(0.01)
  r.gStyle.SetLegendBorderSize(0)
  #r.gStyle.SetLegendTextSize(0.025)
  r.gStyle.SetLegendFont(42)

  return canvas

def set_style_options(hist,style_options, height):

    hist.SetMarkerStyle(style_options.marker_style )
    hist.SetLineStyle(style_options.line_style  )
    hist.SetFillStyle(0)
    #hist.SetFillColorAlpha(r.TColor.GetColor(style_options.fill_color), 0.  )
    hist.SetMarkerColor(r.TColor.GetColor(style_options.marker_color))
    hist.SetLineColor(r.TColor.GetColor(style_options.line_color))
    hist.SetLineWidth(style_options.line_width)

    hist .GetXaxis().SetLabelSize(style_options.x_label_size / height)
    hist .GetXaxis().SetTitleSize(style_options.x_title_size / height)

    hist .GetXaxis().SetTitleOffset(style_options.x_title_offset )
    hist .GetYaxis().SetLabelSize(style_options.y_label_size / height)
    #hist .GetYaxis().SetTitleOffset(style_options.y_title_offset )
    hist .GetYaxis().SetTitleOffset(style_options.y_title_offset / height )
    hist .GetYaxis().SetTitleSize(style_options.y_title_size / height)

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


def draw_atlas_details(labels=[],x_pos= 0.18,y_pos = 0.95, dy = 0.04, text_size = 0.035, sampleName="", atlasLabel = "Simulation Internal", height = 1.0):
    text_size = text_size / height
    dy = dy / height
    if sampleName != "":
          sampleName = ", " + sampleName
    AS.ATLASLabel(x_pos, y_pos, 1, x_pos, dy, atlasLabel)
    y_pos -= dy
    AS.myText(  x_pos, y_pos,1,text_size,"#sqrt{s} = 13 TeV, 44.3 fb^{-1}  %s"%(sampleName))
    y_pos -= dy

    for label in labels:
        AS.myText( x_pos, y_pos, 1, text_size, "%s"%label)
        y_pos -= dy
    return


def SetRange(hists, minMin=-1e6, maxMax=1e6, myMin=-123456, myMax=-123456, isLog=False):
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
          if hist.GetBinContent(cbin+1) > 0 and hist.GetBinContent(cbin+1) < minimum:
            minimum = hist.GetBinContent( cbin+1)
          
      #minimum = maximum / 10.
      #maximum = maximum * math.pow(10, math.log(maximum/minimum)  )
      maximum = maximum * 10
    minimum = minimum / 1.5
  else:

    maximum = maximum + delta*1.
    minimum = minimum - delta*0.2
    if minimum < minMin:
      minimum = minMin
    if maximum > maxMax:
      maximum = maxMax
    if myMin != -123456:
      minimum = myMin
    if myMax != -123456:
      maximum = myMax

  for hist in hists:
    hist.GetYaxis().SetRangeUser(minimum, maximum)

def DrawHists(canvas, hists, legendNames, labels, sampleName = "", drawOptions = ["HIST"], styleOptions=get_finalist_style_opt, isLogX=0):
  canvas.cd()
  canvas.SetLogx(isLogX)

  if len(hists) ==0:
    return
  legend = r.TLegend(0.65,0.9-(len(hists))*0.05,.94,0.90)
  legend.SetFillStyle(0)
  SetStyleOptions(hists, styleOptions)
  if(isLogX):
    hists[0].GetXaxis().SetMoreLogLabels()
  hists[0].Draw("AXIS")

  for hist in range(len(hists)):
    hists[hist].Draw("%s SAME"%(drawOptions[hist%len(drawOptions)]))
    legend.AddEntry(hists[hist], legendNames[hist] , "lp")

  legend.Draw()
  draw_atlas_details(labels=labels, sampleName=sampleName)
  hists[0].Draw("AXIS SAME")
  return legend


def DrawRatioHists(canvas, hists, Ratios, legendNames, labels, sampleName, drawOptions = ["HIST"], styleOptions=get_finalist_style_opt, outName="Test", isLogX = False, isLogY=True):
  canvas.cd()
  canvas.SetLogx(isLogX)

  upperPad = r.TPad("pad1%s"%outName, "pad1",0.0,0.35,1.0,1.0)
  upperPad.SetTopMargin(0.05)
  upperPad.SetBottomMargin(0.01)
  upperPad.SetLeftMargin(0.15)
  upperPad.SetRightMargin(0.05)
  upperPad.Draw()
  upperPad.SetLogx(isLogX)
  upperPad.SetLogy(isLogY)
  upperPad.cd()
  r.SetOwnership(upperPad, False)

  canvas.cd();
  lowerPad = r.TPad("pad2%s"%outName, "pad2", 0.0,0.05,1.0,0.35)
  lowerPad.SetBottomMargin(0.4)
  lowerPad.SetTopMargin(-0.05)
  lowerPad.SetLeftMargin(0.15)
  lowerPad.SetRightMargin(0.05)
  lowerPad.Draw()
  lowerPad.SetLogx(isLogX)
  r.SetOwnership(lowerPad, False)

  if len(hists) ==0:
    return
  upperPad.cd()
  deltaHists=0.1
  if len(hists) > 4:
    deltaHists = 0.06
  legend = r.TLegend(0.7,0.9-(len(hists))*deltaHists,.9,0.90)
  legend.SetFillStyle(0)
  SetStyleOptions(hists, styleOptions, 0.95-0.35)
  SetStyleOptions(Ratios, styleOptions, 0.95-0.35)

  for hist in range(len(hists)):
    hists[hist].Draw("%s SAME"%(drawOptions[hist%len(drawOptions)]))
    legend.AddEntry(hists[hist], legendNames[hist] , "l")
  hists[0].Draw("%s SAME"%(drawOptions[0]))

  legend.Draw()


  draw_atlas_details(labels=labels, sampleName=sampleName, height=0.9-0.35, y_pos=0.85)
  lowerPad.cd()

  rDrawOptions = "B"
  Ratios[0].Draw("%s"%(rDrawOptions))
  #for hist in range(len(Ratios)):
  for ratio in Ratios:
    ratio.SetFillStyle(1000)
    ratio.Draw("%s SAME"%rDrawOptions)

  SaveCanvas(canvas, outName)

  return legend



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


