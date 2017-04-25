#!/usr/bin/env python2.7

import pygame as pg
import sys
from os import path
from settings import *
from sprites import *

class dsSimpleMap:
    
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        #self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.disp_background()
        
    def disp_background(self):
        self.screen.fill(WHITE)
        xOff = 30
        self.make_stairs(xOff, 50, 'l')
        self.make_stairs(WIDTH-xOff, 50, 'r')
        self.make_stairs(WIDTH/2, 50, 's')
    
    def make_stairs(self, xi, yi, dir):
        h = 10
        w = 50
        shift = w/5
        numStairs = 12
        #stairs on right side
        if dir is 'r':
            shift = -shift
            xi = xi - w
        elif dir is 'l':
            # draw background
            self.draw_wall_and_floor(yi+h*numStairs)
        # stairs in middle
        elif dir is 's':
            shift = 0
            xi = xi - w/2
        # draw stairs
        for i in range(0, numStairs):
            pg.draw.rect(self.screen, LIGHTGREY, pg.Rect(xi+shift*i, yi+h*i, w, h))
            pg.draw.rect(self.screen, DARKGREY, pg.Rect(xi+shift*i, yi+h*i, w, h), 2)
        
    def draw_wall_and_floor(self, yi):
        pg.draw.rect(self.screen, TEAL, pg.Rect(0, 0, WIDTH, yi))
        pg.draw.rect(self.screen, BEIGE, pg.Rect(0, yi, WIDTH, HEIGHT-yi))
    
    def draw_prof(self, prof):
        # set color and pos
        x = WIDTH/4
        y = HEIGHT * 3 /4
        s = 30
        name = 'Prof ' + prof
        if prof is 'Emrich':
            color = GREENYELLOW
        else:
            color = PURPLE
        pg.draw.rect(self.screen, color, pg.Rect(x, y, s, s))
        FONT = pg.font.Font(pg.font.get_default_font(), 12)
        text = FONT.render(name, True, BLACK)
        self.screen.blit(text, (x-s*.5, y+s*1.2))
        self.draw_player(FONT, y, s)
            
    def draw_player(self, FONT, y, s):
        x = WIDTH*2/3
        pg.draw.rect(self.screen, RED, pg.Rect(x, y, s, s))
        text = FONT.render("You", True, BLACK)
        self.screen.blit(text, (x, y+s*1.2))

    def start_game(self, prof):
        self.draw_prof(prof)

    def run(self):
        self.running = True
        while self.running:
            pass
            # self.dt = self.clock.tick(FPS) / 1000.0
            #self.events()
            #self.draw()

# create game
classroom = dsSimpleMap()
classroom.start_game('Emrich')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()


