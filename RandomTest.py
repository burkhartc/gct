import random

def randDiv():
    n = random.randint(1, 1000)
    nl=[]
    for x in range(n, n+200):
        if (x%7==0) or (x%13==0):
            nl.append(str(x))
            count = len(nl)
            print(count)
randDiv()
