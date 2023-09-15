import supreme_hangman as shm
import supreme_hangman.user_interface as ui
import supreme_hangman.scenes as scenes


class DifficultySelectScene(scenes.Scene):
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
        self.game.set_scene(scenes.HangmanScene(self.game, difficulty))
