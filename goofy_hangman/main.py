import os
import pygame as pg
import goofy_hangman.game as game
from moviepy.editor import VideoFileClip

pg.mixer.init()
pg.init()

game_display: pg.Surface = pg.display.set_mode((800, 600))
pg.display.set_caption('Ultimate Hangman')
clock = pg.time.Clock()

FREE_SANS_BOLD = pg.font.Font("freesansbold.ttf", 50)

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

game.start()
