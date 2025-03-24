from PIL import Image, ImageColor
import os
from storedData import startingPoints
import math

root = os.getcwd()

# fileName = input("File name: ")
fileName = "main1"
fileType = ".jpg"

startedPoint = startingPoints["Graph2"]

imageGraph = Image.open(root + "/ImagesBase/" + fileName + fileType)

width, height = imageGraph.size


def getCoordinates():
    for i in range(width):
        for j in range(height):
            pixel = imageGraph.getpixel((i,j))
            if pixel[0] > 240 and pixel[1] < 50:
                imageGraph.putpixel(xy=(i,j), value=(0,255,0))
                print(pixel, i, j)
                break


def ForEveryPixel():
    for i in range(width):
        for j in range(height):
            if i != startedPoint[0] and j != startedPoint[1]:
                continue
            imageGraph.putpixel((i,j), (0,255,0))
            print(i,j)


def testing():
    for i in range(startedPoint[0], width, 31):
        for j in range(height):
            imageGraph.putpixel((i,j), (0,255,0))
    
    for j in range(startedPoint[1], height*10, 227):
        for i in range(width):
            imageGraph.putpixel((i, int((j)//10) ), (0,255,0))

# ForEveryPixel()
# getCoordinates()
testing()
imageGraph.show()