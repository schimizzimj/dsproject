#!/usr/bin/env python2.7

import pygame as pg
import sys
from os import path
import scene
from settings import *
from sprites import *
from tilemap import *
import random
import menu
from pytmx.util_pygame import load_pygame

class Game(scene.Scene):
	def __init__(self, director):
		scene.Scene.__init__(self, director)
		self.screen = self.director.screen
		self.background = pg.Surface((WIDTH, HEIGHT))
		self.clock = self.director.clock
		self.dt = self.director.dt
		self.load_data()
		self.new()

	def load_data(self):
		self.game_folder = path.dirname(__file__)
		self.img_folder = path.join(self.game_folder, 'img')
		self.map_folder = path.join(self.game_folder, 'map')
		self.map = TiledMap(path.join(self.map_folder, 'top_world.tmx'))
		self.map_img = self.map.make_map()
		self.overlay_img = self.map.make_overlay()
		image_size = self.map_img.get_size()
		self.map_img = pg.transform.scale(self.map_img, (2*image_size[0], 2*image_size[1]))
		self.overlay_img = pg.transform.scale(self.overlay_img, (2*image_size[0], 2*image_size[1]))
		self.map_rect = self.map_img.get_rect()

	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.walls = pg.sprite.Group()
		self.entities = pg.sprite.Group()
		for tile_object in self.map.tmxdata.objects:
			if tile_object.name == 'wall':
				Obstacle(self, 2*tile_object.x, 2*tile_object.y,
							2*tile_object.width, 2*tile_object.height)
			if tile_object.name == 'player':
				self.player = Player(self, 2*tile_object.x, 2*tile_object.y);
		for x in range(0, random.randrange(5, 10)):
			x_pos = (2 * self.map.width) * random.random()
			y_pos = (2 * self.map.height) * random.random()
			self.ai = AI(self, x_pos, y_pos)
		self.camera = Camera(2*self.map.width, 2*self.map.height)
		self.draw_debug = False

	def update(self):
		self.all_sprites.update()
		self.camera.update(self.player)
		self.update_map()

	def update_map(self):
		if self.player.pos[0] > 1459 and self.player.pos[0] < 1490 and self.player.pos[1] == 1363 and self.player.dir.y == -1:
			self.map = TiledMap(path.join(self.map_folder, 'debart.tmx'))
	 		self.map_img = self.map.make_map()
	 		self.overlay_img = self.map.make_overlay()
	 		image_size = self.map_img.get_size()
	 		self.map_img = pg.transform.scale(self.map_img, (2*image_size[0], 2*image_size[1]))
	 		self.overlay_img = pg.transform.scale(self.overlay_img, (2*image_size[0], 2*image_size[1]))
	 		self.map_rect = self.map_img.get_rect()

	def render(self):
		pg.display.set_caption(TITLE + "\t\tFPS: " + "{:.2f}".format(self.clock.get_fps()))
		self.background.blit(self.map_img, self.camera.apply_rect(self.map_rect))
		if self.draw_debug:
			for wall in self.walls:
				pg.draw.rect(self.background, CYAN, self.camera.apply_rect(wall.rect), 1)
		for sprite in self.all_sprites:
			self.background.blit(sprite.image, self.camera.apply(sprite))
			if self.draw_debug:
				pg.draw.rect(self.background, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
		self.background.blit(self.overlay_img, self.camera.apply_rect(self.map_rect))
		pg.transform.scale(self.background, (SCREEN_SIZE[0], SCREEN_SIZE[1]), self.screen)

	def events(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.director.change_scene(menu.StartMenu(self.director))
				if event.key == pg.K_h:
					self.draw_debug = not self.draw_debug

	def show_start_screen(self):
        	pass

	def show_go_screen(self):
        	pass
