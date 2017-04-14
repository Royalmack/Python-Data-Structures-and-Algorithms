#Binary Search

#Takes a number list and the number to be found
def binarySearch(numList, item):
    bottom = 0
    end = len(numList) - 1   
    found = False

    while not found:
        mid = (bottom + end) // 2   #Find the midpoint of the list
        if numList[mid] == item:
            return 'Found in position: ' + str(mid + 1)
            found = True
        elif numList[mid] < item:   #Move the bottom of the search up if too low
            bottom = mid + 1
        else:   #Else move the end of the search down if too high
            end = mid - 1

#List of numbers to be passed
numberList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binarySearch(numberList, 15))
