#! /usr/bin/env python2.7
import math
import random
import pygame
from settings import *
from pygame.locals import *
import spritesheet

sw = SCREEN_SIZE[0]
sh = SCREEN_SIZE[1]
wr = float(sw)/1920
hr = float(sh)/1080
class spidey(object):
	def __init__(self):
		self.img1 = pygame.image.load("img/spiderman1.png")
		self.img1 = pygame.transform.scale(self.img1, (int(self.img1.get_width()*wr), int(self.img1.get_height()*hr)))
		self.img2 = pygame.image.load("img/spiderman2.png")
		self.img2 = pygame.transform.scale(self.img2, (int(self.img2.get_width()*wr), int(self.img2.get_height()*hr)))
		self.img3 = pygame.image.load("img/spiderman3.png")
		self.img3 = pygame.transform.scale(self.img3, (int(self.img3.get_width()*wr), int(self.img3.get_height()*hr)))
		self.img4 = pygame.image.load("img/spiderman3left.png")
		self.img4 = pygame.transform.scale(self.img4, (int(self.img4.get_width()*wr), int(self.img4.get_height()*hr)))
		self.img5 = pygame.image.load("img/spiderman2left.png")
		self.img5 = pygame.transform.scale(self.img5, (int(self.img5.get_width()*wr), int(self.img5.get_height()*hr)))
		self.img6 = pygame.image.load("img/spiderman1left.png")
		self.img6 = pygame.transform.scale(self.img6, (int(self.img6.get_width()*wr), int(self.img6.get_height()*hr)))
		self.pos = [SCREEN_SIZE[0]/2, SCREEN_SIZE[1] * 0.8]
		self.angle = 3.141592 / 2
		self.status = 4
		self.exists = 1
	def draw(self, screen):
#		pygame.draw.rect(screen, (175, 175, 255), (self.pos[0] - 0.03*sw, self.pos[1] - 0.05*sw, 0.06*sw, 0.1*sw), 0)
		if self.angle < 3.141592/6:
			self.status = 1
			screen.blit(self.img1, (self.pos[0] - 0.05*sw, self.pos[1] - 0.06*sw))
		if self.angle >= 3.141592/6 and self.angle < 3.141592/3:
			self.status = 2
			screen.blit(self.img2, (self.pos[0] - 0.052*sw, self.pos[1] - 0.06*sw))
		if self.angle >= 3.141592/3 and self.angle < 3.141592/2:
			self.status = 3
			screen.blit(self.img3, (self.pos[0] - 0.03*sw, self.pos[1] - 0.075*sw))
		if self.angle >= 3.141592/2 and self.angle < 2*3.141592/3:
			self.status = 4
			screen.blit(self.img4, (self.pos[0] - 0.06*sw, self.pos[1] - 0.075*sw))
		if self.angle >= 2*3.141592/3 and self.angle < 5*3.141592/6:
			self.status = 5
			screen.blit(self.img5, (self.pos[0] - 0.045*sw, self.pos[1] - 0.06*sw))
		if self.angle > 5*3.141592/6:
			self.status = 6
			screen.blit(self.img6, (self.pos[0] - 0.06*sw, self.pos[1] - 0.06*sw))
		pygame.draw.line(screen, (255, 255, 255), (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]*0.8-0.035*sw), (SCREEN_SIZE[0]/2 + 50*math.cos(self.angle), SCREEN_SIZE[1]*0.8 - 50*math.sin(self.angle)-0.035*sw))
class spidweb(object):
	def __init__(self, ang, x, y):
		self.vel = [3*math.cos(ang)*hr, -3*math.sin(ang)*hr]
		self.pos = [float(x), float(y)]
		self.age = 0
		self.exists = 1
		self.img1 = pygame.image.load("img/web.png")
		self.wid = int(self.img1.get_width()*wr)
		self.hei = int(self.img1.get_height()*hr)
		self.img1 = pygame.transform.scale(self.img1, (self.wid, self.hei))
	def draw(self, screen):
		screen.blit(self.img1, (int(self.pos[0]) - self.wid/2, int(self.pos[1]) - self.hei/2))
	def adv(self):
		self.pos[0] = self.pos[0] + self.vel[0]
		self.pos[1] = self.pos[1] + self.vel[1]
		self.age = self.age + 1
class enemy(object):
	def __init__(self, x, spd):
		self.pos = [float(x), -40*hr]
		self.wid = 60*wr
		self.hei = 40*hr
		self.img1 = pygame.image.load("img/virus.png")
		self.img1 = pygame.transform.scale(self.img1, (int(self.img1.get_width()*wr), int(self.img1.get_height()*hr)))
		self.speed = spd*hr
		self.exists = 1
	def draw(self, screen):
		screen.blit(self.img1, (int(self.pos[0]) - self.img1.get_width()/2, int(self.pos[1]) - self.img1.get_height()/2))
		#pygame.draw.rect(screen, (255, 0, 0), (self.pos[0]-self.wid/2, self.pos[1]-self.hei/2, self.wid, self.hei), 0)
	def adv(self):
		self.pos[1] = self.pos[1] + self.speed
class comput(object):
	def __init__(self, x):
		self.pos = [x, SCREEN_SIZE[1]*0.8]
		self.status = 0
		self.counter = 0
		self.exists = 1
		self.img1 = pygame.image.load("img/computer.png")
		self.imwid = int(self.img1.get_width()*wr)
		self.imhei = int(self.img1.get_height()*hr)
		self.img1 = pygame.transform.scale(self.img1, (self.imwid, self.imhei))
		self.img2 = pygame.image.load("img/explosion.png")
		self.imwid2 = int(self.img1.get_width()*wr)
		self.imhei2 = int(self.img1.get_height()*hr)
		self.img2 = pygame.transform.scale(self.img2, (self.imwid2, self.imhei2))
		self.tarwid = 120 * wr
		self.tarhei = 120 * hr
	def draw(self, screen):
		if self.status == 0:
			screen.blit(self.img1, (self.pos[0] - self.imwid/2.65, self.pos[1] - self.imhei/3.3))
#			pygame.draw.rect(screen, (0, 255, 0), (self.pos[0] - self.tarwid/2, self.pos[1] - self.tarhei/2, self.tarwid, self.tarhei), 0)
		if self.status == 1:
			screen.blit(self.img2, (self.pos[0] - self.imwid2/2, self.pos[1] - self.imhei2/2))
#			pygame.draw.rect(screen, (255, 255, 0), (self.pos[0] - self.tarwid/2, self.pos[1] - self.tarhei/2, self.tarwid, self.tarhei), 0)
	def adv(self):
		if self.status == 1:
			self.counter = self.counter + 1
screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
pygame.display.flip()
over = 0
enCounter = 0
swCounter = 1
enList = [enemy(120, 1)]
spidey1 = spidey()
swList = []
compList = [comput(SCREEN_SIZE[0]/11), comput(SCREEN_SIZE[0]/3), comput(2*SCREEN_SIZE[0]/3), comput(10*SCREEN_SIZE[0]/11)]
while over == 0:
	if pygame.key.get_pressed() [K_LEFT] != 0:
		spidey1.angle = spidey1.angle + 0.05
		if spidey1.angle > 3.2:
			spidey1.angle = 3.2
	if pygame.key.get_pressed() [K_RIGHT] != 0:
		spidey1.angle = spidey1.angle - 0.05
		if spidey1.angle < -0.06:
			spidey1.angle = -0.06
	if pygame.key.get_pressed() [K_UP] != 0 and swCounter > 40:
		swList.append(spidweb(spidey1.angle, SCREEN_SIZE[0]/2, SCREEN_SIZE[1]*0.8 - 0.035 * sw))
		swCounter = 0
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		over = 3
	if (enCounter % 100 == 0):
		enList.append(enemy(random.randint(10, SCREEN_SIZE[0]-10), 1))
	for foe in enList:
		foe.adv()
	for webs in swList:
		webs.adv()
	for comps in compList:
		comps.adv()
	compList = [ comps for comps in compList if comps.counter < 30 ]
	for foe in enList:
		for webs in swList:
			if abs(foe.pos[0] - webs.pos[0]) < webs.wid/5 + foe.wid/2 and abs(foe.pos[1] - webs.pos[1]) < webs.hei/5 + foe.hei/2:
				webs.exists = 0
				foe.exists = 0
	for foe in enList:
		if foe.pos[1] + foe.hei/2 > spidey1.pos[1] - 0.03*sw and abs(foe.pos[0]-spidey1.pos[0]) < foe.wid/2 + 0.05*sw:
			over = 2
		for comps in compList:
			if foe.pos[1]+foe.hei/2 > comps.pos[1]-comps.tarhei/2 and abs(foe.pos[0] - comps.pos[0]) < foe.wid/2 + comps.tarwid/2:
				foe.exists = 0
				comps.status = 1
	if len(compList) == 0:
		over = 2
	enList = [ foe for foe in enList if foe.pos[1] < 30+(3*SCREEN_SIZE[1]/4) and foe.exists ]
	swList = [ webs for webs in swList if webs.age < 1102*wr and webs.exists ]
	screen.fill((53, 97, 168))
	pygame.draw.rect(screen, (113, 112, 119), (0, SCREEN_SIZE[1]*0.8, SCREEN_SIZE[0], SCREEN_SIZE[1]*0.2), 0)
	for comps in compList:
		comps.draw(screen)
	spidey1.draw(screen)
	for foe in enList:
		foe.draw(screen)
	for webs in swList:
		webs.draw(screen)
	pygame.display.flip()
	enCounter = enCounter + 1
	swCounter = swCounter + 1
