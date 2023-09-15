import sys
import pygame as pg


class Scene:
    def handle_event(self, event):
        pass

    def render(self):
        raise NotImplementedError


def quit_game():
    pg.quit()
    sys.exit()
