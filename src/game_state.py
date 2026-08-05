from enum import Enum


class GameState(Enum):
    MENU = 1
    PLAYING = 2
    EXPLODING = 3
    GAME_OVER = 4
    VICTORY = 5