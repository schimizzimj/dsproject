import pygame, sys
from pygame.locals import *
import math
import shapely
from shapely.geometry import MultiPoint

pygame.init()

width = 500
height = 400
SURFACE = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('my drawing')

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
GREEN = (0, 255, 0)

# set background color
SURFACE.fill(WHITE)

#draw flower
xc = width/2
yc = height/2
pygame.draw.line(SURFACE, GREEN, (xc, yc), (xc, height-10), 4)
petals = [(xc-70, yc-100), (xc,yc-60), (xc+70, yc-100), (xc+60, yc-30), (xc+120, yc+20), (xc+45, yc+50), (xc, yc+110), (xc-45, yc+50), (xc-120, yc), (xc-60, yc-30)]
pygame.draw.polygon(SURFACE, PINK, petals)
pygame.draw.circle(SURFACE, YELLOW, (xc, yc), 50)

#display screen
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

# generate polygon
def ngon(n = 5, r = 10):
    coords = []
    for p in range(n):
        coords.add(r*math.cos(360*p/n), r*math.sin(360*p/n))

    return coords
