#coding:utf-8
"""ce mecanisme fonctionne pour tout les jeux, l'important ce sont justes les etapes"""
import pygame

class AnimateSprite(pygame.sprite.Sprite):
    """class qui va s'occuper du mecanisme de l'animation"""
    def __init__(self,sprite_name, size=(200, 200)):
        """on aura besoin du nom de l'entite a animer pour savoir si c'est un monstre ou le jouer comme ca plus besoin decree plusieurs class pour chaque entite"""
        super().__init__()
        # limage est une caracteristique obligatoire pour un sprite donc faut toujours le definir s'il s'agit d'un sprite
        self.size = size
        self.image = pygame.image.load("Assets/"+ sprite_name + ".png") # il va aller dans le dossier assets et chercher l'image qui s'appelle le nomdonne.png (mummy.png, player.png) donc ca va fonctionner pour les deux car ils ont la meme extensions. on peut utiliser le f"string
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # va nous permettre de ccommencer l'animation a la premiere image
        self.images = animations.get("sprite_name")
        self.animation = False

    def start_animation(self):
        """permet de demarrer l'animation"""
        self.animation = True


    # methode pour animer les sprites
    def animate(self, loop=False):
        if self.animation:

            # passer a l'image suivante
            self.current_image += 1
            # verifier si on atteint la derniere image
            if self.current_image >= len(self.images):
                # remettre l'animation au depart
                self.current_image = 0
                # verifier sinl'animation n'est pas en mode boucle
                if loop is False:
                    # desactivation de l'animations des qu'elles se termine
                    self.animation = False

            # modifier l'images precedente par la suivantes (l'actuelle)
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

# definir une fonction pour charger les images d'un sprite
def charger_image_animation(sprite_name):
    # charger les 24 images correspondant dans le dossier
    images = []
    # recupperer le chemin du dossier
    path = f"Assets/{sprite_name}/{sprite_name}"

    # faire une boucler pour les parcourir les images
    for im in range(1, 24): # pour ajouter les numeros sur le deuxiexe sprite name vu que c'est numerote dans le dosier
        image_path = path + str(im) + ".png" # convertir le nombre en str pour la concatenation
        im1 = pygame.image.load(image_path)
        # lorsqu'elle sera charger ce sera pour tout le jeu (c'est pour ca que la fonction n'est pas dans la classe sinon les images seront charger a chaque appel de la fonction ce qui sera tres lourd) donc on a juste a l'ajouter a notre listes d'images
        images.append(im1)
        print(im1)
        # renvoyer le contenu de la listes d'images
        return images

# un dictoinnaire qui va contenir tout les imagescharger de chaque entite

animations = {
    'mummy' : charger_image_animation('mummy'),
    'joueur' : charger_image_animation('player'),
    'alien' : charger_image_animation('alien')
}
