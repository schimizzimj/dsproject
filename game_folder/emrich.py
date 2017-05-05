#!/usr/bin/env python2.7

import pygame as pg
import sys
from os import path
from settings import *
from sprites import *

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)
pg.display.set_caption("Data Structures")
font = pg.font.Font(pg.font.get_default_font(), 12)
screen.fill(WHITE)

w = 150
h = 50

pressed = False
drag = False

hi = HEIGHT/4-w/2

xBST = WIDTH/2-w/2
yBST = hi
xLL = WIDTH/2-w/2
yLL = hi + 3*h
xA = WIDTH/2-w/2
yA = hi + 6*h

xe = 0
ye = 0
he = 0
we = 0

def drawButton():
    global xe, ye, he, we
    length = 80
    he = length
    we = length/2
    xe = WIDTH/2 - length/2
    ye = 4*HEIGHT/5
    pg.draw.ellipse(screen, (0,255,0), pg.Rect(xe, ye, length, length/2))
    screen.blit(font.render("Done", True, BLACK), (WIDTH/2-length/4, 4*HEIGHT/5+length/6))

def BSTMoving():
    screen.fill(WHITE)
    drawButton()
    drawHeader()
    drawLLRect()
    drawARect()

def LLMoving():
    screen.fill(WHITE)
    drawButton()
    drawHeader()
    drawBSTRect()
    drawARect()

def AMoving():
    screen.fill(WHITE)
    drawButton()
    drawHeader()
    drawBSTRect()
    drawLLRect()

def drawBSTRect():
    global xBST, yBST
    rect = pg.draw.rect(screen, TEAL, pg.Rect(xBST, yBST, w, h))
    pg.display.update()
    addText(xBST, yBST, h, "Binary Search Tree")

def drawLLRect():
    global xLL, yLL
    rect = pg.draw.rect(screen, TEAL, pg.Rect(xLL, yLL, w, h))
    pg.display.update()
    addText(xLL, yLL, h, "Single-Linked List")

def drawARect():
    global xA, yA
    rect = pg.draw.rect(screen, TEAL, pg.Rect(xA, yA, w, h))
    pg.display.update()
    addText(xA, yA, h, "Array")

def addText(xT, yT, h, label):
    screen.blit(font.render(label, True, BLACK), (xT, yT+h/2))
    pg.display.update()

def holding():
    global pressed, coords
    if pressed:
        coords = pg.mouse.get_pos()

def drawHeader():
    # header
    screen.blit(font.render("Drag the data structures in smallest to largest average time complexity of accessing an element) ", True, BLACK), (WIDTH/3, HEIGHT/10))
    screen.blit(font.render("Press the green button when done", True, BLACK), (WIDTH/3, HEIGHT/10+12))

def endGame():
    screen.fill(TEAL)
    bigFont = pg.font.Font(pg.font.get_default_font(), 48)
    if xA < xBST < xLL:
        # correct order
        screen.blit(bigFont.render("Correct!", True, WHITE), (WIDTH/3, HEIGHT/2))
    else:
        screen.blit(bigFont.render("Not quite! Try again later", True, WHITE), (WIDTH/3, HEIGHT/2))

drawHeader()
drawButton()
drawBSTRect()
drawLLRect()
drawARect()

while True:
    if pressed:
        holding()
        if xBST < coords[0] < xBST + w and yBST < coords[1] < yBST + h:
            xBST = coords[0] - w/2
            yBST = coords[1] - h/2
            BSTMoving()
            drawBSTRect()
        elif xLL < coords[0] < xLL + w and yLL < coords[1] < yLL + h:
            xLL = coords[0] - w/2
            yLL = coords[1] - h/2
            LLMoving()
            drawLLRect()
        elif xA < coords[0] < xA + w and yA < coords[1] < yA + h:
            xA = coords[0] - w/2
            yA = coords[1] - h/2
            AMoving()
            drawARect()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            pressed = True
            coords = pg.mouse.get_pos()
            # drag bst
            if xBST < coords[0] < xBST + w and yBST < coords[1] < yBST + h:
                xBST = coords[0] - w/2
                yBST = coords[1] - h/2
                BSTMoving()
                drawBSTRect()
            # drag linked list
            elif xLL < coords[0] < xLL + w and yLL < coords[1] < yLL + h:
                xLL = coords[0] - w/2
                yLL = coords[1] - h/2
                LLMoving()
                drawLLRect()
            # drag array
            elif xA < coords[0] < xA + w and yA < coords[1] < yA + h:
                xA = coords[0] - w/2
                yA = coords[1] - h/2
                AMoving()
                drawARect()
            # press button to check order
            elif xe < coords[0] < xe + we and ye < coords[1] < ye + he:
                endGame()
        # stop dragging box
        elif event.type == pg.MOUSEBUTTONUP:
            pressed = False
        pg.display.update()



