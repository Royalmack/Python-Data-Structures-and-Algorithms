#Bubble Sort

#Takes an unodered list
def bubbleSort(numList):
    flag = True

    while flag:
        
        flag = False
        
        for num in range(0, len(numList) - 1):
            if numList[num] > numList[num + 1]:
                temp = numList[num]
                numList[num] = numList[num + 1]
                numList[num + 1] = temp
                flag = True

numberList = [34, 12, 6, 89, 99, 1, -6]
print('Before Sort: ', numberList)
bubbleSort(numberList)
print('After Sort: ', numberList)
