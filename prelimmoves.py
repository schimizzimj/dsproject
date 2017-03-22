#! /usr/bin/env python2.7-32

import pygame
screen = pygame.display.set_mode((640,400))
screen.fill((0,0,255))
pygame.display.flip()
running = 1
x = 75
y = 200
dx = 0
dy = 0
ycounter = 0
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	elif event.type == pygame.KEYDOWN:	
		if event.key == pygame.K_LEFT:
			dx = -3
		if event.key == pygame.K_RIGHT:
			dx = 3
		if ycounter <= 0:
			dy = 0	
			if event.key == pygame.K_UP:
				dy = -7
				ycounter = 13
	if ycounter > 0:
		dy += 1
		ycounter -= 1
	x += dx
	y += dy
	screen.fill((0,0,255))
	pygame.draw.rect(screen, (255,0,0), (x, y, 20, 20), 0)
	pygame.display.flip()
	if x > 621:
		x = 621
	if x < 19:
		x = 19
	if y > 200:
		y = 200
		dy = 0
