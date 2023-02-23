# FrequentistFramework

This code is under construction, and its documentation is a work in progress. 

This is a frequentist statistical analysis framework based on:
https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/XmlAnaWSBuilder

# Install - This follows the README of the XmlAnaWSBuilder and quickFit. pyBumpHunter is run in a virtualenv to run python 3.6 alongside python 2.7 setup with ROOT

```
setupATLAS
lsetup git
git clone https://:@gitlab.cern.ch:8443/atlas-phys-exotics-dijet-tla/FrequentistFramework.git
cd FrequentistFramework/
source scripts/install_FrequentistFramework.sh
source scripts/setup_buildAndFit.sh
```

In a fresh terminal (where you haven't run these scripts), you will also need to install pyBumpHunter in this same directory.
```
source scripts/install_pyBumpHunter.sh
```

# Setup

In the future you can setup your environment via
```
source scripts/setup_buildAndFit.sh
```

# Configuration

Most of the configuration is handled in scripts/config.py. 

To run the code, you will need to change config.py to have cdir be the directory that you set this up in.

There are two main parts to config.py -- the backgrounds (samples) and the signals.
If you want to add a new background file to fit, or a new signal, you will have to change these.

You will need to change the paths to the histograms to match your own path.


Below is an example of the background, with the key components explained.

```
samples["sherpa_yxxjjjj_2javg_alpha1"] = {
                 "categoryfile"  : "../config/category_background.template",
                 "topfile": "../config/background.template",
                 "inputFile": "/afs/cern.ch/work/j/jroloff/nixon/createHistograms/yxxjjjj_Sherpa.root", # The root file with the background spectrum
                 "histname": "h2_resonance_jet_m2javg_alpha_nominal_alphaBin_1", # The histogram name with the root file
                 "alpha": 1, #  The alpha bin
                 "lumi": 139000, # Luminosity (in pb) (for plotting only)
                 "varName": "m_{#LT 2j #GT}, 0.12 < #alpha < 0.14", # A string that identifies what this signal is (for plotting)
                 "varAxis": "m_{#LT 2j #GT} [GeV]", # The x-axis name (for plotting)
                 "varLabel": "0.12 < #alpha < 0.14", # A string describing this (for plotting)
                 "rangelow" : 250, # The low end of the mass range used for fitting
                 "rangehigh" : 3500, # The high end of the mass range used for fitting
                 "legend": "Sherpa AHADIC", # A string describing what samples were used to produce the background (for plotting)
               }


```

Below is an example of the signal, with the components explained.


```
signals["crystalBallHist"] = {
                 "signalfile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/config/signalGauss_meanM_template.xml",
                 "workspacefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/SignalCB_mX_MEAN_mY_MASSX.root",
                 "templatefile": "/afs/cern.ch/work/j/jroloff/nixon/FrequentistFramework/scripts/signalTemplates/SignalCB_mX_MEAN_mY_MASSX.root",
                 "histfile": "/afs/cern.ch/work/j/jroloff/nixon/systematics/gausSignals/gausCB__mX_MEAN_mY_MASSX_alphaBin_ALPHA.root", # The name of the file where the template lives. Some components of this are changed when processing (MEAN, MASSX, ALPHA)
                 "histname": "h2_resonance_jet_m4j_alpha_", # The name of the histogram
                 "systFile": "uncertaintySets/systematics", #The name of the file with the list of systematics. If none, use "empty.txt"
               }
```



# Sets of scripts

Currently, there are different scripts for the m4j and m2javg plots, since there are slight differences in the configuration.
The m4j scripts are the ones that start with yxxjjjj, and the m2javg are the ones that begin with m2j.


# Initial MC fits

```
python yxxjjjj_anaFit.py
```


# Generating pseudodata

For the spurious signal, signal injection, and limits, you will need to generate pseudodata from the initial fits.


```
python yxxjjjj_makePseudodata.py
```

# Creating crystal ball templates

Note: You only need to run this if you are using signal templates, but for many initial studies, this is not necessary, and a Gaussian template can be used instead.


# Spurious signal tests


This script uses the generated pseudodata to run S+B fits, with no injected signal.

These tests can be done with the signal templates or Gaussian templates, and the default is currently using Gaussians.

```
python yxxjjjj_spuriousSignal.py
```

# Signal injection tests

This script uses the generated pseudodata, but also injects and N-sigma signal into this. 
N is determined based on S/sqrt(B) in a window around the signal peak, where the window is determined by the signal width (one of the parameters).
Then, S+B fits are run, and the fit results are saved.

These tests can be done with the signal templates or Gaussian templates, and the default is currently using Gaussians.


```
python yxxjjjj_injections.py
```


# Limits


```
python yxxjjjj_limits.py
```


# Visualizing results

Most of the plotting is handled in a single script, but it can be easier to sometimes comment out parts of it to only run the relevant aspects.


```
python yxxjjjj_plotting.py
```














