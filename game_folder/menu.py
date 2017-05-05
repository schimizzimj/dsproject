#!/usr/bin/env python2.7

import pygame
import sys
import os
from settings import *
from main import *
import scene
import settings_menu
import game

class Item(pygame.font.Font):
	'''
	Used to represent each individual entry in the menu
	'''
	def __init__(self, text, font=None, font_color=(255, 255, 255), (pos_x, pos_y)=(0, 0)):
		pygame.font.Font.__init__(self, font, FONT_SIZE)
		self.text = text
		self.font_size = FONT_SIZE
		self.font_color = ND_BLUE
		self.label = self.render(self.text, 1, self.font_color)
		self.width = self.label.get_rect().width
		self.height = self.label.get_rect().height
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.position = pos_x, pos_y

	def set_position(self, x, y):
		self.position = (x, y)
		self.pos_x = x
		self.pos_y = y

	def set_color(self, rgb_tuple):
		self.font_color = rgb_tuple
		self.label = self.render(self.text, 1, self.font_color)

	def mouse_hover(self, (posx, posy)):
		'''
		Returns a bool; True if the mouse is hovering over
		it and false otherwise
		'''
		if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
			(posy >= self.pos_y and posy <= self.pos_y + self.height):
				return True
		return False

class StartMenu(scene.Scene):
	def __init__(self, director, bg_color=(0,0,0), font=None,
                    font_color=(255, 255, 255)):
		scene.Scene.__init__(self, director) # parent __init__
		self.screen = self.director.screen
		self.clock = self.director.clock
		self.bg_color = bg_color
		items = MENU_ITEMS # create items list from variable stored in settings
		self.font = pygame.font.SysFont(font, FONT_SIZE)
		self.font_color = ND_BLUE
		self.functions = {'Start': self.run_game,
     	 	      	  	  'Quit': sys.exit,
						  'Settings': self.run_settings}
		self.items = []
		for index, item in enumerate(items):
			menu_item = Item(item)
			t_h = len(items) * menu_item.height # represents the height of the whole block of options
			pos_x = (SCREEN_SIZE[0] / 2) - (menu_item.width / 2)
			pos_y = (SCREEN_SIZE[1] / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)
			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)

	def update_menu(self):
		''' Used to recenter menu items when window size is changed '''
		for index, item in enumerate(self.items):
			t_h = len(self.items) * item.height
			pos_x = (SCREEN_SIZE[0] / 2) - (item.width / 2)
			pos_y = (SCREEN_SIZE[1] / 2) - (t_h / 2) + ((index * 2) + index * item.height)
			item.set_position(pos_x, pos_y)

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.director.running = False # quit out of game loop
			if event.type == pygame.MOUSEBUTTONDOWN:
				mpos = pygame.mouse.get_pos()
				for item in self.items:
					if item.mouse_hover(mpos):
						self.functions[item.text]() # call function based on what menu item is pressed

	def run_game(self):
		''' Add StartMenu to scene stack and change scene to game '''
		self.director.scene_stack.append(self.director.scene)
		self.director.change_scene(game.Game(self.director))

	def run_settings(self):
		''' Add StartMenu to scene stack and change scene to settings '''
		self.director.scene_stack.append(self.director.scene)
		self.director.change_scene(settings_menu.SettingsMenu(self.director))
		pass

	def update(self):

		for item in self.items:
			if item.mouse_hover(pygame.mouse.get_pos()):
				# change color on hover
				item.set_color((0, 150, 0))
				item.set_underline(True)
			else:
				item.set_color(self.font_color)
				item.set_underline(False)
		self.update_menu()

	def render(self):
		# draw everything to the screen each frame
		self.screen.fill(ND_GOLD)
		for item in self.items:
			self.screen.blit(item.label, item.position)
