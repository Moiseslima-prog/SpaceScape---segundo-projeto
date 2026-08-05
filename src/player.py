import pygame

from settings import PLAYER_SPEED, WIDTH
from src.game_object import GameObject


class Player(GameObject):

    def __init__(self, image, x, y):

        super().__init__(image, x, y)

        self.speed = PLAYER_SPEED

    def update(self):

        keys = pygame.key.get_pressed()

        # Movimento para a esquerda
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        # Movimento para a direita
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Impede a nave de sair da tela
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):

        return self.rect.centerx, self.rect.top