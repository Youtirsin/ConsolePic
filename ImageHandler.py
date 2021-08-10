from PIL import Image

COLORSINP = {
    "colors": {
        "black": 0, "red": 15,
        "green": 28, "yellow": 45,
        "blue": 190, "purple": 121,
        "darkGreen": 22, "white": 225
    },
    "values": [0, 15, 28, 45, 190, 121, 22, 225],
    "keys": ["black", "red", "green", "yellow", "blue", "purple", "darkGreen", "white"]
}


# return the middle pixel value of the image in mode L
def getMid(img):
    colorArr = img.load()
    li = []
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if li.count(colorArr[i, j]) == 0:
                li.append(colorArr[i, j])
    return int((max(li) + min(li)) / 2)


# rewrite the image in model L with the cutline value
def rewriteImg(img, cutline):
    table = []
    for i in range(256):
        if i < cutline:
            table.append(0)
        else:
            table.append(1)
    return img.point(table, '1')