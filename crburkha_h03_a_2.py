import random

def randDiv():
    n = random.randint(1, 1000)
    randList = []
    divBy7 = []
    divBy13 = []
    for x in range(n, n+200):
        randList.append(x)

        if (x%7==0):
            divBy7.append(x)

        if (x%13==0):
            divBy13.append(x)

    array = [[randList[j * 10 + i] for i in range(10)] for j in range(20)]
    print("The random number for this list is " + str(n))
    print("The list of random numbers is:")
    print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                     for row in array]))
    print(str(len(divBy7)) + " elements are divisible by 7.")
    print(str(len(divBy13)) + " elements are divisible by 13.")
randDiv()
