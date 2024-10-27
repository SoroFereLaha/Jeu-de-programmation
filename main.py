#coding:utf-8

import pygame
import random
from object import Fruit, Python, Python_noir, Java, Java_noir

pygame.init()

clock = pygame.time.Clock()
FPS = 60

surface = pygame.display.set_mode((900,550))
pygame.display.set_caption("CATCH ME BATTLE")
background_image = pygame.image.load("image/a.jpg")
background_image = pygame.transform.scale(background_image, (1000, 600))

fruit = Fruit()
fruits = pygame.sprite.Group()
fruits.add(fruit)
fruits.add(fruit)
fruits.add(fruit)
player = fruit.player
score = fruit.score
game = fruit.game

python = Python()
pythons = pygame.sprite.Group()
pythons.add(python)
pythons.add(python)
pythons.add(python)

python_noir = Python_noir()
pythons_noir = pygame.sprite.Group()
pythons_noir.add(python_noir)
pythons_noir.add(python_noir)
pythons_noir.add(python_noir)

java = Java()

javas = pygame.sprite.Group()
javas.add(java)
javas.add(java)
javas.add(java)

java_noir = Java_noir()

javas_noir = pygame.sprite.Group()
javas_noir.add(java_noir)
javas_noir.add(java_noir)
javas_noir.add(java_noir)

def play_click():
    click = pygame.mixer.Sound("sons/click.ogg")
    click.play()

def play_start():
    start = pygame.mixer.Sound("sons/start_music.ogg")
    start.play()

def play_win():
    win = pygame.mixer.Sound("sons/win.ogg")
    win.play()

def play_lose():
    lose = pygame.mixer.Sound("sons/lose2.ogg")
    lose.play()


run = True
while run:

    # bordel, ne pas oublier de mettre l'affichage du backrground et de l'image du joueur dans la boucle infinie sinon le deplacement ne va pas fonctionner
    surface.blit(background_image, (-50,-50))

    if score.lose_points >= score.max_lose_points:
        game.is_playing = False

    if game.is_playing:
        surface.blit(fruit.image, fruit.rect)
        surface.blit(python.image, python.rect)
        surface.blit(python_noir.image, python_noir.rect)
        surface.blit(java.image, java.rect)
        surface.blit(java_noir.image, java_noir.rect)

        # bordel, ne pas oublier de mettre l'affichage du backrground et de l'image du joueur dans la boucle infinie sinon le deplacement ne va pas fonctionner
        surface.blit(player.image, player.rect)

        fruit.move_fruit()
        
        python_noir.move_fruit()


        for fruit in fruits:
            fruit.move_fruit()

            if pygame.sprite.spritecollide(player, fruits, False, pygame.sprite.collide_mask):
                #print("colision")
                try:
                    fruit.rect.x = random.randint(10, 990)
                    fruit.rect.y = - random.randint(50, 100)
                    score.update_score(0, surface)
                    play_win()
                except Exception as e:
                    print(e)

            if fruit.rect.y >= 500:
                fruit.rect.x = random.randint(10, 990)
                fruit.rect.y = - random.randint(50, 100)

        for python in pythons:
            python.move_fruit()

            if pygame.sprite.spritecollide(player, pythons, False, pygame.sprite.collide_mask):
                python.rect.x = random.randint(10, 990)
                python.rect.y = - random.randint(50, 100)
                score.update_score(50, surface)
                play_win()

        for python_noir in pythons_noir:
            python_noir.move_fruit()

            if pygame.sprite.spritecollide(player, pythons_noir, False, pygame.sprite.collide_mask):
                python_noir.rect.x = random.randint(10, 990)
                python_noir.rect.y = - random.randint(50, 100)
                score.update_score(-50, surface)
                score.lose_points += 10
                play_lose()

        for java in javas:
            java.move_fruit()

            if pygame.sprite.spritecollide(player, javas, False, pygame.sprite.collide_mask):
                java.rect.x = random.randint(10, 990)
                java.rect.y = - random.randint(50, 100)
                score.update_score(5, surface)
                score.lose_points += -1
                play_win()  

        for java_noir in javas_noir:
            java_noir.move_fruit()

            if pygame.sprite.spritecollide(player, javas_noir, False, pygame.sprite.collide_mask):
                java_noir.rect.x = random.randint(10, 990)
                java_noir.rect.y = - random.randint(50, 100)
                score.update_score(-150, surface)
                score.lose_points += 20
                play_lose()

        if score.score >= 1000:
            # agrandit le seau 
            player.image = pygame.transform.scale(player.image, (200,200))

        score.game_over(surface)
        score.update_score(0, surface)
        #print(score.score)

        
        if player.touch.get(pygame.K_RIGHT) and player.rect.x < surface.get_width()-200:
            player.move_right_player()
        elif player.touch.get(pygame.K_LEFT) and player.rect.x > 0:
            player.move_left_player()
        
    else:
        surface.blit(game.image, game.image_rect)
        surface.blit(game.logo, game.rect)

    # raffraichessement (pour sauvergarder les nouveautés)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            player.touch[event.key] = True
        elif event.type == pygame.KEYUP:
            player.touch[event.key] = False 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.rect.collidepoint(event.pos):
                game.is_playing = True
                play_click()
                play_start()
                print(game.is_playing)
            
            print(game.is_playing)
        print(game.is_playing)

clock.tick(FPS)    
