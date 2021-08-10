# find the nearest index of number to the target in the array
def findNearestIndex(arr, target):
    temp_arr = list(arr)
    for i in range(len(temp_arr)):
        temp_arr[i] = abs(temp_arr[i] - target)
    return temp_arr.index(min(temp_arr))
