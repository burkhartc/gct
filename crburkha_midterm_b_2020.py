import os, math
#set current working directory to sPrj
sPrj = os.getcwd()+'\\'

#read cities.csv from cwd and set to fCities, default mode
fPopArea = open(sPrj+'poparea.csv', 'r')
fDensity = open(sPrj+'crburkha_midterm_results_b.csv', 'w')
lRecs = []
fPopArea.readline()

while True:
    lCells = fPopArea.readline().split(',')
    if lCells[0] == '': break
    nDensity = float(lCells[3]) / float(lCells[5])
    lCells.append(nDensity)
    lCells.append(lRecs)

print(nDensity)

