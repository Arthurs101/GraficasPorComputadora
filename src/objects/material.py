import pygame
from pygame.locals import *

from .. import RAYTRACE_CONSTANTS as rc

class Material:
    def __init__(self, clr = (1,1,1) , shine_f = 1 , Kspec = 1, Krefraction = 1, type = rc.OPAQUE , texture = ''):
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
        bitmap = pygame.image.load(fileLocation)

