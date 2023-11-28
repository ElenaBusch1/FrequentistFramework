import ROOT
import sys, re, os, math, argparse


#def getGaussianFunction(signalMass, inputFile, inputFileWidth, syst, sigma=0.1, pruneThreshold = 0.1, jerPruneThreshold = 0.01):
def getGaussianFunction(signalMass, inputFile, inputFileWidth, syst, sigma=0.1, pruneThreshold = 0.1, jerPruneThreshold = 0.01):
  if syst != "" and syst.find("JER") < 0 and (syst.find("JET") >= 0 or syst.find("Shower") >= 0 or syst.find("SHOWER") >= 0):
    try:
      fp = open(inputFile)
    except:
      print  inputFile
      print "broken"
      return 0

    inputFileLines = fp.readlines()
  elif syst.find("JER")>=0:
    fpWidth = open(inputFileWidth)
    widthLines = fpWidth.readlines()

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
      muValUp = signalMass * (muValChangeUp_slope*signalMass + muValChangeUp_intercept + 1) 

      muValChangeDown_intercept = float(inputFileLines[0].split(" ")[2])
      muValChangeDown_slope = float(inputFileLines[0].split(" ")[3])
      muValDown =  signalMass * (muValChangeDown_slope*signalMass + muValChangeDown_intercept + 1)
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
  print "testsigma", inputFile, inputFileWidth, abs(muValUp - signalMass)/signalMass , abs(muValDown - signalMass)/signalMass, muValUp, signalMass
  if syst.find("JER") >=0 :
    print "testsigma", inputFile, inputFileWidth, sigmaValUp, sigma, sigma*signalMass, abs(sigmaValUp - sigma*signalMass)/(signalMass*sigma)

  if syst.find("JER") <0 and ( abs(muValUp - signalMass)/signalMass >= pruneThreshold or abs(muValDown - signalMass)/signalMass >= pruneThreshold):
    isPruned = False
  if syst.find("JER") >=0 and ( abs(sigmaValUp - sigma*signalMass)/(signalMass*sigma) >= jerPruneThreshold or abs(sigmaValDown - sigma*signalMass)/(sigma*signalMass) >= jerPruneThreshold):
    print "JERPrune", jerPruneThreshold, abs(sigmaValUp - sigma*signalMass)/(signalMass*sigma), abs(sigmaValDown - sigma*signalMass)/(sigma*signalMass)
    isPruned = False

  return isPruned

def prepareGaussianTemplate(indir, mY, sigma , pruneThreshold , jerPruneThreshold , systematicNameFile, inputSystName ):

  systs, _ = getVars(inputSystName)
  systematicsFile = open(systematicNameFile,'w')
  print systematicsFile
  for i, syst in enumerate(systs):
      inFile = "SystSlopes_%s.txt"%(syst)
      inFileWidth = "SystSlopes_Width_%s.txt"%(syst)
      isPruned = getGaussianFunction(mY, indir+inFile, indir+inFileWidth, syst=syst, sigma = sigma, pruneThreshold = pruneThreshold, jerPruneThreshold = jerPruneThreshold)
      if isPruned:
        continue
      systematicsString = "%s %s \n"%(syst, syst)
      systematicsFile.write(systematicsString)


def getVars(varFileName):
  varNames = []
  newNames = []
  fp = open(varFileName)
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


def generateSignalWS(infile, histName, doSysts, outfile = "", systematicNameFile = "uncertaintySets/systematics.txt", suffix = "_", mY = 250, pruneThreshold = 0.003, jerPruneThreshold = 5, indirSysts = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/test/", inputSystName =  "uncertaintySets/systematics.txt"):
  print infile, histName

  if doSysts:
    prepareGaussianTemplate(indir = indirSysts, mY = mY, sigma = 0.1, pruneThreshold = pruneThreshold, jerPruneThreshold = jerPruneThreshold, systematicNameFile = systematicNameFile, inputSystName = inputSystName)

  ROOT.RooMsgService.instance().setGlobalKillBelow(ROOT.RooFit.WARNING)

  meas = ROOT.RooStats.HistFactory.Measurement("meas", "meas")
  meas.SetExportOnly( False )    # True omits plots and tables from output file
 
  meas.SetOutputFilePrefix( outfile.replace(".root","") )
  meas.SetLumi(1.0)
  chan = ROOT.RooStats.HistFactory.Channel( histName )

  # Retrieve names from rootfile:
  inFile = ROOT.TFile(infile, "READ")

  # for some mass points there are morphed and original templates: pick up original ones.
  systs, _ = getVars(systematicNameFile)

  signal = ROOT.RooStats.HistFactory.Sample("signal", histName, infile)
  signal.SetNormalizeByTheory(False) #no lumi unc on this

  # TODO: test including stat uncertainties!
  # background.ActivateStatError( "background1_statUncert", InputFile )
  if doSysts:
    for syst in systs:
      print histName, syst
      signal.AddHistoSys(syst, histName +syst+"%s1down"%(suffix), infile, "", histName + syst+"%s1up"%(suffix), infile, "")

  chan.AddSample( signal )
  meas.AddChannel( chan )

  # Collect the histograms from their files,
  # print some output, 
  meas.CollectHistograms()
  meas.PrintTree();

  # Now, do the measurement
  hist2workspace = ROOT.RooStats.HistFactory.HistoToWorkspaceFactoryFast( meas )
  ws = hist2workspace.MakeCombinedModel( meas )

  ws.Print("all")

  print "Saving in fileName:", outfile
  f_out = ROOT.TFile(outfile, "RECREATE")
  f_out.cd()
  ws.Write()
  f_out.Close()
  inFile.Close()

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('--infile', dest='infile', type=str, default='', help='Input file name')
  parser.add_argument('--histName', dest='histName', type=str, default='', help='Input file name')
  parser.add_argument('--outfile', dest='outfile', type=str, default='', help='Output file name')
  parser.add_argument('--doSysts', dest='doSysts', type=int, default=0, help='mass point')
  args = parser.parse_args()
  
  generateSignalWS(infile=args.infile, histName=args.histName, doSysts=args.doSysts, outfile = args.outfile)

