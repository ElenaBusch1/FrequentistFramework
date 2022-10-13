# FrequentistFramework

This code is very preliminary and under construction, and its documentation is a work in progress. 

This is a frequentist statistical analysis framework based on:
https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/XmlAnaWSBuilder

# Install - This follows the README of the XmlAnaWSBuilder and quickFit. pyBumpHunter is run in a virtualenv to run python 3.6 alongside python 2.7 setup with ROOT
```
setupATLAS
lsetup git
git clone -b bba https://:@gitlab.cern.ch:8443/atlas-phys-exotics-dijet-tla/FrequentistFramework.git
cd FrequentistFramework/
source scripts/install_FrequentistFramework.sh
```

# Setup

In the future you can setup your environment via
```
source scripts/setup_buildAndFit.sh
```


# Scripts

The directory scripts contains a number of standalone Python scripts to plot and extracts the information from the workspace.
A few things need to be configured in scripts/config.py, which can be used to set paths to your input histograms.
For starting, it is probably easiest to use Gaussian signals.

For each of the scripts below, they should each be configured to use the correct background and N-parameter fit.
Eventually, I will make this more easily configurable, but I have not gotten to this yet.



# Generating pseudodata

First, the initial MC needs to be fit with an N+1 parameter fit.
Then, this can be used as input to make pseudodata, with the number of toys configured in config.py.

```
python yxxjjjj_runAna.py
python yxxjjjj_makePseudodata.py
```


# Spurious signal tests
```
python yxxjjjj_spuriousSignal.py
```


# Signal injection tests
```
python yxxjjjj_injections.py
```

