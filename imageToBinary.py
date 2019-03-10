import sys
from PIL import Image as im
from PIL import ImageEnhance as ie
from PIL import ImageOps as io

if (len(sys.argv)<4):
    print("To execute use:\n\t python3 imageToBinary.py <image-filename> <contrast-percent> <output-filename> <dimension-OTPIONAL>")
    sys.exit(0)

image = im.open(sys.argv[1])

size = (128, 128)
if (len(sys.argv)==5):
    d = int(sys.argv[4])
    size = (d,d)
if (image.size!=size):
    image = io.fit(image,size,im.ANTIALIAS)

image = io.grayscale(io.equalize(image))
image = ie.Contrast(image).enhance(float(sys.argv[2])).convert("1")

list_image = io.mirror(image).rotate(90).load()

out = open(sys.argv[3], "w+")
out.write(str(size[0])+"\n")
for i in range(size[0]):
    for j in range(size[1]):
        if list_image[i,j]==255:
            out.write(str(i)+" "+str(j)+"\n")



