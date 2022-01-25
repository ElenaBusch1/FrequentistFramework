import scripts.config as config
import python.createExtractionGraphs as createExtractionGraphs
import python.plotLimits_jjj as plotLimits_jjj
import python.getChi2Distribution as getChi2Distribution




infileExtraction='jjj/FitResult_sigPlusBkg_Fit_300_1200_Sig_MEAN_width_WIDTH_amp_AMP_*.root'
infilePD='run/PD_swift_fivePar_bkgonly_range_300_1200_injected_meanMEAN_widthWIDTH_ampAMP.root'
outfileExtraction='run/PD_swift_fivePar_bkgonly_range_300_1200_injected_meanMEAN_widthWIDTH_ampAMP.root'
sigmeans=[ 550]
sigwidths=[ 7 ]
sigamps=[1, 5, 10 ]
lumis = [ 29300 ]



createExtractionGraphs.createExtractionGraphs(sigmeans=sigmeans, sigwidths=sigwidths, sigamps=sigamps, infile=infileExtraction, infilePD=infilePD, outfile=outfileExtraction)

pathsLimits = [ config.cdir+"/run/jjj/Limits_sigPlusBkg_Fit_300_1200_Sig_MEAN_width_WIDTH_amp_1_3.root",]
plotLimits_jjj.plotLmits(sigmeans=sigmeans, sigwidths=sigwidths, paths=pathsLimits, lumis=lumis, outdir="jjj")


infilesChi2 = [config.cdir+"/run/jjj/PostFit_sigPlusBkg_Fit_300_1200_Sig_550_width_7_amp_0_10.root", config.cdir+"/run/jjj/PostFit_sigPlusBkg_Fit_300_1200_Sig_550_width_7_amp_0_9.root", config.cdir+"/run/jjj/PostFit_sigPlusBkg_Fit_300_1200_Sig_550_width_7_amp_0_8.root"]
inhistChi2="chi2"
outfileChi2="chi2.root"
outhistChi2="chi2"
getChi2Distribution.getChi2Distribution.py(infiles=infilesChi2, inhist=inhistChi2, outfile=outfileChi2, outhist=outhistChi2)



