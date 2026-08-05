import pygame

from settings import HEIGHT
from src.game_object import GameObject


class Bullet(GameObject):

    def __init__(self, image, x, y):

        super().__init__(image, x, y)

        self.speed = 12

    def update(self):

        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()