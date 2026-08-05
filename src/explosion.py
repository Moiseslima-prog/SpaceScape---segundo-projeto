import pygame


class Explosion(pygame.sprite.Sprite):

    def __init__(self, image, center):

        super().__init__()

        self.image = image

        self.rect = self.image.get_rect(center=center)

        self.start_time = pygame.time.get_ticks()

        self.duration = 700  # milissegundos

    def update(self):

        elapsed = pygame.time.get_ticks() - self.start_time

        # Faz a explosão desaparecer aos poucos
        alpha = max(0, 255 - int((elapsed / self.duration) * 255))
        self.image.set_alpha(alpha)

        if elapsed >= self.duration:
            self.kill()