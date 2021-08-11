from ImageHandler import *
from StrPainter import *
from MyUtil import *


def printWithColor(filename, size):
    # record information of every pixel
    log = open("log.txt", "w")

    img = Image.open(filename).resize(size).convert("P")

    arr = img.load()
    for i in range(size[0]):
        for j in range(size[1]):
            index = findNearestIndex(COLORSINP["values"], arr[j, i])
            log.write("pixel: %d, index: %d, match: %d, color: %s\n"
                      % (arr[j, i], index, COLORSINP['values'][index], COLORSINP["keys"][index]))
            print(paintedStr("0", COLORSINP["keys"][index]), end='')
        print()

    log.close()
