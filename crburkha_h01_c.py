# Chris Burkhart: Create a function that finds and prints the length of a line segment between two coordinates.
# Import Math module
import math
# Define function to calculate distance to coordinate sets
def lenLineSeg(x1, y1, x2, y2):
    # x = [10, 12]
    # y = [15, 20]
    # Define my length variable as pythagorean theorem; answer round to 2 decimals
    myLength = round(math.sqrt(math.pow(x2 - x1, 2) +
                     math.pow(y2 - y1, 2) * 1.0),2)
    # Print: The length of the line segment is ""
    print("The length of the line segment is " +str(myLength))
# Call function lenLineSeg
lenLineSeg(10, 15, 12, 20)
