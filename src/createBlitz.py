import pygame

colours = {
    'red' : (255,0,0),
    'green' : (0,255,0),
    'blue' : (0,0,255),
    'yellow' : (255,255,0),
    'white' : (255,255,255),
    'black' : (0,0,0)
}

    
class RectBlit():
    
    def  __init__(self, colour, coordDimensions):
        self.colour = colour
        self.rect = coordDimensions
        
    def createBlit(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)
        
  
        
    
