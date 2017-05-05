#!/usr/bin/env python2.7

'''
This is the base class for scenes that every other scene in the
game will inherit from. Scenes are things like the start menu,
the settings menu, the minigames, and the main game itself.
'''

class Scene(object):
	def __init__(self, director):
		self.director = director

	def events(self):
		raise NotImplementedError

	def update(self):
		raise NotImplementedError

	def render(self):
		raise NotImplementedError
