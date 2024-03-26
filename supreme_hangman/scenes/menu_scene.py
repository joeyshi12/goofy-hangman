import os
import random
import pygame as pg

import supreme_hangman as shm
import supreme_hangman.user_interface as ui
import supreme_hangman.scenes as scenes


class MenuScene(scenes.Scene):
    def __init__(self, game):
        self.game = game
        self.logo_image = pg.image.load(os.path.join("assets", "images", "supreme_logo.png"))
        self.hanging_knuckles_image = pg.image.load(os.path.join("assets", "images", "sad.png"))
        self.display_messages = []
        self.buttons = [
            ui.Button("Play", 100, 250, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_select_difficulty),
            ui.Button("Multiplayer", 100, 320, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__add_single_player_message),
            ui.Button("Options", 100, 390, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_options),
            ui.Button("Exit", 100, 460, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, scenes.quit_game)
        ]
        if not pg.mixer.music.get_busy():
            pg.mixer.music.load(os.path.join("assets", "sounds", "opening.wav"))
            pg.mixer.music.play(-1)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        shm.game_display.fill(shm.WHITE)
        shm.game_display.blit(self.logo_image, (30, -30))
        shm.game_display.blit(self.hanging_knuckles_image, (450, 250))
        pg.draw.line(shm.game_display, shm.BRIGHT_RED, (586, 150), (586, 250), 8)
        for display_text in self.display_messages:
            display_text.render()
        for button in self.buttons:
            button.render()

    def __navigate_to_select_difficulty(self):
        self.game.set_scene(scenes.DifficultySelectScene(self.game))

    def __navigate_to_multiplayer(self):
        self.game.set_scene(scenes.MultiplayerScene(self.game))

    def __navigate_to_options(self):
        self.game.set_scene(scenes.OptionsScene(self.game))

    def __add_single_player_message(self):
        self.display_messages.append(
            ui.DisplayText(
                "This is a single player game",
                random.random() * shm.DISPLAY_WIDTH,
                random.random() * shm.DISPLAY_HEIGHT,
                20,
                shm.RED
            )
        )
