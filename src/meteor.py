import random

from settings import HEIGHT, WIDTH
from src.game_object import GameObject


class Meteor(GameObject):

    def __init__(self, image, speed, health, points):

        x = random.randint(0, WIDTH - image.get_width())
        y = -image.get_height()

        super().__init__(image, x, y)

        self.speed = speed
        self.health = health
        self.points = points
        self.counted = False

    def update(self):

        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            return True

        return False

    def take_damage(self):

        self.health -= 1

        return self.health <= 0