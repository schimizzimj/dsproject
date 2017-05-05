#! /usr/bin/env python2.7

import pygame
import os
from settings import *
from pygame.locals import *
import random
import dialogue
import textbox
import scene

SCREEN_SIZE[0] = SCREEN_SIZE[0]
SCREEN_SIZE[1]= SCREEN_SIZE[1]

class card(object):#object for cards to be matched
	def __init__(self, type, x, y):
		self.type = type;#one of six gates or shark type
		self.x = x# x and y coords
		self.y = y
		self.wid = 3 * SCREEN_SIZE[0] / 16 #size of card (depends on screen size)
		self.hei = 3 * SCREEN_SIZE[1]/ 16
		wr = float(SCREEN_SIZE[0])/1920# ratios help calculate sizes
		hr = float(SCREEN_SIZE[1])/1080
		self.status = 0#unflipped = 0, flipped = 1
		if type == 1:
			self.image = pygame.image.load(os.path.join(IMG_FOLDER, "andgate.png"))#loading appropriate image for each card type
			self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*wr), int(self.image.get_height()*hr)))#and scaling by screensize
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
		pygame.draw.rect(screen, (102, 255, 255), (self.x-self.wid/2, self.y-self.hei/2, self.wid, self.hei), 0)#draw rectangle for card
		if self.status == 1:#if flipped, print image
			screen.blit(self.image, (self.x - self.image.get_width()/2, self.y-self.image.get_height()/2))

class logicGame(scene.Scene):
	def __init__(self, director, game, post_win):
		scene.Scene.__init__(self, director)
		self.game = game
		self.screen = game.screen
		self.post_win = post_win
		self.font = pygame.font.Font(None, 35)
		self.lastType = 0#previous flipped card for determining pairs
		self.matchFound = 0#match found if two cards match
		self.cardsFlipped = 0#number of cards currently facing up
		self.sharkFound = 0#a shark has been found on last flip
		self.cardsLeft = 0#cards remaining in the deck
		self.totShark = 0#number of sharks that have been flipped
		self.typeList = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7]#used to initialize card deck
		random.shuffle(self.typeList)#shuffle for placement
		self.cardList = []
		for p in [1, 2, 3, 4]:#create list of appropriately placed random-type cards
			for q in [1, 2, 3, 4]:
				self.cardList.append(card(self.typeList.pop(), p*SCREEN_SIZE[0]/4-SCREEN_SIZE[0]/8, q*SCREEN_SIZE[1]/4-SCREEN_SIZE[1]/8))
		self.counter = 0#counter to time for animations

	def events(self):
		event = pygame.event.poll()#check for click
		if event.type == pygame.MOUSEBUTTONDOWN and self.cardsFlipped < 2:#do not flip card if two are flipped
			self.coords = pygame.mouse.get_pos()
			for crd in self.cardList:
				if abs(crd.x - self.coords[0]) < crd.wid/2 and abs(crd.y-self.coords[1]) < crd.hei/2:#if card clicked on...
					if crd.status != 1 and self.sharkFound != 1:#and the card has not been flipped, and a shark is not currently showing
						crd.status = 1#mark the card as flipped
						if self.cardsFlipped == 0 and crd.type != 7:#if it is not a shark and it is the first in the attempt:
							self.lastType = crd.type#set the last type variable for comparisons
						if self.cardsFlipped == 1 and crd.type != 7:#if a card is already up, check for a match
							if self.lastType == crd.type:#if there is a match
								self.matchFound = 1#set the variable for a later loop
								self.counter = 0#start the match counter to show the user the match
						if crd.type != 7:#increment the cards flipped, unless this is a shark
							self.cardsFlipped = self.cardsFlipped + 1
						else:#uh-oh
							 self.sharkFound = 1#you found a shark (if type is 7)
		if self.cardsFlipped >= 2:#if two cards are facing up (and by definition neither is shark)
			self.counter += 1#increment the counter to display the cards for the right length of time
			if self.counter > FPS*2:#if the counter is high enough
				if self.matchFound == 1:#if there is a match, remove the two matching cards
					self.cardList = [crd for crd in self.cardList if crd.status == 0]
				else:#otherwise flip all cards to facing down
					for crd in self.cardList:
						crd.status = 0
				self.cardsFlipped = 0#no cards are now facing up
				self.lastType = 0#there is no last card to compare the next card to
				self.matchFound = 0#you have no longer found a match
				self.counter = 0#reset the timer to 0
		if self.sharkFound == 1:#if you found a shark :(
			self.counter += 1#increment timer to show the user
			if self.counter > FPS*2:#if the timer has been reached
				self.totShark += 1#add to the number of sharks found
				self.counter = 0#reset appropriate variables
				self.lastType = 0
				self.matchFound = 0
				self.sharkFound = 0
				self.cardsFlipped = 0
				for crd in self.cardList:#flip all cards facing down
					crd.status = 0
				if self.totShark > 3:#if you have found all four sharks you lose
					self.game.director.change_scene(self.game.director.scene_stack.pop())
		for crd in self.cardList:
			if crd.type != 7:#count number of non-shark cards in the deck
				self.cardsLeft = self.cardsLeft + 1
		if self.cardsLeft == 0:#if you have removed them all, you win
			self.game.json['npcs'][1]['logic']['completed'] = True
			self.game.director.change_scene(self.game.director.scene_stack[-1])
			self.game.director.scene.render()
			self.game.director.change_scene(self.post_win)
		self.cardsLeft = 0#reset the cardsLeft counter for next check
	def update(self):
		pass
	def render(self):#print all images
		self.screen.fill((153, 102, 51))
		for crd in self.cardList:
			crd.draw(self.screen)
