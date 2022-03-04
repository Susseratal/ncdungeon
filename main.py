import sys
import random
import curses
from curses import wrapper

class room:
    def __init__(self, icon):
        self.i = icon

    def spawn(self, window, x, y):
        window.addstr(int(x), int(y), self.i)

def main(window):
    start = room("s")
    connector = room("x")
    boss = room("b")
    treasure = room("t")

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

    start.spawn(window, x, y)
    window.box()
    window.refresh()

    while True:
        try:
            key = window.getkey()
        except curses.error:
            key = None

        if key == "q":
            sys.exit(0)

        elif key == "a": # how do I check if something is already there?
            direction = random.randint(0,1)
            mult = random.randint(0,1)
            if mult == 0:
                mult = -1
            if direction == 0:
                x = (x + mult)
            else:
                y = (y + mult)

            attrs = window.inch(int(y), int(x))
            ch = chr(attrs & 255)
            isbold = bool(attrs & curses.A_BOLD)
            if isbold: # this just locks everything out
                pass
            # if char in ["x", "b", "t", "s"]: # this seems to do a whole lot of nothing
                # pass
            else:
                connector.spawn(window, x, y)

wrapper(main)
