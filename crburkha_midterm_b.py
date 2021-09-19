# Chris Burkhart: GEOS 5073 Midterm Script b
# 1. Read the poparea.csv file that contains information about the population and area of major U.S. cities;
#    this file includes 5 attributes, i.e. Rank, Name, POP2010, AREAkm (area in km2), and AREAmi (area in mi2).
# 2. Calculate the density of each city; density = population / area [you can use either AREAkm or AREAmi].
# 3. Print out the top 5 most dense cities, and 5 cities with the minimum density
# 4. Create a new CSV file containing a table with all cities sorted by population density from lowest value to highest
#    value; name this file <username>_midterm_b_results.csv; the seven column names in the output table should be
#    DensityIndex, Rank, Name, POP2010, AREAkm, AREAmi, and Density (DensityIndex is the index of the sorted list)

import os
# set current working directory to sPrj
sPrj = os.getcwd()+'\\'
# read cities.csv from cwd and set to fCities, default mode
fPoparea = open(sPrj+'poparea.csv', 'r')
fResults = open(sPrj+'crburkha_midterm_b_results.csv', 'w')

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
