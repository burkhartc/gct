#GEOS 3103/5073 Midterm Script A
#Adapted from Tullis(2019)
#Possible solution from Dr. Tullis
#Assumes midterm data is in same folder as this script
#24 Oct 2019

#Import module and open CSV files
#import OS Module
import os
#set current working directory to sPrj
sPrj = os.getcwd()+'\\'
#read cities.csv from cwd and set to fCities, default mode
fCities = open(sPrj+'cities.csv', 'r')
#read states.csv from cwd and set to fStates, default mode
fStates = open(sPrj+'states.csv', 'r')
#read crburkha_midterm_a_results.csv from cwd to fResults, open to write
fResults = open(sPrj+'crburkha_midterm_a_results.csv', 'w')

#Read and process data
#Define states dictionary as Dstates
dStates = {}
#Creates loop for State calues in states.csv
for sState in fStates:
    #creates sState, removing trailing new lines
    sState = sState.rstrip('\n')
    #defines start and range of values in csv file and calls state names from position 3 or '2:'
    dStates[sState[0:2]] = sState[2:]
#set interval
i = 0
#Creates loop for Cities values in cities.csv
for sCity in fCities:
    #creates sCity, removing trailing new lines
    sCity = sCity.rstrip('\n')
    #sets condition for individual iterations to write STATE_NAME, STATE to fResults
    if (i == 0): fResults.write(sCity+',STATE_NAME,STATE')
    else:
        #object sStateKey created using split list on coma separations
        sStateKey = sCity.split(',')[1][0:2]
        #writes new lines for every loop iterations, adding state name and state abbreviation per
        fResults.write('\n'+sCity+str(dStates.get(sStateKey)))
    # adds 1 consecutive new line per iteration
    i += 1

#Close CSV files
#closes cities.csv
fCities.close()
#closes states.csv
fStates.close()
#closes crbukha_midterm_a_results.csv
fResults.close()
