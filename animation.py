import pygame, sys
from pygame.locals import *

pygame.init()

# display window
w = 400
h = 400
SURF = pygame.display.set_mode((w, h), 0, 32)
pygame.display.set_caption('animated square')

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SURF.fill(WHITE)

# draw square
xi = 50
yi = 170
dy = 0
s = 30
pygame.draw.rect(SURF, RED, pygame.Rect(xi, yi, s, s))

# set up clock
clock = pygame.time.Clock()

while xi < w-2*s:
    # slow down clock
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # clear screen
    SURF.fill(WHITE)


    xi += 10
    dy += 30
    dy %= 60
    yi = 200 + dy
    pygame.draw.rect(SURF, RED, pygame.Rect(xi, yi, 30, 30))
    pygame.display.flip()

pygame.quit()
