#!/usr/bin/env python2.7

import pygame as pg
from settings import *
from tilemap import collide_hit_rect
import spritesheet
import os
import random
from datetime import datetime
import math
import textbox
import systems
vec = pg.math.Vector2

def collide_with_walls(sprite, group, dir):
	'''
	Checks for collisions between a sprite and any sprite group in a certain direction
	'''
	if dir == 'x':
		hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
		if hits:
			if hits[0].hit_rect.centerx > sprite.hit_rect.centerx:
				sprite.pos.x = hits[0].hit_rect.left - sprite.hit_rect.width / 2
			if hits[0].hit_rect.centerx < sprite.hit_rect.centerx:
				sprite.pos.x = hits[0].hit_rect.right + sprite.hit_rect.width / 2
			sprite.vel.x = 0
			sprite.hit_rect.centerx = sprite.pos.x
	if dir == 'y':
		hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
		if hits:
			if hits[0].hit_rect.centery > sprite.hit_rect.centery:
				sprite.pos.y = hits[0].hit_rect.top - sprite.hit_rect.height / 2
			if hits[0].hit_rect.centery < sprite.hit_rect.centery:
				sprite.pos.y = hits[0].hit_rect.bottom + sprite.hit_rect.height / 2
			sprite.vel.y = 0
			sprite.hit_rect.centery = sprite.pos.y

def sprite_collide(sprite, group):
	for member in group:
		if pg.sprite.collide_rect(sprite, member):
			return True
	return False

class Player(pg.sprite.Sprite):
	def __init__(self, level, game, x, y, zoom):
		self.groups = level.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.name = 'Player'
		self.level = level
		self.zoom = zoom # used to properly scale the player based on current environment

		# Load player spritesheet
		ss = spritesheet.spritesheet(os.path.join(IMG_FOLDER, "lep.png"))

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
		self.dir = vec(0, -1) # direction vector
		self.vel = vec(0, 0) # velocity vector
		self.pos = vec(x, y) # position vector

		# create rect and hit_rect, scale them based on zoom settings
		self.rect = self.image.get_rect()
		self.rect = self.rect.inflate(self.rect.width * self.zoom, self.rect.height * self.zoom)
		self.rect.center = self.pos
		self.hit_rect = PLAYER_HIT_RECT.inflate(PLAYER_HIT_RECT.width * self.zoom, PLAYER_HIT_RECT.height * self.zoom)
		self.hit_rect.center = (self.rect.center[0], self.rect.center[1])


	def get_keys(self):
		self.vel = vec(0, 0)
		keys = pg.key.get_pressed()
		if keys[pg.K_UP] or keys[pg.K_w]:
			frame = (self.pos.y // 30) % len(self.img_up)
			self.vel.y = -PLAYER_SPEED
			self.image = self.img_up[int(frame)]
			self.dir.y = -1
		if keys[pg.K_DOWN] or keys[pg.K_s]:
			frame = (self.pos.y // 30) % len(self.img_down)
			self.vel.y = PLAYER_SPEED
			self.image = self.img_down[int(frame)]
			self.dir.y = 1
		if keys[pg.K_LEFT] or keys[pg.K_a]:
			frame = (self.pos.x // 30) % len(self.img_left)
			self.vel.x = -PLAYER_SPEED
			self.image = self.img_left[int(frame)]
			self.dir.x = -1
		if keys[pg.K_RIGHT] or keys[pg.K_d]:
			frame = (self.pos.x // 30) % len(self.img_right)
			self.vel.x = PLAYER_SPEED
			self.image = self.img_right[int(frame)]
			self.dir.x = 1
		if self.vel.x != 0 and self.vel.y != 0:
			self.vel *= 0.7071

	def update(self):
		self.get_keys()
		self.rect = self.image.get_rect()
		self.rect.inflate_ip(self.rect.width * self.zoom, self.rect.height * self.zoom)
		self.rect.center = self.pos
		self.prev = self.pos
		self.pos += self.vel * self.game.dt
		self.hit_rect.centerx = self.pos.x
		collide_with_walls(self, self.level.walls, 'x')
		self.hit_rect.centery = self.pos.y
		collide_with_walls(self, self.level.walls, 'y')
		self.hit_rect.centerx = self.pos.x
		if self.level.name == 'top_world':
			collide_with_walls(self, self.level.squirrels, 'x')
			self.hit_rect.centery = self.pos.y
			collide_with_walls(self, self.level.squirrels, 'y')
			self.rect.center = self.hit_rect.center

class Obstacle(pg.sprite.Sprite):
	def __init__(self, level, game, x, y, w, h):
		self.groups = level.walls
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.rect = pg.Rect(x, y, w, h)
		self.hit_rect = self.rect
		self.x = x
		self.y = y
		self.rect.x = x
		self.rect.y = y

class Squirrels(pg.sprite.Sprite):
	def __init__(self, level, game, x, y, zoom):
		self.groups = level.all_sprites, level.squirrels
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.name = 'Squirrel'
		self.level = level
		random.seed(datetime.now())
		self.zoom = zoom
		self.speech = game.json['npcs'][4]

		# Load player spritesheet
		ss = spritesheet.spritesheet(os.path.join(IMG_FOLDER, "squirrel.png"))

		# These will store the images for the player sprite animations
		self.img_up = []
		self.img_down = []
		self.img_right = []
		self.img_left = []

		# Load individual images
		image = ss.image_at((0, 193, 32, 32), colorkey = WHITE) 	# Load down
		self.img_down.append(image)
		image = ss.image_at((33, 193, 32, 32), colorkey = WHITE)
		self.img_down.append(image)
		image = ss.image_at((65, 193, 32, 32), colorkey = WHITE)
		self.img_down.append(image)

		image = ss.image_at((0, 161, 32, 32), colorkey = WHITE)	# Load left
		self.img_left.append(image)
		image = ss.image_at((33, 161, 32, 32), colorkey = WHITE)
		self.img_left.append(image)
		image = ss.image_at((65, 161, 32, 32), colorkey = WHITE)
		self.img_left.append(image)

		image = ss.image_at((0, 129, 32, 32), colorkey = WHITE)	# Load right
		self.img_right.append(image)
		image = ss.image_at((33, 129, 32, 32), colorkey = WHITE)
		self.img_right.append(image)
		image = ss.image_at((65, 129, 32, 32), colorkey = WHITE)
		self.img_right.append(image)

		image = ss.image_at((0, 224, 32, 32), colorkey = WHITE)	# Load up
		self.img_up.append(image)
		image = ss.image_at((33, 224, 32, 32), colorkey = WHITE)
		self.img_up.append(image)
		image = ss.image_at((65, 224, 32, 32), colorkey = WHITE)
		self.img_up.append(image)

		self.image = self.img_down[0]
		self.vel = vec(1, 1)
		self.pos = vec(x, y)
		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.hit_rect = pg.Rect(0, 0, 16, 16)
		self.hit_rect.center = self.rect.center
		self.step = 1001
		self.wander_angle = 0
		self.circle_dist = 50
		self.max_velocity = 150
		self.circle_radius = 10
		self.angle_change = math.pi / 4





	def move(self):
		threshold = random.randrange(FPS,20*FPS)
		if self.step >= threshold:
			self.vel.x = ((2*PLAYER_SPEED)*random.random()) - 200
			self.vel.y = ((2*PLAYER_SPEED)*random.random()) - 200
			self.step = 0
			threshold = random.randrange(FPS,20*FPS)
		self.step += 1

	def wander(self):
		# Generate Reynold's Wander circle
		if self.vel.x and self.vel.y:
			circle_center = self.vel
			circle_center = circle_center * self.circle_dist
			dx = math.cos(self.wander_angle)
			dy = math.sin(self.wander_angle)
			displacement = vec(dx, dy) * self.circle_radius
			self.wander_angle += (random.random() - 0.5) * self.angle_change
			self.vel += circle_center + displacement

	def update(self):
		self.move()

		if self.vel.x > 0:
			frame = (self.pos.x // 5) % len(self.img_right)
			self.image = self.img_right[int(frame)]
		elif self.vel.x < 0:
			frame = (self.pos.x // 5) % len(self.img_left)
			self.image = self.img_left[int(frame)]
		elif self.vel.y > 0:
			frame = (self.pos.y // 5) % len(self.img_down)
			self.image = self.img_down[int(frame)]
		else:
			frame = (self.pos.y // 5) % len(self.img_up)
			self.image = self.img_up[int(frame)]
		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.pos += self.vel * self.game.dt
		self.hit_rect.centerx = self.pos.x
		collide_with_walls(self, self.level.walls, 'x')
		self.hit_rect.centery = self.pos.y
		collide_with_walls(self, self.level.walls, 'y')
		self.rect.center = self.hit_rect.center

class NPC(pg.sprite.Sprite):
	def __init__(self, level, data, x, y, dir='s'):
		self.groups = level.npcs, level.all_sprites, level.walls
		pg.sprite.Sprite.__init__(self, self.groups)
		self.pos = vec(x, y)
		self.rand = data['rand']
		self.dialogue = data['dialogue']
		self.name = data['name']
		self.logic = data['logic']
		img_files = data['file']
		self.level = level
		self.zoom = 1
		self.game = level.game
		if img_files:
			self.img_down = pg.transform.scale(pg.image.load(os.path.join(IMG_FOLDER, img_files[0])), (32, 48))
			self.img_up = pg.transform.scale(pg.image.load(os.path.join(IMG_FOLDER, img_files[1])), (32, 48))
			self.img_left = pg.transform.scale(pg.image.load(os.path.join(IMG_FOLDER, img_files[2])), (32, 48))
			self.img_right = pg.transform.scale(pg.image.load(os.path.join(IMG_FOLDER, img_files[3])), (32, 48))
		else:
			self.img_up = pg.Surface((32, 48))
			self.img_left = pg.Surface((32, 48))
			self.img_right = pg.Surface((32, 48))
			self.img_down = pg.Surface((32, 48))
			self.img_up.fill(YELLOW)
			self.img_left.fill(TEAL)
			self.img_right.fill(RED)
			self.img_down.fill(GREEN)
		if dir is 'n' or 'N':
			self.image = self.img_down
		elif dir is 's' or 'S':
			self.image = self.img_up
		elif dir is 'w' or 'W':
			self.image = self.img_left
		elif dir is 'e' or 'E':
			self.image = self.img_right
		self.rect = self.image.get_rect()
		self.rect = self.rect.inflate(self.rect.width * self.zoom, self.rect.height * self.zoom)
		self.rect.center = self.pos
		self.hit_rect = NPC_HIT_RECT.inflate(NPC_HIT_RECT.width, NPC_HIT_RECT.height)
		self.hit_rect.center = (self.rect.center[0], self.rect.center[1])


	def events(self):
		player = self.level.player
		if self.pos.distance_to(player.pos) < 80:
			if player.dir.x == -1 and self.pos.x < player.pos.x:
				self.image = self.img_right
				self.game.director.scene.render()
				self.game.director.scene_stack.append(self.game.director.scene)
				self.speak()
			elif player.dir.x == 1 and self.pos.x > player.pos.x:
				self.image = self.img_left
				self.game.director.scene.render()
				self.game.director.scene_stack.append(self.game.director.scene)
				self.speak()
			elif player.dir.y == -1 and self.pos.y < player.pos.y:
				self.image = self.img_down
				self.game.director.scene.render()
				self.game.director.scene_stack.append(self.game.director.scene)
				self.speak()
			elif player.dir.y == 1 and self.pos.y > player.pos.y:
				self.image = self.img_up
				self.game.director.scene.render()
				self.game.director.scene_stack.append(self.game.director.scene)
				self.speak()

	def speak(self):
		print self.name
		if self.name == 'Professor Bui':
			print self.logic['spoken']
			if not self.logic['spoken']:
				self.start_game(1)
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[0], False))
				self.logic['spoken'] = True
			elif self.logic['spoken'] and not self.logic['completed']:
				self.start_game(1)
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[1], False))
			elif self.logic['completed']:
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[2], False))

		elif self.name is 'Professor Emrich':
			if not self.logic['spoken']:
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[0], False))
				self.logic['spoken'] = True
			else:
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[1], False))

		elif self.name is 'Professor Kumar':
			if not self.logic['spoken']:
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[0], False))
				self.logic['spoken'] = True
			else:
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[1], False))

		elif self.name is 'Professor Brockman':
			if not self.logic['spoken']:
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[0], False))
				self.logic['spoken'] = True
			else:
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[1], False))

		elif self.name is 'Professor Bualuan':
			if not self.logic['spoken']:
				self.start_game(2)
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.game.level.player.name, self.dialogue[0], False))
				self.logic['spoken'] = True
			elif self.logic['squirrels'] >= 3:
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[2], False))
				randnum = random.random()
				if randnum >= 0.5:
					self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[3], False))
				else:
					self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[4], False))
			else:
				self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[5], False))


	def start_game(self, game):
		if game is 1:
			self.game.director.scene_stack.append(systems.SpideyGame(self.game.director, self.game, textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[2], False)))
		if game is 2:
			self.game.director.scene_stack.append(textbox.TextBox(self.game.director, self.game.screen, self.name, self.dialogue[1], False))

