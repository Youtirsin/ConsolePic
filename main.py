from os import system

from DrawWithColor import printWithColor
from DrawWithoutColor import printWithoutColor




def main():
    system("cls")
    # printWithoutColor(filename="./src/img/name.png", size=(80, 80))
    printWithColor(filename="src/img/name.png", size=(80, 80))
    test()


if __name__ == '__main__':
    main()
