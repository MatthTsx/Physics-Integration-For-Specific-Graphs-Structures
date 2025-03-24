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


# Its easier to just make the program count the pixels from top to bottom for each division
# I can aussi make the divisions a user's selection or a video from 0 divisions to full

divisions = 20

def ForEveryPixel():
    for i in range(startedPoint[0],width, divisions):
        for j in range(startedPoint[1], height):
            imageGraph.putpixel((i,j), (0,255,0))

ForEveryPixel()
# getCoordinates()
imageGraph.show()