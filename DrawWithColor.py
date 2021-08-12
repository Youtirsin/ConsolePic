from ImageHandler import *
from StrPainter import *
from MyUtil import *


def printWithColor(filename, width=80):
    # record information of every pixel
    # log = open("log.txt", "w")
    raw_img = Image.open(filename)
    size = (width, int(width * raw_img.size[1] / raw_img.size[0]))

    img = raw_img.resize(size).convert("P")

    arr = img.load()
    for i in range(size[1]):
        for j in range(size[0]):
            index = findNearestIndex(COLORSINP["values"], arr[j, i])
            # log.write("pixel: %d, index: %d, match: %d, color: %s\n"
            #         % (arr[j, i], index, COLORSINP['values'][index], COLORSINP["keys"][index]))
            print(paintedStr("0", COLORSINP["keys"][index]), end='')
        print()

    # log.close()


def printWithColorBg(filename, width=80):
    # record information of every pixel
    # log = open("log.txt", "w")
    raw_img = Image.open(filename)
    size = (width, int(width * raw_img.size[1] / raw_img.size[0]))

    img = raw_img.resize(size).convert("P")

    arr = img.load()
    for i in range(size[1]):
        for j in range(size[0]):
            index = findNearestIndex(COLORSINP["values"], arr[j, i])
            # log.write("pixel: %d, index: %d, match: %d, color: %s\n"
            #           % (arr[j, i], index, COLORSINP['values'][index], COLORSINP["keys"][index]))
            print(paintedStrBg(" ", COLORSINP["keys"][index]), end='')
        print()

    # log.close()
