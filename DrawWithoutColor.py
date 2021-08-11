from ImageHandler import *


def printWithoutColor(filename, size):
    img_L = Image.open(filename).resize(size).convert("L")
    middle_L = getMid(img_L)

    img = rewriteImg(img_L, middle_L)

    arr = img.load()
    # print("sample pixel: ", arr[10, 10])
    # print("sample pixel type: ", type(arr[10, 10]))
    # img.show()
    for i in range(size[0]):
        for j in range(size[1]):
            if arr[j, i] == 1:
                print("0", end='')
            else:
                print("1", end='')
        print()

