#!/usr/bin/env python
import ROOT
import sys, re, os, math, argparse
from array import array
from ROOT import *
from math import sqrt
from math import isnan
from glob import glob
import config as config
import LocalFunctions as lf
import DrawingFunctions as df
import AtlasStyle as AS

ROOT.gROOT.SetBatch(ROOT.kTRUE)

gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasLabels.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasStyle.C")
gROOT.LoadMacro("../atlasstyle-00-04-02/AtlasUtils.C")


def xToNDC(x):
    gPad.Update()
    lm = gPad.GetLeftMargin()
    rm = 1.-gPad.GetRightMargin()
    xndc = (rm-lm)*((gPad.XtoPad(x)-gPad.GetUxmin())/(gPad.GetUxmax()-gPad.GetUxmin()))+lm
    return xndc

def createFillBetweenGraphs(g1, g2):
  g_fill = TGraph()
  
  for i in range(g1.GetN()):
      x=ROOT.Double()
      y=ROOT.Double()
    
      g1.GetPoint(i, x, y)
    
      g_fill.SetPoint(g_fill.GetN(), x, y)

  for i in range(g2.GetN()-1, -1, -1):
      x=ROOT.Double()
      y=ROOT.Double()
    
      g2.GetPoint(i, x, y)
    
      g_fill.SetPoint(g_fill.GetN(), x, y)

  return g_fill

def plotLimits(sigmeans, sigwidths, paths, lumis, outdir, cdir, channelNames, atlasLabel="Simulation Internal", deltaMassAboveFit=0, sigamp=0, ntoy=None, alphaBins = [], meansCentered = [1500, 2500, 3500, 5000, 7000, 9000, 11000], postfitPaths = [], isMx = False, signalfile="Gaussian"):
    SetAtlasStyle()

    red = [0.001462, 0.002258, 0.003279, 0.004512, 0.005950, 0.007588, 0.009426, 0.011465, 0.013708, 0.016156, 0.018815, 0.021692, 0.024792, 0.028123, 0.031696, 0.035520, 0.039608, 0.043830, 0.048062, 0.052320, 0.056615, 0.060949, 0.065330, 0.069764, 0.074257, 0.078815, 0.083446, 0.088155, 0.092949, 0.097833, 0.102815, 0.107899, 0.113094, 0.118405, 0.123833, 0.129380, 0.135053, 0.140858, 0.146785, 0.152839, 0.159018, 0.165308, 0.171713, 0.178212, 0.184801, 0.191460, 0.198177, 0.204935, 0.211718, 0.218512, 0.225302, 0.232077, 0.238826, 0.245543, 0.252220, 0.258857, 0.265447, 0.271994, 0.278493, 0.284951, 0.291366, 0.297740, 0.304081, 0.310382, 0.316654, 0.322899, 0.329114, 0.335308, 0.341482, 0.347636, 0.353773, 0.359898, 0.366012, 0.372116, 0.378211, 0.384299, 0.390384, 0.396467, 0.402548, 0.408629, 0.414709, 0.420791, 0.426877, 0.432967, 0.439062, 0.445163, 0.451271, 0.457386, 0.463508, 0.469640, 0.475780, 0.481929, 0.488088, 0.494258, 0.500438, 0.506629, 0.512831, 0.519045, 0.525270, 0.531507, 0.537755, 0.544015, 0.550287, 0.556571, 0.562866, 0.569172, 0.575490, 0.581819, 0.588158, 0.594508, 0.600868, 0.607238, 0.613617, 0.620005, 0.626401, 0.632805, 0.639216, 0.645633, 0.652056, 0.658483, 0.664915, 0.671349, 0.677786, 0.684224, 0.690661, 0.697098, 0.703532, 0.709962, 0.716387, 0.722805, 0.729216, 0.735616, 0.742004, 0.748378, 0.754737, 0.761077, 0.767398, 0.773695, 0.779968, 0.786212, 0.792427, 0.798608, 0.804752, 0.810855, 0.816914, 0.822926, 0.828886, 0.834791, 0.840636, 0.846416, 0.852126, 0.857763, 0.863320, 0.868793, 0.874176, 0.879464, 0.884651, 0.889731, 0.894700, 0.899552, 0.904281, 0.908884, 0.913354, 0.917689, 0.921884, 0.925937, 0.929845, 0.933606, 0.937221, 0.940687, 0.944006, 0.947180, 0.950210, 0.953099, 0.955849, 0.958464, 0.960949, 0.963310, 0.965549, 0.967671, 0.969680, 0.971582, 0.973381, 0.975082, 0.976690, 0.978210, 0.979645, 0.981000, 0.982279, 0.983485, 0.984622, 0.985693, 0.986700, 0.987646, 0.988533, 0.989363, 0.990138, 0.990871, 0.991558, 0.992196, 0.992785, 0.993326, 0.993834, 0.994309, 0.994738, 0.995122, 0.995480, 0.995810, 0.996096, 0.996341, 0.996580, 0.996775, 0.996925, 0.997077, 0.997186, 0.997254, 0.997325, 0.997351, 0.997351, 0.997341, 0.997285, 0.997228, 0.997138, 0.997019, 0.996898, 0.996727, 0.996571, 0.996369, 0.996162, 0.995932, 0.995680, 0.995424, 0.995131, 0.994851, 0.994524, 0.994222, 0.993866, 0.993545, 0.993170, 0.992831, 0.992440, 0.992089, 0.991688, 0.991332, 0.990930, 0.990570, 0.990175, 0.989815, 0.989434, 0.989077, 0.988717, 0.988367, 0.988033, 0.987691, 0.987387, 0.987053]
    green = [0.000466, 0.001295, 0.002305, 0.003490, 0.004843, 0.006356, 0.008022, 0.009828, 0.011771, 0.013840, 0.016026, 0.018320, 0.020715, 0.023201, 0.025765, 0.028397, 0.031090, 0.033830, 0.036607, 0.039407, 0.042160, 0.044794, 0.047318, 0.049726, 0.052017, 0.054184, 0.056225, 0.058133, 0.059904, 0.061531, 0.063010, 0.064335, 0.065492, 0.066479, 0.067295, 0.067935, 0.068391, 0.068654, 0.068738, 0.068637, 0.068354, 0.067911, 0.067305, 0.066576, 0.065732, 0.064818, 0.063862, 0.062907, 0.061992, 0.061158, 0.060445, 0.059889, 0.059517, 0.059352, 0.059415, 0.059706, 0.060237, 0.060994, 0.061978, 0.063168, 0.064553, 0.066117, 0.067835, 0.069702, 0.071690, 0.073782, 0.075972, 0.078236, 0.080564, 0.082946, 0.085373, 0.087831, 0.090314, 0.092816, 0.095332, 0.097855, 0.100379, 0.102902, 0.105420, 0.107930, 0.110431, 0.112920, 0.115395, 0.117855, 0.120298, 0.122724, 0.125132, 0.127522, 0.129893, 0.132245, 0.134577, 0.136891, 0.139186, 0.141462, 0.143719, 0.145958, 0.148179, 0.150383, 0.152569, 0.154739, 0.156894, 0.159033, 0.161158, 0.163269, 0.165368, 0.167454, 0.169530, 0.171596, 0.173652, 0.175701, 0.177743, 0.179779, 0.181811, 0.183840, 0.185867, 0.187893, 0.189921, 0.191952, 0.193986, 0.196027, 0.198075, 0.200133, 0.202203, 0.204286, 0.206384, 0.208501, 0.210638, 0.212797, 0.214982, 0.217194, 0.219437, 0.221713, 0.224025, 0.226377, 0.228772, 0.231214, 0.233705, 0.236249, 0.238851, 0.241514, 0.244242, 0.247040, 0.249911, 0.252861, 0.255895, 0.259016, 0.262229, 0.265540, 0.268953, 0.272473, 0.276106, 0.279857, 0.283729, 0.287728, 0.291859, 0.296125, 0.300530, 0.305079, 0.309773, 0.314616, 0.319610, 0.324755, 0.330052, 0.335500, 0.341098, 0.346844, 0.352734, 0.358764, 0.364929, 0.371224, 0.377643, 0.384178, 0.390820, 0.397563, 0.404400, 0.411324, 0.418323, 0.425390, 0.432519, 0.439703, 0.446936, 0.454210, 0.461520, 0.468861, 0.476226, 0.483612, 0.491014, 0.498428, 0.505851, 0.513280, 0.520713, 0.528148, 0.535582, 0.543015, 0.550446, 0.557873, 0.565296, 0.572706, 0.580107, 0.587502, 0.594891, 0.602275, 0.609644, 0.616999, 0.624350, 0.631696, 0.639027, 0.646344, 0.653659, 0.660969, 0.668256, 0.675541, 0.682828, 0.690088, 0.697349, 0.704611, 0.711848, 0.719089, 0.726324, 0.733545, 0.740772, 0.747981, 0.755190, 0.762398, 0.769591, 0.776795, 0.783977, 0.791167, 0.798348, 0.805527, 0.812706, 0.819875, 0.827052, 0.834213, 0.841387, 0.848540, 0.855711, 0.862859, 0.870024, 0.877168, 0.884330, 0.891470, 0.898627, 0.905763, 0.912915, 0.920049, 0.927196, 0.934329, 0.941470, 0.948604, 0.955742, 0.962878, 0.970012, 0.977154, 0.984288, 0.991438]
    blue = [0.013866, 0.018331, 0.023708, 0.029965, 0.037130, 0.044973, 0.052844, 0.060750, 0.068667, 0.076603, 0.084584, 0.092610, 0.100676, 0.108787, 0.116965, 0.125209, 0.133515, 0.141886, 0.150327, 0.158841, 0.167446, 0.176129, 0.184892, 0.193735, 0.202660, 0.211667, 0.220755, 0.229922, 0.239164, 0.248477, 0.257854, 0.267289, 0.276784, 0.286321, 0.295879, 0.305443, 0.315000, 0.324538, 0.334011, 0.343404, 0.352688, 0.361816, 0.370771, 0.379497, 0.387973, 0.396152, 0.404009, 0.411514, 0.418647, 0.425392, 0.431742, 0.437695, 0.443256, 0.448436, 0.453248, 0.457710, 0.461840, 0.465660, 0.469190, 0.472451, 0.475462, 0.478243, 0.480812, 0.483186, 0.485380, 0.487408, 0.489287, 0.491024, 0.492631, 0.494121, 0.495501, 0.496778, 0.497960, 0.499053, 0.500067, 0.501002, 0.501864, 0.502658, 0.503386, 0.504052, 0.504662, 0.505215, 0.505714, 0.506160, 0.506555, 0.506901, 0.507198, 0.507448, 0.507652, 0.507809, 0.507921, 0.507989, 0.508011, 0.507988, 0.507920, 0.507806, 0.507648, 0.507443, 0.507192, 0.506895, 0.506551, 0.506159, 0.505719, 0.505230, 0.504692, 0.504105, 0.503466, 0.502777, 0.502035, 0.501241, 0.500394, 0.499492, 0.498536, 0.497524, 0.496456, 0.495332, 0.494150, 0.492910, 0.491611, 0.490253, 0.488836, 0.487358, 0.485819, 0.484219, 0.482558, 0.480835, 0.479049, 0.477201, 0.475290, 0.473316, 0.471279, 0.469180, 0.467018, 0.464794, 0.462509, 0.460162, 0.457755, 0.455289, 0.452765, 0.450184, 0.447543, 0.444848, 0.442102, 0.439305, 0.436461, 0.433573, 0.430644, 0.427671, 0.424666, 0.421631, 0.418573, 0.415496, 0.412403, 0.409303, 0.406205, 0.403118, 0.400047, 0.397002, 0.393995, 0.391037, 0.388137, 0.385308, 0.382563, 0.379915, 0.377376, 0.374959, 0.372677, 0.370541, 0.368567, 0.366762, 0.365136, 0.363701, 0.362468, 0.361438, 0.360619, 0.360014, 0.359630, 0.359469, 0.359529, 0.359810, 0.360311, 0.361030, 0.361965, 0.363111, 0.364466, 0.366025, 0.367783, 0.369734, 0.371874, 0.374198, 0.376698, 0.379371, 0.382210, 0.385210, 0.388365, 0.391671, 0.395122, 0.398714, 0.402441, 0.406299, 0.410283, 0.414390, 0.418613, 0.422950, 0.427397, 0.431951, 0.436607, 0.441361, 0.446213, 0.451160, 0.456192, 0.461314, 0.466526, 0.471811, 0.477182, 0.482635, 0.488154, 0.493755, 0.499428, 0.505167, 0.510983, 0.516859, 0.522806, 0.528821, 0.534892, 0.541039, 0.547233, 0.553499, 0.559820, 0.566202, 0.572645, 0.579140, 0.585701, 0.592307, 0.598983, 0.605696, 0.612482, 0.619299, 0.626189, 0.633109, 0.640099, 0.647116, 0.654202, 0.661309, 0.668481, 0.675675, 0.682926, 0.690198, 0.697519, 0.704863, 0.712242, 0.719649, 0.727077, 0.734536, 0.742002, 0.74950]
	


    stops = [ 0.0, 0.0039, 0.0078, 0.0118, 0.0157, 0.0196, 0.0235, 0.0275, 0.0314, 0.0353, 0.0392, 0.0431, 0.0471, 0.051, 0.0549, 0.0588, 0.0627, 0.0667, 0.0706, 0.0745, 0.0784, 0.0824, 0.0863, 0.0902, 0.0941, 0.098, 0.102, 0.1059, 0.1098, 0.1137, 0.1176, 0.1216, 0.1255, 0.1294, 0.1333, 0.1373, 0.1412, 0.1451, 0.149, 0.1529, 0.1569, 0.1608, 0.1647, 0.1686, 0.1725, 0.1765, 0.1804, 0.1843, 0.1882, 0.1922, 0.1961, 0.2, 0.2039, 0.2078, 0.2118, 0.2157, 0.2196, 0.2235, 0.2275, 0.2314, 0.2353, 0.2392, 0.2431, 0.2471, 0.251, 0.2549, 0.2588, 0.2627, 0.2667, 0.2706, 0.2745, 0.2784, 0.2824, 0.2863, 0.2902, 0.2941, 0.298, 0.302, 0.3059, 0.3098, 0.3137, 0.3176, 0.3216, 0.3255, 0.3294, 0.3333, 0.3373, 0.3412, 0.3451, 0.349, 0.3529, 0.3569, 0.3608, 0.3647, 0.3686, 0.3725, 0.3765, 0.3804, 0.3843, 0.3882, 0.3922, 0.3961, 0.4, 0.4039, 0.4078, 0.4118, 0.4157, 0.4196, 0.4235, 0.4275, 0.4314, 0.4353, 0.4392, 0.4431, 0.4471, 0.451, 0.4549, 0.4588, 0.4627, 0.4667, 0.4706, 0.4745, 0.4784, 0.4824, 0.4863, 0.4902, 0.4941, 0.498, 0.502, 0.5059, 0.5098, 0.5137, 0.5176, 0.5216, 0.5255, 0.5294, 0.5333, 0.5373, 0.5412, 0.5451, 0.549, 0.5529, 0.5569, 0.5608, 0.5647, 0.5686, 0.5725, 0.5765, 0.5804, 0.5843, 0.5882, 0.5922, 0.5961, 0.6, 0.6039, 0.6078, 0.6118, 0.6157, 0.6196, 0.6235, 0.6275, 0.6314, 0.6353, 0.6392, 0.6431, 0.6471, 0.651, 0.6549, 0.6588, 0.6627, 0.6667, 0.6706, 0.6745, 0.6784, 0.6824, 0.6863, 0.6902, 0.6941, 0.698, 0.702, 0.7059, 0.7098, 0.7137, 0.7176, 0.7216, 0.7255, 0.7294, 0.7333, 0.7373, 0.7412, 0.7451, 0.749, 0.7529, 0.7569, 0.7608, 0.7647, 0.7686, 0.7725, 0.7765, 0.7804, 0.7843, 0.7882, 0.7922, 0.7961, 0.8, 0.8039, 0.8078, 0.8118, 0.8157, 0.8196, 0.8235, 0.8275, 0.8314, 0.8353, 0.8392, 0.8431, 0.8471, 0.851, 0.8549, 0.8588, 0.8627, 0.8667, 0.8706, 0.8745, 0.8784, 0.8824, 0.8863, 0.8902, 0.8941, 0.898, 0.902, 0.9059, 0.9098, 0.9137, 0.9176, 0.9216, 0.9255, 0.9294, 0.9333, 0.9373, 0.9412, 0.9451, 0.949, 0.9529, 0.9569, 0.9608, 0.9647, 0.9686, 0.9725, 0.9765, 0.9804, 0.9843, 0.9882, 0.9922, 0.9961, 1.0]
    nb=255;
    TColor.CreateGradientColorTable(256, array('d', stops), array('d', red), array('d', green), array('d', blue), nb);

    # colors = [kBlue, kMagenta+2, kRed+1, kGreen+2]
    colors = [kBlue, kRed+1, kOrange-3]
    meansCentered = []
    meansCentered.append(sigmeans[0] - (sigmeans[1]-sigmeans[0])/2.)
    for i in range(len(sigmeans)-1):
      #print sigmeans[i], sigmeans[i+1], (sigmeans[i] + sigmeans[i+1])/2.
      meansCentered.append((sigmeans[i] + sigmeans[i+1])/2.)
    nbins = len(sigmeans)
    meansCentered.append(sigmeans[nbins-1] + (sigmeans[nbins-1] - sigmeans[nbins-2])/2.)
    #print meansCentered

    #limits2D = TGraph2D()

  
    massLabel = "m_{Y}"
    if isMx:
      massLabel = "m_{X}"
    limits2D = TH2D("limits2D", ";%s [GeV];#alpha;#sigma #times #it{A} #times #it{BR} [pb]"%(massLabel), len(sigmeans), array('d', meansCentered), len(alphaBins)-1, array('d', alphaBins))

    for alphaBin, channelName in enumerate(channelNames):
        g_obs_datasets = []
        g_exp_datasets = []
        g_exp1_datasets = []
        g_exp2_datasets = []
        g_exp1u_datasets = []
        g_exp2u_datasets = []
        g_exp1d_datasets = []
        g_exp2d_datasets = []
  

        #for dataset in range(len(paths)):

        g_obs = []
        g_exp = []
        g_exp1 = []
        g_exp2 = []
        g_exp1u = []
        g_exp2u = []
        g_exp1d = []
        g_exp2d = []

        for i,sigwidth in enumerate(sigwidths):

            g_obs.append( TGraph() )
            g_exp.append( TGraph() )
            g_exp1u.append( TGraph() )
            g_exp2u.append( TGraph() )
            g_exp1d.append( TGraph() )
            g_exp2d.append( TGraph() )

            for j,sigmean in enumerate(sigmeans):

                if isMx:
                  alpha = config.alphaBins[alphaBin]
                  mY = round(sigmean / alpha / 10) * 10
                  if sigmean < 500:
                    continue
                  if mY < 3000:
                    continue
                  if mY > 10000:
                    continue
                else:
                  alpha = config.alphaBins[alphaBin]
                  if (sigmean * alpha) < 500:
                    continue
                  #print sigmean, mY, alpha

                rangelow = config.samples[channelNames[alphaBin]]["rangelow"]
                if sigmean < (rangelow + deltaMassAboveFit) :
                   continue

                # TODO need a better way of choosing a file. sometimes they don't get created, so making a second option.
                # Obviously this won't matter with real data, but it does for the tests
                tmp_path = paths[alphaBin]
                tmp_path = config.getFileName(paths[alphaBin], cdir, None, outdir + channelNames[alphaBin], sigmean, sigwidth, sigamp) + ".root"
                f = TFile(tmp_path, "READ")

                if f.IsZombie():
                    tmp_path = config.getFileName(paths[alphaBin], cdir, None, outdir + channelNames[alphaBin], sigmean, sigwidth, sigamp) + "_%s.root"%(ntoy)
                    f = TFile(tmp_path, "READ")
                    if f.IsZombie():
                      continue
                h = f.Get("limit")
                obs = h.GetBinContent(h.GetXaxis().FindBin("Observed")) / lumis
                exp = h.GetBinContent(h.GetXaxis().FindBin("Expected")) / lumis
                exp1u = h.GetBinContent(h.GetXaxis().FindBin("+1sigma")) / lumis
                exp2u = h.GetBinContent(h.GetXaxis().FindBin("+2sigma")) / lumis
                exp1d = h.GetBinContent(h.GetXaxis().FindBin("-1sigma")) / lumis
                exp2d = h.GetBinContent(h.GetXaxis().FindBin("-2sigma")) / lumis

                g_exp[i].SetPoint(g_exp[i].GetN(), sigmean, exp)
                g_exp1u[i].SetPoint(g_exp1u[i].GetN(), sigmean, exp1u)
                g_exp2u[i].SetPoint(g_exp2u[i].GetN(), sigmean, exp2u)
                g_exp1d[i].SetPoint(g_exp1d[i].GetN(), sigmean, exp1d)
                g_exp2d[i].SetPoint(g_exp2d[i].GetN(), sigmean, exp2d)

                if isnan(obs):
                    continue


                csuffix = ""
                if ntoy != None:
                  csuffix = "%s_%d"%(suffix, toy)
                postfitPath = config.getFileName(postfitPaths[alphaBin], cdir, channelNames[alphaBin], outdir + channelNames[alphaBin], sigmean, sigwidth, sigamp) + ".root"
                #chi2Hist = lf.read_histogram(postfitPath, "chi2"+channelName+"_"+csuffix)
                #chi2 = chi2Hist.GetBinContent(2)
                #pval = chi2Hist.GetBinContent(6)
                #if pval < 0.05:
                #  continue


                g_obs[i].SetPoint(g_obs[i].GetN(), sigmean, obs)
                #limits2D.SetPoint(limits2D.GetN(), sigmean, alphaBin, obs)
                limits2D.Fill(sigmean, alphaBins[alphaBin], obs)
                #print sigmean, alphaBins[alphaBin], exp


            #g_exp1.append( createFillBetweenGraphs(g_exp1d[-1], g_exp1u[-1]) )
            #g_exp2.append( createFillBetweenGraphs(g_exp2d[-1], g_exp2u[-1]) )

            #g_exp1[-1].SetFillColorAlpha(colors[i], 0.2)
            #g_exp2[-1].SetFillColorAlpha(colors[i], 0.2)
            #g_exp[-1].SetLineColor(colors[i])
            #g_exp[-1].SetLineStyle(2)
            #g_exp[-1].SetLineWidth(2)
            #g_obs[-1].SetLineWidth(2)
            #g_obs[-1].SetLineColor(colors[i])
            #g_obs[-1].SetMarkerColor(colors[i])

        g_obs_datasets.append(g_obs)
        g_exp_datasets.append(g_exp)
        g_exp1_datasets.append(g_exp1)
        g_exp2_datasets.append(g_exp2)
        g_exp1u_datasets.append(g_exp1u)
        g_exp2u_datasets.append(g_exp2u)
        g_exp1d_datasets.append(g_exp1d)
        g_exp2d_datasets.append(g_exp2d)

  
        leg_obs = TLegend(0.65,0.76,0.85,0.86)
        leg_exp = TLegend(0.65,0.6,0.85,0.7)
  
        minY = 0.00001
        maxY = 0.7
  
        '''
        g_exp_datasets[0][0].Draw("af")
        g_exp_datasets[0][0].GetXaxis().SetTitle("M_{G} [GeV]")
        g_exp_datasets[0][0].GetYaxis().SetTitle("#sigma #times #it{A} #times #it{BR} [pb]")
        g_exp_datasets[0][0].GetYaxis().SetTitleOffset(1.0)
        g_exp_datasets[0][0].GetHistogram().SetMinimum(minY)
        g_exp_datasets[0][0].GetHistogram().SetMaximum(maxY)
        g_exp_datasets[0][0].GetXaxis().SetLimits(min(sigmeans)-49.9, max(sigmeans)+49.9)
  
        c.Modified()
  
        for dataset in range(len(paths)):
          if dataset != len(paths)-1:

            l=TLine()
            l.DrawLineNDC(xToNDC(sigmeans[-1]), gPad.GetBottomMargin(), xToNDC(sigmeans[-1]), 0.72)

          g_exp2_datasets[dataset][0].Draw("f")
          g_exp1_datasets[dataset][0].Draw("f")

          for i,g in enumerate(g_exp_datasets[dataset]):
            g.Draw("l")
            if (dataset==0):
                leg_exp.AddEntry(g, "#sigma_{G}/M_{G} = %.2f" % (sigwidths[i]/100.), "l")
          for i,g in enumerate(g_obs_datasets[dataset]):
            g.Draw("pl")
            if (dataset==0):
                leg_obs.AddEntry(g, "#sigma_{G}/M_{G} = %.2f" % (sigwidths[i]/100.), "lp")


        ATLASLabel(0.20, 0.90, atlasLabel, 13)
        myText(0.20, 0.84, 1, "95% CL_{s} upper limits", 13)
        myText(0.2, 0.78, 1, "#sqrt{s}=13 TeV", 13)
        myText(0.2, 0.72, 1, "%.1f fb^{-1}" % (lumis*0.001), 13)
  
        myText(0.65, 0.92, 1, "Observed:", 13)
        myText(0.65, 0.76, 1, "Expected:", 13)
        leg_exp.Draw()
        leg_obs.Draw()

        c.Print("%s/limitPlot_swift_fivepar_%s.pdf"%(outdir, channelNames[alphaBin]))
        '''


    import MLBStyle
    ROOT.TColor.CreateGradientColorTable(256, # NRGBs
                                     MLBStyle.stops_array,
                                     MLBStyle.red_plasma_array,
                                     MLBStyle.green_plasma_array,
                                     MLBStyle.blue_plasma_array, # can also try 'inferno' and 'plasma'
                                     255);

    c = TCanvas("c1_%s"%(outdir), "c1", 800, 600)
    c.SetRightMargin(0.2)
    c.SetTopMargin(0.1)
    c.SetLogz()
    limits2D.GetZaxis().SetTitleOffset(1.2)
    limits2D.GetXaxis().SetLabelOffset(0.015)
    limits2D.Draw("COLZ")
    #df.draw_atlas_details(x_pos= 0.18,y_pos = 0.96, dy = 0.055, text_size = 0.05, sampleName="", atlasLabel = "Internal", lumi=140)
    df.draw_atlas_details(x_pos= 0.18,y_pos = 0.96, dy = 0.055, text_size = 0.05, sampleName="", atlasLabel = "Internal", lumi=140)
    lumi = 140
    sampleName = ""
    x_pos = 0.18
    y_pos = 0.91
    text_size = 20
    AS.myText(  x_pos, y_pos,1,text_size,"#sqrt{s} = 13 TeV, %.0f fb^{-1}  %s"%(lumi, sampleName))



    c.Print("%s/limits2D_%s_%d.pdf"%(outdir, signalfile, sigwidths[0]))


def main(args):
  paths = [ "jjj/Limits_sigPlusBkg_Fit_300_1200_Sig_MEAN_width_WIDTH_amp_1_3.root",]
  sigmeans  =  [ 550, 650]
  sigwidths =  [ 7, ]
  lumis = [ 29300 ]
  plotLimits(sigmeans=sigmeans, sigwidths=sigwidths, paths=paths, lumis=lumis, outdir="jjj")
  


if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
