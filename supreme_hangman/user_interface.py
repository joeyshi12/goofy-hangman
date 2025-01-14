import os
import pygame as pg
import supreme_hangman as shm


class Button:
    def __init__(self, text, left, top, width, height, background_color, hover_color, on_click=None):
        self.display_text = DisplayText(text, left + width / 2, top + height / 2, 20, shm.RED)
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.background_color = background_color
        self.hover_color = hover_color
        self.on_click = on_click
        self.is_hovered = False
        self.sound = pg.mixer.Sound(os.path.join("assets", "sounds", "button.wav"))

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.MOUSEMOTION:
            self.__update_is_hovered()
        elif event.type == pg.MOUSEBUTTONUP and self.on_click is not None and self.is_hovered:
            self.sound.play()
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
        self.display_text.render()

    def __update_is_hovered(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        self.is_hovered = self.left < mouse_x < self.left + self.width and self.top < mouse_y < self.top + self.height


class TextInput:
    FONT = pg.font.Font("freesansbold.ttf", 20)
    MAX_INPUT_LENGTH = 21

    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.content = ""
        self.__update_display_text()

    def handle_event(self, event: pg.event.Event):
        if event.type != pg.KEYDOWN or event.key == pg.K_RETURN:
            return
        if event.key == pg.K_BACKSPACE:
            self.content = self.content[:-1]
        elif len(self.content) <= TextInput.MAX_INPUT_LENGTH:
            user_input = event.dict.get("unicode")
            self.content += user_input

        self.__update_display_text()

    def render(self):
        draw_box(self.left, self.left + self.width, self.top, self.top + self.height, 5)
        shm.game_display.blit(self.text_surface, self.text_rect)

    def clear(self):
        self.content = ""
        self.__update_display_text()

    def __update_display_text(self):
        self.text_surface = TextInput.FONT.render(self.content, True, shm.RED)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midleft = (self.left + 5, self.top + self.height / 2)


class DisplayText:
    def __init__(self, message, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.update_message(message)

    def render(self):
        shm.game_display.blit(self.text_surface, self.text_rect)

    def update_message(self, message):
        font = pg.font.Font("freesansbold.ttf", self.size)
        self.text_surface = font.render(message, True, self.color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x, self.y)


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
