import pygame

from settings import GAME_TIME
from src.game_state import GameState


class HUD:

    def __init__(self):

        self.font = pygame.font.Font(
            "assets/fonts/PressStart2P-Regular.ttf",
            18
        )

        self.big_font = pygame.font.Font(
            "assets/fonts/PressStart2P-Regular.ttf",
            42
        )

    def draw(self, screen, state, start_time, score):

        if state == GameState.PLAYING:

            elapsed = (pygame.time.get_ticks() - start_time) / 1000

            remaining = max(0, GAME_TIME - int(elapsed))

            text = self.font.render(
                f"Tempo: {remaining}",
                True,
                (255, 255, 255)
            )

            screen.blit(text, (20, 20))

            score_text = self.font.render(
                f"Pontos: {score}",
                True,
                (255, 255, 255)
            )

            screen.blit(score_text, (20, 60))


        elif state == GameState.GAME_OVER:

            text = self.big_font.render(

                "GAME OVER",

                True,

                (255, 50, 50)

            )

            rect = text.get_rect(center=(500, 250))

            screen.blit(text, rect)

            score_text = self.font.render(
                f"Pontuação: {score}",
                True,
                (255, 255, 0)
            )

            score_rect = score_text.get_rect(center=(500, 500))

            screen.blit(score_text, score_rect)

            info = self.font.render(

                "ENTER - Jogar novamente",

                True,

                (255, 255, 255)

            )

            info_rect = info.get_rect(center=(500, 360))

            screen.blit(info, info_rect)

            menu = self.font.render(
                "ESC - Voltar ao menu inicial",
                True,
                (255, 255, 255)
            )

            menu_rect = menu.get_rect(center=(500, 420))

            screen.blit(menu, menu_rect)


        elif state == GameState.VICTORY:

            text = self.big_font.render(

                "VOCÊ VENCEU",

                True,

                (50, 255, 50)

            )

            rect = text.get_rect(center=(500, 250))

            screen.blit(text, rect)

            score_text = self.font.render(
                f"Pontuação: {score}",
                True,
                (255, 255, 0)
            )

            score_rect = score_text.get_rect(center=(500, 500))

            screen.blit(score_text, score_rect)

            info = self.font.render(

                "ENTER - Jogar novamente",

                True,

                (255, 255, 255)

            )

            info_rect = info.get_rect(center=(500, 360))

            screen.blit(info, info_rect)

            menu = self.font.render(
                "ESC - Voltar ao menu inicial",
                True,
                (255, 255, 255)
            )

            menu_rect = menu.get_rect(center=(500, 420))

            screen.blit(menu, menu_rect)