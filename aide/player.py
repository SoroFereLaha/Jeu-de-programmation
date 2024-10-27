#coding:utf-8

import pygame
import animation
from projectile import Projectile

# class qui represente le joueur
class Player(animation.AnimateSprite): 
    """ pour que nos joueurs, ennemis comet etcc soient pris comme etant des composants du jeu, on doit les transformer comme des sprites. un sprite dans un jeu video c'est un objet qui peut se deplacer. pour cela a chaque fois qu'on veut faire d'un objet un sprite, sa class doit heriter de pygame.sprite.Sprite"""
    def __init__(self, game):
        super().__init__("player") # on appelle le constructeur de la super class pour initiaser ses composants
        self.game = game # on passe l'instance de la classe en parametre ( game = Game ) comme ca maintenant on peut utiliser tout les ettributs et methode de la classe Game
        self.max_health = 100
        self.health = 100
        self.attack = 10
        # les sprite.Group permettent de creee un groupe d'elements et ici on veut cree un groupe de projectile pour que l'utilisateur puissent lancer plusieurs projectiles
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 2 #5px
        self.image = pygame.image.load("Assets/player.png")
        # pour deplacer l'image sur notre jeu on doit recuperer ses coordonnès, en fait les images sont dans un rect, donc on recupere se rect et c'est se rect qu'on va deplacer
        self.rect = self.image.get_rect()
        self.rect.x = 400 # en px
        self.rect.y = 300
    
    def update_animation(self):
        self.animate()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de point de vie
            self.game.game_over()

    def health_bar(self, surface): 
        # dessiner notre barre de vie background a l'ecran
        pygame.draw.rect(surface, (0, 0, 0), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        # dessiner notre barre de vie a l'ecran
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])



    def lancer_projectile(self):
        #projectile = Projectile() ||| self.all_projectiles.add(projectile) autre methodes moins optimale
        self.all_projectiles.add(Projectile(self)) # a chaque fois qu'on cree un projectile on l'ajoute au groupe de projectiles comme ca le joueur peut en lancer plusieurs. et le self en argument va nous permettre de recupperer les coordonnees du joueur qui a lancer le profectile pouvoir positionner le prjectile en face de lui
        # demarrer l'animation quand le joueur lance le projectile
        self.start_animation()
        self.game.sound_manager.play("tir")

    def move_right(self):
        """le deplacement se fait seulemnt si le joueur n'est pas en colission avec un monstre, deplacement a droite du joueur
                pour deplacer a droite on ajoute sa vitesse sur sa position en x 
        """

        # si le joueur n'est pas en collision il peut se deplacer
        if not self.game.verifier_collision(self, self.game.all_monstres):# comme dit precedement la fonction verifier_colision prend en parametre un objet et un group de sprite et ici notre objet est l'objet courant c'est pour qu'on a mis self et le groupe c'est le groupe de monstre
            self.rect.x += self.velocity

    def move_left(self):
        """deplacement a gauche du joueur
                pour deplacer a gauche on retire sa vitesse à sa position en x      
        """
        self.rect.x -= self.velocity
