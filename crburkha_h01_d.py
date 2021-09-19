# Chris Burkhart: Create function to find centroid of triangle

# Create centroidTriangle function
def centroidTriangle(x1, y1, x2, y2, x3, y3):
    # define x of centroid
    x = round((x1 + x2 + x3) / 3, )
    # define y of centroid
    y = round((y1 + y2 + y3) / 3, )
    #define myCentroid variable
    myCentroid = x,y
    # Print: The x,y the centroid is ""
    print("The x,y the centroid is " + str(myCentroid))

# Call centroidTriangle function
centroidTriangle(43, 7, 47, 40, 90, 39)
