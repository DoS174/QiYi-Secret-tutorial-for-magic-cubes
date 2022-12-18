from PIL import Image

images = list()
for i in range(-4, 87, 2):
    img = Image.open(rf'images\{i}.jpg')
    if img.size[0] != 2048:
        print(f"{i} resize {img.size}")
        img = img.resize((2048, 1456))
    images.append(img)
    print(images[-1].size)

images[0].save(r'QiYi Secret tutorial for magic cubes.pdf', save_all=True, append_images=images[1:])
