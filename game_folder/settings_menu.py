#!/usr/bin/env python2.7

#Import Modules
import pygame
from pygame.locals import *
import time
import math
import settings
# import gui stuff
from pgu import text, gui as pgui

screenSize = (settings.SCREEN_SIZE[0], settings.SCREEN_SIZE[1])
lines = []
lineLimit = 20

class setting():
	def __init__(self):
		font = pygame.font.SysFont("default", 14)
		fontBig = pygame.font.SysFont("default", 36)
		fontSub = pygame.font.SysFont("default", 12)

	    # create GUI object
		self.gui = pgui.App()

	    # layout using document
		lo = pgui.Container(width= settings.SCREEN_SIZE[0] / 2)

	    # create page label
	    #lo.block(align=-1) #lo.br(8) #lo.tr()
		title = pgui.Label("Game Settings", font=fontBig)
		lo.add(title,29,13)

		ddl = pgui.Label("Screen Resolution")
		lo.add(ddl,40,195)
		dd_width = 200
		self.dd = pgui.Select(size=32,width=dd_width,height=16)
		self.dd.add("1920 x 1080", (1920, 1080))
		self.dd.add("1280 x 720", (1280, 720))
		lo.add(self.dd,((settings.SCREEN_SIZE[0] / 2) - dd_width),195) #, colspan=3)

		self.gui.init(lo)

	def run(self, menu):
	    #Main Loop
		while 1:

	        #Handle Input Events
			for event in pygame.event.get():
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					return
				self.gui.event(event)
			if self.dd.value is not None:
				settings.SCREEN_SIZE[1] = 1080
				settings.SCREEN_SIZE[0] = 1920
				menu.update_menu()
				menu.screen = pygame.display.set_mode((settings.SCREEN_SIZE[0], settings.SCREEN_SIZE[1]))
	        # clear background, and draw clock-spinner
			menu.screen.fill(settings.ND_GOLD)
			self.gui.paint(menu.screen)

			pygame.display.flip()
