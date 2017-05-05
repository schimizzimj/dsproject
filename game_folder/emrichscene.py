#!/usr/bin/env python2.7

import pygame as pg
import sys
from os import path
import scene
from settings import *
from sprites import *

class emrichscene(scene.Scene):
    def __init__(self, director):
        # make screen
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pg.display.set_caption("Data Structures")
        font = pg.font.Font(pg.font.get_default_font(), 12)
        self.screen.fill(WHITE)

        # set vars
        # width, height
        self.w = 150
        self.h = 50
        # mouse vars
        self.pressed = False
        self.drag = False
        # height of first rectangle
        self.hi = HEIGHT/4-w/2

        # rectangle vars
        self.xBST = WIDTH/2-w/2
        self.yBST = hi
        self.xLL = WIDTH/2-w/2
        self.yLL = hi + 3*h
        self.xA = WIDTH/2-w/2
        self.yA = hi + 6*h

        # ellipsis vars
        self.xe = 0
        self.ye = 0
        self.he = 0
        self.we = 0

        # draw elements
        self.drawHeader()
        self.drawButton()
        self.drawBSTRect()
        self.drawLLRect()
        self.drawARect()

    def events(self):
        # get one event
        event = pg.event.poll()
        # mouse pressed
        if event.type == pg.MOUSEBUTTONDOWN:
            self.pressed = True
            self.coords = pg.mouse.get_pos()
            # drag bst
            if self.xBST < coords[0] < self.xBST + self.w and self.yBST < coords[1] < self.yBST + self.h:
                self.xBST = coords[0] - self.w/2
                self.yBST = coords[1] - self.h/2
            # drag linked list
            elif self.xLL < coords[0] < self.xLL + self.w and self.yLL < coords[1] < self.yLL + self.h:
                self.xLL = coords[0] - self.w/2
                self.yLL = coords[1] - self.h/2
            # drag array
            elif self.xA < coords[0] < self.xA + self.w and self.yA < coords[1] < self.yA + self.h:
                self.xA = coords[0] - self.w/2
                self.yA = coords[1] - self.h/2
            # press button to check order
            elif self.xe < coords[0] < self.xe + self.we and self.ye < coords[1] < self.ye + self.he:
                endGame()
        # stop dragging box
        elif event.type == pg.MOUSEBUTTONUP:
            self.pressed = False

    def update(self):
        if self.pressed:
            holding(self)
            # drag bst
            if self.xBST < coords[0] < self.xBST + self.w and self.yBST < coords[1] < self.yBST + self.h:
                self.xBST = coords[0] - self.w/2
                self.yBST = coords[1] - self.h/2
            # drag linked list
            elif self.xLL < coords[0] < self.xLL + self.w and self.yLL < coords[1] < self.yLL + self.h:
                self.xLL = coords[0] - self.w/2
                self.yLL = coords[1] - self.h/2
            # drag array
            elif self.xA < coords[0] < self.xA + self.w and self.yA < coords[1] < self.yA + self.h:
                self.xA = coords[0] - self.w/2
                self.yA = coords[1] - self.h/2

    def render(self, screen):
        self.screen.fill(WHITE)
        self.drawHeader()
        self.drawButton()
        self.drawBSTRect()
        self.drawLLRect()
        self.drawARect()

    def drawButton(self):
        #global xe, ye, he, we
        length = 80
        self.he = length
        self.we = length/2
        self.xe = WIDTH/2 - length/2
        self.ye = 4*HEIGHT/5
        pg.draw.ellipse(screen, (0,255,0), pg.Rect(self.xe, self.ye, length, length/2))
        screen.blit(font.render("Done", True, BLACK), (WIDTH/2-length/4, 4*HEIGHT/5+length/6))

    def drawBSTRect(self):
        #global xBST, yBST
        rect = pg.draw.rect(screen, TEAL, pg.Rect(self.xBST, self.yBST, self.w, self.h))
        pg.display.update()
        addText(self.xBST, self.yBST, self.h, "Binary Search Tree")

    def drawLLRect(self):
        # global xLL, yLL
        rect = pg.draw.rect(screen, TEAL, pg.Rect(self.xLL, self.yLL, self.w, self.h))
        pg.display.update()
        addText(self.xLL, self.yLL, self.h, "Single-Linked List")

    def drawARect(self):
        # global xA, yA
        rect = pg.draw.rect(screen, TEAL, pg.Rect(self.xA, self.yA, self.w, self.h))
        pg.display.update()
        addText(self.xA, self.yA, self.h, "Array")

    def addText(self, xT, yT, h, label):
        self.screen.blit(font.render(label, True, BLACK), (xT, yT+h/2))
        pg.display.update()

    def holding(self):
        #global pressed, coords
        if self.pressed:
            self.coords = pg.mouse.get_pos()

    def drawHeader(self):
        # header
        self.screen.blit(font.render("Drag the data structures in smallest to largest average time complexity of accessing an element) ", True, BLACK), (WIDTH/3, HEIGHT/10))
        self.screen.blit(font.render("Press the green button when done", True, BLACK), (WIDTH/3, HEIGHT/10+12))

    def endGame(self):
        self.screen.fill(TEAL)
        bigFont = pg.font.Font(pg.font.get_default_font(), 48)
        if self.xA < self.xBST < self.xLL:
            # correct order
            screen.blit(bigFont.render("Correct!", True, WHITE), (WIDTH/3, HEIGHT/2))
        else:
            screen.blit(bigFont.render("Not quite! Try again later", True, WHITE), (WIDTH/3, HEIGHT/2))
