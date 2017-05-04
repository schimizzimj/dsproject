#!/usr/bin/env python2.7

# Import modules
import pygame as pg
import sys
from settings import *

class Director(object):
	"""
		This class serves as a director of which scene needs to be displayed at each time.
		It runs the main game loop and switches between scenes as necessary.
	"""
	def __init__(self):
		gameIcon = pg.image.load('img/icon.png')
		pg.display.set_icon(gameIcon)
		self.screen = pg.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]), 0, 32)
		self.scene = None
		self.clock = pg.time.Clock()
		self.running = True
		pg.key.set_repeat(500, 100)

	def run(self):
		while self.running:
			self.dt = self.clock.tick(FPS) / 1000.0
			if pg.event.get(pg.QUIT):
				self.quit()

			self.scene.events()
			self.scene.update()
			self.scene.render()
			pg.display.flip()

	def quit(self):
		self.running = False

	def change_scene(self, scene):
		self.scene = scene