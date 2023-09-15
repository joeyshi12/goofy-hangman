import os
import sys
import random
import socket
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
        self.display_messages = []
        self.buttons = [
            ui.Button("Play", 100, 250, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_select_difficulty),
            #ui.Button("Multiplayer", 100, 320, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_multiplayer),
            ui.Button("Multiplayer", 100, 320, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__add_single_player_message),
            ui.Button("Options", 100, 390, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_options),
            ui.Button("Exit", 100, 460, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, quit_game)
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
        for display_text in self.display_messages:
            display_text.render()
        for button in self.buttons:
            button.render()

    def __navigate_to_select_difficulty(self):
        self.game.set_scene(DifficultySelectScene(self.game))

    def __navigate_to_multiplayer(self):
        self.game.set_scene(MultiplayerScene(self.game))

    def __navigate_to_options(self):
        self.game.set_scene(OptionsScene(self.game))

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


class OptionsScene(Scene):
    def __init__(self, game):
        self.game = game
        self.display_messages = [
            ui.DisplayText("THIS IS NOT DA WEI", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 2), 50, shm.GREEN)
        ]
        self.buttons = [
            ui.Button("ABORT", shm.DISPLAY_WIDTH * 0.43, 450, 120, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_menu)
        ]

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        shm.game_display.fill(shm.WHITE)
        shm.game_display.blit(shm.BURNING_KNUCKLES_IMAGE, (0, 0))
        for display_text in self.display_messages:
            display_text.render()
        for button in self.buttons:
            button.render()

    def __navigate_to_menu(self):
        self.game.set_scene(MenuScene(self.game))


class DifficultySelectScene(Scene):
    def __init__(self, game):
        self.game = game
        self.display_messages = [
            ui.DisplayText("Choose your difficulty", (shm.DISPLAY_WIDTH / 2), (150), 50, shm.RED)
        ]
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
        shm.game_display.blit(shm.EASY_DIFFICULTY_IMAGE, (shm.DISPLAY_WIDTH * 0.1, 250))
        shm.game_display.blit(shm.MEDIUM_DIFFICULTY_IMAGE, (shm.DISPLAY_WIDTH * 0.38, 250))
        shm.game_display.blit(shm.HARD_DIFFICULTY_IMAGE, (shm.DISPLAY_WIDTH * 0.7 - 10, 250))
        for display_text in self.display_messages:
            display_text.render()
        for button in self.buttons:
            button.render()

    def __navigate_to_hangman(self, difficulty):
        self.game.set_scene(HangmanScene(self.game, difficulty))


class MultiplayerScene(Scene):
    # TODO: finish implementation

    def __init__(self, game):
        self.game = game
        self.socket = None
        self.internet_image = pg.image.load(os.path.join("assets", "images", "internet.png"))
        self.text_input = ui.TextInput(270, 380, 260, 40)
        self.host_game_button = ui.Button("Host Game", shm.DISPLAY_WIDTH * 0.38, 450, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__click_host_game)
        self.buttons = [
            ui.Button("Back", shm.DISPLAY_WIDTH * 0.1 - 20, 450, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__navigate_to_menu),
            self.host_game_button,
            ui.Button("Connect to host", shm.DISPLAY_WIDTH * 0.7 - 20, 450, 200, 50, shm.GREEN, shm.BRIGHT_GREEN, lambda: None)
        ]

    def handle_event(self, event):
        self.text_input.handle_event(event)
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        shm.game_display.fill(shm.WHITE)
        shm.game_display.blit(self.internet_image, (shm.DISPLAY_WIDTH * 0.2, 80))
        self.text_input.render()
        for button in self.buttons:
            button.render()

    def __navigate_to_menu(self):
        self.game.set_scene(MenuScene(self.game))

    async def __click_host_game(self):
        if self.socket is None:
            tokens = self.text_input.content.split(":")
            if len(tokens) != 2 or not tokens[1].isdigit():
                return
            host, port = tokens
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                self.host_game_button.display_text.update_message("Awaiting")
                sock.bind((host, int(port)))
                sock.listen()
                conn, addr = sock.accept()
                with conn:
                    print(f"Connected by {addr}")
        else:
            self.host_game_button.display_text.update_message("Host Game")


class HangmanScene(Scene):
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

        self.buttons = [
            ui.Button("Enter", 130, 300, 100, 50, shm.GREEN, shm.BRIGHT_GREEN, self.__submit_guess)
        ]
        self.guess_the_word_display_text = ui.DisplayText("Guess the Word!", 180, 100, 30, shm.RED)
        self.hangman_display_text = ui.DisplayText(self.hangman_text, shm.DISPLAY_WIDTH * 0.5, shm.DISPLAY_HEIGHT - 100, 50, shm.RED)
        self.time_label_display_text = ui.DisplayText("Time:", 538, 375, 20, shm.RED)
        self.time_value_display_text = ui.DisplayText(str(int(self.time)), 625, 375, 20, shm.RED)
        self.fails_label_display_text = ui.DisplayText("Fails:", 540, 400, 20, shm.RED)
        self.num_fails_display_text = ui.DisplayText(str(self.failed_attempts) + "/" + str(HangmanScene.LIVES), 640, 400, 20, shm.RED)

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

        self.guess_the_word_display_text.render()
        self.hangman_display_text.render()
        self.time_label_display_text.render()
        self.time_value_display_text.render()
        self.fails_label_display_text.render()
        self.num_fails_display_text.render()
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
            self.game.set_scene(WinnerScene(self.game, self.time, self.failed_attempts))
        elif text_content == "omae wa mou shindeiru":
            shm.MEME_VIDEO.preview()
            self.game.set_scene(WinnerScene(self.game, self.time, -9999999999))
        elif text_content not in self.guessed_letters:
            self.failed_attempts += 1
            self.fails_label_display_text.update_message(str(self.failed_attempts))

        self.text_input.clear()
        if self.failed_attempts >= HangmanScene.LIVES:
            self.game.set_scene(LoserScene(self.game, self.time, self.failed_attempts))


class WinnerScene(Scene):
    def __init__(self, game, time, score):
        self.game = game
        self.display_messages = [
            ui.DisplayText("SUPREME WIN", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 150), 50, shm.GREEN),
            ui.DisplayText("Time: " + str(int(time)) + " seconds", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 190), 25, shm.GREEN),
            ui.DisplayText("Score: " + str(score) + " fails", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 220), 25, shm.GREEN)
        ]
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
        for display_text in self.display_messages:
            display_text.render()
        for button in self.buttons:
            button.render()

    def __navigate_to_menu(self):
        self.game.set_scene(MenuScene(self.game))


class LoserScene(Scene):
    def __init__(self, game, time, score):
        self.game = game
        self.display_messages = [
            ui.DisplayText("NO SUPREME FOR YOU", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3), 50, shm.RED),
            ui.DisplayText("Time: " + str(int(time)) + " seconds", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 70), 25, shm.RED),
            ui.DisplayText("Score: " + str(score) + " fails", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 100), 25, shm.RED)
        ]
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
        for display_text in self.display_messages:
            display_text.render()
        for button in self.buttons:
            button.render()

    def __navigate_to_menu(self):
        self.game.set_scene(MenuScene(self.game))
