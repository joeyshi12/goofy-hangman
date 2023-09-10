import goofy_hangman.game_manager as game
import goofy_hangman.main as ghm
from scene import Scene


class MenuScene(Scene):
    def __init__(self, game: game.GameManager):
        self.game = game
        ghm.pg.mixer.music.load('assets/sounds/opening.wav')
        ghm.pg.mixer.music.play(-1)

    def render(self):
        ghm.game_display.fill(ghm.WHITE)
        ghm.game_display.blit(ghm.LOGO_IMAGE, (30, -30))
        ghm.game_display.blit(ghm.HANGING_KNUCKLES_IMAGE, (450, 250))
        ghm.pg.draw.line(ghm.game_display, ghm.BRIGHT_RED, (586, 150), (586, 250), 8)
        game.button("Play", 100, 250, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, self.__navigate_to_select_difficulty)
        game.button("Options", 100, 350, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, self.__navigate_to_options)
        game.button("Exit", 100, 450, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, self.__quit_game)

    def __navigate_to_select_difficulty(self):
        pass

    def __navigate_to_options(self):
        pass

    def __quit_game(self):
        pass
