import pygame

class Node:
    'single grid node class'

    def __init__(self):
        self.id = 0
        self.color = 0 # 0 - white
        self.neighbours = []
        self.rect = pygame.Rect(0,0,50,50)
        self.handled = False
        self.isWall = False
        self.x = 0
        self.y = 0
        self.parent = None
        self.inOpenSet = False
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False
    
    def __lt__(self,other):
        return self.f < other.f


    def draw(self, window, x, y, sprites):
        if self.color == 0:
            window.blit(sprites[0], (x, y))
        elif self.color == 1:
            window.blit(sprites[1], (x, y))
        elif self.color == 2:
            window.blit(sprites[2], (x, y))
        elif self.color == 3:
            window.blit(sprites[3], (x, y))
        elif self.color == 4:
            window.blit(sprites[4], (x, y))

    def getColor(self):
        return self.color