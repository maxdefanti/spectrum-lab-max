import numpy as np
import pandas as pd
from matplotlib import pylab as plt 
from matplotlib import pyplot
import cv2 as cv
from glob import glob 
from PIL import Image

img = cv.imread('PUT YOUR FILE HERE')
img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

im2write = np.zeros((1080,1920,3))

# change rgb values to meet your shadow's color values

for x in range(1080):
   for y in range(1920):
           if((img[x][y][0] > 15 and img[x][y][0] < 110) and (img[x][y][1] > 20 and img[x][y][1] < 110) and (img[x][y][2] > 25 and img[x][y][2] < 100)):
                im2write[x][y][0] = 255
                im2write[x][y][0] = 255
                im2write[x][y][0] = 255
            

cv.imwrite('result.png', im2write)
