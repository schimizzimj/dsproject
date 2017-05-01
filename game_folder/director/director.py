#!/usr/bin/env python2.7

# Import modules
import pygame as pg
import sys

class Director():
	"""
		This class serves as a director of which scene needs to be displayed at each time.
		It runs the main game loop and switches between scenes as necessary.
	"""
	def __init__(self):
		
