#!/usr/bin/env python2.7

import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *
import random
from pytmx.util_pygame import load_pygame

class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.background = pg.Surface((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		pg.key.set_repeat(500, 100)
		self.load_data()

	def load_data(self):
		game_folder = path.dirname(__file__)
		img_folder = path.join(game_folder, 'img')
		map_folder = path.join(game_folder, 'map')
		self.map = TiledMap(path.join(map_folder, 'top_world.tmx'))
		self.map_img = self.map.make_map()
		self.overlay_img = self.map.make_overlay()
		image_size = self.map_img.get_size()
		self.map_img = pg.transform.scale(self.map_img, (2*image_size[0], 2*image_size[1]))
		self.overlay_img = pg.transform.scale(self.overlay_img, (2*image_size[0], 2*image_size[1]))
		self.map_rect = self.map_img.get_rect()

	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.walls = pg.sprite.Group()
		# for row, tiles in enumerate(self.map.data):
		# 	for col, tile in enumerate(tiles):
		# 		if tile == '1':
		#			Wall(self, col, row)
		#		if tile =='P':
		#			self.player = Player(self, col, row)
		for tile_object in self.map.tmxdata.objects:
			if tile_object.name == 'wall':
				Obstacle(self, 2*tile_object.x, 2*tile_object.y,
							2*tile_object.width, 2*tile_object.height)
			if tile_object.name == 'player':
				self.player = Player(self, 2*tile_object.x, 2*tile_object.y);
		for x in range(1, random.randrange(1, 6)):
			x_pos = (2 * self.map.width) * random.random()
			y_pos = (2 * self.map.height) * random.random()
			self.ai = AI(self, x_pos, y_pos)
		self.camera = Camera(2*self.map.width, 2*self.map.height)
		self.draw_debug = False

	def run(self):
		self.running = True
		while self.running:
			self.dt = self.clock.tick(FPS) / 1000.0
			if not self.events():
				return False
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
		pg.display.set_caption(TITLE + "\t\tFPS: " + "{:.2f}".format(self.clock.get_fps()))
		self.background.blit(self.map_img, self.camera.apply_rect(self.map_rect))
		# self.draw_grid()
		if self.draw_debug:
			for wall in self.walls:
				pg.draw.rect(self.background, CYAN, self.camera.apply_rect(wall.rect), 1)
		for sprite in self.all_sprites:
			self.background.blit(sprite.image, self.camera.apply(sprite))
			if self.draw_debug:
				pg.draw.rect(self.background, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
		self.background.blit(self.overlay_img, self.camera.apply_rect(self.map_rect))
		pg.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT), self.screen)
		pg.display.flip()

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					return False
				if event.key == pg.K_h:
					self.draw_debug = not self.draw_debug
		return True

	def show_start_screen(self):
        	pass

	def show_go_screen(self):
        	pass
