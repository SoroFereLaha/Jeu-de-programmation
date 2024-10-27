#coding:utf-8

import pygame

# class qui va gerer le profectile de notre joueur
class Projectile(pygame.sprite.Sprite):
    """"""
    def __init__(self, joueur): # JOUEUR, pour recuperer les donnes su jouer grace au self dans self.all_projectiles.add(Projectile(self))
        super().__init__()
        self.velocity = 1
        self.joueur = joueur
        self.image = pygame.image.load("Assets/projectile.png")
        # redimensionner notre image de projectile
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 120 # pour bien position le projectile sinon il va apparaitre au point zero du joueur (haut gauche)
        self.rect.y = joueur.rect.y + 80
        self.origine_image = self.image # image originel sans rotation
        self.angle = 0 

    def rotation(self):
        """permet de faire tourner le projectile lorsqu'il se deplace"""
        self.angle += 10
        # a chaque fois qu'on transforme une image ou un composant on va utiliser ca
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1) # le dernier c'est le scale
        # la rotation se fait par rapport au point le plus haut du rectangle donc va falloir metttre ca au centre
        self.rect = self.image.get_rect(center=self.rect.center)
        

    def remove(self):
        """pour supprimer les projectiles en dehors de notre ecran. remove est une fonction native du langage et le self designe l'objet qui est sorti. on utlise self.joueur grace aux donnees qu'on a recuperer via Projectiles(self) """
        self.joueur.all_projectiles.remove(self) # self pour supprimer l'objet courant

    def move_projectile(self):
        self.rect.x += self.velocity
        # detruire les projectiles qui ne sont plus dans notre ecran
        self.rotation()

        # verifier collision projectile groupe de monstre
        # au lieu de if on met for monstre in ... pour recuoerer les monstre touche par le projectile et leurs infliger des degats
        for monstre in self.joueur.game.verifier_collision(self, self.joueur.game.all_monstres):
            # suuprimer le projectile
            self.remove()
            # infliger degat
            monstre.damage(self.joueur.attack)

        if self.rect.x > 1080:
            self.remove()
            #print("delete")
            