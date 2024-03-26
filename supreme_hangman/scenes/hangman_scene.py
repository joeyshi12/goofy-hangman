import os
import random
from typing import List
import pygame as pg
from moviepy.editor import VideoFileClip

import supreme_hangman as shm
import supreme_hangman.user_interface as ui
import supreme_hangman.scenes as scenes


class HangmanScene(scenes.Scene):
    # TODO: include more words
    EASY_WORDS: List[str] = ["string", "planet", "random", "vector", "genius", "python", "volume", "poetry"]
    MEDIUM_WORDS: List[str] = ["trampoline", "aftershock", "bankruptcy", "monarchist"]
    HARD_WORDS: List[str] = ["misconjugatedly", "dermatoglyphics"]
    LIVES: int = 7

    def __init__(self, game, difficulty):
        self.game = game
        self.difficulty = difficulty
        if difficulty == "eazy":
            self.word = random.choice(HangmanScene.EASY_WORDS)
        elif difficulty == "medium":
            self.word = random.choice(HangmanScene.MEDIUM_WORDS)
        elif difficulty == "hard":
            self.word = random.choice(HangmanScene.HARD_WORDS)
        else:
            raise Exception("Invalid difficulty")

        self.text_input = ui.TextInput(50, 230, 260, 40)
        self.guessed_letters = set()
        self.hangman_text = " ".join(["_"] * len(self.word))
        self.failed_attempts = 0
        self.time = 0
        self.meme_video = VideoFileClip(os.path.join("assets", "videos", "movie.mp4"))
        self.buttons = [
            ui.Button("Enter", 130, 300, 100, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__submit_guess)
        ]
        self.hangman_display_text = ui.DisplayText(self.hangman_text, shm.DISPLAY_WIDTH * 0.5, shm.DISPLAY_HEIGHT - 100, 50, shm.RED)
        self.time_value_display_text = ui.DisplayText(str(int(self.time)), 625, 375, 20, shm.RED)
        self.num_fails_display_text = ui.DisplayText(str(self.failed_attempts) + "/" + str(HangmanScene.LIVES), 640, 400, 20, shm.RED)
        self.display_messages = [
            ui.DisplayText("Guess the Word!", 180, 100, 30, shm.RED),
            self.hangman_display_text,
            ui.DisplayText("Time:", 538, 375, 20, shm.RED),
            self.time_value_display_text,
            ui.DisplayText("Fails:", 540, 400, 20, shm.RED),
            self.num_fails_display_text
        ]

        pg.mixer.music.load(os.path.join("assets", "sounds", "wii.mp3"))
        pg.mixer.music.play(-1)

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.__submit_guess()
            else:
                self.text_input.handle_event(event)

        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        self.time += 1/60
        self.time_value_display_text.update_message(str(int(self.time)))

        shm.game_display.fill(shm.WHITE)
        ui.draw_box(shm.DISPLAY_WIDTH * 0.5, shm.DISPLAY_WIDTH - 25, 25, shm.DISPLAY_HEIGHT - 250, 5)
        ui.draw_stand(480, 305)

        for display_text in self.display_messages:
            display_text.render()

        self.text_input.render()

        if self.failed_attempts >= 1:
            pg.draw.circle(shm.game_display, shm.BLACK, (600, 120), 25, 5)  # Head
            if self.failed_attempts >= 2:
                pg.draw.line(shm.game_display, shm.BLACK, (600, 145), (600, 200), 5)  # Body
                if self.failed_attempts >= 3:
                    pg.draw.line(shm.game_display, shm.BLACK, (600, 160), (575, 180), 5)  # left arm
                    if self.failed_attempts >= 4:
                        pg.draw.line(shm.game_display, shm.BLACK, (600, 160), (625, 180), 5)  # right arm
                        if self.failed_attempts >= 5:
                            pg.draw.line(shm.game_display, shm.BLACK, (600, 200), (580, 235), 5)  # left leg
                            if self.failed_attempts >= 6:
                                pg.draw.line(shm.game_display, shm.BLACK, (600, 200), (620, 235), 5)  # right leg

        for button in self.buttons:
            button.render()

    def __submit_guess(self):
        text_content = self.text_input.content

        if len(text_content) == 1 and text_content in self.word:
            self.guessed_letters.add(text_content)
            self.hangman_text = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
            self.hangman_display_text.update_message(self.hangman_text)

        if text_content == self.word or set(self.word) == self.guessed_letters:
            self.game.set_scene(scenes.WinnerScene(self.game, self.time, self.failed_attempts))
            return
        elif text_content == "omae wa mou shindeiru":
            self.meme_video.preview()
            self.game.set_scene(scenes.WinnerScene(self.game, self.time, -9999999999))
            return
        elif text_content not in self.guessed_letters:
            self.failed_attempts += 1
            self.num_fails_display_text.update_message(f"{self.failed_attempts}/{HangmanScene.LIVES}")

        self.text_input.clear()
        if self.failed_attempts >= HangmanScene.LIVES:
            self.game.set_scene(scenes.LoserScene(self.game, self.time, self.failed_attempts))
