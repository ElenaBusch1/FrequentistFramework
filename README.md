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

# Run
Example run command:
```
./xmlAnaWSBuilder/exe/XMLReader -x config/dijetTLA/20200701_j75_bkgonly_test/dijetTLA_J75yStar03_v01.xml -s 0 -b 1 --plotOption logy
```
This command will make a RooWorkspace starting J75-triggered data from https://arxiv.org/abs/1804.03496, fitted with the UA2 background function. 

# Scripts

The directory _python/_ contains a number of standalone Python scripts to plot and extracts the information from the workspace. Test files and .pdf files of how the output should look like are provided in each of the directories. 

   * _PlotWorkspace/PlotWorkspaceFit.py_ plots the fit and the data in the workspace (obtained from the command above) together with its residuals and pulls, and overlays it with the fit result from the previous statistical analysis framework. 