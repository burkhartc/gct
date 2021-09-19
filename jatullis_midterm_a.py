#GEOS 3103/5073 Midterm Script A
#Possible solution from Dr. Tullis
#Assumes midterm data is in same folder as this script
#24 Oct 2019

#Import module and open CSV files
import os
sPrj = os.getcwd()+'\\'
fCities = open(sPrj+'cities.csv', 'r')
fStates = open(sPrj+'states.csv', 'r')
fResults = open(sPrj+'jatullis_midterm_a_results.csv', 'w')

#Read and process data
dStates = {}
for sState in fStates:
    sState = sState.rstrip('\n')
    dStates[sState[0:2]] = sState[2:]
i = 0
for sCity in fCities:
    sCity = sCity.rstrip('\n')
    if (i == 0): fResults.write(sCity+',STATE_NAME,STATE')
    else:
        sStateKey = sCity.split(',')[1][0:2]
        fResults.write('\n'+sCity+str(dStates.get(sStateKey)))
    i += 1

#Close CSV files
fCities.close()
fStates.close()
fResults.close()
