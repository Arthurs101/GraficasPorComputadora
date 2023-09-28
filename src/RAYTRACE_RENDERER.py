from math import tan,pi,atan2,acos
from . import RAYTRACE_CONSTANTS as rc
from .math.vector import Vec3
import pygame
import random
class RayTraceInstance:
    def __init__(self,window,camPos:Vec3):
        self.window = window
        self.recursion_depth = rc.MAX_RECURSIVE
        self.camPos = camPos

        _,_,self.width,self.height = window.get_rect()
        
        #set up view port
        self.set_viewport(self.camPos.x,self.camPos.y,self.width,self.height)

        #set up projection

    def set_viewport(self, posx, posy, height, width):
        self.Vpx = posx
        self.Vpy = posy
        self.Vph = self.height
        self.Vpw = self.width
    
    def set_perspective(self, fov = 60 , n = 0.1):
        aspectRatio =  self.vpWidth/self.vpHeight
        self.nearPlane = n
        self.topEdge = tan((fov*pi/180)/2)*self.nearPlane
        self.rightEdge = self.topEdge*aspectRatio

    def clearColor(self, clr:Vec3):
        self.clrColor = Vec3(clr.x *255 , clr.y *255 ,clr.z *255)