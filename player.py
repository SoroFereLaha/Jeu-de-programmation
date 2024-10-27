#coding:utf-8

import pygame
import random

class Player(pygame.sprite.Sprite):
    """"""
    def __init__(self):
        super().__init__()
        self.velocity = 3
        self.image = pygame.image.load("image/goutte-de-seau.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10,700)
        self.rect.y = 340
        self.image = pygame.transform.scale(self.image, (100,200))
        self.touch = {}
    
    def move_right_player(self):
        """"""
        self.rect.x += self.velocity 

    def move_left_player(self):
        """"""
        self.rect.x -= self.velocity     


class Score:
    """permet de gerer le score du joueur"""
    def __init__(self):
        self.lose_points = 0
        self.max_lose_points = 110
        self.score = 0
        self.font = pygame.font.Font("image/PottaOne-Regular.ttf", 40)
        self.best_score = self.score # a faire
        
    def update_score(self, points, surface):
        """mise a jour du score"""
        self.text = self.font.render(f"Score : {self.score}", 1, (0,0,0))
        surface.blit(self.text, (0,0))
        self.score = self.score + points
        #print("+",points)

    def game_over(self, surface):
        self.progessbar_white = pygame.draw.rect(surface,(196,104,204),(680,25,200,10))
        self.progessbar_noir = pygame.draw.rect(surface,(0,0,0),(680,25,(680 / 370) * self.lose_points,10))
        self.end = pygame.mixer.Sound("sons/game_over1.ogg")

        if self.lose_points >= self.max_lose_points:
            
            self.score = 0
            self.progressbar = 0  
            self.is_playing = False
            self.end.play()

class Game:
    def __init__(self):
        self.is_playing = False
        self.logo = pygame.image.load("image/start-button.png")
        self.logo = pygame.transform.scale(self.logo, (250,250))
        self.origine_logo = self.logo
        self.logo = pygame.transform.rotozoom(self.origine_logo,-5, 1)
        self.rect = self.logo.get_rect()
        self.rect.x = 310
        self.rect.y = 250
        self.image = pygame.image.load("image/recolter.png")
        self.image = pygame.transform.scale(self.image, (500,500))
        self.origine_image = self.image
        self.image = pygame.transform.rotozoom(self.origine_image, -20, 1)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 290/2
        self.image_rect.y = -50

