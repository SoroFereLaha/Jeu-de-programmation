#coding:utf-8


import pygame
from comet import Comet

# class pour gerer les evenement de nos commetes
class CometFallEvent(pygame.sprite.Sprite):
    """class pour gerer la chutte de commetes"""

    def __init__(self, game):
        """lors du chargement --> cree un compteur pour l'evenemnet comete"""
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False # pour activer l'evenement chute

        # definir un groupe sprite pour stocker nos commetes vu qe y'en a plusieurs
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        """va nous permetre d'incrementer nos barre de jauge"""
        self.percent += self.percent_speed / 100 # comme ca ca va augmenter lentement
    
    def reset_percent(self):
        self.percent = 0

    def est_rempli(self):
        """determine si la jauge est rempli"""
        return self.percent >= 100

    def chute_comet(self):
        """permet de faire apparaitre les commetes 15 fois"""
        for i in range(1, 15):
            self.all_comets.add(Comet(self))
    
    def pluie_comet(self):
        if self.est_rempli() and len(self.game.all_monstres) == 0:
            print("les commetes arrives")
            self.chute_comet()
            self.fall_mode = True # activer l'evenement quand la jauge est remplie et les monstres sont supprimés

    def update_bar(self, surface):
        """on fera pareil que pour les barres de vies ( deux barres superposées )"""
        pygame.draw.rect(surface, (0,0,0), (0,surface.get_height()-20, surface.get_width(), 10))
        pygame.draw.rect(surface, (187,11,11), (0,surface.get_height()-20, (surface.get_width() / 100) * self.percent, 10))

        # ajouter du pourcentage a la barre
        self.add_percent()

