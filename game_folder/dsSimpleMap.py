#!/usr/bin/env python2.7

import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
import time


class dsSimpleMap:
    def __init__(self):
        # pg.init()
        print "initializng"
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.disp_background()
        
    def disp_background(self):
        self.screen.fill(WHITE)
        xOff = 30
        yOff = 50
        self.draw_wall_and_floor(yOff + 10*12)
        self.draw_doors(xOff, yOff)
        self.draw_doors(WIDTH-2*xOff, yOff)
        self.draw_doors(WIDTH/2-.5*xOff, yOff)
        self.make_stairs(xOff, yOff, 'l')
        self.make_stairs(WIDTH-xOff, yOff, 'r')
        self.make_stairs(WIDTH/2, yOff, 's')
    
    def draw_doors(self, x, y):
        w = 30
        pg.draw.rect(self.screen, BROWN, pg.Rect(x, 0, w, y))
        pg.draw.rect(self.screen, BLACK, pg.Rect(x, 0, w, y), 2)
        pg.draw.rect(self.screen, BLACK, pg.Rect(x+w/4, w/4, w/2, w/2), 1)
        pg.draw.rect(self.screen, BLACK, pg.Rect(x+w/4, w*7/8, w/2, w/2), 1)
    
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
            #     self.draw_wall_and_floor(yi+h*numStairs)
            pass
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
        text = FONT.render(name, True, BLACK)
        self.screen.blit(text, (x-s*.5, y+s*1.2))
        self.draw_player(y, s)
            
    def draw_player(self, y, s):
        x = WIDTH*2/3
        pg.draw.rect(self.screen, RED, pg.Rect(x, y, s, s))
        text = FONT.render("You", True, BLACK)
        self.screen.blit(text, (x, y+s*1.2))

    def start_game(self, prof):
        self.draw_prof(prof)
        time.sleep(1)
        print "drawn prof"
        self.message(prof)

    def message(self, prof):
        x = WIDTH/4
        y = HEIGHT*2/3
        greeting = "Welcome to Data Structures!"
        text = FONT.render(greeting, True, BLACK)
        self.screen.blit(text, (x, y))
        pg.display.update()

        if prof is 'Kumar':
            msg = "Thanks for coming to class. A million points to you!"
        else:
            msg = "Are you excited for Demo Day? There will be lots of pizza."

        time.sleep(2)
        print "message"
        text = FONT.render(msg, True, BLACK)
        self.screen.blit(text, (x, y))
        pg.display.update()

    def run(self):
        self.running = True
        while self.running:
            pass
            # self.dt = self.clock.tick(FPS) / 1000.0
            #self.events()
            #self.draw()

pg.init()
FONT = pg.font.Font(pg.font.get_default_font(), 12)

# create game
classroom = dsSimpleMap()
pg.display.update()

prof = 'Kumar'
if prof is 'Kumar':
    classroom.start_game('Kumar')
else:
    classroom.start_game('Emrich')

while True:
   for event in pg.event.get():
       if event.type == pg.QUIT:
           pg.quit()
           sys.exit()
       pg.display.update()


