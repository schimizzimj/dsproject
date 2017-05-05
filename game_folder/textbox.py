from __future__ import division

import pygame as pg
import scene
from settings import *
from Queue import *
import random

class TextBox(scene.Scene):
	def __init__(self, director, screen, name, dialogue, rand):
		scene.Scene.__init__(self, director) # call parent __init__
		self.screen = screen
		self.name = name
		self.width = self.screen.get_width() / 2
		self.height = self.screen.get_height() / 8
		self.box = pg.Surface((self.width, self.height))
		self.box.fill(WHITE)
		self.rect = self.box.get_rect()
		if rand: # decide whether dialog should be random or chronological
			self.create_queue(dialogue[self.randomize(len(dialogue))])
		else:
			self.create_queue(dialogue)
		self.next_line() # display first line of text

	def events(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					self.next_line() # display next line of text or exit when user hits space

	def update(self):
		# nothing necessary here yet
		pass

	def randomize(self, size):
		return random.randint(0, size - 1) # allows random text to be shown


	def next_line(self):
		if self.queue.empty():
			''' leave text state if queue is empty '''
			self.director.change_scene(self.director.scene_stack.pop())
		else:
			''' else draw next line '''
			self.box.fill(WHITE)
			draw_text(self.box, self.name, self.queue.get(), self.rect)

	def render(self):
		''' Actually draws text box onto screen '''
		self.screen.blit(self.box, (self.width / 2, (8*self.height) - self.height * 1.5))

	def create_queue(self, dialogue):
		''' Create a text queue from the input list of strings '''
		self.queue = Queue()
		for line in dialogue:
				self.queue.put(line)


def draw_text(surface, name=None, text=None, rect=pg.Rect(0, 0, 0, 0), font=None, font_size=30, font_color=(0, 0, 0)):

	left, top, width, height = rect
	font = pg.font.Font(font, font_size) # create font object
	title = pg.font.Font(None, int(1.2*font_size)) # for speaking NPC's name
	padding = 10 # pads both sides of text box

	# find how many pixels wide each letter is
	text_surface = font.render(text, 1, font_color)
	letter_width = text_surface.get_width() / len(text)

	lines = [] # list of each line
	words = [] # list of individual words to check for line's length

    # iterate through all words in the input text
	for word in text.split():

		words.append(word)
		if len(" ".join(words)) * letter_width + padding > width:
            # if the length of the line plus padding is too long, add that line
			# to the list of lines (minus the line that caused it to go over)
			lines.append(" ".join(words[:-1]))

            # clear the words list for the next line, and add the stripped off word
			words = []
			words.append(word)

	if " ".join(words) != '':
		# add the last line if it is not blank
		lines.append(" ".join(words))

	if name:
		# if a name is given, display that as a title before the dialogue
		name = title.render(name, 1, ND_GOLD)
		surface.blit(name, (left + padding, top + padding))
		spacing = name.get_height() + padding
 	else:
		# else, treat it normally and display dialogue normally
		spacing = 0

	for item in lines:
		# print the lines in the text box
		line = font.render(item, 1, font_color)
		surface.blit(line, (left + padding, top + spacing))
		spacing += line.get_height()  # add the spacing due to that line
