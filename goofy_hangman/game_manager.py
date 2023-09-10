import sys
import goofy_hangman.main as ghm
from goofy_hangman.menu_scene import MenuScene
from scene import Scene


def box(x1, x2, y1, y2, w):
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x1, y1), (x2, y1), w)
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x2, y1), (x2, y2), w)
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x2, y2), (x1, y2), w)
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x1, y2), (x1, y1), w)


def stand(x, y):
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x, y), (x, y - 240), 5)
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x - 40, y), (x + 80, y), 5)
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x, y - 240), (x + 120, y - 240), 5)
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x + 120, y - 240), (x + 120, y - 210), 5)


def man(x, y):
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x, y - 55), (x, y), 5)
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x, y - 40), (x - 25, y - 20), 5)
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x, y - 40), (x + 25, y - 20), 5)
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x, y), (x - 20, y + 35), 5)
    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (x, y), (x + 20, y + 35), 5)


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def text(msg, x, y, size, color):
    smallText = ghm.pg.font.Font("freesansbold.ttf", size)
    textSurf, textRect = text_objects(msg, smallText, color)
    textRect.center = (x, y)
    ghm.game_display.blit(textSurf, textRect)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = ghm.pg.mouse.get_pos()
    click = ghm.pg.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        ghm.pg.draw.rect(ghm.game_display, ac, (x - 10, y - 10, w + 20, h + 20))
        if click[0] == 1 and action is not None:
            ghm.BUTTON_SOUND.play()
            if action is not None:
                action()
    else:
        ghm.pg.draw.rect(ghm.game_display, ic, (x, y, w, h))

    small_text = ghm.pg.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(msg, small_text, ghm.RED)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    ghm.game_display.blit(text_surf, text_rect)


class GameManager:
    def __init__(self):
        self.scene = MenuScene(self)

    def start(self):
        ghm.pg.mixer.music.load('assets/sounds/opening.wav')
        ghm.pg.mixer.music.play(-1)
        while True:
            for event in ghm.pg.event.get():
                if event.type == ghm.pg.QUIT:
                    ghm.pg.quit()
                    sys.exit()
                self.scene.handle_event(event)
            self.scene.render()
            ghm.pg.display.update()
            ghm.clock.tick(200)

    def set_scene(self, scene: Scene):
        self.scene = scene
