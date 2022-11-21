import ROOT as r
import sys, re, os, math, argparse


def getVars(varFileName):
  varNames = []
  newNames = []
  fp = open(varFileName + ".txt")
  varNames = fp.readlines()
  for varName in range(len(varNames)):
    varNames[varName] = varNames[varName]. rstrip('\n')
    if(varNames[varName].find(" ")>0):
      newNames.append( (varNames[varName].split(" "))[1])
      varNames[varName] = (varNames[varName].split(" "))[0]
    else:
      newNames.append(varNames[varName])
      varNames.append(varNames[varName])

    while(newNames[varName].find("*")>0):
      #print newNames[varName]
      newNames[varName] = newNames[varName].replace("*", " ")

  return varNames, newNames


def getCrystalBallFunction(mY, alpha, inputFile, histName, syst):
  try:
    fp = open(inputFile)
  except:
    print  inputFile
    return 0,0

  inputFileLines = fp.readlines()
  muVals = []
  sigmaVals = []
  alphaVals = []
  nVals = []
  mYs = []

  #center of Gaussian will move along the parameter points
  w = r.RooWorkspace('w_%d_%.2f_%s'%(mY, alpha, inputFile))
  mu = w.factory('mu_%d_%.2f_%s[0,13000]'%(mY, alpha, inputFile)) #this is our continuous interpolation parameter
  pdfs = r.RooArgList()
  frame = None

  for line in inputFileLines:
    calpha = float(line.split(" ")[2])
    cmY = float(line.split(" ")[0])
    if alpha != calpha:
      continue

    muVal = float(line.split(" ")[4])
    sigmaVal = float(line.split(" ")[5])
    alphaVal = float(line.split(" ")[6])
    nVal = float(line.split(" ")[7])

    muVals.append(muVal)
    sigmaVals.append(sigmaVal)
    alphaVals.append(alphaVal)
    nVals.append(nVal)

    w.factory("RooCBShape::CBall{i}(x[0,11000], mu{i}[{cmu}, 0,13000], sigma{i}[{csig}, 100, 3000], alphaCB{i}[{calpha}, 0.1, 4.0], n{i}[{cn}, 100,1e11])".format(i=cmY, cmu = muVal, csig=sigmaVal, calpha=alphaVal, cn = nVal));
    pdf = w.pdf('CBall{i}'.format(i=cmY))
    pdfs.add(pdf)
    mYs.append(cmY)

    if not frame:
      x = w.var('x')
      frame = x.frame()


  paramVec = r.TVectorD(len(mYs))
  for i, cmY in enumerate(mYs):
    paramVec[i] = cmY

  if not frame:
    return None
  #ok, now construct the MomentMorph, can choose from these settings
  #  { Linear, NonLinear, NonLinearPosFractions, NonLinearLinFractions, SineLinear } ;
  setting = r.RooMomentMorph.Linear
  morph = r.RooMomentMorph('morph','morph',mu,r.RooArgList(x),pdfs, paramVec, setting)
  getattr(w,'import')(morph) # work around for morph = w.import(morph)

  ##make plots of interpolated pdf
  mu.setVal(mY) #offset from the original point a bit to see morphing
  histCB = morph.createHistogram("x", 11000, 0, 11000)
  histCB.SetName("%s_%d_%.2f_%s"%(histName, mY, alpha, syst))

  return histCB



def prepareCBTemplate(indir = "/afs/cern.ch/work/j/jroloff/nixon/signalMorphing/systs/", histName = "h2_resonance_jet_m4j_alpha", doSysts = True, mY = 6000, alpha = 5, outfile = "systematicsTest"):
  f_out = r.TFile("%s_%d_%.2f.root"%(outfile, mY, alpha), "RECREATE")
  f_out.cd()
  systs, _ = getVars("uncertaintySets/systematics")
  suffixes = ["_1up", "_1down"]
  if doSysts:
    for i, syst in enumerate(systs):
     for suffix in suffixes:
      inFile = "Syst_%s%s_h2_resonance_jet_m4j_alpha.txt"%(syst, suffix)
      histCB = getCrystalBallFunction(mY, alpha, indir+inFile, histName=histName, syst=syst + suffix)
      if not histCB:
        print indir+inFile, histName, syst
        continue
      f_out.cd()
      histCB.Write("%s_%s%s"%(histName, syst, suffix))
      

  print "Saving in fileName:", outfile
  f_out.Close()
  #inFile.Close()


