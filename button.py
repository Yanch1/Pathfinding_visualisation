import pygame
import os

class Button:
    'Button util'

    def __init__(self, x, y):
        self.clicked = False
        self.rect = pygame.Rect(x,y,100,50)

        self.bIdle = pygame.image.load(os.path.join('nodes', 'button.png'))
        self.bClicked = pygame.image.load(os.path.join('nodes', 'button_clicked.png'))

    def draw(self, window):
        if self.clicked:
            window.blit(self.bClicked, (self.rect.x, self.rect.y))
        else:
            window.blit(self.bIdle, (self.rect.x, self.rect.y))
