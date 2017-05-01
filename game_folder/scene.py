#!/usr/bin/env python2.7

class Scene(object):
	def __init__(self, director):
		self.director = director

	def events(self):
		raise NotImplementedError

	def update(self):
		raise NotImplementedError

	def render(self):
		raise NotImplementedError
