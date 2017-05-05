#! /usr/bin/env python2.7

import pygame
import os
from settings import *
from pygame.locals import *
import random
import dialogue
import textbox
import scene

sw = SCREEN_SIZE[0]
sh = SCREEN_SIZE[1]
wr = float(sw)/1920
hr = float(sh)/1080

class card(object):
	def __init__(self, type, x, y):
		self.type = type;
		self.x = x
		self.y = y
		self.wid = 3 * sw / 16
		self.hei = 3 * sh / 16
		self.status = 0
		if type == 1:
			self.image = pygame.image.load(os.path.join(IMG_FOLDER, "andgate.png"))
			self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*wr), int(self.image.get_height()*hr)))
		if type == 2:
			self.image = pygame.image.load(os.path.join(IMG_FOLDER, "orgate.png"))
			self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*wr), int(self.image.get_height()*hr)))
		if type == 3:
			self.image = pygame.image.load(os.path.join(IMG_FOLDER, "nandgate.png"))
			self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*wr), int(self.image.get_height()*hr)))
		if type == 4:
			self.image = pygame.image.load(os.path.join(IMG_FOLDER, "norgate.png"))
			self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*wr), int(self.image.get_height()*hr)))
		if type == 5:
			self.image = pygame.image.load(os.path.join(IMG_FOLDER, "notgate.png"))
			self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*wr), int(self.image.get_height()*hr)))
		if type == 6:
			self.image = pygame.image.load(os.path.join(IMG_FOLDER, "xorgate.png"))
			self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*wr), int(self.image.get_height()*hr)))
		if type == 7:
			self.image = pygame.image.load(os.path.join(IMG_FOLDER, "shark.png"))
			self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*wr), int(self.image.get_height()*hr)))
	def draw(self, screen):
		pygame.draw.rect(screen, (102, 255, 255), (self.x-self.wid/2, self.y-self.hei/2, self.wid, self.hei), 0)
		if self.status == 1:
			screen.blit(self.image, (self.x - self.image.get_width()/2, self.y-self.image.get_height()/2))

class logicGame(scene.Scene):
	def __init__(self, director, game, post_win):
		scene.Scene.__init__(self, director)
		self.game = game
		self.screen = game.screen
		self.font = pygame.font.Font(None, 35)
		self.lastType = 0
		self.matchFound = 0
		self.cardsFlipped = 0
		self.sharkFound = 0
		self.cardsLeft = 0
		self.totShark = 0
		self.typeList = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7]
		random.shuffle(self.typeList)
		self.cardList = []
		for p in [1, 2, 3, 4]:
			for q in [1, 2, 3, 4]:
				self.cardList.append(card(self.typeList.pop(), p*sw/4-sw/8, q*sh/4-sh/8))
		self.counter = 0
	def events(self):
		event = pygame.event.poll()
		if event.type == pygame.MOUSEBUTTONDOWN and self.cardsFlipped < 2:
			self.coords = pygame.mouse.get_pos()
			for crd in self.cardList:
				if abs(crd.x - self.coords[0]) < crd.wid/2 and abs(crd.y-self.coords[1]) < crd.hei/2:
					crd.status = 1
					if self.cardsFlipped == 0 and crd.type != 7:
						self.lastType = crd.type
					if self.cardsFlipped == 1 and crd.type != 7:
						if self.lastType == crd.type:
							self.matchFound = 1
					if crd.type != 7:
						self.cardsFlipped = self.cardsFlipped + 1
					else:
						 sharkFound = 1
		if self.cardsFlipped >= 2:
			if self.counter > FPS*2:
				if self.matchFound == 1:
					self.cardList = [crd for crd in self.cardList if crd.status == 0]
				else:
					for crd in self.cardList:
						crd.status = 0
				self.cardsFlipped = 0
				self.lastType = 0
				self.matchFound = 0
				self.counter = 0
		if self.sharkFound == 1:
			if self.counter > FPS*2:
				self.totShark = self.totShark + 1
				self.counter = 0
				self.lastType = 0
				self.matchFound = 0
				self.sharkFound = 0
				self.cardsFlipped = 0
				for crd in self.cardList:
					crd.status = 0
				if self.totShark > 3:
					self.game.director.change_scene(self.game.director.scene_stack.pop())
		for crd in self.cardList:
			if crd.type != 7:
				self.cardsLeft = self.cardsLeft + 1
		if self.cardsLeft == 0:
			########
			print "hello"
		self.cardsLeft = 0
	def update(self):
		pass
	def render(self):
		self.screen.fill((153, 102, 51))
		for crd in self.cardList:
			crd.draw(self.screen)
