#This was created to create a sphere class in Python
#Arturo Ortiz
#arturo.ortiz1@marist.edu

import math


class Sphere(GraphicsObject):
    def __init__(self,radius):
        self.radius= radius
        self.surfacearea= (4/3) *math.pi * self.radius **3
        self.volume= 4* math.pi* self.radius **2
        
    def getRadius(self):
        return self.radius
    
    def surfaceArea(self):
        return self.surfacearea
    
    def volume(self):
        return self.volume    
