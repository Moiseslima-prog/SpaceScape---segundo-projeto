import pygame


class CollisionManager:

    @staticmethod
    def player_hit(player, meteors):

        return pygame.sprite.spritecollideany(
            player,
            meteors
        )
