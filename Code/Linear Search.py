#Linear Search

#Function to recieve a list and the desired item to be found
def search(myList, myItem):
    i = 0
    while i < len(myList):
        if myList[i] == myItem:
            return 'Found ' + str(myItem) + ' in location: ' + str(i + 1)
        i += 1

    return 'Item could not be found'

#The list to be searched
numberList = [3, 7, 19, 1, 45, 10, 32]
print(search(numberList, 19))   #Will return position 3
print(search(numberList, 99))   #Will return not found
