import pygame


class Menu:

    def __init__(self):

        self.title_font = pygame.font.Font(
            "assets/fonts/Orbitron-VariableFont_wght.ttf",
            72
        )

        self.subtitle_font = pygame.font.Font(
            "assets/fonts/Orbitron-VariableFont_wght.ttf",
            24
        )

        self.enter_font = pygame.font.Font(
            "assets/fonts/Orbitron-VariableFont_wght.ttf",
            30
        )

        self.info_font = pygame.font.Font(
            "assets/fonts/Orbitron-VariableFont_wght.ttf",
            18
        )

    def draw(self, screen):

        width = screen.get_width()

        # ------------------------
        # TÍTULO
        # ------------------------

        shadow = self.title_font.render(
            "SPACE ESCAPE",
            True,
            (20, 40, 80)
        )

        title = self.title_font.render(
            "SPACE ESCAPE",
            True,
            (0, 220, 255)
        )

        screen.blit(
            shadow,
            shadow.get_rect(center=(width // 2 + 3, 103))
        )

        screen.blit(
            title,
            title.get_rect(center=(width // 2, 100))
        )

        # ------------------------
        # SUBTÍTULO
        # ------------------------

        subtitle = self.subtitle_font.render(
            "Sobreviva por 30 segundos",
            True,
            (220, 220, 220)
        )

        screen.blit(
            subtitle,
            subtitle.get_rect(center=(width // 2, 185))
        )

        objective = self.info_font.render(
            "Desvie dos meteoros e destrua-os para ganhar mais pontuação.",
            True,
            (180, 180, 180)
        )

        screen.blit(
            objective,
            objective.get_rect(center=(width // 2, 225))
        )

        # ------------------------
        # CONTROLES
        # ------------------------

        controls = self.info_font.render(
            "CONTROLES",
            True,
            (0, 220, 255)
        )

        screen.blit(
            controls,
            controls.get_rect(center=(width // 2, 305))
        )

        move = self.info_font.render(
            "Mover: A / D ou <- ->",
            True,
            (220, 220, 220)
        )

        screen.blit(
            move,
            move.get_rect(center=(width // 2, 340))
        )

        shoot = self.info_font.render(
            "Atirar: ESPACO",
            True,
            (220, 220, 220)
        )

        screen.blit(
            shoot,
            shoot.get_rect(center=(width // 2, 370))
        )

        # ------------------------
        # ENTER PISCANDO
        # ------------------------

        blink = (pygame.time.get_ticks() // 500) % 2 == 0

        if blink:

            enter = self.enter_font.render(
                "PRESSIONE ENTER",
                True,
                (255, 255, 255)
            )

            screen.blit(
                enter,
                enter.get_rect(center=(width // 2, 470))
            )

        # ------------------------
        # RODAPÉ
        # ------------------------

        version = self.info_font.render(
            "Versão 1.0",
            True,
            (120, 120, 120)
        )

        screen.blit(
            version,
            (20, 660)
        )

        author = self.info_font.render(
            "Developed by Moisés Felipe",
            True,
            (120, 120, 120)
        )

        screen.blit(
            author,
            author.get_rect(bottomright=(980, 680))
        )