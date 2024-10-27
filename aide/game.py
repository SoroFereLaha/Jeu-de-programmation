#coding:utf-8

import pygame
from player import Player
from monster import Monstre, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager

# class qui va representer notre jeu
class Game:
    def __init__(self):
        """les caracteristiques de base du jeu"""

        # definir si le jeu a commencer ou non
        self.is_playing = False
        # charger le joueur a chaque nouvelle partie
        self.joueur = Player(self) # vu qu'on a demander dans player l'instance de game alors on doit lui donner l'acces avec self vu que nous sommes deja dans la classe
        # groupe de monstre
        self.all_joueurs = pygame.sprite.Group() # on cree un groupe de sprite qui va contenir le joueur comme ca on pourra cree la collision du point de vu du monstre(on cree chez le joueur et chez le monstre sinon le monstre va continuer d'avancer) car la verifiercation de la colision se fait entre un objet et un group (a ne pas oublier)
        self.all_joueurs.add(self.joueur)
        # generer evnement comet
        self.comet_event = CometFallEvent(self) # on passe l'instance game dans cometfallevent pour pouvoir l'utiliser dans comet vu qu'on a deja passer l'insance de comet_event dans comet (c'est genre une inclusion dans une inslusions)
        self.all_monstres = pygame.sprite.Group()
        self.sounds_manager = SoundManager()
        self.touche_appuyer = {}
        self.font = pygame.font.Font("Assets/PottaOne-Regular.ttf", 25)
        self.score = 0


    def start(self):
        self.is_playing = True
        self.apparition_monstre(Mummy)
        self.apparition_monstre(Mummy)
        self.apparition_monstre(Alien)

    def add_score(self, points=10):
        self.game.score += points

    
    def game_over(self):
        # renouveller les parametre du jeu
        # on ecraser notre groupe de sprite avec un nouveau groupe vierges pour supprimer les joueurs
        self.all_monstres = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.joueur.health = self.joueur.max_health
        #self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.sounds_manager.play("game_over")

    def update_game_start(self, surface):
        # afficher le score sur l'ecran
        score_text = self.font.render(f"score : {self.score}", 1, (0,0,0))
        surface.blit(score_text, (20,20))
        # afficher le joueur à l'ecran
        surface.blit(self.joueur.image, self.joueur.rect) # faire attention c'est game et non Game c'est pour ca dans mes autres projets j'avais des erreurs. c'etait du a ca 

        # actualiser la barre de vie du joueur
        self.joueur.health_bar(surface)

        # actualiser la barre de comet
        self.comet_event.update_bar(surface)

        # actualiser l'animation du joueur
        self.joueur.update_animation()

        # recuperer les projectiles
        for projectiles in self.joueur.all_projectiles:
            projectiles.move_projectile()

        # recuperer les monstre
        for monstre in self.all_monstres:
            monstre.move_monstre()
            monstre.health_bar(surface)
            monstre.update_animation()

        # recuperer les cometes
        for comet in self.comet_event.all_comets:
            comet.chute()

        #afficher nos projectiles a l'ecran, comme le backgroung et le joueur
        self.joueur.all_projectiles.draw(surface)

        #afficher nos monstre a l'ecran
        self.all_monstres.draw(surface)

        # appliquer les image de mon groupe de commetes
        self.comet_event.all_comets.draw(surface)
        
        # il faut ajouter la taille du joueur a la taille de la surface sinon le joueur poura sortir de l'ecran un petit peu 
        if self.touche_appuyer.get(pygame.K_RIGHT) and self.joueur.rect.x + self.joueur.rect.width < surface.get_width(): # si on met 1080 qui est la taille de l'ecrsn ici, on peut avoir un soucis si la taille change du coup mieux vaux utilisé screen.get_width
            self.joueur.move_right()
        elif self.touche_appuyer.get(pygame.K_LEFT) and self.joueur.rect.x > 0:
            self.joueur.move_left()
    
    def verifier_collision(self, sprite, group):
        """pour verifier les collisions on met en paramettre un objet et groupe de sprite et tout est gerer par pygame.
        spritecollide(objet1, objet2, do kill ? (false ou true), type de collision) """
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def apparition_monstre(self, monstre_class_name):
        self.all_monstres.add(monstre_class_name.__call__(self)) # on appelle la class et on fais l'instance grace a call c'est comme si on faisais Alien() ou Monstre()

    