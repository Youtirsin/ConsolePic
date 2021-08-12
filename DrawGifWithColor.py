from ImageHandler import *
from StrPainter import *
from MyUtil import *
from os import system
from time import sleep


def gifTest(filename, width=80):
    img = resizedGif(filename, width)
    size = img.size
    img.seek(1)
    print(img.info)
    img.show()


def playGifWithColor(filename, width=80, frameDuration=0.05):
    # record information of every pixel
    # log = open("log.txt", "w")
    print("current duration between frames: ", frameDuration)

    newFilename = resizedGif(filename, width)

    img = Image.open(newFilename)
    size = img.size

    frameCount = 0
    while 1:
        try:
            img.seek(frameCount)
            frameCount += 1

            arr = img.load()
            for i in range(size[1]):
                for j in range(size[0]):
                    index = findNearestIndex(COLORSINP["values"], arr[j, i])
                    # log.write("pixel: %d, index: %d, match: %d, color: %s\n"
                    #           % (arr[j, i], index, COLORSINP['values'][index], COLORSINP["keys"][index]))
                    print(paintedStr("0", COLORSINP["keys"][index]), end='')
                print()
        except:
            print("frame count: ", frameCount - 1)
            break
        sleep(frameDuration)
        system("cls")

    # log.close()


def resizedGif(filename, width=80):
    raw_img = Image.open(filename)
    size = (width, int(width * raw_img.size[1] / raw_img.size[0]))

    baseDir = "./src/img/"
    resizedName = "xxewrwrwerwerew.gif"
    path = baseDir + resizedName

    imgs = []

    raw_img.seek(0)
    firstFrame = raw_img.copy().resize(size)
    imgs.append(firstFrame)

    frameCount = 1

    print("resizing gif...")
    while 1:
        try:
            raw_img.seek(frameCount)
            temp = raw_img.copy().resize(size)
            frameCount += 1
            imgs.append(temp)
        except:
            break
    firstFrame.save(path, save_all=True,
                    append_images=imgs, duration=raw_img.info['duration'])

    print(firstFrame.info)
    # firstFrame.show()
    print("resize process over.")
    return path
