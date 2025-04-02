from PIL import Image
import os
from storedData import Data
import math
import moviepy as mv
import numpy as np
from time import sleep

ImagesArray = []

root = os.getcwd()

# fileName = input("File name: ")
fileName = "TG1 (1)"
GenerateVideo = {
    "FileName": "sla",
    "Genarate": False,
    "DerivateLines": True,
    "IntegralDivisions": True
}

Debug = False
DebugDerivate = False

fileType, coords, zero, startingPoint, targetColors, scale, integrate, derivate, maxDivisions, derivateTarget, scalar = Data[fileName].values()


imageGraph = Image.open(root + "/ImagesBase/" + fileName + fileType)

iwidth, iheight = imageGraph.size
divisions = maxDivisions

newImage = imageGraph.copy()
# resizeRatio = 1/4
# newImage.resize((math.floor(iwidth*resizeRatio), iheight*resizeRatio), Image.Resampling.LANCZOS)


# def putpixel(tuple = (0,0), color = (0,0,0)):
#     newImage.putpixel((tuple[0]/4))

def getCoordinates():
    mult = 10
    for i in range (-mult,max(mult, 1)):
        for j in range(-mult, max(mult, 1)):
            newImage.putpixel((coords[0] + i, coords[1] + j), (0,255,255))
            newImage.putpixel((coords[2] + i, coords[3] + j), (0,255,255))
            newImage.putpixel((coords[2] + i, zero + j), (0,255,255))
            newImage.putpixel((coords[0] + i, startingPoint + j), (0,255,255))
    pass


# Its easier to just make the program count the pixels from top to bottom for each division
# I can aussi make the divisions a user's selection or a video from 0 divisions to full

print(imageGraph.size)

def ForEveryPixelIntegrateOrDerivate(integrate = False, derivate = False, thickness = -1, Debug = False, LinesThick = 4, divisions=divisions):
    ant_Ipoint = startingPoint
    ant_y = "undefined"
    derivatePixels = []
    
    for i in range(coords[0], coords[2]+1, int(math.floor((coords[2]-coords[0])/divisions)) ):
        y = 0
        count = 0
        if GenerateVideo["IntegralDivisions"] and GenerateVideo["Genarate"]:
            ImagesArray.append(np.asarray(newImage))
            
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
                    newImage.putpixel((i,j), (0,255,0))
        
        if not count:
            continue
        
        if Debug:
            newImage.putpixel(
                (i, int(math.floor(y/count))),
                (255,0,0)
            )
        y = int(math.floor(y/count))
        
        
        if thickness >= 0 and Debug:
            for j in range(1, abs(zero - y)):
                for k in range(-thickness, max(thickness, 1)):
                    newImage.putpixel((i+k,zero + j * int(abs(zero-y)/(zero-y)) * -1 ), (0,0,0))
                    
    
    
        y = zero - y
        height = math.floor(abs(coords[0]-coords[2])/divisions)/(coords[2]-coords[0])*scale
        
        if ant_y == "undefined":
            ant_y = y
            continue
        
        if derivate:
            ratio = (y-ant_y)/height
            derivatePixels.append((i, ratio *-1 + zero))
            if DebugDerivate:
                for k in range(-LinesThick*2, max(LinesThick*2, 1)):
                    for l in range(-LinesThick*2,max(LinesThick*2,1)):
                        if(pow(k,2) + pow(l,2) > 10 * math.log10(LinesThick*2)): continue
                        print((i+k), int(math.floor(ant_Ipoint))+l)
                        newImage.putpixel((i+k, int(math.floor(ratio *-1 + zero))+l), (155,155,155))
        
        if ant_y*y < 0:
            ant_y = 0
        
        if integrate:
            area = (ant_y+y)*height/2
            
            ant_Ipoint = ant_Ipoint + area *-1
            print((ant_Ipoint))
            for k in range(-LinesThick, max(LinesThick, 1)):
                for l in range(-LinesThick,max(LinesThick,1)):
                    if(pow(k,2) + pow(l,2) > 10 * math.log10(LinesThick)): continue
                    # newImage.putpixel((min(i+k, iwidth-1), min(int(math.floor(ant_Ipoint))+l, iheight-1)), integrate)
                    newImage.putpixel((i+k, int(math.floor(ant_Ipoint))+l), integrate)
        
        ant_y = y
    
    if derivate:
        derivatePoints = []
        
        for i in range(0,len(derivatePixels), scalar):
            medianY = 0
            counter_ = 0
            for j in range(i, min(i + scalar, len(derivatePixels))):
                medianY += derivatePixels[j][1]
                counter_ += 1
            medianY /= counter_
            derivatePoints.append((
                derivatePixels[min(int(math.floor(i + scalar/2)), len(derivatePixels)-1)][0],
                (medianY)
            ))
        DrawGraph(derivatePoints)
    

def DrawGraph(points = [()], LinesThick = 3):
    ant_Ipoint = "undefined"
    ant_x = "undefined"
    
    counter = 0
    for i in points:
        counter += 1
        if ant_Ipoint == "undefined":
            ant_Ipoint = i[1]
            ant_x = i[0]
            continue
        
        increaseFactor = (ant_Ipoint-i[1])/(ant_x-i[0])
        count = 0
        for w in range(0, i[0]-ant_x):
            for k in range(-LinesThick, max(LinesThick, 1)):
                for l in range(-LinesThick,max(LinesThick,1)):
                    if imageGraph.getpixel((w+ant_x + k, math.floor(ant_Ipoint + increaseFactor*w) + l)) == derivate:
                        continue
                    newImage.putpixel( (w+ant_x + k, math.floor(ant_Ipoint + increaseFactor*w) + l), (
                        derivate[0], derivate[1], derivate[2]
                    ) )
            count += 1
            if(count < scalar): continue
            count = 0
            
            if GenerateVideo["Genarate"] and GenerateVideo["DerivateLines"]:
                print("Loading", counter , "/", len(points))
                ImagesArray.append(np.asarray(newImage))
            
        
        ant_Ipoint = i[1]
        ant_x = i[0]
    pass


#ForEveryPixelIntegrateOrDerivate(integrate=integrate, derivate=derivate, LinesThick=10, Debug=False, thickness=1)        

# if derivate:
#     DerivateWithLinearDrawing(divisions=Data[fileName]["derivateTarget"], LinesThick=3, Debug=False)
ForEveryPixelIntegrateOrDerivate(integrate=integrate, derivate=derivate, LinesThick=10, Debug=Debug, thickness=0)

# getCoordinates()

newImage.show()

if GenerateVideo["Genarate"]:
    clip = mv.ImageSequenceClip(ImagesArray, fps=math.floor(30*divisions/45))
    clip.write_videofile(root + "/" + fileName + "-Video.mp4")
#imageGraph.save(root + "/ImagesBase/" + fileName + " (2)" + fileType)mv.