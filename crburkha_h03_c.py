#Chris Burkhart: Homework 3 c

#Import modules
import math, os, random

#Generate a single random point within the given range
nXRand = random.randint(-104,-79)
nYRand = random.randint(31,45)

#Open and read the CSV data file and compute distances to the random point
fCities = open(os.getcwd()+'\\cities.csv', 'r')
lRecs = []
fCities.readline()

while True:
    lCells = fCities.readline().split(',')
    if lCells[0] == '': break
    nDeltaX = float(lCells[3]) - nXRand
    nDeltaY = float(lCells[4]) - nYRand
    nDistToRand = math.sqrt(math.pow(nDeltaX, 2) + math.pow(nDeltaY, 2))
    lCells.append(nDistToRand)
    lRecs.append(lCells)

#Identify the 10 nearest cities and which one of those has the highest population
lNearest10 = sorted(lRecs, key = lambda rec: rec[5])[0:10]
lHighestPop = sorted(lNearest10, key = lambda rec: rec[2], reverse = True)[0]

#Print all the results
print('Executed from random coordinates: '+str(nXRand)+', '+str(nYRand))
print('Total points read in: '+str(len(lRecs)))
print('Ten nearest cities are:')
#Iterates print loop of specified strings for TOP 10 cities
for r in lNearest10:
    print(' PID: '+str(r[0]))
    print('   Distance: '+str(r[5]))
    print('   Name: '+str(r[1]))
    print('   POP2000: '+str(r[2]))
sReport = ('This city, from these 10, with the highest population is , '+str(lHighestPop[1])
           +', at '+str(lHighestPop[2])+' in 2000')
print(sReport)

#Close the CSV data file
fCities.close()
