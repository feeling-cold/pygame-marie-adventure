from itertools import cycle
import random

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,200))
clock = pygame.time.Clock()
'''
map = pygame.image.load("image/bg.png").convert_alpha()
map_rect = map.get_rect()
map_rect.x = 0
map_rect.y = 0
map2 = pygame.image.load("image/bg.png").convert_alpha()
map2_rect = map.get_rect()
map2_rect.x = 800
map2_rect.y = 0
'''

class Map():
    def __init__(self,path):
        self.map_img = pygame.image.load(path).convert_alpha()
        self.map_rect = self.map_img.get_rect()

    def rolling(self,x,y):
        self.map_rect.x = x
        self.map_rect.y = y

    def draw_map(self):
        screen.blit(self.map_img,self.map_rect)


class Marie():
    def __init__(self,x,y):
        self.runstate = False
        self.jumpstate = False
        self.jumpvalue = 0
        self.movespeed = random.randint(5,10)
        self.hero_img = (pygame.image.load("image/adventure1.png").convert_alpha(),
                pygame.image.load("image/adventure2.png").convert_alpha(),
                pygame.image.load("image/adventure3.png").convert_alpha(),)
        self.rect = self.hero_img[0].get_rect()
        self.index = 0
        self.list = cycle([0, 1, 2])

        self.rect.x = x
        self.tmp = x
        # self.ytmp = y
        self.rect.y = y
        self.lowest = y

    def posintion(self,x,y):
        pass

    def run(self):
        self.tmp += self.movespeed
        self.rect.x = self.tmp

    def back(self):
        self.tmp -= self.movespeed
        self.rect.x = self.tmp

    def jump(self):
        self.rect.y -= 137
        if self.rect.y == 0:
            self.rect.y = 137



    def draw_marie(self):
        self.index = next(self.list)
        screen.blit(self.hero_img[self.index],self.rect)

map1 = Map("image/bg.png")
map2 = Map("image/bg.png")
map1.rolling(0,0)
map2.rolling(800,0)
marie = Marie(50,137)



while True:

    map1.map_rect.x-=5
    map2.map_rect.x -= 5
    map1.draw_map()
    map2.draw_map()

    if map1.map_rect.x <= -800:
        map1.map_rect.x = 0
    if map2.map_rect.x <= 0:
        map2.map_rect.x = 800



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN and event.key == K_w:
            marie.jump()

        if event.type == KEYDOWN and event.key == K_d:
            marie.run()

        if event.type == KEYDOWN and event.key == K_a:
            marie.back()


    marie.draw_marie()
    clock.tick(30)
    pygame.display.update()
