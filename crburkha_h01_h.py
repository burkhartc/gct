# defines centroidRectangle() function
def centroidRectangle():
    #prompts user input
    print('Please enter coordinates of the rectangle (comma-separated):')
    # collects minimum coordinates for rectangle using input function
    lMinCoord = input('Minimum x,y >>> ').split(',')
    # collects maximum coordinates for rectangle using input function
    lMaxCoord = input('Maximum x,y >>> ').split(',')
    #calculates and stores user defined average x coordinate in variable
    sX = str((float(lMinCoord[0])+float(lMaxCoord[0]))/2.0)
    # stores and stores user defined average y coordinate in variable
    sY = str((float(lMinCoord[1])+float(lMaxCoord[1]))/2.0)
    #prints centroid coordinates and message in string
    print('\nThe x,y centroid coordinates of the rectangle are: '+sX+','+sY)
#calls centroidRectangle function
centroidRectangle()