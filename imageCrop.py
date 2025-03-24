from PIL import Image
import os

root = os.getcwd() + "/PdfsForConversion/"
folderName = input("Folder name: ")
fileName = input("File name: ")

folderName = "main_JPGS"
fileName = "main1"

image = Image.open(root + folderName + "/" + fileName + ".jpg")

width, height = image.size

# specify as you wish
left = width/6.9
top = height/2.1
right = width*20/21
bottom = height*14/15


image = image.crop(( left, top, right, bottom ))
image.show()

image.save(root + "CropedImages/" + fileName + "Croped1.jpg")