from matrix.utils import dispText
from matrix import consts, matrixSetup
import time

def displayCurrentTime():
    currentText = ''
    text_color = consts.GREEN

    while True:
        currentText = time.strftime("%H:%M:%S", time.gmtime())
        dispText.dispText(currentText, 64-len(currentText)*5, 32+6, text_color)
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        displayCurrentTime()

    except KeyboardInterrupt:
        matrixSetup.rgbMatrix.Clear()