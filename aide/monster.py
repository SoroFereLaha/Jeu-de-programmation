#coding:utf-8

import pygame
import random
import animation

class Monstre(animation.AnimateSprite):
    """nos monstres ne vont plus heriter de sprite.Sprite mais de animetSprite qui herite elle meme de sprite.Sprite, tout est relier"""


    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        """donc maintenant quand on defini le constructeur, il va appeller la super classe AnimateSprite et comme elle a besoin du nom de l'entier alors on la passe en parametre"""
        self.game = game
        self.max_health = 100
        self.health = 100
        self.attack = 0.3
        self.image = pygame.image.load("Assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 340 - offset 
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(0, 1)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    
    def damage(self, amount):
        """les degats subit par le monstre"""
        self.health -= amount
        # verifier si le nombre de vie restant est inferieur a zero
        if self.health <= 0:
            # au lieu de supprimer et recree un nouveau monstre, on redefinir ses proprietes et le faire reapparaitre
            self.rect.x = 1000 + random.randint(0, 100)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # ajouter nombre de points
            self.game.add_score(self.loot_amount)

            # si la barre d'evenement est charger a son maximun
            if self.game.comet_event.est_rempli():
                self.game.all_monstres.remove(self) #supprimer le monstre actuelle

            # declencher les commetes
            self.game.comet_event.pluie_comet()

    def update_animation(self):
        self.animate(loop=True)

    def health_bar(self, surface): # prend en parametre la surface sur laquelle on veut dessiner
        # couleur de bar de vie
        bar_color = (111, 210, 46) # vert
        background_bar_color = (0, 0, 0)
        # position x y width height de la barre de vie
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        # position x y width height de la barre de vie qui est en background
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        
        # dessiner notre barre de vie background a l'ecran
        pygame.draw.rect(surface, background_bar_color, back_bar_position)
        # dessiner notre barre de vie a l'ecran
        pygame.draw.rect(surface, bar_color, bar_position)


    def move_monstre(self):
        """deplacement du monstre. le deplacement ne se fait que s'il n'y pas de collion avec le groupe de joueur"""
        if not self.game.verifier_collision(self, self.game.all_joueurs): # pareil que collision joueur
            self.rect.x -= self.velocity
        # verifer le cas ou le monste est en collision avec le joueur pour lui infliger des degats
        else:
            self.game.joueur.damage(self.attack)


# definir une class pour la momie 
class Mummy(Monstre):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)

# definir une class pour l'alien
class Alien(Monstre):
    def __init__(self, game):
        super().__init__(game, "alien", (300,300), 30)
        self.health = 250
        self.max_health = 250
        self.set_speed(1)
        self.attack = 0.8
        self.set_loot_amount(80)