#!/usr/bin/env python2.7

import pygame as pg
from settings import *
from tilemap import collide_hit_rect
vec = pg.math.Vector2

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

class Player(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = game.player_img
		self.rect = self.image.get_rect()
		self.vel = vec(0, 0)
		self.pos = vec(x, y) * TILESIZE

	def get_keys(self):
		self.vel = vec(0, 0)
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT] or keys[pg.K_a]:
			self.vel.x = -PLAYER_SPEED
		if keys[pg.K_RIGHT] or keys[pg.K_d]:
			self.vel.x = PLAYER_SPEED
		if keys[pg.K_UP] or keys[pg.K_w]:
			self.vel.y = -PLAYER_SPEED
		if keys[pg.K_DOWN] or keys[pg.K_s]:
			self.vel.y = PLAYER_SPEED
		if self.vel.x != 0 and self.vel.y != 0:
			self.vel *= 0.7071


	def collide_with_walls(self, dir):
		if dir == 'x':
			hits = pg.sprite.spritecollide(self, self.game.walls, False)
			if hits:
				if self.vel.x > 0:
					self.pos.x = hits[0].rect.left - self.rect.width
				if self.vel.x < 0:
					self.pos.x = hits[0].rect.right
				self.vel.x = 0
				self.rect.x = self.pos.x

		if dir == 'y':
			hits = pg.sprite.spritecollide(self, self.game.walls, False)
			if hits:
				if self.vel.y > 0:
					self.pos.y = hits[0].rect.top - self.rect.width
				if self.vel.y < 0:
					self.pos.y = hits[0].rect.bottom
				self.vel.y = 0
				self.rect.y = self.pos.y

	def update(self):
		self.get_keys()
		self.pos += self.vel * self.game.dt
		self.rect.x = self.pos.x
		self.collide_with_walls('x')
		self.rect.y = self.pos.y
		self.collide_with_walls('y')

class Obstacle(pg.sprite.Sprite):
	def __init__(self, game, x, y, w, h):
		self.groups = game.walls
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.rect = pg.Rect(x, top, w, h)
		self.x = x
		self.y = y
		self.rect.x = x
		self.rect.y = y

class Wall(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.walls
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pg.Surface((TILESIZE, TILESIZE))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE
