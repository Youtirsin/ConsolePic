from PIL import Image


def test():
    print("Hello \u001b[31m world \u001b[0m")


def test1():
    filename = "./src/img/guai.jpg"
    size = (80, 80)

    img = Image.open(filename).resize(size).convert("P")

    palette = img.getpalette()
    print(len(palette))
    print(palette)


if __name__ == '__main__':
    test1()
