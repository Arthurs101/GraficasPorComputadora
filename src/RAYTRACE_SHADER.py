from .objects import shapes as sp
from .math.vector import Vec3

def ray_intersect (origin:Vec3,dir:Vec3, obj:sp.Shape):
    if isinstance(dir, sp.Sphere):
        L = obj.position.__sub__(origin)
        tca = L.dot(dir)
        d = (L.__magnitude__()**2 - tca**2)**0.5