from PIL import Image, ImageColor
import os
from storedData import Data
import math

root = os.getcwd()

# fileName = input("File name: ")
fileName = "main1"
fileType = ".jpg"

coords, points, zero, startingPoint = Data["Graph2"].values()


imageGraph = Image.open(root + "/ImagesBase/" + fileName + fileType)

width, height = imageGraph.size


def getCoordinates():
    print(points)
    for i in points:
        imageGraph.putpixel((coords[0], i[1]), (0,255,0))
        imageGraph.putpixel((coords[0]+1, i[1]), (0,255,0))
        imageGraph.putpixel((coords[0]-1, i[1]), (0,255,0))


# Its easier to just make the program count the pixels from top to bottom for each division
# I can aussi make the divisions a user's selection or a video from 0 divisions to full

divisions = 200

def ForEveryPixel():
    ant_point = startingPoint
    ant_y = "undefined"
    
    for i in range(coords[0], coords[2]+1, int(math.floor((coords[2]-coords[0])/divisions)) ):
        y = 0
        count = 0
        for j in range(coords[1], coords[3]):
            pixel = imageGraph.getpixel((i,j))
            
            if pixel[2] > 195 and pixel[0] + pixel[1] < 300:
                y += j
                count += 1
                imageGraph.putpixel((i,j), (0,255,0))
        
        if not count:
            continue
        y = int(math.floor(y/count))
        
        for j in range(1, abs(zero - y)):
            imageGraph.putpixel((i-1,zero + j * int(abs(zero-y)/(zero-y)) * -1 ), (0,0,0))
            imageGraph.putpixel((i,zero + j * int(abs(zero-y)/(zero-y)) * -1 ), (0,0,0))
            imageGraph.putpixel((i+1,zero + j * int(abs(zero-y)/(zero-y)) * -1 ), (0,0,0))
    
        imageGraph.putpixel(
            (i, int(math.floor(y/count))),
            (255,0,0)
        )
        y = zero - y
        
        if ant_y == "undefined":
            ant_y = y
            continue
        
        if abs(ant_y)/ant_y != abs(y)/y:
            ant_y = 0
        
        
        height = math.floor(abs(coords[0]-coords[2])/divisions)/(coords[2]-coords[0])*10
        area = (ant_y+y)*height/2
        print("para: ", ant_y, y, height)
        print(area, (ant_y+y), y)
        
        area = int(math.floor(area))
        ant_point = ant_point + area *-1
        for k in range(-5,5):
            for l in range(-5,5):
                imageGraph.putpixel((i+k, ant_point+l), (255,0,0))
        ant_y = y
        
        
        
ForEveryPixel()
# getCoordinates()
imageGraph.show()