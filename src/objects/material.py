import pygame
from pygame.locals import *
from ..math.vector import Vec3
from .. import RAYTRACE_CONSTANTS as rc

class Material:
    def __init__(self, clr = Vec3(1,1,1) , shine_f = 1 , Kspec = 1, Krefraction = 1, type = rc.OPAQUE , texture = ''):
        self.clr = clr
        self.spec = shine_f
        self.Kspec = Kspec
        self.Kr = Krefraction
        self.type = type
        if texture != '':
            self.texture = Texture(texture)
        else:
            self.texture = None

class Texture:
    def __init__(self,fileLocation):
        self.bitmap :pygame.surface.Surface = pygame.image.load(fileLocation)

