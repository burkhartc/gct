import random

def randDiv():
    n = random.randint(1, 1000)
    randList=[]
    for x in range(n, n+200):
        if (x%7==0) or (x%13==0):
            randList.append(str(x))
    print(len(randList))
randDiv()
