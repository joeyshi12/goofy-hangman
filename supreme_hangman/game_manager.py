import sys
import pygame as pg

import supreme_hangman as shm
from supreme_hangman.scenes import MenuScene


class GameManager:
    def __init__(self):
        self.scene = MenuScene(self)

    def start(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                self.scene.handle_event(event)
            self.scene.render()
            pg.display.update()
            shm.clock.tick(60)

    def set_scene(self, scene):
        self.scene = scene
