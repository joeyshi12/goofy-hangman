import goofy_hangman.main as ghm
from scene import Scene


class HangmanScene(Scene):
    def __init__(self, difficulty):
        self.attempts = 0
        self.guess = []
        if difficulty == "eazy":
            self.words = (list('s t r i n g'), list('p l a n e t'), list('r a n d o m'), list('v e c t o r'),
                          list('g e n i u s'), list('p y t h o n'), list('v o l u m e'), list('p o e t r y'))
            self.string = list("_ _ _ _ _ _")
            self.word_length = 6
        elif difficulty == "medium":
            self.words = (list('t r a m p o l i n e'), list('a f t e r s h o c k'), list('b a n k r u p t c y'), list('m o n a r c h i s t'))
            self.string = list("_ _ _ _ _ _ _ _ _ _")
            self.word_length = 10
        else:
            self.words = (list('m i s c o n j u g a t e d l y'), list('d e r m a t o g l y p h i c s'))
            self.string = list("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            self.word_length = 15


    def handle_event(self, event):
        if event.type == ghm.pg.KEYDOWN:
            if len(self.guess) <= 21:
                if event.key == ghm.pg.K_BACKSPACE:
                    if len(self.guess) == 0:
                        return
                    else:
                        self.guess.pop(-1)
                elif event.key == ghm.pg.K_RETURN:
                    guess_str = "".join(self.guess)
                    self.attempts += 1
                    if len(self.guess) == 0:
                        return
                    elif str(''.join(self.guess)) == "omae wa mou shindeiru":
                        attempts = -9999999999999999999999999999
                        NANI = True
                        return
                    elif guess_str == answer:
                        self.attempts -= 1
                        for i in range(self.word_length):
                            self.string[2 * i] = self.word[2 * i]
                    else:
                        for i in range(0, len(self.guess)):
                            self.guess.pop(-1)
                        for i in range(self.word_length):
                            if guess_str == word[2 * i]:
                                self.attempts -= 1
                                self.string[2 * i] = word[2 * i]
                else:
                    user_input = str(event)[30]
                    self.guess.append(user_input)
                    guess_str = ''.join(self.guess)


    def render(self):
        ghm.game_display.fill(ghm.WHITE)
        time += 1 / 200
        box(50, 310, 230, 270, 5)
        box(display_width * 0.5, display_width - 25, 25, display_height - 250, 5)
        text("Guess the Word!", 180, 100, 30, ghm.RED)
        text(''.join(guess), 180, 250, 20, ghm.RED)
        text(''.join(string), display_width * 0.5, display_height - 100, 50, ghm.RED)
        text("Time:", 538, 375, 20, ghm.ghm.RED)
        text(str(int(time)), 625, 375, 20, ghm.ghm.RED)
        text("Fails:", 540, 400, 20, ghm.ghm.RED)
        text(str(attempts) + "/" + str(lives), 640, 400, 20, ghm.RED)
        stand(480, 305)
        if attempts >= 1:
            ghm.pg.draw.circle(ghm.game_display, ghm.BLACK, (600, 120), 25, 5)
            if attempts >= 2:
                ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (600, 145), (600, 200), 5)
                if attempts >= 3:
                    ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (600, 160), (575, 180), 5)
                    if attempts >= 4:
                        ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (600, 160), (625, 180), 5)
                        if attempts >= 5:
                            ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (600, 200), (580, 235), 5)
                            if attempts >= 6:
                                ghm.pg.draw.line(ghm.game_display, ghm.BLACK, (600, 200), (620, 235), 5)

        if button("Enter", 130, 300, 100, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "enter") == "enter":
            for event in ghm.pg.event.get():
                if event.type == ghm.pg.MOUSEBUTTONUP:
                    attempts += 1
                    if len(guess) == 0:
                        continue
                    for i in range(0, len(guess)):
                        guess.pop(-1)
                    if guess_str == answer:
                        for i in range(r):
                            string[2 * i] = word[2 * i]
                    for i in range(r):
                        if guess_str == word[2 * i]:
                            attempts -= 1
                            string[2 * i] = word[2 * i]

        if string == word:
            end_screen(time, attempts)

        if attempts == lives:
            death_screen(time, attempts)

        if NANI:
            ghm.MEME_VIDEO.preview()
            end_screen(time, attempts)

