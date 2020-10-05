import pygame

def isHolding(points):
    val = False
    for point in points:
        if point.move:
            val = True
    
    return val

class Point:
    'class for start/finish points'

    def __init__(self, x, y, sprite):
        self.rect = pygame.Rect(x,y,50,50)
        self.sprite = sprite
        self.move = False
        self.nodeID = 0

    def draw(self, window):
        window.blit(self.sprite, (self.rect.x, self.rect.y))
