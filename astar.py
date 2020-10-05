from collections import deque
from queue import PriorityQueue
import math
import time
import pygame

def calculateH(current, destination, method='m'):
    if method == 'm':
        h = abs(destination.x - current.x) + abs(destination.y - current.y)
    elif method == 'e':
        h = math.sqrt(pow((destination.x - current.x), 2) + pow((destination.y - current.y), 2))
    else:
        print('incorrect method, using manhattan distance as default')
        h = abs(destination.x - current.x) + abs(destination.y - current.y)
    
    current.h = h

def update_win(WIN, grid, pStart, pFinish, bFind, sprites):
    pygame.event.pump()
    WIN.fill((255,255,255))

    for i in range(10):
        for j in range(10):
            grid[i][j].draw(WIN, i * 50, j * 50, sprites)

    pStart.draw(WIN)
    pFinish.draw(WIN)
    bFind.draw(WIN)

    pygame.display.update()
    time.sleep(0.2)

def aStar(pStart, pFinish,grid, args):
    path = [] # stack - append / pop

    openSet = PriorityQueue(maxsize=0)
    closedSet = []
    pStart.g = 0
    calculateH(pStart, pFinish)
    pStart.f = pStart.h + pStart.g

    openSet.put((pStart.f, pStart))
    pStart.inOpenSet = True

    while(not openSet.empty()):

        #grab lowest fscore node
        currentNode = (openSet.get())[1]
        currentNode.inOpenSet = False

        # move current node to closed set
        closedSet.append(currentNode)
        currentNode.color = 2
        update_win(args[0], grid, args[1], args[2], args[3], args[4])
        
        if currentNode == pFinish:
            path.append(currentNode)
            break
        
        for n in currentNode.neighbours:
            if not n.isWall:
                if n in closedSet:
                    continue

                if not n.inOpenSet:
                    n.parent = currentNode
                    calculateH(n, pFinish)
                    n.g = n.parent.g + 1
                    n.f = n.h + n.g
                    openSet.put((n.f, n))
                    n.inOpenSet = True
                    n.color = 3
                    update_win(args[0], grid, args[1], args[2], args[3], args[4])
                else:
                    tempG = currentNode.g + 1
                    if tempG < n.g:
                        n.g = tempG
                        n.parent = currentNode
    
    while not openSet.empty():
        a = openSet.get()
        a[1].inOpenSet = False

    curr = path.pop()
    
    while curr != pStart:
        curr.color = 4
        curr = curr.parent
        update_win(args[0], grid, args[1], args[2], args[3], args[4])
    
    pStart.color = 4

    
    


