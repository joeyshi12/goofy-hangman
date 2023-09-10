import goofy_hangman.main as ghm
import goofy_hangman.game_manager as manager
from scene import Scene


class DeathScene(Scene):
    def __init__(self, game: manager.GameManager, time: int, score: int):
        self.game = game
        self.time = time
        self.score = score
        ghm.pg.mixer.music.load('assets/sounds/lose_music.wav')
        ghm.pg.mixer.music.play(-1)

    def render(self):
        ghm.game_display.fill(ghm.WHITE)
        ghm.game_display.blit(ghm.LOSE_IMAGE, (0, 0))
        manager.text("NO SUPREME FOR YOU", int(ghm.DISPLAY_WIDTH / 2), int(ghm.DISPLAY_HEIGHT / 3), 50, ghm.RED)
        manager.text("Time: " + str(self.time) + " seconds", int(ghm.DISPLAY_WIDTH / 2), int(ghm.DISPLAY_HEIGHT / 3 + 70), 25, ghm.RED)
        manager.text("Score: " + str(self.score) + " fails", int(ghm.DISPLAY_WIDTH / 2), int(ghm.DISPLAY_HEIGHT / 3 + 100), 25, ghm.RED)
        manager.button("Quit", 150, 450, 120, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "quit")
        manager.button("Menu", 550, 450, 120, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "intro")
