import os
import pygame as pg

import supreme_hangman as shm
import supreme_hangman.user_interface as ui
import supreme_hangman.scenes as scenes


class LoserScene(scenes.Scene):
    def __init__(self, game, time, score):
        self.game = game
        self.lose_image = pg.image.load(os.path.join("assets", "images", "lost_image.png"))
        self.display_messages = [
            ui.DisplayText("NO SUPREME FOR YOU", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3), 50, shm.RED),
            ui.DisplayText("Time: " + str(int(time)) + " seconds", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 70), 25, shm.RED),
            ui.DisplayText("Score: " + str(score) + " fails", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 100), 25, shm.RED)
        ]
        self.buttons = [
            ui.Button("Quit", 150, 450, 120, 50, shm.GREEN, shm.BRIGHT_GREEN, scenes.quit_game),
            ui.Button("Menu", 550, 450, 120, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_menu)
        ]
        pg.mixer.music.load(os.path.join("assets", "sounds", "lose_music.wav"))
        pg.mixer.music.play(-1)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        shm.game_display.fill(shm.WHITE)
        shm.game_display.blit(self.lose_image, (0, 0))
        for display_text in self.display_messages:
            display_text.render()
        for button in self.buttons:
            button.render()

    def __navigate_to_menu(self):
        self.game.set_scene(scenes.MenuScene(self.game))
