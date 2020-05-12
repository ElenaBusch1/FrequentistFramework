# FrequentistFramework

A statistical analysis framework based on:
https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/XmlAnaWSBuilder

# Install
```
setupATLAS
lsetup git
git clone https://:@gitlab.cern.ch:8443/atlas-phys-exotics-dijet-tla/FrequentistFramework.git
git submodule init
git submodule update --remote
cd xmlAnaWSBuilder/
source setup.sh
make
```

```
ln -s AnaWSBuilder.dtd ../../xmlAnaWSBuilder/dtd/AnaWSBuilder.dtd 
```
