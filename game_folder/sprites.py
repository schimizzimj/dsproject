#!/usr/bin/env python2.7

import pygame as pg
from settings import *
from tilemap import collide_hit_rect
import spritesheet
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

		# Load player spritesheet
		ss = spritesheet.spritesheet("img/lep.png")

		# These will store the images for the player sprite animations
		self.img_up = []
		self.img_down = []
		self.img_right = []
		self.img_left = []

		# Load individual images
		image = ss.image_at((0, 0, 32, 48), colorkey = BLACK) 	# Load down
		self.img_down.append(image)
		image = ss.image_at((33, 0, 32, 48), colorkey = BLACK)
		self.img_down.append(image)
		image = ss.image_at((65, 0, 32, 48), colorkey = BLACK)
		self.img_down.append(image)
		image = ss.image_at((97, 0, 32, 48), colorkey = BLACK)
		self.img_down.append(image)
		image = ss.image_at((0, 49, 32, 48), colorkey = BLACK)	# Load left
		self.img_left.append(image)
		image = ss.image_at((33, 49, 32, 48), colorkey = BLACK)
		self.img_left.append(image)
		image = ss.image_at((65, 49, 32, 48), colorkey = BLACK)
		self.img_left.append(image)
		image = ss.image_at((97, 49, 32, 48), colorkey = BLACK)
		self.img_left.append(image)
		image = ss.image_at((0, 97, 32, 48), colorkey = BLACK)	# Load right
		self.img_right.append(image)
		image = ss.image_at((33, 97, 32, 48), colorkey = BLACK)
		self.img_right.append(image)
		image = ss.image_at((65, 97, 32, 48), colorkey = BLACK)
		self.img_right.append(image)
		image = ss.image_at((97, 97, 32, 48), colorkey = BLACK)
		self.img_right.append(image)
		image = ss.image_at((0, 145, 32, 48), colorkey = BLACK)	# Load up
		self.img_up.append(image)
		image = ss.image_at((33, 145, 32, 48), colorkey = BLACK)
		self.img_up.append(image)
		image = ss.image_at((65, 145, 32, 48), colorkey = BLACK)
		self.img_up.append(image)
		image = ss.image_at((97, 145, 32, 48), colorkey = BLACK)
		self.img_up.append(image)
		self.image = self.img_down[0]

		self.vel = vec(0, 0)
		self.pos = vec(x, y)
		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.hit_rect = PLAYER_HIT_RECT
		self.hit_rect.center = self.rect.center


	def get_keys(self):
		self.vel = vec(0, 0)
		keys = pg.key.get_pressed()
		if keys[pg.K_UP] or keys[pg.K_w]:
			frame = (self.pos.y // 30) % len(self.img_up)
			print frame
			self.vel.y = -PLAYER_SPEED
			self.image = self.img_up[int(frame)]
		if keys[pg.K_DOWN] or keys[pg.K_s]:
			frame = (self.pos.y // 30) % len(self.img_down)
			self.vel.y = PLAYER_SPEED
			self.image = self.img_down[int(frame)]
		if keys[pg.K_LEFT] or keys[pg.K_a]:
			frame = (self.pos.x // 30) % len(self.img_left)
			self.vel.x = -PLAYER_SPEED
			self.image = self.img_left[int(frame)]
		if keys[pg.K_RIGHT] or keys[pg.K_d]:
			frame = (self.pos.x // 30) % len(self.img_right)
			self.vel.x = PLAYER_SPEED
			self.image = self.img_right[int(frame)]
		if self.vel.x != 0 and self.vel.y != 0:
			self.vel *= 0.7071

	def update(self):
		self.get_keys()
		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.pos += self.vel * self.game.dt
		self.hit_rect.centerx = self.pos.x
		collide_with_walls(self, self.game.walls, 'x')
		self.hit_rect.centery = self.pos.y
		collide_with_walls(self, self.game.walls, 'y')
		self.rect.center = self.hit_rect.center

class Obstacle(pg.sprite.Sprite):
	def __init__(self, game, x, y, w, h):
		self.groups = game.walls
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.rect = pg.Rect(x, y, w, h)
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
