from PIL import Image
from StrPainter import *


def test():
    print(paintedStrBg(" " * 10, "red"))


def test1():
    filename = "./src/img/guai.jpg"
    size = (80, 80)

    img = Image.open(filename).resize(size).convert("P")

    palette = img.getpalette()
    print(len(palette))
    print(palette)


if __name__ == '__main__':
    test()
