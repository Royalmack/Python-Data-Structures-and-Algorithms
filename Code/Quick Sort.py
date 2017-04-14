#Quick Sort

def quickSort(nums, start, end):
    if start < end:
        pivot = split(nums, start, end)

        quickSort(nums, start, pivot - 1)
        quickSort(nums, pivot + 1, end)  

def split(nums, start, end):
    pivot = nums[start]
    left = start + 1
    right = end
    done = False

    while not done:

        while left <= right and nums[left] <= pivot:
            left += 1
        while right >= left and nums[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            
    temp = nums[start]
    nums[start] = nums[right]
    nums[right] = temp
    return right

num = [3,7,8,5,2,1,9,5,4]
print(num)
quickSort(num, 0, len(num) - 1)
print(num) 
