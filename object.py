#coding:utf-8

import pygame
import random
from player import Player, Score, Game

class Fruit(pygame.sprite.Sprite):
    """"""
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.score = Score()
        self.game = Game()
        self.all_player = pygame.sprite.Group()
        self.all_player.add(self.player)
        self.velocity = 1
        self.image = pygame.image.load("image/pomme.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10, 990)
        self.rect.y = - random.randint(50, 100)    


    def move_fruit(self):
        """"""
        self.rect.y += self.velocity


class Python(pygame.sprite.Sprite):
    """"""
    def __init__(self):
        super().__init__()
        self.velocity = 2
        self.image = pygame.image.load("image/python.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.origine_image = self.image
        self.image_rot = pygame.transform.rotozoom(self.origine_image, 5, 1)
        self.rect = self.image_rot.get_rect()
        self.rect.x = random.randint(10, 990)
        self.rect.y = - random.randint(50, 100)

    def move_fruit(self):
        """"""
        self.rect.y += self.velocity

        if self.rect.y >= 500:
            self.rect.x = random.randint(10, 990)
            self.rect.y = - random.randint(50, 100)

class Python_noir(Fruit):
    """"""
    def __init__(self):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load("image/pythonNoir.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10, 990)
        self.rect.y = - random.randint(50, 100)

    def move_fruit(self):
        """"""
        self.rect.y += self.velocity

        if self.rect.y >= 550 :
            self.rect.x = random.randint(10, 990)
            self.rect.y = - random.randint(50, 100)

class Java(Fruit):
    """"""
    def __init__(self):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load("image/java.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10, 990)
        self.rect.y = - random.randint(50, 100)

    def move_fruit(self):
        """"""
        self.rect.y += self.velocity

        if self.rect.y >= 550 :
            self.rect.x = random.randint(10, 990)
            self.rect.y = - random.randint(40, 100)

class Java_noir(Fruit):
    """"""
    def __init__(self):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load("image/javaNoir.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10, 990)
        self.rect.y = - random.randint(50, 100)

    def move_fruit(self):
        """"""
        self.rect.y += self.velocity

        if self.rect.y >= 550 :
            self.rect.x = random.randint(10, 990)
            self.rect.y = - random.randint(40, 100)