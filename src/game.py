import pygame

from settings import WIDTH, HEIGHT, TITLE, FPS, GAME_TIME
from src.bullet import Bullet
from src.player import Player
from src.game_state import GameState
from src.asset_manager import AssetManager
from src.meteor_manager import MeteorManager
from src.collision_manager import CollisionManager
from src.hud import HUD
from src.menu import Menu
from src.explosion import Explosion


class Game:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        AssetManager.load_assets()

        self.clock = pygame.time.Clock()

        self.running = True

        self.state = GameState.MENU

        self.score = 0

        self.start_time = pygame.time.get_ticks()

        self.hud = HUD()
        self.menu = Menu()

        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.player = None

        self.meteor_manager = MeteorManager(
            self.all_sprites,
            self.meteors
        )

        pygame.mixer.music.load(
            AssetManager.menu_music
        )

        pygame.mixer.music.set_volume(0.35)

        pygame.mixer.music.play(-1)

    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    if self.state in (
                            GameState.GAME_OVER,
                            GameState.VICTORY
                    ):
                        self.back_to_menu()

                if event.key == pygame.K_RETURN:

                    if self.state == GameState.MENU:
                        self.reset()

                    elif self.state in (
                            GameState.GAME_OVER,
                            GameState.VICTORY
                    ):
                        self.reset()

                if (
                        event.key == pygame.K_SPACE
                        and self.state == GameState.PLAYING
                ):
                    AssetManager.laser_sound.play()

                    x, y = self.player.shoot()

                    bullet = Bullet(
                        AssetManager.bullet,
                        x - AssetManager.bullet.get_width() // 2,
                        y
                    )

                    self.bullets.add(bullet)
                    self.all_sprites.add(bullet)

    def update(self):

        if self.state == GameState.MENU:
            return

        if self.state == GameState.PLAYING:

            # Atualiza todos os sprites
            self.all_sprites.update()

            # Tempo de jogo
            elapsed = (
                              pygame.time.get_ticks() - self.start_time
                      ) / 1000

            # Atualiza dificuldade
            self.meteor_manager.update_difficulty(elapsed)

            # Spawn de meteoros
            self.meteor_manager.update()

            # Pontuação por desviar dos meteoros
            for meteor in self.meteors:

                if meteor.rect.top > HEIGHT and not meteor.counted:
                    meteor.counted = True
                    self.score += 10

            # ==========================
            # COLISÃO TIRO x METEORO
            # ==========================

            hits = pygame.sprite.groupcollide(
                self.bullets,
                self.meteors,
                True,  # remove o tiro
                False  # não remove o meteoro
            )

            for bullet, meteors in hits.items():

                for meteor in meteors:

                    if meteor.take_damage():
                        meteor.kill()

                        AssetManager.explosion_meteor_sound.play()

                        self.score += meteor.points

                        explosion = Explosion(
                            AssetManager.explosion,
                            meteor.rect.center
                        )

                        self.explosions.add(explosion)
                        self.all_sprites.add(explosion)

            # ==========================
            # COLISÃO NAVE x METEORO
            # ==========================

            if (
                    self.player is not None
                    and CollisionManager.player_hit(
                self.player,
                self.meteors
            )
            ):
                pygame.mixer.music.stop()
                AssetManager.explosion_sound.play()

                explosion = Explosion(
                    AssetManager.explosion,
                    self.player.rect.center
                )

                self.explosions.add(explosion)
                self.all_sprites.add(explosion)

                self.player.kill()
                self.player = None

                self.explosion_start = pygame.time.get_ticks()

                self.state = GameState.EXPLODING

            # Verifica vitória
            self.check_win()

        elif self.state == GameState.EXPLODING:

            self.explosions.update()

            if (
                    pygame.time.get_ticks()
                    - self.explosion_start
                    >= 700
            ):
                self.state = GameState.GAME_OVER

                pygame.mixer.music.load(
                    AssetManager.game_over_music
                )

                pygame.mixer.music.play()

    def draw(self):

        self.screen.blit(
            AssetManager.background,
            (0, 0)
        )

        if self.state == GameState.MENU:

            self.menu.draw(self.screen)

        else:

            self.all_sprites.draw(self.screen)

            self.hud.draw(
                self.screen,
                self.state,
                self.start_time,
                self.score
            )

        pygame.display.flip()

    def check_win(self):

        if self.state != GameState.PLAYING:
            return

        elapsed = (
                          pygame.time.get_ticks() - self.start_time
                  ) / 1000

        if elapsed >= GAME_TIME:
            pygame.mixer.music.stop()

            pygame.mixer.music.load(
                AssetManager.victory_music
            )

            pygame.mixer.music.play()

            self.state = GameState.VICTORY

    def reset(self):

        pygame.mixer.music.stop()

        pygame.mixer.music.load(
            AssetManager.gameplay_music
        )

        pygame.mixer.music.play(-1)

        self.all_sprites.empty()
        self.meteors.empty()
        self.explosions.empty()

        self.player = Player(
            AssetManager.player,
            WIDTH // 2 - AssetManager.player.get_width() // 2,
            HEIGHT - AssetManager.player.get_height() - 20
        )

        self.all_sprites.add(self.player)

        self.meteor_manager = MeteorManager(
            self.all_sprites,
            self.meteors
        )

        self.start_time = pygame.time.get_ticks()

        self.score = 0

        self.state = GameState.PLAYING

    def back_to_menu(self):

        self.all_sprites.empty()
        self.meteors.empty()
        self.explosions.empty()

        self.player = None

        self.score = 0

        self.state = GameState.MENU

        pygame.mixer.music.stop()

        pygame.mixer.music.load(
            AssetManager.menu_music
        )

        pygame.mixer.music.play(-1)

    def run(self):

        while self.running:

            self.clock.tick(FPS)

            self.events()

            self.update()

            self.draw()

        pygame.mixer.music.stop()
        pygame.quit()