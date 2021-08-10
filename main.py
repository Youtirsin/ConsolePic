from ImageHandler import *
from StrPainter import *
from MyUtil import *
from os import system


def printWithoutColor():
    filename = "./src/han.png"
    PIC_SIZE = (30, 30)
    # filename = "./src/me.jpg"
    # PIC_SIZE = (8, 8)
    raw_img = Image.open(filename).convert("RGB").resize(PIC_SIZE)

    img_L = raw_img.convert("L")
    middle_L = getMid(img_L)

    img = rewriteImg(img_L, middle_L)

    arr = img.load()
    # print("sample pixel: ", arr[10, 10])
    # print("sample pixel type: ", type(arr[10, 10]))
    # img.show()
    for i in range(PIC_SIZE[0]):
        for j in range(PIC_SIZE[1]):
            if arr[j, i] == 1:
                print("0", end='')
            else:
                print("1", end='')
        print()


def printWithColor():
    filename = "./src/han.png"
    PIC_SIZE = (30, 30)

    log = open("log.txt", "w")

    img = Image.open(filename).resize(PIC_SIZE).convert("P")
    img.show()

    arr = img.load()
    for i in range(PIC_SIZE[0]):
        for j in range(PIC_SIZE[1]):
            i = findNearestIndex(COLORSINP["values"], arr[j, i])
            log.write("pixel: %d, index: %d, color: %s\n" % (arr[j, i], i, COLORSINP["keys"][i]))
            print(paintedStr("0", COLORSINP["keys"][i]), end='')
        print()

    log.close()


def main():
    system("cls")
    # printWithoutColor()
    printWithColor()


if __name__ == '__main__':
    main()
