#!/usr/bin/env python2.7
import sys
import pygame

# this code is based off the pygame tutorial from the following URL:
# www.nerdparadise.com/programming/pygame/part1

pygame.init()
screen = pygame.display.set_mode((500))
done = False

is_green = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_green = not is_green # changes from green to yellow
    
    if is_green:
        color = (0, 100, 0) # dark green 
    else:
        color = (255, 255, 0) # yellow
    
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60)) # draws a green rectangle
    
    # at the end
    pygame.display.flip()
