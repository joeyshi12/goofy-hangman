import pygame as pg
import supreme_hangman as shm


class Button:
    def __init__(self, text, left, top, width, height, background_color, hover_color, on_click=None):
        self.text = text
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.background_color = background_color
        self.hover_color = hover_color
        self.on_click = on_click
        self.is_hovered = False

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.MOUSEMOTION:
            self.__update_is_hovered()
        elif event.type == pg.MOUSEBUTTONUP and self.on_click is not None and self.is_hovered:
            shm.BUTTON_SOUND.play()
            self.on_click()

    def render(self):
        if self.is_hovered:
            pg.draw.rect(shm.game_display,
                         self.hover_color,
                         (self.left - 10, self.top - 10, self.width + 20, self.height + 20))
        else:
            pg.draw.rect(shm.game_display,
                         self.background_color,
                         (self.left, self.top, self.width, self.height))
        button_font = pg.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = create_text_surface(self.text, button_font, shm.RED)
        text_rect.center = ((self.left + (self.width / 2)), (self.top + (self.height / 2)))
        shm.game_display.blit(text_surf, text_rect)

    def __update_is_hovered(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        self.is_hovered = self.left < mouse_x < self.left + self.width and self.top < mouse_y < self.top + self.height


def draw_box(x1, x2, y1, y2, w):
    pg.draw.line(shm.game_display, shm.BLACK, (x1, y1), (x2, y1), w)
    pg.draw.line(shm.game_display, shm.BLACK, (x2, y1), (x2, y2), w)
    pg.draw.line(shm.game_display, shm.BLACK, (x2, y2), (x1, y2), w)
    pg.draw.line(shm.game_display, shm.BLACK, (x1, y2), (x1, y1), w)


def draw_stand(x, y):
    pg.draw.line(shm.game_display, shm.BLACK, (x, y), (x, y - 240), 5)
    pg.draw.line(shm.game_display, shm.BLACK, (x - 40, y), (x + 80, y), 5)
    pg.draw.line(shm.game_display, shm.BLACK, (x, y - 240), (x + 120, y - 240), 5)
    pg.draw.line(shm.game_display, shm.BLACK, (x + 120, y - 240), (x + 120, y - 210), 5)


def draw_stickman(x, y):
    pg.draw.line(shm.game_display, shm.BLACK, (x, y - 55), (x, y), 5)
    pg.draw.line(shm.game_display, shm.BLACK, (x, y - 40), (x - 25, y - 20), 5)
    pg.draw.line(shm.game_display, shm.BLACK, (x, y - 40), (x + 25, y - 20), 5)
    pg.draw.line(shm.game_display, shm.BLACK, (x, y), (x - 20, y + 35), 5)
    pg.draw.line(shm.game_display, shm.BLACK, (x, y), (x + 20, y + 35), 5)


def create_text_surface(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def draw_text(msg, x, y, size, color):
    small_text = pg.font.Font("freesansbold.ttf", size)
    text_surf, text_rect = create_text_surface(msg, small_text, color)
    text_rect.center = (x, y)
    shm.game_display.blit(text_surf, text_rect)
