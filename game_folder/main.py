#!/usr/bin/env python2.7

# Import modules
import pygame
import director
import menu

'''
Main driver file that instantiates an object of the director class and starts
the game in the StartMenu state.
'''

def main():
    d = director.Director()
    scene = menu.StartMenu(d)
    d.change_scene(scene)
    d.run()

if __name__ == '__main__':
    pygame.init()
    main()
