import math

def makeHepData(data, fit, histName = "test", labels = {}): 

  #xaxis = "$" + data.GetXaxis().GetTitle() + "$"
  #yaxis = "$" + data.GetYaxis().GetTitle() + "$"
  xaxis = data.GetXaxis().GetTitle() 
  yaxis = data.GetYaxis().GetTitle() 

  xaxis = xaxis.replace("[GeV]", "")
  xaxis = xaxis.replace("#", "\\")
  xaxis = xaxis.replace("{", "")
  #xaxis = xaxis.replace("{", "\{")
  xaxis = xaxis.replace("}", "")
  #xaxis = xaxis.replace("}", "\}")
  xaxis = xaxis.replace("#", "")
  xaxis = xaxis.replace(",", "")
  xaxis = xaxis.replace("_", " ")

  yaxis = yaxis.replace("#", "\\")
  yaxis = yaxis.replace("{", "")
  yaxis = yaxis.replace("}", "")
  yaxis = yaxis.replace("#", "")
  yaxis = yaxis.replace("_", " ")

  myfile = open ("%s.yaml"%(histName), "w");


  myfile.write("dependent_variables: \n")
  myfile.write("- header: {name: %s, units: none}\n"%(yaxis))
  myfile.write("  qualifiers: \n")
  myfile.write("  - {name: Number of Events, value: Observed} \n")
  myfile.write("  - {name: RE, value: P P to JET JET JET JET}\n")
  myfile.write("  - {name: SQRT(S), units: GEV, value: 13000} \n")
  myfile.write("  values: \n")
  for k in range(data.GetNbinsX()):
    myfile.write("    - {value: %.0f} \n"%(data.GetBinContent(k+1)))

  myfile.write("- header: {name: %s, units: none}\n"%(yaxis))
  myfile.write("  qualifiers: \n")
  myfile.write("  - {name: Number of Events, value: Fit} \n")
  myfile.write("  - {name: RE, value: P P to JET JET JET JET}\n")
  myfile.write("  - {name: SQRT(S), units: GEV, value: 13000} \n")
  myfile.write("  values: \n")
  for k in range(data.GetNbinsX()):
    myfile.write("    - value: %.4f \n"%(fit.GetBinContent(k+1)))
    #myfile.write("      errors:\n")
    #myfile.write("      - {symerror: %.3f}\n"%(math.sqrt(fit.GetBinContent(k+1))))

  myfile.write("independent_variables: \n")
  myfile.write("- header: {name: %s, units: none}\n"%(xaxis))
  myfile.write("  values: \n")

  for k in range(data.GetNbinsX()):
    myfile.write("  - {low: %.0f, high: %.3f}\n"%(data.GetBinLowEdge(k+1),  data.GetBinLowEdge(k+2)))


  myfile.close();

def makeLimitHepData(expecteds, observeds, expected1downs, expected1ups, expected2downs, expected2ups, legNames, histName = "test", labels = {}):

  xaxis = expecteds[0].GetXaxis().GetTitle();
  yaxis = expecteds[0].GetYaxis().GetTitle();

  xaxis = xaxis.replace("[GeV]", "")
  xaxis = xaxis.replace("#it", "")
  xaxis = xaxis.replace("{", "")
  xaxis = xaxis.replace("}", "")
  xaxis = xaxis.replace("#", "")
  xaxis = xaxis.replace(",", "")
  xaxis = xaxis.replace("_", " ")

  yaxis = yaxis.replace("#times", "*")
  yaxis = yaxis.replace("#it", "")
  yaxis = yaxis.replace("[pb]", "")
  yaxis = yaxis.replace("{", "")
  yaxis = yaxis.replace("}", "")
  yaxis = yaxis.replace("#", "")
  yaxis = yaxis.replace("_", " ")


  print "labels", xaxis, yaxis

  myfile = open ("%s.yaml"%(histName), "w");

  myfile.write("dependent_variables: \n")

  for expected, observed, expected1up, expected1down, expected2up, expected2down, legName in zip(expecteds, observeds, expected1ups, expected1downs, expected2ups, expected2downs, legNames):
    myfile.write("- header: {name: %s, units: pb}\n"%(yaxis))
    myfile.write("  qualifiers: \n")
    myfile.write("  - {name: Number of Events, value: Observed %s} \n"%(legName))
    myfile.write("  - {name: RE, value: P P to JET JET JET JET}\n")
    myfile.write("  - {name: SQRT(S), units: GEV, value: 13000} \n")
    myfile.write("  values: \n")
    for k in range(expected.GetN()):
      myfile.write("    - {value: %.8f} \n"%(observed.GetPointY(k)))

    myfile.write("- header: {name: %s, units: pb}\n"%(yaxis))
    myfile.write("  qualifiers: \n")
    myfile.write("  - {name: Number of Events, value: Fit %s} \n"%(legName))
    myfile.write("  - {name: RE, value: P P to JET JET JET JET}\n")
    myfile.write("  - {name: SQRT(S), units: GEV, value: 13000} \n")
    myfile.write("  values: \n")
    for k in range(expected.GetN()):
      myfile.write("    - value: %.8f \n"%(expected.GetPointY(k)))
      myfile.write("      errors:\n")
      myfile.write("      - {asymerror: {plus: %.8f, minus: -%.8f}, label: '1 sigma'} \n"%(abs(expected.GetPointY(k)-expected1up.GetPointY(k)), abs(expected.GetPointY(k)-expected1down.GetPointY(k))))
      myfile.write("      - {asymerror: {plus: %.8f, minus: -%.8f}, label: '2 sigma'} \n"%(abs(expected.GetPointY(k)-expected2up.GetPointY(k)), abs(expected.GetPointY(k)-expected2down.GetPointY(k))))

  myfile.write("independent_variables: \n")
  myfile.write("- header: {name: %s, units: GeV}\n"%(xaxis))
  myfile.write("  values: \n")

  for k in range(expected.GetN()):
    myfile.write("  - {value: %.0f}\n"%(expected.GetPointX(k)))


  myfile.close();


def make2DHepData(data, histName, labels = {}):
  xaxis = data.GetXaxis().GetTitle();
  yaxis = data.GetYaxis().GetTitle();

  xaxis = xaxis.replace("[GeV]", "")
  xaxis = xaxis.replace("{", "")
  xaxis = xaxis.replace("}", "")
  xaxis = xaxis.replace("#", "")
  xaxis = xaxis.replace(",", "")
  xaxis = xaxis.replace("_", " ")

  yaxis = yaxis.replace("{", "")
  yaxis = yaxis.replace("}", "")
  yaxis = yaxis.replace("#", "")
  yaxis = yaxis.replace("_", " ")


  myfile = open ("%s.yaml"%(histName), "w");

  myfile.write("independent_variables: \n")
  myfile.write("- header: {name: %s, units: none}\n"%(xaxis))
  myfile.write("  values: \n")
  for k in range(data.GetNbinsX()):
    for m in range(data.GetNbinsY()):
      myfile.write("  - {low: %.2f, high: %.2f}\n"%(data.GetXaxis().GetBinLowEdge(k+1), data.GetXaxis().GetBinLowEdge(k+2)))

  myfile.write("- header: {name: %s, units: none}\n"%(yaxis))
  myfile.write("  values: \n")
  for k in range(data.GetNbinsX()):
    for m in range(data.GetNbinsY()):
      myfile.write("  - {low: %.2f, high: %.2f}\n"%(data.GetYaxis().GetBinLowEdge(m+1), data.GetYaxis().GetBinLowEdge(m+2)))


  myfile.write("dependent_variables: \n")
  myfile.write("- header: {name: Uncertainty, units: none}\n")
  myfile.write("  qualifiers: \n")
  myfile.write("  - {name: RE, value: P P to JET JET JET JET}\n")
  myfile.write("  - {name: SQRT(S), units: GEV, value: 13000} \n")
  myfile.write("  values: \n")
  for k in range(data.GetNbinsX()):
    for m in range(data.GetNbinsY()):
      myfile.write("    - value: %.15f \n"%(data.GetBinContent(k+1, m+1)))

  myfile.close();



