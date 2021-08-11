from os import system

from DrawWithColor import printWithColor
from DrawWithoutColor import printWithoutColor


def main():
    system("cls")
    # printWithoutColor(filename="./src/img/han1.jpg", size=(80, 80))
    printWithColor(filename="src/img/han1.jpg", size=(80, 80))
    # test()


if __name__ == '__main__':
    main()
