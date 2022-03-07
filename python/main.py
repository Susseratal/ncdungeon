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
    miniboss = room("m")
    treasure = room("t")
    specialRooms = [boss, treasure, treasure, miniboss]

    length = random.randint(3, 20)
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

        elif key == "a": 
            while True:
                direction = random.randint(0,1)
                mult = random.choice([-1, 1])
                if length <= 0: 
                    choice = random.choice(specialRooms)
                else:
                    choice = connector

                if direction == 0:
                    newX = (x + mult)
                    newY = y
                else:
                    newX = x
                    newY = (y + mult)

                if window.instr(int(newX), int(newY), 1) in [b'x', b't', b's', b'b']: 
                    continue # this will lock here if it works itself into a corner
                    # Also it can get to the edge of the screen and then it gets stumped
                else:
                    x = newX
                    y = newY
                    choice.spawn(window, x, y)
                    length -= 1
                    break

        elif key == "r":
            x = startPosX
            y = startPosY
            window.clear()
            window.box()
            start.spawn(window, x, y)
            window.refresh

wrapper(main)
