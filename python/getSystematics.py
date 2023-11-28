def get2DSystematic(systName, mY, alpha, inputFile):
  par0 = 0
  par1 = 0
  par2 = 0
  isFound = 0
  for line in inputFileLines:
    if line.find(systName) >= 0:
      par0 = line.split(" ")[1]
      par1 = line.split(" ")[2]
      par2 = line.split(" ")[3]
      isFound = 1
      break
  if not isFound:
    print("didn't find the systematic!!!!!")
    return 0

  systSize = par0 + mY * par1 + alpha * par2
  return systSize

def getEffSystematic(systName, mY, inputFile):
  #print "testing efficiency", inputFile
  try:
    fp = open(inputFile)
  except:
    print inputFile
    print "Did not find systematic!!!!"
    return 0,0

  inputFileLines = fp.readlines()

  for line in inputFileLines:
      splitLine = line.split(" ")
      parUpIntercept = float(splitLine[0])
      parUpSlope = float(splitLine[1])
      parDownIntercept = float(splitLine[2])
      parDownSlope = float(splitLine[3])
      parUp = parUpIntercept + parUpSlope*mY
      parDown = parDownIntercept + parDownSlope*mY
      #print  inputFile, systName, parUp, parDown
      break

  return float(parUp), float(parDown)



def getSystematic(systName, mY, alpha, inputFile):
  par0 = 0
  par1 = 0
  par2 = 0
  isFound = 0
  try:
    fp = open(inputFile + ".txt")
  except:
    return 0,0

  #print inputFile + ".txt"
  inputFileLines = fp.readlines()

  for line in inputFileLines:
    if line.find(systName) >= 0:
      parUp = line.split(" ")[1]
      parDown = line.split(" ")[2]
      isFound = 1
      break
  if not isFound:
    print("didn't find the systematic!!!!!", systName)
    return 0

  #systSize = par0 + mY * par1 + alpha * par2
  return float(parUp), float(parDown)


def getVars(varFileName):
  varNames = []
  newNames = []
  try:
    fp = open(varFileName )
  except:
    return varNames, newNames
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

def writeSystematics(systNames, mY, inputFile):

  systString = ""
  #systList,_ = getVars(systNames) 
  systList,_ = getVars(inputFile)
  print systList, inputFile
  for systName in systList:

    #print "running syst ", systName
    #systUp, systDown = getSystematic(systName, mY, alpha, inputFile)
    #systString = systString + "<Systematic Name='%s' Constr='asym' CentralValue='1' Mag='%.4f,%.4f' WhereTo='shape'/>\n"%(systName, systDown, systUp)
    #systString = systString + "<ExtSyst ConstrName='%s__1Constraint' NPName='%s__1' GOName='nom_%s__1' />\n"%(systName, systName, systName)
    #systString = systString + "<ExtSyst ConstrName='%sConstraint' NPName='%s' GOName='nom_%s' />\n"%(systName, systName, systName)
    systString = systString + "<ExtSyst ConstrName='alpha_%sConstraint' NPName='alpha_%s' GOName='nom_alpha_%s' />\n"%(systName, systName, systName)

  print systList, systString, systNames, inputFile
  return systString


def writeEfficiencySystematics(systNames, mY, inputFile, inDir = "/afs/cern.ch/work/j/jroloff/dijetPlusISR/adversarialNN/test"):

  systList,_ = getVars(inputFile)
  #print systList, inputFile

  # Adding the PDF uncertainty by hand
  systString = "<Systematic Name='alpha_PDF_eff' Constr='asym' CentralValue='1.0' Mag='0.013,0.013' WhereTo='yield'/> \n"
  #return systString
  for systName in systList:

    inputFile = "%s/SystEff_%s.txt"%(inDir, systName)
    systUp, systDown = getEffSystematic(systName, mY, inputFile)
    print "running syst ", systName, systUp, systDown
    
    #if systUp != 0 and systDown != 0:
    #  if abs(systUp)/systUp < 0 and abs(systDown)/systDown < 0:
    #    print "Oh NOOOOOOOOOOOOOOOOO", systUp, systDown
    #  if abs(systUp)/systUp > 0 and abs(systDown)/systDown > 0:
    #    print "Oh NOOOOOOOOOOOOOOOOO", systUp, systDown
    #if abs(systUp) > 0.004 or abs(systDown) > 0.004:
    #if abs(systUp) > 0.003 or abs(systDown) > 0.003:
    #if abs(systUp) > 0.002 or abs(systDown) > 0.002:
    #if abs(systUp) > 0.001 or abs(systDown) > 0.001:
    if abs(systUp) > 0.008 or abs(systDown) > 0.008:
    #if abs(systUp) > 0.006 or abs(systDown) > 0.006:
      systString = systString + "    <Systematic Name='alpha_%s_eff' Constr='asym' CentralValue='1.0' Mag='%s,%s' WhereTo='yield'/> \n"%(systName, systUp, systDown)
      #systString = systString + "<Systematic Name='alpha_%s' Constr='asym' CentralValue='1.0' Mag='%s,%s' WhereTo='yield'/> \n"%(systName, systUp, systDown)

  print systList, systString, systNames, inputFile
  return systString


def getCrystalBallParameters(mY, alpha, inputFile):
  try:
    fp = open(inputFile + ".txt")
  except:
    return 0,0

  inputFileLines = fp.readlines()
  muVals = []
  sigmaVals = []
  alphaVals = []
  nVals = []
  mYs = []

  #center of Gaussian will move along the parameter points
  mu = w.factory('mu[0,13000]') #this is our continuous interpolation parameter
  sigma = w.factory('sigma[100, 3000]')
  alphaCB = w.factory('alpha[0.1, 4.0]')
  n = w.factory('n[100,1e10]')
  pdfs = r.RooArgList()

  for line in inputFileLines:
    calpha = float(line.split(" ")[2])
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

    w = r.RooWorkspace('w_%d'%(count))
    w.factory("RooCBShape::CBall{i}(x[0,11000], mu{i}[{cmu}, 0,13000], sigma{i}[{csig}, 100, 3000], alphaCB{i}[{calpha}, 0.1, 4.0], n{i}[{cn}, 100,1e11])".format(i=mY, cmu = muVal, csig=sigmaVal, calpha=alphaVal, cn = nVal));

  paramVec = r.TVectorD(len(mYs))

  #ok, now construct the MomentMorph, can choose from these settings
  #  { Linear, NonLinear, NonLinearPosFractions, NonLinearLinFractions, SineLinear } ;
  setting = r.RooMomentMorph.Linear
  morph = r.RooMomentMorph('morph','morph',mu,r.RooArgList(x),pdfs, paramVec,setting)
  getattr(w,'import')(morph) # work around for morph = w.import(morph)

  ##make plots of interpolated pdf
  mu.setVal(mY) #offset from the original point a bit to see morphing
  sigma.setVal(mY) #offset from the original point a bit to see morphing
  alphaVal.setVal(mY) #offset from the original point a bit to see morphing
  n.setVal(mY) #offset from the original point a bit to see morphing
  return mu.getValV(), sigma.getValV(), alphaVal.getValV(), n.getValV()








