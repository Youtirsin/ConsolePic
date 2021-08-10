# find the nearest index of number to the target in the array
def findNearestIndex(arr, target):
    temp_arr = list(arr)
    for i in range(len(temp_arr)):
        temp_arr[i] = abs(temp_arr[i] - target)
    return temp_arr.index(min(temp_arr))


if __name__ == '__main__':
    # dict = {
    #     '1': 1,
    #     '2': 2,
    #     '3': 3
    # }
    # arr = [7, 3, 5, 5, 6, 0, 8]
    #
    # print(findNearestIndex(arr, 0))
    COLORSINP = {
        "colors": {
            "black": 0, "red": 15,
            "green": 28, "yellow": 45,
            "blue": 190, "purple": 121,
            "darkGreen": 22, "white": 225
        },
        "values": [0, 15, 28, 45, 190, 121, 22, 225],
        "keys": ["black", "red", "green", "yellow", "blue", "purple", "darkGreen", "white"]
    }
    print("COLORSINP: ", type(COLORSINP))
