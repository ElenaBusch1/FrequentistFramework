# generate all the mass- and width- varied input automatically and put them into the signal/ directory

for mass in 200 225 250 300 350 450 550 625 700 800
do 
    for width in 3 5 7 10 12 15
    do
	cp signalGauss_meanM_widthW.xml signal/signalGauss_mean${mass}_width${width}.xml	
	sed -i 's/MASS/'$mass'/g' signal/signalGauss_mean${mass}_width${width}.xml
	sed -i 's/WIDTHPERCENT/0'$(bc <<<"scale=2;"$width"/100")'/g' signal/signalGauss_mean${mass}_width${width}.xml
	sed -i 's/WIDTH/'$width'/g' signal/signalGauss_mean${mass}_width${width}.xml
    done
done	
