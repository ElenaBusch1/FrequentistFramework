#!/bin/bash

cd pyBumpHunter
virtualenv --python=/cvmfs/sft.cern.ch/lcg/releases/LCG_96bpython3/Python/3.6.5/x86_64-centos7-gcc8-opt/bin/python3 pyBH_env  # create a venv w/ python3 (if we don’t use --python=... then it defaults to python 2.7)
source pyBH_env/bin/activate # activate it 
# installing everything
pip install --upgrade pip
python3 -m pip install numpy 
python3 -m pip install matplotlib
python3 -m pip install scipy
python3 -m pip install uproot
python3 -m pip install --upgrade setuptools
python3 -m pip install setuptools_scm

python3 setup.py install

deactivate
cd ..
