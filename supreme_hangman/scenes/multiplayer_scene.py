import os
import socket
import pygame as pg
import supreme_hangman as shm
import supreme_hangman.user_interface as ui
import supreme_hangman.scenes as scenes


class MultiplayerScene(scenes.Scene):
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
        self.game.set_scene(scenes.MenuScene(self.game))

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
