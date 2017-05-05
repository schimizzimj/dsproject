#! /usr/bin/env python2.7
import math
import random
import pygame
import os
from settings import *
from pygame.locals import *
import spritesheet
import dialogue
import textbox
import scene

sw = SCREEN_SIZE[0]
sh = SCREEN_SIZE[1]
wr = float(sw)/1920
hr = float(sh)/1080
class spidey(object):
	def __init__(self):
		self.img1 = pygame.image.load(os.path.join(IMG_FOLDER, "spiderman1.png"))#get spidey images and resize
		self.img1 = pygame.transform.scale(self.img1, (int(self.img1.get_width()*wr), int(self.img1.get_height()*hr)))
		self.img2 = pygame.image.load(os.path.join(IMG_FOLDER, "spiderman2.png"))
		self.img2 = pygame.transform.scale(self.img2, (int(self.img2.get_width()*wr), int(self.img2.get_height()*hr)))
		self.img3 = pygame.image.load(os.path.join(IMG_FOLDER, "spiderman3.png"))
		self.img3 = pygame.transform.scale(self.img3, (int(self.img3.get_width()*wr), int(self.img3.get_height()*hr)))
		self.img4 = pygame.image.load(os.path.join(IMG_FOLDER, "spiderman3left.png"))
		self.img4 = pygame.transform.scale(self.img4, (int(self.img4.get_width()*wr), int(self.img4.get_height()*hr)))
		self.img5 = pygame.image.load(os.path.join(IMG_FOLDER, "spiderman2left.png"))
		self.img5 = pygame.transform.scale(self.img5, (int(self.img5.get_width()*wr), int(self.img5.get_height()*hr)))
		self.img6 = pygame.image.load(os.path.join(IMG_FOLDER, "spiderman1left.png"))
		self.img6 = pygame.transform.scale(self.img6, (int(self.img6.get_width()*wr), int(self.img6.get_height()*hr)))
		self.pos = [SCREEN_SIZE[0]/2, SCREEN_SIZE[1] * 0.8]#set spidey position
		self.angle = 3.141592 / 2#initialize aiming angle
		self.status = 4#direction spidey is pointing
		self.exists = 1#has he been hit?
	def draw(self, screen):
#		pygame.draw.rect(self.screen, (175, 175, 255), (self.pos[0] - 0.03*sw, self.pos[1] - 0.05*sw, 0.06*sw, 0.1*sw), 0)
		if self.angle < 3.141592/6:#print pointing right
			self.status = 1
			screen.blit(self.img1, (self.pos[0] - 0.05*sw, self.pos[1] - 0.06*sw))
		if self.angle >= 3.141592/6 and self.angle < 3.141592/3:#if slightly rotated left
			self.status = 2
			screen.blit(self.img2, (self.pos[0] - 0.052*sw, self.pos[1] - 0.06*sw))
		if self.angle >= 3.141592/3 and self.angle < 3.141592/2:#more rotations etc
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
		pygame.draw.line(screen, (255, 255, 255), (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]*0.8-0.035*sw), (SCREEN_SIZE[0]/2 + 50*math.cos(self.angle), SCREEN_SIZE[1]*0.8 - 50*math.sin(self.angle)-0.035*sw))#line helps with aiming webs
class spidweb(object):# web class
	def __init__(self, ang, x, y):
		self.vel = [3*math.cos(ang)*hr, -3*math.sin(ang)*hr]#set veocity according to angle of departure
		self.pos = [float(x), float(y)]#set position
		self.age = 0#increment length of time of existance to eventually delete
		self.exists = 1#goes out of existance after collision or expiration
		self.img1 = pygame.image.load(os.path.join(IMG_FOLDER, 'web.png'))#load and resize image
		self.wid = int(self.img1.get_width()*wr)
		self.hei = int(self.img1.get_height()*hr)
		self.img1 = pygame.transform.scale(self.img1, (self.wid, self.hei))
	def draw(self, screen):
		screen.blit(self.img1, (int(self.pos[0]) - self.wid/2, int(self.pos[1]) - self.hei/2))#display image
	def adv(self):
		self.pos[0] = self.pos[0] + self.vel[0]#add velocity to position
		self.pos[1] = self.pos[1] + self.vel[1]
		self.age = self.age + 1#age toward expiration
class enemy(object):#class for viruses
	def __init__(self, x, spd):
		self.pos = [float(x), -40*hr]#set position
		self.wid = 60*wr#variables for size
		self.hei = 40*hr
		self.img1 = pygame.image.load(os.path.join(IMG_FOLDER, "virus.png"))#get and resize image
		self.img1 = pygame.transform.scale(self.img1, (int(self.img1.get_width()*wr), int(self.img1.get_height()*hr)))
		self.speed = spd*hr#set speed
		self.exists = 1#dies after collision or after landing
	def draw(self, screen):
		screen.blit(self.img1, (int(self.pos[0]) - self.img1.get_width()/2, int(self.pos[1]) - self.img1.get_height()/2))#print image of virus
		#pygame.draw.rect(self.screen, (255, 0, 0), (self.pos[0]-self.wid/2, self.pos[1]-self.hei/2, self.wid, self.hei), 0)
	def adv(self):
		self.pos[1] = self.pos[1] + self.speed#add velocity to position
class comput(object):#computers/bases you are protecting
	def __init__(self, x):
		self.pos = [x, SCREEN_SIZE[1]*0.8]#position
		self.status = 0#0 for exists, 1 for is exploding, 2 after has exploded
		self.counter = 0#to time for explosion duration
		self.exists = 1#for advance method, to determine if the object should be deleted
		self.img1 = pygame.image.load(os.path.join(IMG_FOLDER, "computer.png"))#get and resize image for computer and for explosion
		self.imwid = int(self.img1.get_width()*wr)
		self.imhei = int(self.img1.get_height()*hr)
		self.img1 = pygame.transform.scale(self.img1, (self.imwid, self.imhei))
		self.img2 = pygame.image.load(os.path.join(IMG_FOLDER, "explosion.png"))
		self.imwid2 = int(self.img1.get_width()*wr)
		self.imhei2 = int(self.img1.get_height()*hr)
		self.img2 = pygame.transform.scale(self.img2, (self.imwid2, self.imhei2))
		self.tarwid = 120 * wr#width of target rectangle
		self.tarhei = 120 * hr#height of target rectangle
	def draw(self, screen):
		if self.status == 0:#print various images according to status
			screen.blit(self.img1, (self.pos[0] - self.imwid/2.65, self.pos[1] - self.imhei/3.3))
#			pygame.draw.rect(self.screen, (0, 255, 0), (self.pos[0] - self.tarwid/2, self.pos[1] - self.tarhei/2, self.tarwid, self.tarhei), 0)
		if self.status == 1:
			screen.blit(self.img2, (self.pos[0] - self.imwid2/2, self.pos[1] - self.imhei2/2))
#			pygame.draw.rect(self.screen, (255, 255, 0), (self.pos[0] - self.tarwid/2, self.pos[1] - self.tarhei/2, self.tarwid, self.tarhei), 0)
	def adv(self):#advance toward status 2 if in status 1
		if self.status == 1:
			self.counter = self.counter + 1


class SpideyGame(scene.Scene):
	def __init__(self, director, game, post_win):
		scene.Scene.__init__(self, director)
		self.game = game
		self.screen = game.screen
		self.font = pg.font.Font(None, 35) # create font object
		self.enCounter = 0#counts time to spawn new enemies
		self.swCounter = 1#counts time to allow new webs
		self.enList = []
		self.victory = 3600#if you survive for this long you win (60s)
		self.spidey1 = spidey()#initialize spidey, your player
		self.swList = []#declare list of webs you can shoot
		self.post_win = post_win#makes it easier to transition to post-win sequence
		self.compList = [comput(SCREEN_SIZE[0]/11), comput(SCREEN_SIZE[0]/3), comput(2*SCREEN_SIZE[0]/3), comput(10*SCREEN_SIZE[0]/11)]#list of computers to defend
	def events(self):
		event = pygame.event.poll()#check for events
		if event.type == pygame.QUIT:#check for quit
			self.game.director.change_scene(self.game.director.scene_stack.pop()) #return to menu
		if pygame.key.get_pressed() [K_LEFT] != 0:#check for left arrow key
			self.spidey1.angle = self.spidey1.angle + 0.05#aim to the left
			if self.spidey1.angle > 3.2:#not too far left
				self.spidey1.angle = 3.2
		if pygame.key.get_pressed() [K_RIGHT] != 0:#see above, but to right
			self.spidey1.angle = self.spidey1.angle - 0.05
			if self.spidey1.angle < -0.06:
				self.spidey1.angle = -0.06
		if pygame.key.get_pressed() [K_UP] != 0 and self.swCounter > 40:#check for up key to shoot web
			self.swList.append(spidweb(self.spidey1.angle, SCREEN_SIZE[0]/2, SCREEN_SIZE[1]*0.8 - 0.035 * sw))
			self.swCounter = 0#reset counter to disallow rapid-fire shooting
	def update(self):
		self.victory -= 1#countdown to victory!!
		if (self.enCounter % 100 == 0):#spawn enemy once every 100 cycles
			self.enList.append(enemy(random.randint(10, SCREEN_SIZE[0]-10), 1))#add enemy to list
		for foe in self.enList:#advance position of viruses
			foe.adv()
		for webs in self.swList:#advance position of webs
			webs.adv()
		for comps in self.compList:#advance state of computers as appropriate
			comps.adv()
		self.compList = [ comps for comps in self.compList if comps.counter < 30 ]#delete computers that have reached state 2
		for foe in self.enList:#check for virus/web collisions
			for webs in self.swList:
				if abs(foe.pos[0] - webs.pos[0]) < webs.wid/5 + foe.wid/2 and abs(foe.pos[1] - webs.pos[1]) < webs.hei/5 + foe.hei/2:
					webs.exists = 0#neither object exists after collision
					foe.exists = 0
		for foe in self.enList:#check for spidey-virus collisions
			if foe.pos[1] + foe.hei/2 > self.spidey1.pos[1] - 0.03*sw and abs(foe.pos[0]-self.spidey1.pos[0]) < foe.wid/2 + 0.05*sw:
				self.game.director.change_scene(self.game.director.scene_stack.pop())#if collision occurs you die

			for comps in self.compList:#check for computer-virus collisions
				if foe.pos[1]+foe.hei/2 > comps.pos[1]-comps.tarhei/2 and abs(foe.pos[0] - comps.pos[0]) < foe.wid/2 + comps.tarwid/2:
					foe.exists = 0#if collsion occurs virus no longer exists
					comps.status = 1#computer goes into explosion stage, will cease to exist soon
		if len(self.compList) == 0:#if all computers are gone, game over
			self.game.director.change_scene(self.game.director.scene_stack.pop())
		self.enList = [ foe for foe in self.enList if foe.pos[1] < 30+(3*SCREEN_SIZE[1]/4) and foe.exists ]#if virus does not exist, delete it
		self.swList = [ webs for webs in self.swList if webs.age < 1102*wr and webs.exists ]#delete webs that should not exist
		self.enCounter = self.enCounter + 1#increment spawning counters
		self.swCounter = self.swCounter + 1
		if self.victory <= 0:#if coundown completes, you win
			self.game.json['npcs'][0]['logic']['completed'] = True
			self.game.director.change_scene(self.game.director.scene_stack[-1])
			self.game.director.scene.render()
			self.game.director.change_scene(self.post_win)

	def render(self):
		self.screen.fill((53, 97, 168))#print background
		pygame.draw.rect(self.screen, (113, 112, 119), (0, SCREEN_SIZE[1]*0.8, SCREEN_SIZE[0], SCREEN_SIZE[1]*0.2), 0)#draw other part fo background
		for comps in self.compList:#draw computers by function
			comps.draw(self.screen)
		self.spidey1.draw(self.screen)#draw spidey according to function
		for foe in self.enList:#draw viruses
			foe.draw(self.screen)
		for webs in self.swList:#draw webs
			webs.draw(self.screen)
		timer_string = "Time remaining: " + str(self.victory)#print timer and time left
		time_left = self.font.render(str(timer_string), 1, WHITE)
		self.screen.blit(time_left, (SCREEN_SIZE[0] - 300, 10))
