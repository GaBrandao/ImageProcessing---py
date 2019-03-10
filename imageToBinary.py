import sys
from PIL import Image as im
from PIL import ImageEnhance as ie
from PIL import ImageOps as io

if (len(sys.argv)<4):
    print("To execute use:\n\t python3 imageToBinary.py <image-filename> <contrast-percent> <output-filename> <dimension-OTPIONAL>")
    sys.exit(0)

image = im.open(sys.argv[1])    #Load the imagem from file
if (image.mode == "RGBA"):      #Convert image mode for better result
    image = image.convert("RGB")

size = (128, 128)
if (len(sys.argv)==5):
    d = int(sys.argv[4])
    size = (d,d)
if (image.size!=size):          #Resize image resolution and format
    image = io.fit(image,size,im.ANTIALIAS)

image = io.grayscale(io.equalize(image))    #Convert image to grayscale after equalize contrast
image = ie.Contrast(image).enhance(float(sys.argv[2])).convert("1") #Convert image to bynare representation

list_image = io.mirror(image).rotate(90).load()     #Load pixel values into a list

#   Write description of the post processing image (dimension and white pixels coord)
#   into output file
out = open(sys.argv[3], "w+")
out.write(str(size[0])+"\n")
for i in range(size[0]):
    for j in range(size[1]):
        if list_image[i,j]==255:
            out.write(str(i)+" "+str(j)+"\n")



