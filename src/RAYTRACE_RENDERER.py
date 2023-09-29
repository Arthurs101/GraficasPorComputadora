from math import tan,pi,atan2,acos
from .RAYTRACE_CONSTANTS import *
from .math.vector import Vec3
from RAYTRACE_SHADER import *
import pygame
import random
class RayTraceInstance:
    def __init__(self,window,camPos:Vec3,recursionDepth = MAX_RECURSIVE):
        self.window = window
        self.recursion_depth = recursionDepth
        self.camPos = camPos

        _,_,self.width,self.height = window.get_rect()
        

        #set up view port
        self.set_viewport(self.camPos.x,self.camPos.y,self.width,self.height)

        #set up projection
        self.set_perspective()

        #map on the scene
        self.scene = []
        self.lights = []
        self.envMAP = None

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
    
    def setClrColor(self, clr:Vec3):
        self.currColor = Vec3(clr.x * 255,clr.y * 255,clr.y * 255)

    def clearWindow(self):
        self.window.fill(self.clrColor)

    def clrPoint(self, x,y, clr:Vec3 = None):
        y = self.height - y 
        if (0 <= x <= self.width) and (0 <= y <= self.height):
            if clr:
                self.window.set_at((x,y),
                                   (int(clr.x * 255),
                                    int(clr.y * 255),
                                    int(clr.y * 255)))
            else: 
                self.window.set_at((x,y),
                                   (int(self.currColor.x),
                                    int(self.currColor.y),
                                    int(self.currColor.z)))

    def castRay(self,dir,origin,sceneObj=None,recursion=0):
        if recursion >= self.recursion_depth:
            return None
        depth = float('inf')
        intercept=None
        hit = None
      

        for obj in self.scene:
            if sceneObj != obj:
                intercept = ray_intersect(origin,dir,sceneObj)
                if intercept!=None:
                    if intercept.distance<depth:
                        hit = intercept
                        depth = intercept.distance
        
        return hit

    def render():
        pass
