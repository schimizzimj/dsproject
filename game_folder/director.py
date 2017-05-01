#!/usr/bin/env python2.7

# Import modules
import pygame as pg
import sys
from settings import *

class Director():
	"""
		This class serves as a director of which scene needs to be displayed at each time.
		It runs the main game loop and switches between scenes as necessary.
	"""
	def __init__(self):
		gameIcon = pg.image.load('img/icon.png')
		pg.display.set_icon(gameIcon)
		self.screen = pg.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]), 0, 32)
