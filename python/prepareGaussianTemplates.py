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
      newNames[varName] = newNames[varName].replace("*", " ")

  return varNames, newNames


def getGaussianFunction(signalMass, alpha, inputFile, inputFileWidth, histName, syst, maxX = 11000, sigma=0.1):
  #if syst!= "" and syst.find("JER") < 0 and syst.find("JET") >= 0:
  if syst != "" and syst.find("JER") < 0 and (syst.find("JET") >= 0 or syst.find("Shower") >= 0 or syst.find("SHOWER") >= 0):
    try:
      fp = open(inputFile)
    except:
      print  inputFile
      print "broken"
      return 0,0
    inputFileLines = fp.readlines()
  if syst.find("JER")>=0:
    fpWidth = open(inputFileWidth)
    widthLines = fpWidth.readlines()


  #center of Gaussian will move along the parameter points
  mygausUp = r.TF1( 'mygausUp_%s_%d_%s'%(syst, signalMass, histName), 'gaus', 0, maxX)
  mygausDown = r.TF1( 'mygausDown_%s_%d_%s'%(syst, signalMass, histName), 'gaus', 0, maxX)

  #print syst, syst.find("JER"), syst.find("JET")
  if syst.find("JER") < 0 and (syst.find("JET") >= 0 or syst.find("Shower") >= 0 or syst.find("SHOWER") >= 0):
      muValChangeUp_intercept = float(inputFileLines[0].split(" ")[0])/100.
      muValChangeUp_slope = float(inputFileLines[0].split(" ")[1])/100.
      muValUp = signalMass * (muValChangeUp_slope*signalMass + muValChangeUp_intercept + 1) + muValChangeUp_intercept
      print syst, muValChangeUp_intercept

      muValChangeDown_intercept = float(inputFileLines[0].split(" ")[2])/100.
      muValChangeDown_slope = float(inputFileLines[0].split(" ")[3])/100.
      muValDown =  signalMass * (muValChangeDown_slope*signalMass + muValChangeDown_intercept + 1) 
  else:
      muValUp = signalMass
      muValDown = signalMass


  if syst.find("JER") >= 0:
      sigmaValChangeUp_intercept = float(widthLines[0].split(" ")[0])/100.
      sigmaValChangeUp_slope = float(widthLines[0].split(" ")[1])/100.
      sigmaValUp = signalMass * sigma * (sigmaValChangeUp_slope*signalMass*sigma + sigmaValChangeUp_intercept + 1)

      sigmaValChangeDown_intercept = float(widthLines[0].split(" ")[2])/100.
      sigmaValChangeDown_slope = float(widthLines[0].split(" ")[3])/100.
      sigmaValDown = signalMass * sigma * (sigmaValChangeDown_slope*signalMass*sigma + sigmaValChangeDown_intercept + 1)

  else:
      sigmaValUp = signalMass*sigma
      sigmaValDown = signalMass*sigma


  mygausUp.SetParameters(1.0, muValUp, sigmaValUp)
  mygausDown.SetParameters(1.0, muValDown, sigmaValDown)
  mygausUp.SetNpx(maxX)
  mygausDown.SetNpx(maxX)
  h_gausUpTmp = mygausUp.CreateHistogram()
  h_gausDownTmp = mygausDown.CreateHistogram()
  h_gausUp = h_gausUpTmp.Clone("testUp")
  h_gausDown = h_gausDownTmp.Clone("testDown")
  h_gausUp.SetDirectory(0)
  h_gausDown.SetDirectory(0)


  return h_gausUp, h_gausDown



def prepareGaussianTemplate(indir = "/afs/cern.ch/work/j/jroloff/nixon/systematics/", histName = "h2_resonance_jet_m4j_alpha", doSysts = True, mY = 6000, alpha = 5, outfile = "systematicsGaus", maxX=11000, sigma = 0.1):
  outfileName = "%s_%d_%.2f.root"%(outfile, mY, alpha)
  f_out = r.TFile(outfileName, "RECREATE")
  f_out.cd()
  systs, _ = getVars("uncertaintySets/systematics")
  inFile = "SystSlopes_%s___alphaBin_%d.txt"%(histName, alpha)
  inFileWidth = "SystSlopes_Width_%s___alphaBin_%d.txt"%(histName, alpha)
  histUp, histDown = getGaussianFunction(mY, alpha, indir+inFile, indir+inFileWidth, histName=histName, syst="", maxX=maxX, sigma = sigma)
  if not histUp:
    print " did not find ", indir+inFile, histName+"_"
    return None
  f_out.cd()
  histUp.Write("%s_"%(histName))

  if doSysts:
    for i, syst in enumerate(systs):
      inFile = "SystSlopes_%s_%s_alphaBin_%d.txt"%(histName, syst, alpha)
      inFileWidth = "SystSlopes_Width_%s_%s_alphaBin_%d.txt"%(histName, syst, alpha)
      histUp, histDown = getGaussianFunction(mY, alpha, indir+inFile, indir+inFileWidth, histName=histName, syst=syst, maxX=maxX, sigma = sigma)
      if not histUp:
        print " did not find ", indir+inFile, histName, syst
        continue
      f_out.cd()
      histUp.Write("%s_%s_1up"%(histName, syst))
      histDown.Write("%s_%s_1down"%(histName, syst))


  print "Saving in fileName:", outfile
  f_out.Close()

  return outfileName


