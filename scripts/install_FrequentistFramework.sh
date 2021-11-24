#!/bin/bash

git submodule init
git submodule update

#needs to be done before setup, because that changes /usr/bin/python
source scripts/install_pyBumpHunter.sh

source scripts/setup_buildCombineFit.sh

source scripts/install_roofitext.sh
export RooFitExtensions_DIR=../RooFitExtensions/

cd xmlAnaWSBuilder/
mkdir build && cd build
cmake ..
make -j4
make install

cd ../../quickFit/
mkdir build && cd build
cmake ..
make -j4
make install

cd ../../workspaceCombiner
mkdir build && cd build
cmake ..
make -j4 
make install

cd ../..
