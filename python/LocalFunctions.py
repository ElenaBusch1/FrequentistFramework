import ROOT as r

def open_file(file_name, option="READ" ):
  try:
    f = r.TFile(file_name,option)
    if not f.IsOpen():
        return None
    return f
  except:
    return None

def read_histogram(fileName, histName):
    myfile = open_file(fileName)
    if myfile==None:
        return None
    hist = myfile.Get(histName)
    if not isinstance(hist,r.TH1F):
      if not isinstance(hist,r.TH1D):
        #print "Did not find ", histName, " in ", fileName
        return None
    hist.SetDirectory(0)
    myfile.Close()
    return hist

