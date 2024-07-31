import math
import numpy as np
from numpy.linalg import inv


class Line:
    
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.slope = float((y1 - y0)/(x1 - x0))
        self.theta = math.atan((y1-y0)/(x1-x0))
        self.r = math.dist([x0,y0],[x1,y1])
        self.intercept = y0 - self.slope*x0

    def __str__(self):
        return ("radius: " + str(self.r) + " theta: " + "{:.4f}".format(self.theta))

    def getx0(self):
         return self.x0
    
    def gety0(self):
         return self.y0
    
    def getx1(self):
         return self.x1
    
    def gety1(self):
         return self.y1
    
    def getSlope(self):
        return self.slope
   
    def getTheta(self):
        return self.theta
    
    def getR(self):
        return self.r
    
    def getInter(self):
         return self.intercept


class Corner:
        
        def __init__(self, l1, l2):
            
             self.l1 = l1
             self.l2 = l2
             self.line1 = Line(self.l1.getx0(),self.l1.gety0(),self.l1.getx1(),self.l1.gety1())
             self.line2 = Line(self.l2.getx0(),self.l2.gety0(),self.l2.getx1(),self.l2.gety1())
             self.poi = None 
             self.angle = None
             
             self.xends1 = [self.line1.getx0(), self.line1.getx1()]
             self.yends1 = [self.line1.gety0(), self.line1.gety1()]
             self.xends2 = [self.line2.getx0(), self.line2.getx1()]
             self.yends2 = [self.line2.gety0(), self.line2.gety1()]
             
             refA = np.array([[1., float(-1*self.line1.getSlope())], [1., float(-1*self.line2.getSlope())]])
             refS = np.array([[self.line1.getInter()],[self.line2.getInter()]])
             refInv = np.linalg.inv(refA)
             point = np.matmul(refInv, refS)

             if(point[0] >= min(self.xends1) and point[0] <= max(self.xends1) and point[1] >= min(self.yends1) and point[1] <= max(self.yends1) and point[0] >= min(self.xends2) and point[0] <= max(self.xends2) and point[1] >= min(self.yends2) and point[1] <= max(self.yends2)):
            
                self.poi = point
                self.angle =  abs(self.l1.getTheta()-self.l2.getTheta())


        def __str__(self):
             return(self.line1, self.line2)
        
        def getLine1(self):
             return self.line1
        
        def getLine2(self):
             return self.line2
        
        def getPoi(self):
                return self.poi
         
        
        def getAngle(self):
                return self.angle
        
        def getAngleInDeg(self):
             return self.angle*180/math.pi
