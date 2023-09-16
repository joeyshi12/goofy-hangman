import os
import pygame as pg

pg.mixer.init()
pg.init()

DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 600
game_display: pg.Surface = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("Supreme Hangman")
clock: pg.time.Clock = pg.time.Clock()

BUTTON_SOUND = pg.mixer.Sound(os.path.join("assets", "sounds", "button.wav"))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
DARK_RED = (150, 0, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)

from supreme_hangman.game_manager import GameManager
game_manager = GameManager()
