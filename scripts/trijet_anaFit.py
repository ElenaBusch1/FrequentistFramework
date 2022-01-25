import scripts.config as config
import python.run_anaFit as run_anaFit
import os


# May want to loop over these at some point?
cdir = config.cdir
channelName="BkgLow_3_alpha0_SR1_tagged"
rangelow=300
rangehigh=1200

fitFunction = config.fitFunctions["fivePar"]["Config"]

nbkg="1E7,0,1E8"
topfile=config.samples[channelName]["topfile"]
categoryfile=config.samples[channelName]["categoryfile"]
dataFile=config.samples[channelName]["inputFile"]
datahist=config.samples[channelName]["histname"]

# Output file names, which will be written to outputdir
wsfile = config.getFileName("FitResult_1GeVBin_GlobalFit", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
outputfile = config.getFileName("FitResult_bkgonly", cdir + "/scripts/", channelName, rangelow, rangehigh) + ".root"
print wsfile, outputfile


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
           cdir=cdir ,
           wsfile=wsfile,
           nbkg=nbkg,
           outdir=outputdir,
           rangelow=rangelow,
           rangehigh=rangehigh,
           outputfile=outputfile,
           dosignal=dosignal,
           dolimit=dolimit,)


