from PIL import Image, ImageDraw, ImageFont
from time import sleep
import math

ratio = 1/4
width =  int(8160*ratio)
height = int(4592*ratio)
image = Image.new(size=(width, height), mode="RGB", color="white")

f = open("input.in", "r")
lines = f.read().replace(",", ".").split("\n")


initialT = 200
finalT = width - initialT

initialX = 200
finalX = height - initialX

zero = int((finalX - initialX) / 2)

scaleT = [20, 0]
scaleX = [0, 0]

coords = []

for line in lines:
    t,x = line.split("\t")
    t = float(t)
    x = float(x)
    
    scaleT[0] = min(scaleT[0], t)
    scaleT[1] = max(scaleT[1], t)
    
    scaleX[0] = min(scaleX[0], x // 1)
    scaleX[1] = max(scaleX[1], x // 1)

    coords.append((t,x))

coords2 = []

for i in coords:
    coords2.append((int(i[0]/(scaleT[1]-scaleT[0]) * (finalT-initialT) + initialT), int(  i[1]/(scaleX[1]-scaleX[0]) * (finalX-initialX) * -1 + zero ) ))

def DrawGraph(points = [()], LinesThick = 3, scalar = 5):
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
                    image.putpixel( (w+ant_x + k, math.floor(ant_Ipoint + increaseFactor*w) + l), (
                        255,0,0
                    ) )
            count += 1
            if(count < scalar): continue
            count = 0
            
        
        ant_Ipoint = i[1]
        ant_x = i[0]
    pass

font = ImageFont.truetype("Acme-Regular.ttf", 24)
draw = ImageDraw.Draw(image)

accrementT = int((finalT-initialT)/(scaleT[1]-scaleT[0]))
accrementX = int((finalX-initialX)/(scaleX[1]-scaleX[0]) )

finalT_coord = 0
zeroCoord = 0

counter = scaleT[0] // 1 - 1
for k in range(initialT, finalT+int(scaleT[1])+accrementT, accrementT ):
    counter += 1
    
    for i in range(initialX-accrementX, finalX):
        for j in range(-1,1):
            image.putpixel((k+j, i), (0,0,0))
    
    text_ = "%.2f" % (counter)
    draw.text((k-12/2, finalX+50), text_, (0,0,0), font)
    
    finalT_coord = max(finalT_coord, k)


counter = -scaleX[1] - scaleX[0]
for k in range(initialX - accrementX, finalX+int(scaleX[1]), accrementX):
    counter -= 1
    
    for i in range(initialT, finalT_coord ):
        for j in range(-1,1):
            image.putpixel((i, j+k), (0,0,0))
    
    text_ = "%.2f" % (counter)
    draw.text((initialT -50, k-12/2), text_, (0,0,0), font)
    if(counter == 0): zeroCoord = k
    print(counter, k)


for i in range(initialT, finalT_coord):
    for j in range(-2, 2):
        image.putpixel((i, zeroCoord+j), (0,0,0))

DrawGraph(coords2, 3)

image.show()