#!/usr/bin/env python2.7
import sys
import pygame as pg
import pytmx
from pytmx.util_pygame import load_pygame
from settings import *

def collide_hit_rect(one, two):
	return one.hit_rect.colliderect(two.rect)

class Map:
	def __init__(self, filename):
		self.data = []
		with open(filename, 'rt') as f:
			for line in f:
				self.data.append(line.strip())

		self.tilewidth = len(self.data[0])
		self.tileheight = len(self.data)
		self.width = self.tilewidth * TILESIZE
		self.height = self.tileheight * TILESIZE

class TiledMap:
	def __init__(self, filename):
		tm = load_pygame(filename, pixelalpha=True)
		self.width = tm.width * tm.tilewidth
		self.height = tm.height * tm.tileheight
		self.tmxdata = tm

	def render(self, surface, overlay):
		ti = self.tmxdata.get_tile_image_by_gid
		for layer in self.tmxdata.visible_layers:
			if layer.name == 'overlay' and overlay:
				if isinstance(layer, pytmx.TiledTileLayer):
					for x, y, gid, in layer:
						tile = ti(gid)
						if tile:
							surface.blit(tile,
								(x * self.tmxdata.tilewidth,
								  y * self.tmxdata.tileheight))
			elif not overlay:
				if isinstance(layer, pytmx.TiledTileLayer):
					for x, y, gid, in layer:
						tile = ti(gid)
						if tile:
							surface.blit(tile,
								(x * self.tmxdata.tilewidth,
								  y * self.tmxdata.tileheight))

	def make_map(self):
		temp_surface = pg.Surface((self.width, self.height))
		self.render(temp_surface, False)
		return temp_surface

	def make_overlay(self):
		temp_surface = pg.Surface((self.width, self.height), pg.SRCALPHA, 32)
		temp_surface = temp_surface.convert_alpha()
		self.render(temp_surface, True)
		return temp_surface

class Camera:
  def __init__(self, width, height):
    self.camera = pg.Rect(0, 0, width, height)
    self.width = width
    self.height = height

  def apply(self, entity):
    return entity.rect.move(self.camera.topleft)

  def apply_rect(self, rect):
    return rect.move(self.camera.topleft)

  def update(self, target):
    x = -target.rect.x + int(WIDTH / 2)
    y = -target.rect.y + int(HEIGHT / 2)

    # limit scrolling
    x = min(0, x)
    x = max(-(self.width - WIDTH), x)
    y = min(0, y)
    y = max(-(self.height - HEIGHT), y)
    self.camera = pg.Rect(x, y, self.width, self.height)
