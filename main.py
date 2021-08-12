from os import system

from DrawWithColor import printWithColor, printWithColorBg
from DrawWithoutColor import printWithoutColor
from DrawGifWithColor import *


def main():
    system("cls")
    # printWithoutColor(filename="./src/img/han1.jpg")
    # printWithColor(filename="src/img/gakki.gif")
    # printWithColorBg(filename="src/img/gakki.gif")
    playGifWithColor(filename="./src/img/kun.gif")
    # resizedGif(filename="./src/img/gakki.gif")
    # gifTest(filename="./src/img/gakki.gif")


if __name__ == '__main__':
    main()
