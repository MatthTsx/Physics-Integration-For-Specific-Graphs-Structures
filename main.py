from PIL import Image
import os
from storedData import Data
import math

root = os.getcwd()

# fileName = input("File name: ")
fileName = "Graph4 (2)"

fileType, coords, zero, startingPoint, targetColors, scale, integrate, derivate, maxDivisions = Data[fileName].values()


imageGraph = Image.open(root + "/ImagesBase/" + fileName + fileType)

iwidth, iheight = imageGraph.size
divisions = maxDivisions


def getCoordinates():
    mult = 0
    for i in range (-mult,max(mult, 1)):
        for j in range(-mult, max(mult, 1)):
            imageGraph.putpixel((coords[0] + i, coords[1] + j), (0,255,255))
            imageGraph.putpixel((coords[2] + i, coords[3] + j), (0,255,255))
            imageGraph.putpixel((coords[2] + i, zero + j), (0,255,255))
            imageGraph.putpixel((coords[0] + i, startingPoint + j), (0,255,255))
    pass


# Its easier to just make the program count the pixels from top to bottom for each division
# I can aussi make the divisions a user's selection or a video from 0 divisions to full

print(imageGraph.size)

def ForEveryPixelIntegrateOrDerivate(integrate = False, derivate = False, thickness = -1, Debug = False, LinesThick = 4):
    ant_Ipoint = startingPoint
    ant_y = "undefined"
    
    for i in range(coords[0], coords[2]+1, int(math.floor((coords[2]-coords[0])/divisions)) ):
        y = 0
        count = 0
        for j in range(coords[1], coords[3]):
            pixel = imageGraph.getpixel((i,j))
            
            if (
                abs(pixel[0] - targetColors["r"][0]) < targetColors["r"][1]
                and abs(pixel[1] - targetColors["g"][0]) < targetColors["g"][1]
                and abs(pixel[2] - targetColors["b"][0]) < targetColors["b"][1]
            ):
                y += j
                count += 1
                if Debug:
                    imageGraph.putpixel((i,j), (0,255,0))
        
        if not count:
            continue
        
        if Debug:
            imageGraph.putpixel(
                (i, int(math.floor(y/count))),
                (255,0,0)
            )
        y = int(math.floor(y/count))
        
        
        if thickness >= 0:
            for j in range(1, abs(zero - y)):
                for k in range(-thickness, max(thickness, 1)):
                    imageGraph.putpixel((i+k,zero + j * int(abs(zero-y)/(zero-y)) * -1 ), (0,0,0))
    
    
        y = zero - y
        height = math.floor(abs(coords[0]-coords[2])/divisions)/(coords[2]-coords[0])*scale
        
        if ant_y == "undefined":
            ant_y = y
            continue
        
        if derivate:
            ratio = (y-ant_y)/height
            for k in range(-LinesThick*2, max(LinesThick*2, 1)):
                for l in range(-LinesThick*2,max(LinesThick*2,1)):
                    if(pow(k,2) + pow(l,2) > 10 * math.log10(LinesThick*2)): continue
                    print((i+k), int(math.floor(ant_Ipoint))+l)
                    imageGraph.putpixel((i+k, int(math.floor(ratio *-1 + zero))+l), derivate)
        
        if ant_y*y < 0:
            ant_y = 0
        
        if integrate:
            area = (ant_y+y)*height/2
            
            ant_Ipoint = ant_Ipoint + area *-1
            print((ant_Ipoint))
            for k in range(-LinesThick, max(LinesThick, 1)):
                for l in range(-LinesThick,max(LinesThick,1)):
                    if(pow(k,2) + pow(l,2) > 10 * math.log10(LinesThick)): continue
                    # imageGraph.putpixel((min(i+k, iwidth-1), min(int(math.floor(ant_Ipoint))+l, iheight-1)), integrate)
                    imageGraph.putpixel((i+k, int(math.floor(ant_Ipoint))+l), integrate)
        
        ant_y = y
        
        
        
ForEveryPixelIntegrateOrDerivate(integrate=integrate, derivate=derivate, LinesThick=10)
#getCoordinates()

imageGraph.show()
#imageGraph.save(root + "/ImagesBase/" + fileName + " (2)" + fileType)