#! /usr/bin/env python2.7
import math
import random
import pygame
from settings import *
from pygame.locals import *
import spritesheet

scwid = SCREEN_SIZE[0]
schgt = SCREEN_SIZE[1]
widrat = float(scwid)/1920
hgtrat = float(schgt)/1080

class intro(object):
	def __init__(self):
		self.image1 = pygame.image.load("Ramzi.jpeg") # picture of Ramzi
		self.image1 = pygame.transform.scale(self.image1, (int(self.image1.get_width()*widrat), int(self.image1.get_height()*hgtrat)))
		
		self.image2 = pygame.image.load("Textbox1") # picture of textbox asking for PIN number
		self.image2 = pygame.transform.scale(self.image2, (int(self.image2.get_width()*widrat), int(self.image2.get_height()*hgtrat)))
				
		#self.pos = [SCREEN_SIZE[0]/2, SCREEN_SIZE[1] * 0.8]
		#self.status = 4
		self.exists = 1
		
class ramzi(object):
	def __init__(self):
		self.image5 = pygame.image.load("Textbox4") # picture of textbox saying to enter DS course number
		self.image5 = pygame.transform.scale(self.image5, (int(self.image5.get_width()*widrat), int(self.image5.get_height()*hgtrat)))
		
class outro(object):
	def __init__(self):
		self.image3 = pygame.image.load("Textbox2") # picture of textbox giving PIN number to user 
		self.image3 = pygame.transform.scale(self.image3, (int(self.image3.get_width()*widrat), int(self.image3.get_height()*hgtrat)))
		
		self.image4 = pygame.image.load("Textbox3") # picture of textbox saying thank you 
		self.image4 = pygame.transform.scale(self.image4, (int(self.image4.get_width()*widrat), int(self.image4.get_height()*hgtrat)))

class coursenum(object):
	events = pygame.event.get()
	userinput = [] # initializes empty string vector
	while event.key != K_RETURN: # while the enter key is not pressed
		userinput.append(event.key) # adds each user input key pressed to the string vector

	i = 0
	match = 0
	while i < len(userinput):
		if i == 0:
			if userinput[i] == '2':
				correct = correct + 1
		if i == 1:
			if userinput[i] == '0':
				correct = correct + 1
		if i == 2:
			if userinput[i] == '3':
				correct = correct + 1
		if i == 3:
			if userinput[i] == '1':
				correct = correct + 1
		if i == 4:
			if userinput[i] == '2':
				correct = correct + 1
		return correct

	if correct == 5
		# Ramzi gives you your PIN number
