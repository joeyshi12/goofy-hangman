import goofy_hangman.game_manager as manager
import goofy_hangman.main as ghm
from menu_scene import MenuScene
from scene import Scene


class OptionsScene(Scene):
    def __init__(self, game: manager.GameManager):
        self.game = game

    def render(self):
        ghm.game_display.fill(ghm.WHITE)
        ghm.game_display.blit(ghm.BURNING_KNUCKLES_IMAGE, (0, 0))
        manager.text("THIS IS NOT DA WEI", int(ghm.DISPLAY_WIDTH / 2), int(ghm.DISPLAY_HEIGHT / 2), 50, ghm.GREEN)
        manager.button("ABORT", ghm.DISPLAY_WIDTH * 0.43, 450, 120, 50, ghm.GREEN, ghm.BRIGHT_GREEN, self.__navigate_to_menu)

    def __navigate_to_menu(self):
        self.game.set_scene(MenuScene(self.game))
