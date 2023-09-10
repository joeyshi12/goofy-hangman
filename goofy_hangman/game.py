import random
import goofy_hangman.main as ghm


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
            if action == "intro":
                start()
            elif action == "play":
                game_select()
            elif action == "option":
                option()
            elif action == "quit":
                ghm.pg.quit()
                quit()
            elif action == "enter":
                return "enter"
            elif action == "eazy" or action == "medium" or action == "hard":
                gameloop(action)
    else:
        ghm.pg.draw.rect(ghm.game_display, ic, (x, y, w, h))

    small_text = ghm.pg.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(msg, small_text, ghm.RED)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    ghm.game_display.blit(text_surf, text_rect)


def start():
    ghm.pg.mixer.music.load('assets/sounds/opening.wav')
    ghm.pg.mixer.music.play(-1)
    logo = ghm.pg.image.load("assets/images/supreme_logo.png")
    hanging_knuckles = ghm.pg.image.load("assets/images/sad.png")
    while True:
        for event in ghm.pg.event.get():
            if event.type == ghm.pg.QUIT:
                ghm.pg.quit()
                quit()
        ghm.game_display.fill(ghm.WHITE)
        ghm.game_display.blit(logo, (30, -30))
        ghm.game_display.blit(hanging_knuckles, (450, 250))
        ghm.pg.draw.line(ghm.game_display, ghm.BRIGHT_RED, (586, 150), (586, 250), 8)
        button("Play", 100, 250, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "play")
        button("Options", 100, 350, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "option")
        button("Exit", 100, 450, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "quit")
        ghm.pg.display.update()
        ghm.clock.tick(200)


def game_select():
    i_sleep = ghm.pg.image.load("assets/images/i_sleep.png")
    real = ghm.pg.image.load("assets/images/real.png")
    power_of_god_and_anime = ghm.pg.image.load("assets/images/power_of_god_and_anime.png")
    DISPLAY_WIDTH, DISPLAY_HEIGHT = ghm.game_display.get_size()
    while True:
        for event in ghm.pg.event.get():
            if event.type == ghm.pg.QUIT:
                ghm.pg.quit()
                quit()
        ghm.game_display.fill(ghm.WHITE)
        text("Choose your difficulty", (DISPLAY_WIDTH / 2), (150), 50, ghm.RED)
        ghm.game_display.blit(i_sleep,
                         (DISPLAY_WIDTH * 0.1, 250))
        ghm.game_display.blit(real, (DISPLAY_WIDTH * 0.38, 250))
        ghm.game_display.blit(power_of_god_and_anime, (DISPLAY_WIDTH * 0.7 - 10, 250))
        button("EAZY", DISPLAY_WIDTH * 0.1 - 20, 450, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN,
               "eazy")
        button("MEDIUM", DISPLAY_WIDTH * 0.38, 450, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "medium")
        button("EXPERTS ONLY", DISPLAY_WIDTH * 0.7 - 20, 450, 200, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "hard")
        ghm.pg.display.update()
        ghm.clock.tick(200)


def option():
    knuckles = ghm.pg.image.load("assets/images/knuckles.png")
    while True:
        for event in ghm.pg.event.get():
            if event.type == ghm.pg.QUIT:
                ghm.pg.quit()
                quit()
        ghm.game_display.fill(ghm.WHITE)
        ghm.game_display.blit(knuckles, (0, 0))
        DISPLAY_WIDTH, DISPLAY_HEIGHT = ghm.game_display.get_size()
        text("THIS IS NOT DA WEI", int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 2), 50, ghm.GREEN)
        button("ABORT", DISPLAY_WIDTH * 0.43, 450, 120, 50, ghm.GREEN, ghm.BRIGHT_GREEN,
               "intro")
        ghm.pg.display.update()
        ghm.clock.tick(200)


def death_screen(t, s):
    ghm.pg.mixer.music.load('assets/sounds/lose_music.wav')
    ghm.pg.mixer.music.play(-1)
    lost_image = ghm.pg.image.load("assets/images/lost_image.png")
    DISPLAY_WIDTH, DISPLAY_HEIGHT = ghm.game_display.get_size()
    while True:
        for event in ghm.pg.event.get():
            if event.type == ghm.pg.QUIT:
                ghm.pg.quit()
                quit()
        ghm.game_display.fill(ghm.WHITE)
        ghm.game_display.blit(lost_image, (0, 0))
        text("NO SUPREME FOR YOU", int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 3), 50,
             ghm.RED)
        text("Time: " + str(int(t)) + " seconds", int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 3 + 70), 25,
             ghm.RED)
        text("Score: " + str(s) + " fails", int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 3 + 100), 25,
             ghm.RED)
        button("Quit", 150, 450, 120, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "quit")
        button("Menu", 550, 450, 120, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "intro")
        ghm.pg.display.update()
        ghm.clock.tick(200)


def end_screen(t, s):
    winning = ghm.pg.image.load("assets/images/winning.png")
    DISPLAY_WIDTH, DISPLAY_HEIGHT = ghm.game_display.get_size()
    while True:
        for event in ghm.pg.event.get():
            if event.type == ghm.pg.QUIT:
                ghm.pg.quit()
                quit()
        ghm.game_display.fill(ghm.BLUE)
        ghm.game_display.blit(winning, (170, 15))
        text("SUPREME WIN", int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 3 + 150), 50,
             ghm.GREEN)
        text("Time: " + str(int(t)) + " seconds", int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 3 + 190), 25,
             ghm.GREEN)
        text("Score: " + str(s) + " fails", int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 3 + 220), 25,
             ghm.GREEN)
        button("Quit", 150, 450, 120, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "quit")
        button("Menu", 550, 450, 120, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "intro")
        ghm.pg.display.update()
        ghm.clock.tick(200)


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


def gameloop(difficulty):
    ghm.pg.mixer.music.load('assets/sounds/wii.mp3')
    ghm.pg.mixer.music.play(-1)
    if difficulty == "eazy":
        words = (list('s t r i n g'), list('p l a n e t'), list('r a n d o m'), list('v e c t o r'),

                 list('g e n i u s'), list('p y t h o n'), list('v o l u m e'), list('p o e t r y'))
        string = list("_ _ _ _ _ _")
        r = 6
    elif difficulty == "medium":
        words = (list('t r a m p o l i n e'), list('a f t e r s h o c k'), list('b a n k r u p t c y'),
                 list('m o n a r c h i s t'))
        string = list("_ _ _ _ _ _ _ _ _ _")
        r = 10
    else:
        words = (list('m i s c o n j u g a t e d l y'),
                 list('d e r m a t o g l y p h i c s'))
        string = list("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        r = 15

    lives = 7
    guess = []
    word = random.choice(words)
    answer = ''.join(word).replace(" ", "")
    NANI = False
    attempts = 0
    time = 0
    display_width, display_height = ghm.game_display.get_size()
    while True:
        for event in ghm.pg.event.get():
            if event.type == ghm.pg.QUIT:
                ghm.pg.quit()
            elif event.type == ghm.pg.KEYDOWN:
                if len(guess) <= 21:
                    if event.key == ghm.pg.K_BACKSPACE:
                        if len(guess) == 0:
                            continue
                        else:
                            guess.pop(-1)
                    elif event.key == ghm.pg.K_RETURN:
                        guess_str = "".join(guess)
                        attempts += 1
                        if len(guess) == 0:
                            continue
                        elif str(''.join(guess)) == "omae wa mou shindeiru":
                            attempts = -9999999999999999999999999999
                            NANI = True
                            continue
                        elif guess_str == answer:
                            attempts -= 1
                            for i in range(r):
                                string[2 * i] = word[2 * i]
                        else:
                            for i in range(0, len(guess)):
                                guess.pop(-1)
                            for i in range(r):
                                if guess_str == word[2 * i]:
                                    attempts -= 1
                                    string[2 * i] = word[2 * i]
                    else:
                        user_input = str(event)[30]
                        guess.append(user_input)
                        guess_str = ''.join(guess)

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

        ghm.pg.display.update()
        ghm.clock.tick(200)
