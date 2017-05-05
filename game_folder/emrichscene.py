#!/usr/bin/env python2.7

import pygame as pg
import sys
from os import path
import scene
from settings import *
from sprites import *
import scene
import dialogue

# ordering data structures horizontally
class DataStructures(scene.Scene):
	def __init__(self, director, game, post_win):
		scene.Scene.__init__(self, director)
		self.game = game
		# make screen
		self.screen = self.game.director.screen
		pg.display.set_caption("Data Structures")
		self.font = pg.font.Font(pg.font.get_default_font(), 16)
		self.post_win = post_win
		# set vars
		self.changed = True
		# width, height
		self.w = 200
		self.h = 50
		# mouse vars
		self.pressed = False
		self.drag = False
		# height of first rectangle
		self.hi = HEIGHT/3-self.w/2

		# rectangle vars
		self.xBST = WIDTH/2-self.w/2
		self.yBST = self.hi
		self.xLL = WIDTH/2-self.w/2
		self.yLL = self.hi + 3*self.h
		self.xA = WIDTH/2-self.w/2
		self.yA = self.hi + 6*self.h

		# ellipsis vars
		self.xe = 0
		self.ye = 0
		self.he = 0
		self.we = 0


	def events(self):
		# get one event
		event = pg.event.poll()
		# mouse pressed
		if event.type == pg.MOUSEBUTTONDOWN:
			self.pressed = True
			self.coords = pg.mouse.get_pos()
    		# drag bst
			if self.xBST < self.coords[0] < self.xBST + self.w and self.yBST < self.coords[1] < self.yBST + self.h:
				self.changed = True
				self.xBST = self.coords[0] - self.w/2
				self.yBST = self.coords[1] - self.h/2
            # drag linked list
			elif self.xLL < self.coords[0] < self.xLL + self.w and self.yLL < self.coords[1] < self.yLL + self.h:
				self.changed = True
				self.xLL = self.coords[0] - self.w/2
				self.yLL = self.coords[1] - self.h/2
            # drag array
			elif self.xA < self.coords[0] < self.xA + self.w and self.yA < self.coords[1] < self.yA + self.h:
				self.changed = True
				self.xA = self.coords[0] - self.w/2
				self.yA = self.coords[1] - self.h/2
            # press button to check order
			elif self.xe < self.coords[0] < self.xe + self.we and self.ye < self.coords[1] < self.ye + self.he:
				self.endGame()
        # stop dragging box
		elif event.type == pg.MOUSEBUTTONUP:
			self.pressed = False

	def update(self):
		if self.pressed:
			self.holding()
            # drag bst
			if self.xBST < self.coords[0] < self.xBST + self.w and self.yBST < self.coords[1] < self.yBST + self.h:
				self.changed = True
				self.xBST = self.coords[0] - self.w/2
				self.yBST = self.coords[1] - self.h/2
            # drag linked list
			elif self.xLL < self.coords[0] < self.xLL + self.w and self.yLL < self.coords[1] < self.yLL + self.h:
				self.changed = True
				self.xLL = self.coords[0] - self.w/2
				self.yLL = self.coords[1] - self.h/2
            # drag array
			elif self.xA < self.coords[0] < self.xA + self.w and self.yA < self.coords[1] < self.yA + self.h:
				self.changed = True
				self.xA = self.coords[0] - self.w/2
				self.yA = self.coords[1] - self.h/2

	def render(self):
		if self.changed:
			self.screen.fill(WHITE)
			self.drawHeader()
			self.drawButton()
			self.drawBSTRect()
			self.drawLLRect()
			self.drawARect()
		self.changed = False

	def drawButton(self):
		#global xe, ye, he, we
		length = 80
		self.he = length
		self.we = length/2
		self.xe = WIDTH/2 - length/2
		self.ye = 4*HEIGHT/5
		pg.draw.ellipse(self.screen, (0,255,0), pg.Rect(self.xe, self.ye, length, length/2))
		self.screen.blit(self.font.render("Done", True, BLACK), (WIDTH/2-length/4, 4*HEIGHT/5+length/6))

	def drawBSTRect(self):
		#global xBST, yBST
		rect = pg.draw.rect(self.screen, TEAL, pg.Rect(self.xBST, self.yBST, self.w, self.h))
		pg.display.update()
		self.addText(self.xBST+10, self.yBST, self.h, "Binary Search Tree")

	def drawLLRect(self):
		# global xLL, yLL
		rect = pg.draw.rect(self.screen, TEAL, pg.Rect(self.xLL, self.yLL, self.w, self.h))
		pg.display.update()
		self.addText(self.xLL+10, self.yLL, self.h, "Single Linked List")

	def drawARect(self):
		# global xA, yA
		rect = pg.draw.rect(self.screen, TEAL, pg.Rect(self.xA, self.yA, self.w, self.h))
		pg.display.update()
		self.addText(self.xA+self.w/3, self.yA, self.h, "Array")

	def addText(self, xT, yT, h, label):
		self.screen.blit(self.font.render(label, True, BLACK), (xT, yT+h/2))
		pg.display.update()

	def holding(self):
		#global pressed, coords
		if self.pressed:
			self.coords = pg.mouse.get_pos()

	def drawHeader(self):
		# header
		self.screen.blit(self.font.render("Drag the data structures in smallest to largest average time complexity of accessing an element.", True, BLACK), (WIDTH+10, HEIGHT/13))
		self.screen.blit(self.font.render("Put the smallest time complexity closest to the left side of the screen and the largest closest to the right side.", True, BLACK), (WIDTH/7, HEIGHT/13+20))
		self.screen.blit(self.font.render("*in case you didn't pay attention in class: the order is array, bst, linked list.", True, BLACK), (WIDTH/5, HEIGHT/13+40))
		self.screen.blit(self.font.render("Press the green button when done.", True, BLACK), (WIDTH/3, HEIGHT/13+60))

	def endGame(self):
		#self.screen.fill(TEAL)
		#bigFont = pg.font.Font(pg.font.get_default_font(), 48)
		if self.xA < self.xBST < self.xLL:
			self.game.json['npcs'][0]['logic']['completed'] = True
			self.game.director.change_scene(self.game.director.scene_stack[-1])
			self.game.director.scene.render()
			self.game.director.change_scene(self.post_win)

	def drawButton(self):
        #global xe, ye, he, we
		length = 80
		self.he = length
		self.we = length/2
		self.xe = WIDTH/2 - length/2
		self.ye = 4*HEIGHT/5
		pg.draw.ellipse(self.screen, (0,255,0), pg.Rect(self.xe, self.ye, length, length/2))
		self.screen.blit(self.font.render("Done", True, BLACK), (WIDTH/2-length/4, 4*HEIGHT/5+length/6))

	def drawBSTRect(self):
        #global xBST, yBST
		rect = pg.draw.rect(self.screen, TEAL, pg.Rect(self.xBST, self.yBST, self.w, self.h))
		pg.display.update()
		self.addText(self.xBST+10, self.yBST, self.h, "Binary Search Tree")

	def drawLLRect(self):
        # global xLL, yLL
		rect = pg.draw.rect(self.screen, TEAL, pg.Rect(self.xLL, self.yLL, self.w, self.h))
		pg.display.update()
		self.addText(self.xLL+10, self.yLL, self.h, "Single Linked List")

	def drawARect(self):
        # global xA, yA
		rect = pg.draw.rect(self.screen, TEAL, pg.Rect(self.xA, self.yA, self.w, self.h))
		pg.display.update()
		self.addText(self.xA+self.w/3, self.yA, self.h, "Array")

	def addText(self, xT, yT, h, label):
		self.screen.blit(self.font.render(label, True, BLACK), (xT, yT+h/2))
		pg.display.update()

	def holding(self):
        #global pressed, coords
		if self.pressed:
			self.coords = pg.mouse.get_pos()

	def drawHeader(self):
        # header
		self.screen.blit(self.font.render("Drag the data structures in smallest to largest average time complexity of accessing an element.", True, BLACK), (WIDTH/10, HEIGHT/13))
		self.screen.blit(self.font.render("Put the smallest time complexity closest to the left side of the screen and the largest closest to the right side.", True, BLACK), (WIDTH/7, HEIGHT/13+20))
		self.screen.blit(self.font.render("*in case you didn't pay attention in class: the order is array, bst, linked list.", True, BLACK), (WIDTH/5, HEIGHT/13+40))
		self.screen.blit(self.font.render("Press the green button when done.", True, BLACK), (WIDTH/3, HEIGHT/13+60))

	def endGame(self):
		#self.screen.fill(TEAL)
		#bigFont = pg.font.Font(pg.font.get_default_font(), 48)
		if self.xA < self.xBST < self.xLL:
			self.game.json['npcs'][2]['logic']['completed'] = True
			print "done"
			self.game.director.change_scene(self.game.director.scene_stack[-1])
			self.game.director.scene.render()
			self.game.director.change_scene(self.post_win)
 		#   self.screen.blit(bigFont.render("Correct!", True, WHITE), (WIDTH/3, HEIGHT/2))
		# lose, go back
		else:
			self.game.director.change_scene(self.game.director.scene_stack.pop())
			#    self.screen.blit(bigFont.render("Not quite! Try again later", True, WHITE), (WIDTH/3, HEIGHT/2))
		pg.display.update()
