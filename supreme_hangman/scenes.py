import os
import sys
import random
from typing import List
import pygame as pg
import supreme_hangman as shm
import supreme_hangman.user_interface as ui


class Scene:
    def handle_event(self, event):
        pass

    def render(self):
        raise NotImplementedError


def quit_game():
    pg.quit()
    sys.exit()


class MenuScene(Scene):
    def __init__(self, game):
        self.game = game
        self.buttons = [
            ui.Button("Play", 100, 250, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_select_difficulty),
            ui.Button("Options", 100, 350, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_options),
            ui.Button("Exit", 100, 450, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, quit_game)
        ]
        pg.mixer.music.load(os.path.join("assets", "sounds", "opening.wav"))
        pg.mixer.music.play(-1)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        shm.game_display.fill(shm.WHITE)
        shm.game_display.blit(shm.LOGO_IMAGE, (30, -30))
        shm.game_display.blit(shm.HANGING_KNUCKLES_IMAGE, (450, 250))
        pg.draw.line(shm.game_display, shm.BRIGHT_RED, (586, 150), (586, 250), 8)
        for button in self.buttons:
            button.render()

    def __navigate_to_select_difficulty(self):
        self.game.set_scene(DifficultySelectScene(self.game))

    def __navigate_to_options(self):
        self.game.set_scene(OptionsScene(self.game))


class OptionsScene(Scene):
    def __init__(self, game):
        self.game = game
        self.buttons = [
            ui.Button("ABORT", shm.DISPLAY_WIDTH * 0.43, 450, 120, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_menu)
        ]

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        shm.game_display.fill(shm.WHITE)
        shm.game_display.blit(shm.BURNING_KNUCKLES_IMAGE, (0, 0))
        ui.draw_text("THIS IS NOT DA WEI", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 2), 50, shm.GREEN)
        for button in self.buttons:
            button.render()

    def __navigate_to_menu(self):
        self.game.set_scene(MenuScene(self.game))


class DifficultySelectScene(Scene):
    def __init__(self, game):
        self.game = game
        self.buttons = [
            ui.Button("EAZY", shm.DISPLAY_WIDTH * 0.1 - 20, 450, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, lambda: self.__navigate_to_hangman("eazy")),
            ui.Button("MEDIUM", shm.DISPLAY_WIDTH * 0.38, 450, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, lambda: self.__navigate_to_hangman("medium")),
            ui.Button("EXPERTS ONLY", shm.DISPLAY_WIDTH * 0.7 - 20, 450, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, lambda: self.__navigate_to_hangman("hard"))
        ]

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        shm.game_display.fill(shm.WHITE)
        ui.draw_text("Choose your difficulty", (shm.DISPLAY_WIDTH / 2), (150), 50, shm.RED)
        shm.game_display.blit(shm.EASY_DIFFICULTY_IMAGE, (shm.DISPLAY_WIDTH * 0.1, 250))
        shm.game_display.blit(shm.MEDIUM_DIFFICULTY_IMAGE, (shm.DISPLAY_WIDTH * 0.38, 250))
        shm.game_display.blit(shm.HARD_DIFFICULTY_IMAGE, (shm.DISPLAY_WIDTH * 0.7 - 10, 250))
        for button in self.buttons:
            button.render()

    def __navigate_to_hangman(self, difficulty):
        self.game.set_scene(HangmanScene(self.game, difficulty))


class HangmanScene(Scene):
    # TODO: include more words
    EASY_WORDS: List[str] = ["string", "planet", "random", "vector", "genius", "python", "volume", "poetry"]
    MEDIUM_WORDS: List[str] = ["trampoline", "aftershock", "bankruptcy", "monarchist"]
    HARD_WORDS: List[str] = ["misconjugatedly", "dermatoglyphics"]
    LIVES: int = 7
    MAX_INPUT_LENGTH = 21

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

        self.text_input = ""
        self.guessed_letters = set()
        self.hangman_text = " ".join(["_"] * len(self.word))
        self.failed_attempts = 0
        self.time = 0
        self.buttons = [
            ui.Button("Enter", 130, 300, 100, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__submit_guess)
        ]
        pg.mixer.music.load(os.path.join("assets", "sounds", "wii.mp3"))
        pg.mixer.music.play(-1)

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.__submit_guess()
            elif event.key == pg.K_BACKSPACE:
                if len(self.text_input) > 0:
                    self.text_input = self.text_input[:-1]
            elif len(self.text_input) <= HangmanScene.MAX_INPUT_LENGTH:
                user_input = event.dict.get("unicode")
                self.text_input += user_input
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        shm.game_display.fill(shm.WHITE)
        self.time += 1/60
        ui.draw_box(50, 310, 230, 270, 5)
        ui.draw_box(shm.DISPLAY_WIDTH * 0.5, shm.DISPLAY_WIDTH - 25, 25, shm.DISPLAY_HEIGHT - 250, 5)
        ui.draw_text("Guess the Word!", 180, 100, 30, shm.RED)
        ui.draw_text(self.text_input, 180, 250, 20, shm.RED)
        ui.draw_text(self.hangman_text, shm.DISPLAY_WIDTH * 0.5, shm.DISPLAY_HEIGHT - 100, 50, shm.RED)
        ui.draw_text("Time:", 538, 375, 20, shm.RED)
        ui.draw_text(str(int(self.time)), 625, 375, 20, shm.RED)
        ui.draw_text("Fails:", 540, 400, 20, shm.RED)
        ui.draw_text(str(self.failed_attempts) + "/" + str(HangmanScene.LIVES), 640, 400, 20, shm.RED)
        ui.draw_stand(480, 305)
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
        if len(self.text_input) == 1 and self.text_input in self.word:
            self.guessed_letters.add(self.text_input)
            self.hangman_text = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

        if self.text_input == self.word or set(self.word) == self.guessed_letters:
            self.game.set_scene(WinnerScene(self.game, self.time, self.failed_attempts))
        elif self.text_input == "omae wa mou shindeiru":
            shm.MEME_VIDEO.preview()
            self.game.set_scene(WinnerScene(self.game, self.time, -9999999999))
        elif self.text_input not in self.guessed_letters:
            self.failed_attempts += 1

        self.text_input = ""
        if self.failed_attempts >= HangmanScene.LIVES:
            self.game.set_scene(LoserScene(self.game, self.time, self.failed_attempts))


class WinnerScene(Scene):
    def __init__(self, game, time, score):
        self.game = game
        self.time = time
        self.score = score
        self.buttons = [
            ui.Button("Quit", 150, 450, 120, 50, shm.GREEN, shm.BRIGHT_GREEN, quit_game),
            ui.Button("Menu", 550, 450, 120, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_menu)
        ]

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        shm.game_display.fill(shm.BLUE)
        shm.game_display.blit(shm.WIN_IMAGE, (170, 15))
        ui.draw_text("SUPREME WIN", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 150), 50, shm.GREEN)
        ui.draw_text("Time: " + str(int(self.time)) + " seconds", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 190), 25, shm.GREEN)
        ui.draw_text("Score: " + str(self.score) + " fails", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 220), 25, shm.GREEN)
        for button in self.buttons:
            button.render()

    def __navigate_to_menu(self):
        self.game.set_scene(MenuScene(self.game))


class LoserScene(Scene):
    def __init__(self, game, time, score):
        self.game = game
        self.time = time
        self.score = score
        self.buttons = [
            ui.Button("Quit", 150, 450, 120, 50, shm.GREEN, shm.BRIGHT_GREEN, quit_game),
            ui.Button("Menu", 550, 450, 120, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_menu)
        ]
        pg.mixer.music.load(os.path.join("assets", "sounds", "lose_music.wav"))
        pg.mixer.music.play(-1)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        shm.game_display.fill(shm.WHITE)
        shm.game_display.blit(shm.LOSE_IMAGE, (0, 0))
        ui.draw_text("NO SUPREME FOR YOU", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3), 50, shm.RED)
        ui.draw_text("Time: " + str(int(self.time)) + " seconds", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 70), 25, shm.RED)
        ui.draw_text("Score: " + str(self.score) + " fails", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 100), 25, shm.RED)
        for button in self.buttons:
            button.render()

    def __navigate_to_menu(self):
        self.game.set_scene(MenuScene(self.game))
