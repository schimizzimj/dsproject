#!/usr/bin/env python2.7

import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *
from pytmx.util_pygame import load_pygame

class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg. display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		pg.key.set_repeat(500, 100)
		self.load_data()

	def load_data(self):
		game_folder = path.dirname(__file__)
		img_folder = path.join(game_folder, 'img')
		map_folder = path.join(game_folder, 'map')
		self.map = TiledMap(path.join(map_folder, 'top_world.tmx'))
		self.map_img = self.map.make_map()
		self.map_rect = self.map_img.get_rect()
		self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()

	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.walls = pg.sprite.Group()
		# for row, tiles in enumerate(self.map.data):
		# 	for col, tile in enumerate(tiles):
		# 		if tile == '1':
		#			Wall(self, col, row)
		#		if tile =='P':
		#			self.player = Player(self, col, row)
		#for tile_object in self.map.tmxdata.objects:
			#if tile_object.name == 'player':
			#	self.player = Player(self, tile_object.x, tile_object.y)
			#if tile_object.name == 'wall':
			#	Obstacle(self, tile_object.x, tile_object.y,
			#				tile_object.width, tile_object.height)
		self.player = Player(self, 10, 10)
		self.camera = Camera(self.map.width, self.map.height)

	def run(self):
		self.running = True
		while self.running:
			self.dt = self.clock.tick(FPS) / 1000.0
			self.events()
			self.update()
			self.draw()

	def quit(self):
		pg.quit()
		sys.exit()

	def update(self):
		self.all_sprites.update()
		self.camera.update(self.player)

	def draw_grid(self):
		for x in range(0, WIDTH, TILESIZE):
			pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
		for y in range(0, HEIGHT, TILESIZE):
			pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

	def draw(self):
		pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
		self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
		# self.draw_grid()
		for sprite in self.all_sprites:
			self.screen.blit(sprite.image, self.camera.apply(sprite))
		pg.display.flip()
    
	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.quit()

	def show_start_screen(self):
        	pass

	def show_go_screen(self):
        	pass
    
# create game object
g = Game()
g.show_start_screen()
while True:
	g.new()
	g.run()
	g.show_go_screen()

pg.quit()


