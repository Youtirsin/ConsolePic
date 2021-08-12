from PIL import Image


def test():
    img = Image.open("./src/img/kun.gif")
    print(img.size)
    print(img.info)

    frameCount = 0
    while 1:
        try:
            img.seek(frameCount)
            frameCount += 1
        except:
            break
    print("frame count: ", frameCount - 1)


def test1():
    filename = "./src/img/guai.jpg"
    size = (80, 80)

    img = Image.open(filename).resize(size).convert("P")

    palette = img.getpalette()
    print(len(palette))
    print(palette)


def test2():
    base_dir = "./src/img/"
    names = ["dog.jpg", "girl.jpg", "guai.jpg", "han.png"]

    imgs = []
    first = Image.open(base_dir + names[0]).copy()
    imgs.append(first)

    for i in range(1, len(names)):
        pic_name = base_dir + names[i]
        temp = Image.open(pic_name)
        imgs.append(temp)
    first.save("test.gif", save_all=True, append_images=imgs, duration=130)
    return 1
    # for i in range(n):
    #     pic_name = '{}/{}.png'.format(pics_dir, i)
    #     temp = Image.open(pic_name)
    #     imgs.append(temp)
    # save_name = '{}.gif'.format(pics_dir)
    # imgs[0].save(save_name, save_all=True, append_images=imgs, duration=t)
    # return save_name


if __name__ == '__main__':
    test()
