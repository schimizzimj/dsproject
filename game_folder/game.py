#!/usr/bin/env python2.7

import pygame as pg
import sys
from os import path
import scene
from settings import *
import menu
import level
from dialogue import game_json

class Game(scene.Scene):
	'''
	Scene class for the actual gameplay. Essentially, it is a director class for
	the individual levels (rooms) that can be entered/left when moving around the map.
	'''
	def __init__(self, director):
		scene.Scene.__init__(self, director)
		self.screen = self.director.screen
		self.background = pg.Surface((WIDTH, HEIGHT)) # Creates a surface to draw everything on
		self.clock = self.director.clock
		self.dt = self.director.dt
		self.json = game_json
		self.load_data()

	def load_data(self):
		''' Add variables for the important folders '''
		self.game_folder = GAME_FOLDER
		self.img_folder = IMG_FOLDER
		self.map_folder = MAP_FOLDER

		self.level = level.TopLevel(self, 0) # Initial spawn when starting the game
		self.level_stack = [self.level] # Create stack to keep track of level
		self.level.load() # Load the level

	def update(self):
		self.level.update() # Call update() function for current level

	def change_level(self, level):
		''' Transition between levels '''
		self.screen.fill(BLACK)
		self.level = level

	def render(self):
		''' Draw current frame of game to screen '''
		pg.display.set_caption(TITLE + "\t\tFPS: " + "{:.2f}".format(self.clock.get_fps())) # Print title and FPS as caption
		self.level.render() # Call render for current level
		pg.transform.scale(self.background, (SCREEN_SIZE[0], SCREEN_SIZE[1]), self.screen) # Scale background surface to current screen size, allows you to run window in different resolutions

	def events(self):
		''' Handle events '''
		self.level.events() # Call events function for current level
