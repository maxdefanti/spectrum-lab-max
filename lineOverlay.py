import cv2
import numpy as np

# Read image
image = cv2.imread('bw2.png') # put a path to your image here
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
# Use canny edge detection
edges = cv2.Canny(gray,30,150,apertureSize=3)
 
# Obtain line end points
lines_list =[]
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=150, minLineLength=30, maxLineGap=200)

cleans = np.empty(shape=[0,4], dtype=np.int32) # remove overlapping lines from HoughLines

for l in lines:
        
        # manually extending length of lines so that they all intersect, x can be altered 

        x = 50

        x0 = l[0][0]
        y0 = l[0][1]
        x1 = l[0][2]
        y1 = l[0][3]

        linSlope = (y1 - y0)/(x1 - x0)
        
        if x0 < x1:
             l[0][0] = x0 - x
             l[0][2] = x1 + x
        if x0 > x1: 
             l[0][0] = x0 + x
             l[0][2] = x0 - x

        if y0 < y1:
             l[0][1] = y0 - linSlope*(x)
             l[0][3] = y1 + linSlope*(x)
        if y0 > y1:
             l[0][1] = y0 - linSlope*(x)
             l[0][3] = y1 + linSlope*(x)

        # removing lines that are within 3.5 degrees of another and start and end within 30 pixels of one another

        alfa = np.degrees(np.arctan2(l[0][2]-l[0][0], l[0][3]-l[0][1]))

        if len(cleans) == 0:
            cleans = np.append(cleans, [l[0]], axis=0)
            continue

        similar = False
        for c in cleans:
            beta = np.degrees(np.atan2(c[2]-c[0], c[3]-c[1]))
            other = False
            for d in cleans:
                 if(abs(l[0][0] - d[0]) <= 30 and abs(l[0][1] - d[1] <= 30) and abs(l[0][2] - d[2]) <= 30 and abs(l[0][3] - d[3] <= 30)):
                      other = True
            if abs(alfa-beta) <= 3.5 and other:
                similar = True
                other = False
                break

        if not similar:
            cleans = np.append(cleans, [l[0]], axis=0)
            

for line in [cleans]:
    for x1,y1,x2,y2 in line:
        cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('linedOverlay.png',image)
