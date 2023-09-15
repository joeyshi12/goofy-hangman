import supreme_hangman as shm
import supreme_hangman.user_interface as ui
import supreme_hangman.scenes as scenes


class WinnerScene(scenes.Scene):
    def __init__(self, game, time, score):
        self.game = game
        self.display_messages = [
            ui.DisplayText("SUPREME WIN", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 150), 50, shm.GREEN),
            ui.DisplayText("Time: " + str(int(time)) + " seconds", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 190), 25, shm.GREEN),
            ui.DisplayText("Score: " + str(score) + " fails", int(shm.DISPLAY_WIDTH / 2), int(shm.DISPLAY_HEIGHT / 3 + 220), 25, shm.GREEN)
        ]
        self.buttons = [
            ui.Button("Quit", 150, 450, 120, 50, shm.GREEN, shm.BRIGHT_GREEN, scenes.quit_game),
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
        self.game.set_scene(scenes.MenuScene(self.game))
