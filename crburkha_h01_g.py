# define function
def lenLineSeg(lXCoord,lYCoord):
    #subtract x and y coordinates from each other
    nDX = float(lXCoord[1])-float(lXCoord[0])
    nDY = float(lYCoord[1])-float(lYCoord[0])
    # Finds line segment length using modified pythagorean theorem
    nLenSeg = ((nDX**2)+(nDY**2))**(1/2.0)
    return nLenSeg

# define function 2
def lenTwoLineSeg():
    # creates prompts for and collects user defined x,y coordinate input
    lXCoord = input('Please enter three x coordinates (comma-separated) >>>').split(',')
    lYCoord = input('Please enter three y coordinates (comma-separated) >>>').split(',')
    # uses index values to extract coordinate data from user input
    nLenSeg1 = lenLineSeg(lXCoord[0:2],lYCoord[0:2])
    nLenSeg2 = lenLineSeg(lXCoord[1:3],lYCoord[1:3])
    #prints message and concatonated line segment value argument
    print('\nThe total length of the two line segments is '+str(nLenSeg1+nLenSeg2))
    
#calls function
lenTwoLineSeg()