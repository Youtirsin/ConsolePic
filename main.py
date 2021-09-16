from os import system

from DrawWithColor import printWithColor, printWithColorBg
from DrawWithoutColor import printWithoutColor
from DrawGifWithColor import *


def main():
    system("cls")
    # printWithoutColor(filename="./src/img/han1.jpg")
    printWithColor(filename="src/img/minion.jpg")
    # printWithoutColor(filename="src/img/tea.png")
    # playGifWithColor(filename="./src/img/cat.gif")
    # resizedGif(filename="./src/img/gakki.gif")
    # gifTest(filename="./src/img/gakki.gif")


if __name__ == '__main__':
    main()
