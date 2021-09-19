#Chris Burkhart: Create function that prints the largest number in a list
#Define largest number function
def largestNum(myList):
  #Finds largest number in list
  max(myList)
  #Print: The largest number in this list is ""
  print("The largest number in this list is " +str(max(myList)))

#Call largestNum function
largestNum([5,42,3,9])