import supreme_hangman as shm
import supreme_hangman.user_interface as ui
import supreme_hangman.scenes as scenes


class OptionsScene(scenes.Scene):
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
        self.game.set_scene(scenes.MenuScene(self.game))
