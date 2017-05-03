#!/usr/bin/env python2.7

#Import Modules
import pygame
from pygame.locals import *
import time
import math
import settings
import scene
import menu
# import gui stuff
from pgu import text, gui as pgui

class SettingsMenu(scene.Scene):
	def __init__(self, director):
		scene.Scene.__init__(self, director)
		font = pygame.font.SysFont("default", 14)
		font_big = pygame.font.SysFont("default", 36)
		self.screen = self.director.screen

	    # create GUI object
		self.gui = pgui.App()

	    # create wrapper
		wrapper = pgui.Container(width = settings.SCREEN_SIZE[0] / 2)

	    # create page title
		title = pgui.Label("Game Settings", font=font_big)
		wrapper.add(title,29,13)

		# add select for screen resolutions
		dropdown_label = pgui.Label("Screen Resolution")
		wrapper.add(dropdown_label,40,195)
		dropdown_width = 200
		self.dropdown = pgui.Select(size = 32, width = dropdown_width, height = 16)
		self.dropdown.add("1920 x 1080", 1920)
		self.dropdown.add("1280 x 720", 1280)
		self.dropdown.add("1024 x 576", 1024)
		wrapper.add(self.dropdown, ((settings.SCREEN_SIZE[0] / 2) - dropdown_width), 195) #, colspan=3)

		self.gui.init(wrapper)

	def events(self):
		''' Handle events '''
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				self.director.change_scene(self.director.scene_stack.pop())
			self.gui.event(event)

	def update(self):
		if self.dd.value is not None:
			# if menu select is used, change screen size accordingly
			if self.dd.value == 1920:
				settings.SCREEN_SIZE[0] = 1920
				settings.SCREEN_SIZE[1] = 1080
			elif self.dd.value == 1280:
				settings.SCREEN_SIZE[0] = 1280
				settings.SCREEN_SIZE[1] = 720
			elif self.dd.value == 1024:
				settings.SCREEN_SIZE[0] = 1024
				settings.SCREEN_SIZE[1] = 576
			self.screen = pygame.display.set_mode((settings.SCREEN_SIZE[0], settings.SCREEN_SIZE[1]))



	def render(self):
		''' recolor screen and draw gui '''
		self.screen.fill(settings.ND_GOLD)
		self.gui.paint(self.screen)
