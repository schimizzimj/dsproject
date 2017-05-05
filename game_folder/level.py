import pygame as pg
import tilemap
import sprites
from settings import *
from os import path
import textbox
import random
vec = pg.math.Vector2

class Level(object):
	'''
	Parent class for the individual levels (different rooms) within the game.
	Each level loads its map and sprites by itself, and therefore each have there own sprite groups.
	'''
	def __init__(self, game, entrance=0):
		self.game = game
		self.entrance = entrance

	def load(self):
		raise NotImplementedError

	def events(self):
		raise NotImplementedError

	def update(self):
		raise NotImplementedError

	def render(self):
		raise NotImplementedError


class TopLevel(Level):
	def __init__(self, game, entrance=0):
		Level.__init__(self, game, entrance)
		self.scale = 2
		self.name = 'top_world'
		self.load()

	def load(self):
		self.map = tilemap.TiledMap(path.join(self.game.map_folder, 'top_world.tmx'))
		self.map_img = self.map.make_map()
		self.overlay_img = self.map.make_overlay()
		image_size = self.map_img.get_size()
		self.map_img = pg.transform.scale(self.map_img, (self.scale*image_size[0], self.scale*image_size[1]))
		self.overlay_img = pg.transform.scale(self.overlay_img, (self.scale*image_size[0], self.scale*image_size[1]))
		self.map_rect = self.map_img.get_rect()
		self.all_sprites = pg.sprite.Group()
		self.walls = pg.sprite.Group()
		self.squirrels = pg.sprite.Group()
		for tile_object in self.map.tmxdata.objects:
			if tile_object.name == 'wall':
				sprites.Obstacle(self, self.game, self.scale*tile_object.x, self.scale*tile_object.y,
					self.scale*tile_object.width, self.scale*tile_object.height)
			if tile_object.name == 'player' and int(tile_object.entrance) == self.entrance:
				self.player = sprites.Player(self, self.game, self.scale*tile_object.x, self.scale*tile_object.y, 0);
		self.camera = tilemap.Camera(self.scale*self.map.width, self.scale*self.map.height)
		self.draw_debug = False
		for x in range(0, random.randrange(5, 10)):
			x_pos = (self.scale * self.map.width) * random.random()
			y_pos = (self.scale * self.map.height) * random.random()
			self.ai = sprites.Squirrels(self, self.game, x_pos, y_pos, 0)

	def events(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.game.director.change_scene(self.game.director.scene_stack.pop()) # Return to menu
				if event.key == pg.K_h:
					self.draw_debug = not self.draw_debug
				if event.key == pg.K_SPACE:

					for squirrel in self.squirrels:
						if self.player.pos.distance_to(squirrel.pos) < 50:
							self.game.director.scene_stack.append(self.game.director.scene)
							self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.screen, squirrel.speech['name'], squirrel.speech['dialogue'], True))

					if self.player.pos.x > 1709 and self.player.pos.x < 1719:
						if self.player.pos.y == 467 and self.player.dir.y == -1:
							if self.game.json['npcs'][0]['logic']['completed'] and \
							 	self.game.json['npcs'][1]['logic']['completed'] and \
									self.game.json['npcs'][2]['logic']['completed'] and \
										self.game.json['npcs'][3]['logic']['completed']:
								pass
							else:
								self.game.director.scene_stack.append(self.game.director.scene)
								self.game.director.change_scene(textbox.TextBox(self.game.director, self.game.director.screen, None, ["This door is locked."], False))

		if self.player.pos.x > 1455 and self.player.pos.x < 1492:
			if self.player.pos.y == 1363 and self.player.dir.y == -1:
				self.game.level_stack.append(self.game.level)
				self.game.change_level(DebartLevel(self.game, 0))
			elif self.player.pos.y == 685 and self.player.dir.y == 1:
				self.game.level_stack.append(self.game.level)
				self.game.change_level(DebartLevel(self.game, 1))

		if self.player.pos.x > 1143 and self.player.pos.x < 1165:
			if self.player.pos.y == 563 and self.player.dir.y == -1:
				self.game.level_stack.append(self.game.level)
				self.game.change_level(FitzpatrickLevel(self.game, 0))

		if self.player.pos.x > 1709 and self.player.pos.x < 1719:
			if self.player.pos.y == 467 and self.player.dir.y == -1:
				if self.game.json['npcs'][0]['logic']['completed'] and \
				 	self.game.json['npcs'][1]['logic']['completed'] and \
						self.game.json['npcs'][2]['logic']['completed'] and \
							self.game.json['npcs'][3]['logic']['completed']:
					pass
				

	def update(self):
		self.all_sprites.update()
		self.camera.update(self.player)

	def render(self):
		self.game.background.blit(self.map_img, self.camera.apply_rect(self.map_rect))
		if self.draw_debug:
			for wall in self.walls:
				pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(wall.rect), 1)
		for sprite in self.all_sprites:
			if sprite.name != 'Player':
				if sprite.zoom > 0:
					self.game.background.blit(pg.transform.scale(sprite.image, (sprite.rect.width * sprite.zoom, sprite.rect.height * sprite.zoom)), self.camera.apply(sprite))
				else:
					self.game.background.blit(sprite.image, self.camera.apply(sprite))
				if self.draw_debug:
					pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
		self.game.background.blit(pg.transform.scale(self.player.image, (self.player.rect.width, self.player.rect.height)), self.camera.apply(self.player))
		if self.draw_debug:
			pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(self.player.hit_rect), 1)
		self.game.background.blit(self.overlay_img, self.camera.apply_rect(self.map_rect))


class DebartLevel(Level):
	def __init__(self, game, entrance=0):
		Level.__init__(self, game, entrance)
		self.scale = 4
		self.name = 'debart'
		self.load()

	def load(self):
		self.map = tilemap.TiledMap(path.join(self.game.map_folder, 'debart.tmx'))
		self.map_img = self.map.make_map()
		self.overlay_img = self.map.make_overlay()
		image_size = self.map_img.get_size()
		self.map_img = pg.transform.scale(self.map_img, (self.scale*image_size[0], self.scale*image_size[1]))
		self.overlay_img = pg.transform.scale(self.overlay_img, (self.scale*image_size[0], self.scale*image_size[1]))
		self.map_rect = self.map_img.get_rect()
		self.all_sprites = pg.sprite.Group()
		self.walls = pg.sprite.Group()
		for tile_object in self.map.tmxdata.objects:
			if tile_object.name == 'wall':
				sprites.Obstacle(self, self.game, self.scale*tile_object.x, self.scale*tile_object.y,
					self.scale*tile_object.width, self.scale*tile_object.height)
			if tile_object.name == 'player' and int(tile_object.entrance) == self.entrance:
				self.player = sprites.Player(self, self.game, self.scale*tile_object.x, self.scale*tile_object.y, 1);
		self.camera = tilemap.Camera(self.scale*self.map.width, self.scale*self.map.height)
		self.draw_debug = False

	def events(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.game.director.change_scene(self.game.director.scene_stack.pop()) # Return to menu
				if event.key == pg.K_h:
					self.draw_debug = not self.draw_debug

		if self.player.pos.x > 108 and self.player.pos.x < 162:
			if self.player.pos.y == 166 and self.player.dir.y == -1:
				#self.game.change_level(TopLevel(self.game, 1))
				next_level = self.game.level_stack.pop()
				next_level.player.pos = vec(1472, 675)
				self.game.change_level(next_level)
		if self.player.pos.x > 81 and self.player.pos.x < 176:
			if self.player.pos.y == 2010 and self.player.dir.y == 1:
				#self.game.change_level(TopLevel(self.game, 2))
				next_level = self.game.level_stack.pop()
				next_level.player.pos = vec(1473, 1365)
				self.game.change_level(next_level)

		if self.player.pos.x >= 594 and self.player.pos.x <= 622:
			if self.player.pos.y == 614 and self.player.dir.y == -1:
				self.game.level_stack.append(self.game.level)
				self.game.change_level(ClassroomLevel(self.game, 102, 0))
		elif self.player.pos.x >= 338 and self.player.pos.x <= 366:
			if self.player.pos.y == 1254 and self.player.dir.y == -1:
				self.game.level_stack.append(self.game.level)
				self.game.change_level(ClassroomLevel(self.game, 101, 0))
		elif self.player.pos.x >= 466 and self.player.pos.x <= 494:
			if self.player.pos.y == 1702 and self.player.dir.y == -1:
				self.game.level_stack.append(self.game.level)
				self.game.change_level(ClassroomLevel(self.game, 141, 0))

	def update(self):
		self.all_sprites.update()
		self.camera.update(self.player)

	def render(self):
		self.game.background.blit(self.map_img, self.camera.apply_rect(self.map_rect))
		if self.draw_debug:
			for wall in self.walls:
				pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(wall.rect), 1)
		for sprite in self.all_sprites:
			if sprite.name != 'Player':
				if sprite.zoom > 0:
					self.game.background.blit(pg.transform.scale(sprite.image, (sprite.rect.width * sprite.zoom, sprite.rect.height * sprite.zoom)), self.camera.apply(sprite))
				else:
					self.game.background.blit(sprite.image, self.camera.apply(sprite))
				if self.draw_debug:
					pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
		self.game.background.blit(pg.transform.scale(self.player.image, (self.player.rect.width * self.player.zoom, self.player.rect.height * self.player.zoom)),
			self.camera.apply(self.player))
		if self.draw_debug:
			pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(self.player.hit_rect), 1)
		self.game.background.blit(self.overlay_img, self.camera.apply_rect(self.map_rect))

class ClassroomLevel(Level):
	def __init__(self, game, room, entrance=0):
		Level.__init__(self, game, entrance)
		self.scale = 4
		self.room = room
		self.name = 'classroom'
		self.load()

	def load(self):
		if self.room is 102:
			self.map = tilemap.TiledMap(path.join(self.game.map_folder, '102.tmx'))
		elif self.room is 101:
			self.map = tilemap.TiledMap(path.join(self.game.map_folder, '101.tmx'))
		elif self.room is 141:
			self.map = tilemap.TiledMap(path.join(self.game.map_folder, '141.tmx'))
		self.map_img = self.map.make_map()
		self.overlay_img = self.map.make_overlay()
		image_size = self.map_img.get_size()
		self.map_img = pg.transform.scale(self.map_img, (self.scale*image_size[0], self.scale*image_size[1]))
		self.overlay_img = pg.transform.scale(self.overlay_img, (self.scale*image_size[0], self.scale*image_size[1]))
		self.map_rect = self.map_img.get_rect()
		self.all_sprites = pg.sprite.Group()
		self.npcs = pg.sprite.Group()
		self.walls = pg.sprite.Group()
		for tile_object in self.map.tmxdata.objects:
			if tile_object.name == 'wall':
				sprites.Obstacle(self, self.game, self.scale*tile_object.x, self.scale*tile_object.y,
					self.scale*tile_object.width, self.scale*tile_object.height)
			if tile_object.name == 'NPC':
				sprites.NPC(self, self.game.json['npcs'][int(tile_object.json)], self.scale*tile_object.x, self.scale*tile_object.y)
			if tile_object.name == 'player' and int(tile_object.entrance) == self.entrance:
				self.player = sprites.Player(self, self.game, self.scale*tile_object.x, self.scale*tile_object.y, 1)
		self.camera = tilemap.Camera(self.scale*self.map.width, self.scale*self.map.height)
		self.draw_debug = False

	def events(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.game.director.change_scene(self.game.director.scene_stack.pop()) # Return to menu
				if event.key == pg.K_h:
					self.draw_debug = not self.draw_debug
				if event.key == pg.K_SPACE:
					for npc in self.npcs:
						npc.events()


		if self.player.pos.x >= 402 and self.player.pos.x <= 494:
			if self.player.pos.y == 1306 and self.player.dir.y == 1:
					self.game.change_level(self.game.level_stack.pop())


	def update(self):
		self.all_sprites.update()
		self.camera.update(self.player)

	def render(self):
		self.game.background.blit(self.map_img, self.camera.apply_rect(self.map_rect))
		if self.draw_debug:
			for wall in self.walls:
				pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(wall.rect), 1)
		for sprite in self.all_sprites:
			if sprite.name != 'Player':
				if sprite.zoom > 0:
					self.game.background.blit(pg.transform.scale(sprite.image, (sprite.rect.width * sprite.zoom, sprite.rect.height * sprite.zoom)), self.camera.apply(sprite))
				else:
					self.game.background.blit(sprite.image, self.camera.apply(sprite))
				if self.draw_debug:
					pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
		self.game.background.blit(pg.transform.scale(self.player.image, (self.player.rect.width * self.player.zoom, self.player.rect.height * self.player.zoom)),
			self.camera.apply(self.player))
		if self.draw_debug:
			pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(self.player.hit_rect), 1)
		self.game.background.blit(self.overlay_img, self.camera.apply_rect(self.map_rect))

class FitzpatrickLevel(Level):
	def __init__(self, game, entrance=0):
		Level.__init__(self, game, entrance)
		self.scale = 4
		self.name = 'fitzpatrick'
		self.load()

	def load(self):
		self.map = tilemap.TiledMap(path.join(self.game.map_folder, 'fitzpatrick.tmx'))
		self.map_img = self.map.make_map()
		self.overlay_img = self.map.make_overlay()
		image_size = self.map_img.get_size()
		self.map_img = pg.transform.scale(self.map_img, (self.scale*image_size[0], self.scale*image_size[1]))
		self.overlay_img = pg.transform.scale(self.overlay_img, (self.scale*image_size[0], self.scale*image_size[1]))
		self.map_rect = self.map_img.get_rect()
		self.all_sprites = pg.sprite.Group()
		self.walls = pg.sprite.Group()
		for tile_object in self.map.tmxdata.objects:
			if tile_object.name == 'wall':
				sprites.Obstacle(self, self.game, self.scale*tile_object.x, self.scale*tile_object.y,
					self.scale*tile_object.width, self.scale*tile_object.height)
			if tile_object.name == 'player' and int(tile_object.entrance) == self.entrance:
				self.player = sprites.Player(self, self.game, self.scale*tile_object.x, self.scale*tile_object.y, 1);
		self.camera = tilemap.Camera(self.scale*self.map.width, self.scale*self.map.height)
		self.draw_debug = False

	def events(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.game.director.change_scene(self.game.director.scene_stack.pop()) # Return to menu
				if event.key == pg.K_h:
					self.draw_debug = not self.draw_debug

		if self.player.pos.x >= 466 and self.player.pos.x <= 558:
				if self.player.pos.y == 1498 and self.player.dir.y == 1:
					next_level = self.game.level_stack.pop()
					next_level.player.pos = vec(1153, 563)
					self.game.change_level(next_level)

	def update(self):
		self.all_sprites.update()
		self.camera.update(self.player)

	def render(self):
		self.game.background.blit(self.map_img, self.camera.apply_rect(self.map_rect))
		if self.draw_debug:
			for wall in self.walls:
				pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(wall.rect), 1)
		for sprite in self.all_sprites:
			if sprite.name != 'Player':
				if sprite.zoom > 0:
					self.game.background.blit(pg.transform.scale(sprite.image, (sprite.rect.width * sprite.zoom, sprite.rect.height * sprite.zoom)), self.camera.apply(sprite))
				else:
					self.game.background.blit(sprite.image, self.camera.apply(sprite))
				if self.draw_debug:
					pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
		self.game.background.blit(pg.transform.scale(self.player.image, (self.player.rect.width * self.player.zoom, self.player.rect.height * self.player.zoom)),
			self.camera.apply(self.player))
		if self.draw_debug:
			pg.draw.rect(self.game.background, CYAN, self.camera.apply_rect(self.player.hit_rect), 1)
		self.game.background.blit(self.overlay_img, self.camera.apply_rect(self.map_rect))
