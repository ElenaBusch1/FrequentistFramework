import scripts.config as config
import python.run_anaFit as run_anaFit
import os


# May want to loop over these at some point?
cdir = config.cdir
channelName="BkgLow_3_alpha0_SR1_tagged"
rangelow=300
rangehigh=1200


fitFunction="dijetISR/background_ajj_simpleTrig_yStar0p825_fivePar.xml"

nbkg="1E7,0,1E8"
topfile=config.samples[channelName]["topfile"]
categoryfile=config.samples[channelName]["categoryfile"]
dataFile=config.samples[channelName]["inputFile"]
datahist=config.samples[channelName]["histname"]

# Output file names, which will be written to outputdir
wsfile="FitResult_" + channelName + "_1GeVBin_GlobalFit_%dto_%d_0.root"%(rangelow, rangehigh)
outputfile="FitResult_" + channelName + "_bkgonly_range_%d_%d.root"%(rangelow, rangehigh)


dosignal=0
dolimit=0

outputdir = channelName
if not os.path.exists(outputdir):
        os.makedirs(outputdir)


run_anaFit.run_anaFit(
           datafile=dataFile, 
           datahist=datahist,
           categoryfile=categoryfile,
           topfile=topfile,
           fitFunction=fitFunction,
           cdir=cdir,
           wsfile=outputdir+"/" + wsfile,
           nbkg=nbkg,
           rangelow=rangelow,
           rangehigh=rangehigh,
           outputfile=outputdir+"/" + outputfile,
           dosignal=dosignal,
           dolimit=dolimit,)


