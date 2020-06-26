# FrequentistFramework
This code is very preliminary and under construction!!

This is a frequentist statistical analysis framework based on:
https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/XmlAnaWSBuilder

# Install - follow the README Of the XmlAnaWSBuilder
```
setupATLAS
lsetup git
git clone https://:@gitlab.cern.ch:8443/atlas-phys-exotics-dijet-tla/FrequentistFramework.git
git submodule init
git submodule update --remote
cd xmlAnaWSBuilder/
source setup_lxplus.sh
sh scripts/install_roofitext.sh
mkdir build && cd build
cmake ..
make -j4
cd ..
```

```
cd config/dijetTLA
ln -s AnaWSBuilder.dtd ../../xmlAnaWSBuilder/dtd/AnaWSBuilder.dtd 
cd ../..
```

# Run
Example run command:
```
./xmlAnaWSBuilder/exe/XMLReader -x config/dijetTLA/dijetTLA_J100yStar06_v01.xml -s 0 -b 1 --plotOption logy
```