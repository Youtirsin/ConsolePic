from os import system

from DrawWithColor import printWithColor, printWithColorBg
from DrawWithoutColor import printWithoutColor


def main():
    system("cls")
    printWithoutColor(filename="./src/img/han1.jpg")
    # printWithColor(filename="src/img/han2.jpg", size=(80, 80))
    # printWithColorBg(filename="src/img/girl.jpg")


if __name__ == '__main__':
    main()
