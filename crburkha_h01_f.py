# Chris Burkhart: Creates a function that finds the difference in maximum and minimum values from a user defined list

# creates differenceMaxMin function
def differenceMaxMin():
    # defines values as list
    values = []
    # defines n as user chosen number of list items
    n = int(input("Enter number of elements: "))
    # creates range from user defined n
    #Print: Enter values below:
    print("Enter values below: ")
    for i in range(0, n):
        #defines ele as user input
        ele = int(input())
        # appends user input as list
        values.append(ele)
    # defines diff as the difference between the maximum and minimum value from user list
    diff = max(values) - min(values)
    #Print: The difference between the maximum and minimum for the given values is ""
    print("The difference between the maximum and minimum for the given values is " + str(diff))
# calls function differenceMaxMin
differenceMaxMin()
