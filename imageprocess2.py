import sys
import numpy as np
from PIL import Image as im
from PIL import ImageEnhance as ie
from PIL import ImageOps as io
import matplotlib.pyplot as plt

image = im.open(sys.argv[1])

size = (128, 128)

if (image.size!=size):
    image = io.fit(image,size,im.ANTIALIAS)

image = io.equalize(image)
image = ie.Color(image).enhance(0)
image = ie.Contrast(image).enhance(float(sys.argv[2])).convert("1")

list_image = image.load()
print(size[0])
for i in range(size[0]):
    for j in range(size[1]):
        if list_image[j,i]==255:
            print(j,i)

plt.imshow(image)
plt.show()


