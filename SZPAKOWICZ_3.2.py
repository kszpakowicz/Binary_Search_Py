#Binary Search function
#Takes two input parameters -  a text file and a int value
#Searches for the value within the text file using a binary search algorithm
#Returns the numbers of comparisons done and the index position of the value
#(or -1 if not found)
def biSearch(file, value):
    nList = list(map(int, file.read().split()))
    comparisons = 0
    position = 0 #acts like the middle in this algorithm
    low = 0
    high = len(nList) - 1

    #Binary search keeps splitting the list in half
    #Depending on where the value is located, low or high are changed
    while low <= high:
        comparisons+=1
        position = (high + low)//2
        if nList[position] == value:
            return comparisons, position #break loop
        elif nList[position] > value:
            high = position - 1 #if value is lower than current number at index
        else:
            low = position + 1 #if value is greater than current number at index
            
    print("Desired Value Not Found")    
    return comparisons, -1 #if value is not found in the list

#Driver for testing
file = open("data.txt", "r")
value = 9724 #Value picked for testing data
print("Showing Results in Format: (Number of Comparisons, Postion of Value in File)")
print(biSearch(file, value))
file.close()
