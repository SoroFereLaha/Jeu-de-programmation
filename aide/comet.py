#coding:utf-8

import pygame
import random

# class pour gerer nos commetes
class Comet(pygame.sprite.Sprite):
    """"""
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(20,800)
        self.rect.y = -random.randint(0,800) # vu que nous sommes sur l'axe y on doit mettre un nombre negatif car ca commence a 0 donc pour que ca apparaisent en haut hors de notre vu ca doit etre negatif mais on peut mettre un nombre negatif dans champ de vision d'où le mois -
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son 
        self.comet_event.game.sound_manager.play("meteorite")

        # verifier si il n'y a plus de commetes
        if len(self.comet_event.all_comets) == 0:
            print("l'evenemnt est fini")
            # remettre la jauge au depart
            self.comet_event.reset_percent()
            self.comet_event.game.start()
 
    def chute(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("sol")
            self.remove()

            # verifier si il n'y a plus de commetes
            """if len(self.comet_event.all_comets) == 0:
                print("l'evenemnt est fini")
                # remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False"""

        # verifier si la boule touche le joueur
        if self.comet_event.game.verifier_collision(self, self.comet_event.game.all_joueurs):
            print("joueur toucher")
            # retirer la boule de feu
            self.remove()
            # joueur subit des degats
            self.comet_event.game.joueur.damage(20)