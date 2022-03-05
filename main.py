import sys
import random
import curses
from curses import wrapper

class room:
    def __init__(self, icon):
        self.i = icon

    def spawn(self, window, x, y, icon):
        window.addstr(int(x), int(y), icon)

def main(window):
    start = room("s")
    connector = room("x")
    boss = room("b")
    treasure = room("t")
    icons = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    length = random.randint(8, 30)
    curses.noecho()
    curses.curs_set(0)
    window.keypad(1)
    curses.use_default_colors()

    win_width = (window.getmaxyx()[1] - 1) # y
    win_height = (window.getmaxyx()[0] - 1) # x
    startPosX = (win_height / 2)
    startPosY = (win_width / 2)
    x = startPosX
    y = startPosY

    start.spawn(window, x, y, "s")
    window.box()
    window.refresh()

    while True:
        try:
            key = window.getkey()
        except curses.error:
            key = None

        if key == "q":
            sys.exit(0)

        elif key == "a": 
            direction = random.randint(0,1)
            mult = random.choice([-1, 1])

            if direction == 0:
                newX = (x + mult)
                newY = y
            else:
                newX = x
                newY = (y + mult)

            if window.instr(int(newY), int(newX), 1) in [icons]: # always passes
                pass
            else:
                x = newX
                y = newY
                icon = random.choice(icons)
                connector.spawn(window, x, y, icon)

wrapper(main)
