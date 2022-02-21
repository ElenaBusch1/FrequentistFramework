import ROOT
import sys, re, os, math, argparse

def generateSignalWS():
  ROOT.RooMsgService.instance().setGlobalKillBelow(ROOT.RooFit.WARNING)

  meas = ROOT.RooStats.HistFactory.Measurement("meas", "meas")
  meas.SetExportOnly( False )    # True omits plots and tables from output file
 
  if args.outfile =='':
    fileName = args.infile.split("/")[-1].replace(".root","_mR{0}_histFactoryWS.root").format(args.mass)
  else:
    fileName = args.outfile

  meas.SetOutputFilePrefix( fileName.replace(".root","") )
  # meas.SetPOI( "nsig" )

  meas.SetLumi(1.0)
  # meas.SetLumiRelErr(0)

  chan = ROOT.RooStats.HistFactory.Channel( "SigLow_1_alpha200_SR1" )

  # Retrieve names from rootfile:
  inFile = ROOT.TFile(args.infile, "READ")

  # for some mass points there are morphed and original templates: pick up original ones.
  nominalName = "SigLow_1_alpha200_SR1"
 
  # nominal = ROOT.RooStats.HistFactory.Sample( "nominal", "nominal", args.infile )
  # TODO: test including stat uncertainties!
  # background.ActivateStatError( "background1_statUncert", InputFile )
  signal = ROOT.RooStats.HistFactory.Sample("signal", nominalName, args.infile)
  signal.SetNormalizeByTheory(False) #no lumi unc on this
 
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

  print "Saving in fileName:", fileName
  f_out = ROOT.TFile(fileName, "RECREATE")
  f_out.cd()
  ws.Write()
  f_out.Close()
  inFile.Close()

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('--infile', dest='infile', type=str, default='', help='Input file name')
  parser.add_argument('--outfile', dest='outfile', type=str, default='', help='Output file name')
  parser.add_argument('--mass', dest='mass', type=str, default='', help='mass point')
  args = parser.parse_args()
  
  generateSignalWS()

