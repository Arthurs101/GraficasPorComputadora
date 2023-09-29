from .objects.shapes import *
from .objects.material import *
from .math.vector import Vec3
from .math.intercept import Intercept
from pygame.surface import Surface
from RAYTRACE_CONSTANTS import *
import pygame

def ray_intersect (origin:Vec3,dir:Vec3, obj:Shape):
    if isinstance(obj, Sphere):
        L = obj.position.__sub__(origin)
        tca = L.dot(dir)
        d = (L.__magnitude__()**2 - tca**2)**0.5
        if d > obj.radius:
            return None
        
        thc = (obj.radius**2-d**2)**0.5
        t0:float = tca-thc
        t1 = tca+thc
        
        if t0<0:
            t0=t1
        if t0<0:
            return None
        
        P = origin.__add__(dir.__mul__(t0))
        normal = P.__sub__(obj.position)
        normal = normal.__normalize__()
        
        u = (atan2(normal[2],normal[0])/(2*pi))+0.5
        v = acos(normal[1])/pi

        return Intercept(distance=t0,
                         point=P,
                         normal=normal,
                         texcoords=(u,v),
                         obj=obj)

def getTxtColor(intercept : Intercept , material : Material):
    tX= intercept.texcoords[0] * material.texture.bitmap.get_width()
    tY = intercept.texcoords[1] * material.texture.bitmap.get_height()
    _texcolor:pygame.color.Color = material.texture.bitmap.get_at((int(tX),int(tY)))
    texcolor:Vec3 = Vec3(_texcolor.r/255, _texcolor.g/255, _texcolor.b/255)
    return Vec3(material.clr.x * texcolor.r, material.clr.y * texcolor.g, material.clr.z *texcolor.b)

def fragment_color(intercept : Intercept, raydir: Vec3,obj : Shape, cicle = 0 , envMap: Surface= None ):
    if intercept ==  None:
        if envMap == None:
            return None
        else:
            x = int((atan2(raydir.y,raydir.x)/(2*pi)+0.5)*envMap.get_width())
            y = int(acos(raydir.y)/pi*envMap.get_height())
            _fragColor:pygame.color.Color = envMap.get_at(x,y)
            fragColor:Vec3 = Vec3(_fragColor.r/255, _fragColor.g/255, _fragColor.b/255)
    
    Fragcolor = obj.material.clr

    if obj.material.texture and intercept.texcoords:
        Fragcolor = getTxtColor(intercept, obj.material)
    
    if obj.material.type == OPAQUE:
        pass
    elif obj.material.type == REFLECTIVE:
        pass