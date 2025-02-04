from matrix import utils

import threading

def checkInput():
    global mode

    while True:
        mode = input()

inputChecker = threading.Thread(target=checkInput, daemon=True)
inputChecker.start()

mode = None

try:
    while True:
        match mode:
            case 'clock':
                utils.displayCurrentTime()
            case _:
                utils.clearScreen()

except KeyboardInterrupt:
    utils.clearScreen()
