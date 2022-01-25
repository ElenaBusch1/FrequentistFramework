import scripts.config as config
import python.run_injections_anaFit as run_injections_anaFit
import python.generatePseudoData as generatePseudoData
import os

#. scripts/setup_buildAndFit.sh
dosignal=1
dolimit=0

fitFunction="dijetISR/background_ajj_simpleTrig_yStar0p825_fourPar.xml"

cdir = config.cdir
sigmean=550
sigwidth=7
sigamp=1
rangelow=300
rangehigh=1200
nbkg="1E7,0,1E8"
channelName="BkgLow_3_alpha0_SR1_tagged"
topfile=config.samples[channelName]["topfile"]
categoryfile=config.samples[channelName]["categoryfile"]
dataFile=config.samples[channelName]["inputFile"]



# Output file names, which will be written to outputdir
wsfile="FitResult_" + channelName + "_sigPlusBkg_1GeVBin_GlobalFit_%dto_%d_0.root"%(rangelow, rangehigh)
outputfile="FitResult_" + channelName + "_sigPlusBkg_range_%d_%d_sig_%d_width_%d_amp_%d.root"%(rangelow, rangehigh, sigmean, sigwidth, sigamp)
binedges=[300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200]

# Number of toys
loopstart=0
loopend=20

outputdir = channelName
if not os.path.exists(outputdir):
        os.makedirs(outputdir)

# First make the pseudodata
# TODO: maybe make a flag to decide whether to run this?
pdInputFile = "%s/PostFit_%s_bkgonly_range_%d_%d.root"%(outputdir, channelName, rangelow, rangehigh)
pdFile = "%s/PD_fivePar_bkgonly_range_%d_%d.root"%(outputdir,rangelow, rangehigh)
pdHistName = "pseudodata"
generatePseudoData.generatePseudoData( infile=pdInputFile, inhist ="postfit", nreplicas=loopend, scaling=1,outfile=pdFile, outhist=pdHistName)

# Then run the injection
run_injections_anaFit.run_injections_anaFit(
           datafile=pdFile, 
           datahist=pdHistName,
           categoryfile=categoryfile,
           topfile=topfile,
           fitFunction=fitFunction,
           cdir=cdir,
           wsfile=outputdir+"/" + wsfile,
           sigmean=sigmean,
           sigwidth=sigwidth,
           sigamp=sigamp,
           nbkg=nbkg,
           rangelow=rangelow,
           rangehigh=rangehigh,
           outputfile=outputdir+"/" + outputfile,
           dosignal = dosignal,
           dolimit = dolimit,
           loopstart=loopstart,
           loopend=loopend-1,
           rebinedges=binedges,
           rebinfile=None,
           rebinhist=None,
           maskthreshold=0.01,
          )





