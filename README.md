# FrequentistFramework

This code is very preliminary and under construction, and its documentation is a work in progress. 

This is a frequentist statistical analysis framework based on:
https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/XmlAnaWSBuilder

# Install - follow the README Of the XmlAnaWSBuilder
```
setupATLAS
lsetup git
git clone https://:@gitlab.cern.ch:8443/atlas-phys-exotics-dijet-tla/FrequentistFramework.git
cd FrequentistFramework/
git submodule init
git submodule update --remote
cd xmlAnaWSBuilder/
source setup_lxplus.sh
sh scripts/install_roofitext.sh
mkdir build && cd build
cmake ..
make -j4
cd ../quickFit/
source setup_lxplus.sh
export RooFitExtensions_DIR=../xmlAnaWSBuilder/RooFitExtensions/
mkdir build && cd build
cmake ..
make -j4
cd ../..
```
# Setup

In the future you can setup your environment via
```
source scripts/setup_buildAndFit.sh
```

# Run

Example run command:
```
./xmlAnaWSBuilder/exe/XMLReader -x config/dijetTLA/dijetTLA_J75yStar03.xml -s 0 --plotOption logy
```
This command will make a RooWorkspace starting J75-triggered data from https://arxiv.org/abs/1804.03496, fitted with the five parameter background function. It will also generate a summary PDF with the fit result.

# Scripts

The directory _python/_ contains a number of standalone Python scripts to plot and extracts the information from the workspace. Test files and .pdf files of how the output should look like are provided in each of the directories. 

   * _PlotWorkspace/PlotWorkspaceFit.py_ plots the fit and the data in the workspace (obtained from the command above) together with its residuals and pulls, and overlays it with the fit result from the previous statistical analysis framework. 

# quickFit and quickLimit

The output of the xmlAnaWSBuilder can be used as input for both quickFit and quickLimit to test signal hypotheses. The example from above produced the workspace _workspace/dijetTLA/dijetTLA_J75yStar03.root_ that contains a number of potential Gauss signals whose yields can be fit with quickFit. First, you can run a background-only fit with:
```
quickFit -f workspace/dijetTLA/dijetTLA_J75yStar03.root -d combData --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 -o run/FitResult.root
```
It can happen that quickFit claims "STATUS FAILED" for the fit, the lines above the final fit parameters will tell you the reason. Often it says:
```
Full matrix, but forced positive-definite
```
This usually means that a maximum in the likelihood could be found but that is not unique. E.g. two parameters can be varied leading to more or less the same post fit distribution. We choose to ignore this for now. 

To perform a signal+background fit (e.g. for a Gauss signal at 700 GeV with 7% width) run:
```
quickFit -f workspace/dijetTLA/dijetTLA_J75yStar03.root -d combData -p nsig_mean700_width7 --checkWS 1 --hesse 1 --savefitresult 1 --saveWS 1 --saveNP 1 --saveErrors 1 -o run/FitResult.root
```
quickFit will now treat the parameter _nsig_mean700_width7_ as floating POI in the fit while still keeping all others fixed to 0. The parameter specified here needs to exist in the RooStats workspace, meaninf it needs to be defined by a custom signal .xml card in the xmlAnaWSBuilder.

If quickFit succeeds (or only fails because of forced positive-definite matrix) you can run quickLimit to set 95% CLs limits on your chosen parameter:
```
quickLimit -f workspace/dijetTLA/dijetTLA_J75yStar03.root -d combData -p nsig_mean700_width7 --checkWS 1 --hesse 1 --initialGuess 10000 -o run/Limits.root
```
With _initialGuess_ you need to specify the order of magnitude that you expect your limit to have. The default of 1 might be too small to achieve a difference between likelihoods larger than machine precision.

#Automation

All of this is performed in the bash scripts _scripts/run_buildAndFit_swift_ and _scripts/run_buildAndFit_nlofit_. In there you can specify your _datafile_, _datahist_, _sigmean_ and _sigwidth_ (or set them as env variables before executing). It then uses generic copies of the xmlAnaWsBuilder .xml config files labeled as .template files which you can specify with the _topfile_ and _categoryfile_ variables. They are virtually identically but contain strings like DATAHIST instead of definite entries. These are then replaced in the run script with whatever you provided before executing the xmlAnaWSBuilder. For the analytic window fit also the range and bin count of the fit will be passed on by the run script, as specified by your windowhalfwidth _whw_ and the binning in which to apply it _binedges_.

If you produced many limits for different signal points, they can be summarized in a limit plot with _python/plotLimits.py_ that you will have to adapt to your paths, lumi, mass ranges etc.
