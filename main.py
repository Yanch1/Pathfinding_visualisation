import random
import os
import time
import pygame

from grid import Node
from button import Button
from point import Point, isHolding
import astar


# sprites
START_POINT = pygame.image.load(os.path.join('nodes', 'man.png'))
FINISH_POINT = pygame.image.load(os.path.join('nodes', 'house.png'))

NODE_WHITE = pygame.image.load(os.path.join('nodes', 'white.png'))
NODE_BLACK = pygame.image.load(os.path.join('nodes', 'black.png'))
NODE_RED = pygame.image.load(os.path.join('nodes', 'red.png'))
NODE_BLUE = pygame.image.load(os.path.join('nodes', 'blue.png'))
NODE_GREEN = pygame.image.load(os.path.join('nodes', 'green.png'))
sprites = [NODE_WHITE, NODE_BLACK, NODE_RED, NODE_BLUE, NODE_GREEN]

WIDTH, HEIGHT = 500, 560
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('pathfinding')


def createGrid():
    id = 0
    grid = [[Node() for i in range(10)] for j in range(10)]

    for i in range(10):
        for j in range(10):
            grid[i][j].rect.topleft = (i * 50, j * 50)
            grid[i][j].id = id
            grid[i][j].x = i
            grid[i][j].y = j
            id += 1            
   
    return grid

def getNeighbours(grid):
    for i in range(10):
        for j in range(10):
            if i > 0:
                grid[i][j].neighbours.append(grid[i-1][j])
            if j > 0:
                grid[i][j].neighbours.append(grid[i][j-1])
            if i < 9:
                grid[i][j].neighbours.append(grid[i+1][j])
            if j < 9:
                grid[i][j].neighbours.append(grid[i][j+1])

def block_events():
    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.QUIT)

def resume_events():
    pygame.event.set_allowed(None)

def start():

    run = True
    FPS = 60
    clock = pygame.time.Clock()
    grid = createGrid()
    getNeighbours(grid)
    bFind = Button(390, 505)
    pStart = Point(0,0,START_POINT)
    pFinish = Point(100,300, FINISH_POINT)

    timer = 0
    itemHeld = False


    def redraw_window():
        WIN.fill((255,255,255))

        for i in range(10):
            for j in range(10):
                grid[i][j].draw(WIN, i * 50, j * 50, sprites)

        pStart.draw(WIN)
        pFinish.draw(WIN)
        bFind.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        if bFind.clicked == True:
            if timer > 0:
                timer -= 1
            if timer == 0:
                bFind.clicked = False

        for event in pygame.event.get():
            # follow mouse
            if pStart.move:
                pStart.rect.topleft = pygame.mouse.get_pos()
            elif pFinish.move:
                pFinish.rect.topleft = pygame.mouse.get_pos()
                
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # reset colors on click
                for i in range(10):
                    for j in range(10):
                        if grid[i][j].getColor() != 0 and grid[i][j].getColor() != 1:
                            grid[i][j].color = 0

                mousePos = pygame.mouse.get_pos()
                
                # move S/F points
                if pStart.rect.collidepoint(mousePos) and not pStart.move and not pFinish.move:
                    pStart.move = True
                    itemHeld = True
                elif pFinish.rect.collidepoint(mousePos) and not pFinish.move and not pStart.move:
                    pFinish.move = True
                    itemHeld = True
                elif pStart.move:
                    for i in range(10):
                        for j in range(10):
                            if grid[i][j].rect.collidepoint(mousePos):
                                if grid[i][j].color != 1 and grid[i][j].rect.topleft != pFinish.rect.topleft:
                                    pStart.rect.x = i * 50
                                    pStart.rect.y = j * 50
                                    pStart.move = False
                elif pFinish.move:
                    for i in range(10):
                        for j in range(10):
                            if grid[i][j].rect.collidepoint(mousePos):
                                if grid[i][j].color != 1 and grid[i][j].rect.topleft != pStart.rect.topleft:
                                    pFinish.rect.x = i * 50
                                    pFinish.rect.y = j * 50
                                    pFinish.move = False

                if not itemHeld:
                    nodes = []
                    for line in grid:
                        for node in line:
                            nodes.append(node)

                    clicked = [node for node in nodes if node.rect.collidepoint(mousePos)]

                    for i in range(10):
                        for j in range(10):
                            for node in clicked:
                                if node.id == grid[i][j].id:
                                        if grid[i][j].color == 0:
                                            grid[i][j].color = 1
                                            grid[i][j].isWall = True
                                        elif grid[i][j].color == 1:
                                            grid[i][j].color = 0
                                            grid[i][j].isWall = False

                itemHeld = isHolding([pStart, pFinish])

                # check button clicks
                if bFind.rect.collidepoint(mousePos):
                    bFind.clicked = True
                    timer = 5
                    a = None
                    b = None
                    for i in range(10):
                        for j in range(10):
                            if pStart.rect.topleft == grid[i][j].rect.topleft:
                                a = grid[i][j]
                            if pFinish.rect.topleft == grid[i][j].rect.topleft:
                                b = grid[i][j]

                    if a is not None and b is not None:
                        args = [WIN, pStart, pFinish, bFind, sprites]
                        astar.aStar(a, b, grid, args)                                            

        redraw_window()

start()