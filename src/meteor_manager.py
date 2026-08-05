import pygame
import random

from src.asset_manager import AssetManager
from src.meteor import Meteor
from settings import (
    INITIAL_METEOR_SPEED,
    MAX_METEOR_SPEED,
    INITIAL_SPAWN_DELAY,
    MIN_SPAWN_DELAY,
    SPEED_INCREASE,
    SPAWN_ACCELERATION
)


class MeteorManager:

    def __init__(
            self,
            all_sprites,
            meteors
    ):

        self.spawn_delay = INITIAL_SPAWN_DELAY
        self.meteor_speed = INITIAL_METEOR_SPEED

        self.all_sprites = all_sprites
        self.meteors = meteors

        self.last_spawn = pygame.time.get_ticks()

    def update(self):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_spawn >= self.spawn_delay:

            # Escolhe aleatoriamente o tipo do meteoro
            chance = random.randint(1, 100)

            if chance <= 50:
                # Pequeno
                scale = 0.7
                health = 1
                points = 25
                speed = self.meteor_speed * 1.2

            elif chance <= 85:
                # Médio
                scale = 1.0
                health = 2
                points = 50
                speed = self.meteor_speed

            else:
                # Grande
                scale = 1.3
                health = 3
                points = 75
                speed = self.meteor_speed * 0.8

            meteor_image = pygame.transform.rotozoom(
                AssetManager.meteor,
                0,
                scale
            )

            meteor = Meteor(
                meteor_image,
                speed,
                health,
                points
            )

            self.all_sprites.add(meteor)
            self.meteors.add(meteor)

            self.last_spawn = current_time

    def update_difficulty(self, elapsed_time):

        self.meteor_speed = min(
            INITIAL_METEOR_SPEED + elapsed_time * SPEED_INCREASE,
            MAX_METEOR_SPEED
        )

        self.spawn_delay = max(
            INITIAL_SPAWN_DELAY - elapsed_time * SPAWN_ACCELERATION,
            MIN_SPAWN_DELAY
        )