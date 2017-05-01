#!/usr/bin/env python2.7

# Import modules
import pygame
import director
import menu

def main():
    d = director.Director()
    scene = menu.StartMenu(d)
    d.change_scene(scene)
    d.run()

if __name__ == '__main__':
    pygame.init()
    main()
