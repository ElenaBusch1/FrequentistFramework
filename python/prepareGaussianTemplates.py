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


def getGaussianFunction(signalMass, inputFile, inputFileWidth, histName, syst, maxX = 1000, sigma=0.1, pruneThreshold = 0.1, jerPruneThreshold=0.1):
  if syst != "" and syst.find("JER") < 0 and (syst.find("JET") >= 0 or syst.find("Shower") >= 0 or syst.find("SHOWER") >= 0):
    try:
      fp = open(inputFile)
    except:
      print  inputFile
      print "broken"
      mygaus = r.TF1( 'mygaus_%s_%d_%s'%(syst, signalMass, histName), 'gaus', 0, maxX)
      mygaus.SetParameters(1.0, signalMass, signalMass*sigma)
      mygaus.SetNpx(maxX)
      mygaus.SetNpx(maxX)
      h_gausTmp = mygaus.CreateHistogram()
      return h_gausTmp,0,0

    inputFileLines = fp.readlines()
  elif syst.find("JER")>=0:
    fpWidth = open(inputFileWidth)
    widthLines = fpWidth.readlines()

  #center of Gaussian will move along the parameter points
  mygausUp = r.TF1( 'mygausUp_%s_%d_%s'%(syst, signalMass, histName), 'gaus', 0, maxX)
  mygausDown = r.TF1( 'mygausDown_%s_%d_%s'%(syst, signalMass, histName), 'gaus', 0, maxX)

  muValChangeUp_slope = 0
  muValChangeDown_slope = 0
  muValChangeUp_intercept = 0
  muValChangeDown_intercept = 0
  sigmaValChangeUp_slope = 0
  sigmaValChangeDown_slope = 0
  sigmaValChangeUp_intercept = 0
  sigmaValChangeDown_intercept = 0
  if syst.find("JER") < 0 and (syst.find("JET") >= 0 or syst.find("Shower") >= 0 or syst.find("SHOWER") >= 0):
      muValChangeUp_intercept = float(inputFileLines[0].split(" ")[0])
      muValChangeUp_slope = float(inputFileLines[0].split(" ")[1])
      muValUp = signalMass * (muValChangeUp_slope*signalMass + muValChangeUp_intercept + 1) + muValChangeUp_intercept
      

      muValChangeDown_intercept = float(inputFileLines[0].split(" ")[2])
      muValChangeDown_slope = float(inputFileLines[0].split(" ")[3])
      #muValChangeDown_slope = -1*max(abs(muValChangeDown_slope), abs(muValChangeUp_slope))
      muValDown =  signalMass * (muValChangeDown_slope*signalMass + muValChangeDown_intercept + 1) 
      print muValChangeDown_slope, muValChangeDown_intercept, muValChangeUp_slope,  muValChangeUp_intercept , muValUp, muValDown
  else:
      muValUp = signalMass
      muValDown = signalMass

  if syst.find("JER") >= 0:
      sigmaValChangeUp_intercept = float(widthLines[0].split(" ")[0])
      sigmaValChangeUp_slope = float(widthLines[0].split(" ")[1])
      sigmaValUp = signalMass * sigma * (sigmaValChangeUp_slope*signalMass*sigma + sigmaValChangeUp_intercept + 1)

      sigmaValChangeDown_intercept = float(widthLines[0].split(" ")[2])
      sigmaValChangeDown_slope = float(widthLines[0].split(" ")[3])
      sigmaValDown = signalMass * sigma * (sigmaValChangeDown_slope*signalMass*sigma + sigmaValChangeDown_intercept + 1)

  else:
      sigmaValUp = signalMass*sigma
      sigmaValDown = signalMass*sigma

  isPruned = True
  #if syst.find("JER") >=0 or abs(muValUp - signalMass)/signalMass >= pruneThreshold:
  #  isPruned = False

  if syst.find("JER") <0 and ( abs(muValUp - signalMass)/signalMass >= pruneThreshold or abs(muValDown - signalMass)/signalMass >= pruneThreshold):
    isPruned = False
  if syst.find("JER") >=0 and ( abs(sigmaValUp - sigma*signalMass)/(signalMass*sigma) >= jerPruneThreshold or abs(sigmaValDown - sigma*signalMass)/(sigma*signalMass) >= jerPruneThreshold):
    print "JERPrune", jerPruneThreshold, abs(sigmaValUp - sigma*signalMass)/(signalMass*sigma), abs(sigmaValDown - sigma*signalMass)/(sigma*signalMass)
    isPruned = False



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

  return h_gausUp, h_gausDown, isPruned


def prepareGaussianTemplate(indir = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/test/", histName = "h2_resonance_jet_m4j", doSysts = True, mY = 6000, outfile = "systematicsGaus", maxX=1000, sigma = 0.1, pruneThreshold = 0.1, systematicNameFile = "uncertaintySets/systematics.txt", jerPruneThreshold = 0.1, inputSystName = "uncertaintySets/systematics"):
  outfileName = "%s_%d.root"%(outfile, mY)
  print outfileName
  f_out = r.TFile(outfileName, "RECREATE")
  f_out.cd()
  systs, _ = getVars(inputSystName)
  inFile = "SystSlopes__.txt"
  inFileWidth = "SystSlopes_Width__.txt"
  histUp, histDown, isPruned = getGaussianFunction(mY, indir+inFile, indir+inFileWidth, histName=histName, syst="", maxX=maxX, sigma = sigma, pruneThreshold = pruneThreshold, jerPruneThreshold=jerPruneThreshold)
  systematicsFile = open(systematicNameFile,'w')
  if not histUp:
    print " did not find ", indir+inFile, histName+"_"
    return None
  f_out.cd()
  histUp.Scale(1./histUp.Integral())
  histUp.Write("%s_"%(histName))

  if doSysts:
    for i, syst in enumerate(systs):
      inFile = "SystSlopes_%s.txt"%(syst)
      inFileWidth = "SystSlopes_Width_%s.txt"%(syst)
      histUp, histDown, isPruned = getGaussianFunction(mY, indir+inFile, indir+inFileWidth, histName=histName, syst=syst, maxX=maxX, sigma = sigma, pruneThreshold = pruneThreshold, jerPruneThreshold=jerPruneThreshold)
      if isPruned:
        continue
      if not histUp:
        print " did not find ", indir+inFile, histName, syst
        continue
      f_out.cd()
      histUp.Scale(1./histUp.Integral())
      histDown.Scale(1./histDown.Integral())
      histUp.Write("%s_%s_1up"%(histName, syst))
      histDown.Write("%s_%s_1down"%(histName, syst))

      systematicsString = "%s %s \n"%(syst, syst)
      systematicsFile.write(systematicsString)


  print "Saving in fileName:", outfile
  f_out.Close()

  return outfileName


