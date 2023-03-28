import ROOT
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


def generateSignalWS(infile, histName, doSysts, outfile = ""):
  ROOT.RooMsgService.instance().setGlobalKillBelow(ROOT.RooFit.WARNING)

  meas = ROOT.RooStats.HistFactory.Measurement("meas", "meas")
  meas.SetExportOnly( False )    # True omits plots and tables from output file
 
  meas.SetOutputFilePrefix( outfile.replace(".root","") )
  # meas.SetPOI( "nsig" )

  meas.SetLumi(1.0)

  chan = ROOT.RooStats.HistFactory.Channel( histName )

  # Retrieve names from rootfile:
  inFile = ROOT.TFile(infile, "READ")

  # for some mass points there are morphed and original templates: pick up original ones.
  systs, _ = getVars("uncertaintySets/systematics")

  signal = ROOT.RooStats.HistFactory.Sample("signal", histName, infile)
  signal.SetNormalizeByTheory(False) #no lumi unc on this

  # TODO: test including stat uncertainties!
  # background.ActivateStatError( "background1_statUncert", InputFile )
  if doSysts:
    for syst in systs:
      print histName, syst
      signal.AddHistoSys(syst, histName +syst+"_1down", infile, "", histName + syst+"_1up", infile, "")
      #signal.AddHistoSys(syst, histName +syst+"down", infile, "", histName + syst+"up", infile, "")

  chan.AddSample( signal )
  # Done with this channel
  # Add it to the measurement:
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

