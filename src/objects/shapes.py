from math import tan,pi,atan2,acos
from ..math.vector import Vec3
from material import Material

class Shape:
    def __init__(self,position:Vec3, material:Material):
        self.position = position
        self.material = material


class Sphere(Shape):
    def __init__(self,position:Vec3, material:Material,radius:float):
        super.__init__(position,material)
        self.radius = radius
