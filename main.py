import pygame
import numpy
import sys
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
Clock = pygame.time.Clock()

def drawGrid():
    blockSize = 128
    for x in range(0, SCREEN_WIDTH, blockSize):
        for y in range(0, SCREEN_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, "white", rect, 1)

while(True):
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    Clock.tick(60)    
    

