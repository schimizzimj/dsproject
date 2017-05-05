import pygame as pg
from os import path
vec = pg.math.Vector2

# Declare what some colors are, useful later in other functions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
GREENYELLOW = (50, 205, 50)
BEIGE = (238, 223, 204)
TEAL = (95, 158, 160)
PURPLE = (147, 112, 219)
ND_BLUE = (3, 45, 86)
ND_GOLD = (157, 136, 57)
BROWN = (160, 82, 45)

# game settings
WIDTH = 1024 # 32 * 16
HEIGHT = 768 # 24 * 16
SCREEN_SIZE = [1280, 720] #1920x1080 1280x720
FPS = 60
TITLE = "ND Adventure"
BGCOLOR = DARKGREY

# necessary folders
GAME_FOLDER = path.dirname(__file__)
IMG_FOLDER = path.join(GAME_FOLDER, 'img')
MAP_FOLDER = path.join(GAME_FOLDER, 'map')

# What to display on the start menu
MENU_ITEMS = ('Start', 'Settings', 'Highscore', 'Quit')

# Tile settings
TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

FONT_SIZE = SCREEN_SIZE[1] / 10

#player settings
PLAYER_SPEED = 400
PLAYER_IMG = 'temp.png'
PLAYER_HIT_RECT = pg.Rect(0, 20, 18, 38)
NPC_HIT_RECT = pg.Rect(0, 20, 18, 30)
