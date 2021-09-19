# Chris Burkhart: Create function that returns average of numbers input by user
# import statstics module
import statistics
# create averageInput function
def averageInput():
    # define values variable as list
    values = []
    # define n variable as user input integer with prompt
    n = int(input("Enter number of elements: "))
    #Print: Enter values below prompt
    print("Enter values below: ")
# creates range of from user input element value
    for i in range(0, n):
        # defines ele as user input integers
        ele = int(input())
        # creates running list from user input values
        values.append(ele)
    # defines average as mean of values variable
    average = round(statistics.mean(values), 2)
    # Print: The average of the given values is ""
    print("The average of the given values is " + str(average))
# calls function averageInput
averageInput()