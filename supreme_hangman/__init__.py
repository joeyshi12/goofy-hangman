import os
from moviepy.editor import VideoFileClip
import pygame as pg
from supreme_hangman.game_manager import GameManager

pg.mixer.init()
pg.init()

DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 600
game_display: pg.Surface = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption("Supreme Hangman")
clock: pg.time.Clock = pg.time.Clock()

LOGO_IMAGE = pg.image.load(os.path.join("assets", "images", "supreme_logo.png"))
EASY_DIFFICULTY_IMAGE = pg.image.load(os.path.join("assets", "images", "i_sleep.png"))
MEDIUM_DIFFICULTY_IMAGE = pg.image.load(os.path.join("assets", "images", "real.png"))
HARD_DIFFICULTY_IMAGE = pg.image.load(os.path.join("assets", "images", "power_of_god_and_anime.png"))
BURNING_KNUCKLES_IMAGE = pg.image.load(os.path.join("assets", "images", "knuckles.png"))
HANGING_KNUCKLES_IMAGE = pg.image.load(os.path.join("assets", "images", "sad.png"))
WIN_IMAGE = pg.image.load(os.path.join("assets", "images", "winning.png"))
LOSE_IMAGE = pg.image.load(os.path.join("assets", "images", "lost_image.png"))

BUTTON_SOUND = pg.mixer.Sound(os.path.join("assets", "sounds", "button.wav"))

MEME_VIDEO = VideoFileClip(os.path.join("assets", "videos", "movie.mp4"))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
DARK_RED = (150, 0, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)

game_manager = GameManager()
