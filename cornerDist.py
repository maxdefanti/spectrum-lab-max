import numpy as np
import pandas as pd
from matplotlib import pylab as plt 

import cv2 as cv
from math import *

img = cv.imread('PUT YOUR FILE HERE')
img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

im2write = np.zeros((1080,1920,3))

# change rgb values to meet your shadow's color values

for x in range(1080):
   for y in range(1920):
           if((img[x][y][0] > 15 and img[x][y][0] < 110) and (img[x][y][1] > 20 and img[x][y][1] < 110) and (img[x][y][2] > 25 and img[x][y][2] < 110)):
                im2write[x][y][0] = 255
                im2write[x][y][0] = 255
                im2write[x][y][0] = 255

shadowPointY = []
shadowPointX = []

for x in range(1080):
   for y in range(1920):
        if(im2write[x][y][0] == 255):
             shadowPointY.append(x)
             shadowPointX.append(y)

cY = (max(shadowPointY))
cX = (max(shadowPointX))

xPix4y = []
yPix4x = []

for x in range(1920):
     if((im2write[cY][x][0]) == 255):
          xPix4y.append(x)


for x in range(1080):
     if((im2write[x][cX][0]) == 255):
          yPix4x.append(x)

def distanceForm(x1, y1, x2, y2):
     return '{0:.4f}'.format(sqrt((x1 - x2)**2 + (y1 - y2)**2))

print(distanceForm(xPix4y[0], cY, cX, yPix4x[0]), " pixels")
