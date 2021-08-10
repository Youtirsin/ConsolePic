# use generated images in pure color to know the convertion
# between P mode and RGB mode of some common colors

# result file: color_refercence.txt

from PIL import Image

colors = [
    "black", "red", "green",
    "yellow", "blue", "purple",
    "darkGreen", "white"
]
rgbs = [
    (0, 0, 0), (255, 0, 0), (0, 128, 0),
    (255, 255, 0), (0, 0, 255), (128, 0, 128),
    (0, 100, 0), (255, 255, 255)
]


def main():
    # with open("refercence.txt", 'w') as writer:
    #     for i, color in enumerate(colors):
    #         temp_image = Image.new("RGB", (5, 5), rgbs[i]).convert("P")
    #         writer.write("%s\t\t\t%d\n" % (color, temp_image.load()[0, 0]))
    import json
    j = {}
    for i, color in enumerate(colors):
        temp_image = Image.new("RGB", (5, 5), rgbs[i]).convert("P")
        j[color] = temp_image.load()[0, 0]
    print(j)
    json.dump(j, open("refercence.json", 'w'))


if __name__ == '__main__':
    main()
