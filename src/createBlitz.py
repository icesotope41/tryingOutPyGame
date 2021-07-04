import pygame
from pygame import display
from pygame.surface import Surface 

simpleRect = color, rect = (255, 0, 0), (200, 100, 200, 100)



def drawShapes(surface, rectType):
    pygame.draw.rect(surface, rectType)