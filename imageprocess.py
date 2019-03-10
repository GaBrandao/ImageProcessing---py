from sys import argv
from PIL import Image as im
from PIL import ImageEnhance as ie
from PIL import ImageOps as io
import matplotlib.pyplot as plt

image = im.open(argv[1])

size = (100, 100)

if (image.size!=size):
    image = io.fit(image,size,im.ANTIALIAS)

image = io.grayscale(io.equalize(image))
image = ie.Contrast(image).enhance(float(argv[2])).convert("1")

list_image = io.mirror(image).rotate(90).load()

out = open(argv[3], "w+")
out.write(str(size[0])+"\n")
for i in range(size[0]):
    for j in range(size[1]):
        if list_image[i,j]==255:
            out.write(str(i)+" "+str(j)+"\n")

plt.imshow(image)
plt.show()


