import pygame


class GameObject(pygame.sprite.Sprite):

    def __init__(self, image, x, y):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update(self):
        """
        Será sobrescrito pelas classes filhas.
        """
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)