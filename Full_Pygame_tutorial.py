# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:22:40 2022

@author: James
"""
import pygame
from pygame.locals import*
pygame.init()
#Game loop begins
while True:
    # code
    # more code
    pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
DISPLAYSURF = pygame. display.set_mode(300,300)
color1 = pygame.Color(0,0,0)      #black
color2 = pygame.Color(255,255,255) #white
color3 = pygame.Color(128,128,128) #grey
color4 = pygame.Color(255,0,0)     #red
FPS  = pygame.time.Clock()
FPS.tick(60)
object1 = pygame.React((20,50),(50,100))
object2 = pygame. React((10,10),(100,100))
print(object1.colliderect(object2))
object1 = pygame.React((20,50),(50,100))
print(object1.collidepoint(50,75))
