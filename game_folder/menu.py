#!/usr/bin/env python2.7

import pygame
import sys
import os
from settings import *
from main import *
import menus

pygame.init()

class Item(pygame.font.Font):
    def __init__(self, text, font=None,
                 font_color=(255, 255, 255), (pos_x, pos_y)=(0, 0)):
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
	if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
		(posy >= self.pos_y and posy <= self.pos_y + self.height):
			return True
	return False

class Menu():
	def __init__(self, items, bg_color=(0,0,0), font=None,
                    font_color=(255, 255, 255)):
		gameIcon = pygame.image.load('img/icon.png')
		pygame.display.set_icon(gameIcon)
		self.screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]), 0, 32)
		self.bg_color = bg_color
		self.clock = pygame.time.Clock()

		self.items = items
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
		for index, item in enumerate(self.items):
			t_h = len(self.items) * item.height
			pos_x = (SCREEN_SIZE[0] / 2) - (item.width / 2)
			pos_y = (SCREEN_SIZE[1] / 2) - (t_h / 2) + ((index * 2) + index * item.height)
			item.set_position(pos_x, pos_y)

	def run(self):
		mainloop = True
		while mainloop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					mainloop = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						mainloop = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					mpos = pygame.mouse.get_pos()
					for item in self.items:
						if item.mouse_hover(mpos):
							self.functions[item.text]()

            # draw over the background to ensure nothing remains from previous frames
			#image = pygame.image.load("img/menu.jpg").convert()
			self.screen.fill(ND_GOLD)

			for item in self.items:
				if item.mouse_hover(pygame.mouse.get_pos()):
					item.set_color((0, 150, 0))
					item.set_underline(True)
				else:
					item.set_color(self.font_color)
					item.set_underline(False)
				self.screen.blit(item.label, item.position)
			self.update_menu()
			pygame.display.flip()

	def run_game(self):
		flag = True
		g = Game()
		g.show_start_screen()
		while flag:
			g.new()
			if g.run() is False:
				flag = False
			g.show_go_screen()

	def run_settings(self):
		m = menus.setting()
		m.run(self)


menu_items = ('Start', 'Settings', 'Highscore', 'Quit')



pygame.display.set_caption('Game Menu')
gm = Menu(menu_items)
gm.run()
