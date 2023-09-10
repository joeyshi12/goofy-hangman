
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
        text("SUPREME WIN", int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 3 + 150), 50, ghm.GREEN)
        text("Time: " + str(int(t)) + " seconds", int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 3 + 190), 25, ghm.GREEN)
        text("Score: " + str(s) + " fails", int(DISPLAY_WIDTH / 2), int(DISPLAY_HEIGHT / 3 + 220), 25, ghm.GREEN)
        button("Quit", 150, 450, 120, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "quit")
        button("Menu", 550, 450, 120, 50, ghm.GREEN, ghm.BRIGHT_GREEN, "intro")
        ghm.pg.display.update()
        ghm.clock.tick(200)
