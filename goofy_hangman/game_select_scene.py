import goofy_hangman.game_manager as manager
import goofy_hangman.main as ghm
from hangman_scene import HangmanScene
from scene import Scene


class GameSelectScene(Scene):
    def __init__(self, game: manager.GameManager):
        self.game = game

    def render(self):
        ghm.game_display.fill(ghm.WHITE)
        manager.text("Choose your difficulty", (ghm.DISPLAY_WIDTH / 2), (150), 50, ghm.RED)
        ghm.game_display.blit(ghm.EASY_DIFFICULTY_IMAGE, (ghm.DISPLAY_WIDTH * 0.1, 250))
        ghm.game_display.blit(ghm.MEDIUM_DIFFICULTY_IMAGE, (ghm.DISPLAY_WIDTH * 0.38, 250))
        ghm.game_display.blit(ghm.HARD_DIFFICULTY_IMAGE, (ghm.DISPLAY_WIDTH * 0.7 - 10, 250))
        manager.button("EAZY", ghm.DISPLAY_WIDTH * 0.1 - 20, 450, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, lambda: self.__navigate_to_hangman("eazy"))
        manager.button("MEDIUM", ghm.DISPLAY_WIDTH * 0.38, 450, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, lambda: self.__navigate_to_hangman("medium"))
        manager.button("EXPERTS ONLY", ghm.DISPLAY_WIDTH * 0.7 - 20, 450, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, lambda: self.__navigate_to_hangman("hard"))

    def __navigate_to_hangman(self, difficulty):
        self.game.set_scene(HangmanScene(difficulty))
