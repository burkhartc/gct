# Create function that adds and multiplies together elements of a list

# Import numpy library
import numpy

# Define sumMult function
def sumMult(myList):
    # add a list of numbers
    mySum = sum(myList)
    # multiply a list of numbers
    myProd = numpy.prod(myList)
    # Print: The sum of the list of numbers is ""
    print("The sum of the list of numbers is " +str(mySum))
    # Print: The product of the list of numbers is ""
    print("The product of the list of numbers is " + str(myProd))

#Call function
sumMult([5, 10, 3, 1])
