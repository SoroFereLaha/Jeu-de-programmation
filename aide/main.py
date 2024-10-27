#coding:utf-8

import pygame
import math
from player import Game
pygame.init()

# definir une clock fps

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption("comet fall game")
surface = pygame.display.set_mode((1080,520))

image_de_fond = pygame.image.load("Assets/bg.jpg")

# charger notre jeu (ce qui implique charger notre joueur)
game = Game()

# importer notre banniere de debut de jeu
banniere = pygame.image.load("assets/banner.png")
banniere = pygame.transform.scale(banniere, (500, 500))
banniere_rect = banniere.get_rect()
banniere_rect.x = math.ceil(surface.get_width()/4) # pour arrondir la division

# charger notre bouton
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(surface.get_width()/3.33)
play_button_rect.y = math.ceil(surface.get_height()/1.40)
run = True
while run:

    surface.blit(image_de_fond,(0,-400)) # le tuple c'est la position mais on peut l'utiliser pour jouer sur le zoom de l'image si ellle trop grande, on peut mettre des valeurs negatives

    # verifier notre jeu a commencer
    if game.is_playing:
        # declenche les instruction de ña partie
        game.update_game_start(surface)
    # si je le jeu n'a pas commncer on ajoute notre banniere de bienvenue
    else:
        surface.blit(play_button,play_button_rect)
        surface.blit(banniere, banniere_rect)
        

    pygame.display.flip()
    #-------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # deplacement joueur
        elif event.type == pygame.KEYDOWN : # KEYDOWN lorsqu'on appuie sur une touche
            # faire comme ca permet de rendre le deplacement fluide, sinon on peut faire ca avec if event.KEY == pygame.K_RIGHT: move_right()
            game.touche_appuyer[event.key] = True

            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.joueur.lancer_projectile()
                else:
                    # mettre le jeu en mode lancer
                    game.start() 
                    # jouer le son
                    game.sounds_manager.play("click")
        elif event.type == pygame.KEYUP: # KEYUP lorsqu'on relache une touche
            game.touche_appuyer[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN: # evenement pour clique sur image
            # verifier si la souris se trouve sur notre button grace a collidepoint
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start() 
                # jouer le son
                game.sounds_manager.play("click")


    # fixer le nombre de fps pour la vitesse du jeu en fonction de l'ordinateur
    clock.tick(FPS)
                