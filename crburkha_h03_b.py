import random, statistics

def randStats():
    randList = []
    randList = random.sample(range(1,1000), 150)
    randTotal = sum(randList)
    randMean = statistics.mean(randList)
    randMin = min(randList)
    randMax = max(randList)
    randSD = statistics.stdev(randList)
    print("Total " + str(randTotal))
    print("Mean: " +str(round(randMean,3)))
    print("Minimum: "+ str(randMin))
    print("Maximum: "+ str(randMax))
    print("Standard Deviation: " + str(round(randSD,3)))

randStats()