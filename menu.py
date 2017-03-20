#!/usr/bin/env python2.7
 
import pygame
import sys
 
pygame.init()

# Global Variables
HEIGHT = 480
WIDTH = 640

 
def lines():
	linecolor = 0, 0, 255
	linecolor2 = 255, 0, 0
	bgcolor = 0, 0, 0
	x = 0
	y = 0
	dir_x = 1
	dir_y = 1
	running = 1
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	while running:
        	event = pygame.event.poll()
        	if event.type == pygame.QUIT:
                	running = 0

        	screen.fill(bgcolor)
        	pygame.draw.line(screen, linecolor, (0, y), (WIDTH - 1, y))
        	pygame.draw.line(screen, linecolor2, (x, 0), (x, HEIGHT - 1))

		x += dir_x
		if x == 0 or x == WIDTH - 1: dir_x *= -1

		y += dir_y
		if y == 0 or y == HEIGHT - 1: dir_y *= -1

        	pygame.display.flip()


class Item(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30,
                 font_color=(255, 255, 255), (pos_x, pos_y)=(0, 0)):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
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
    def __init__(self, screen, items, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.screen = screen
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
	self.functions = funcs
 
        self.items = []
       	for index, item in enumerate(items):
    		menu_item = Item(item)
 
    		t_h = len(items) * menu_item.height # represents the height of the whole block of options
    		pos_x = (WIDTH / 2) - (menu_item.width / 2)
		pos_y = (HEIGHT / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)
 
    		menu_item.set_position(pos_x, pos_y)
    		self.items.append(menu_item) 
 
    def run(self):
        mainloop = True
        while mainloop: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mpos = pygame.mouse.get_pos()
			for item in self.items:
				if item.mouse_hover(mpos):
					self.functions[item.text]()
 
            # draw over the background to ensure nothing remains from previous frames
            self.screen.fill(self.bg_color)
 
            for item in self.items:
                if item.mouse_hover(pygame.mouse.get_pos()):
			item.set_color((255, 0, 0))
			item.set_italic(True)
		else:
			item.set_color((255, 255, 255))
			item.set_italic(False)
		self.screen.blit(item.label, item.position)
 
            pygame.display.flip()
 
 
# create the window using the global variables for width and height
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

menu_items = ('Start', 'Settings', 'Highscore', 'Quit')

funcs = {'Start': lines,
     'Quit': sys.exit}

pygame.display.set_caption('Game Menu')
gm = Menu(screen, menu_items)
gm.run()
