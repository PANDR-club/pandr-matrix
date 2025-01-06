import time, argparse
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from matrix import consts
from matrix.utils import dispText

# Flags
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', required=True)
parser.add_argument('-x', '--posX', required=True)
parser.add_argument('-y', '--posY', required=True)

args = parser.parse_args()

# Options (the flags that we used in the examples)
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.gpio_slowdown = 4
options.pwm_bits = 11

rgbMatrix = RGBMatrix(options=options)
canvas = rgbMatrix.CreateFrameCanvas()

def displayCurrentTime():
    global canvas

    currentText = ''
    text_color = consts.GREEN

    while True:
        currentText = time.strftime("%H:%M:%S", time.gmtime())
        dispText(currentText, 64-len(currentText)*5, 32+6, text_color)
        canvas = rgbMatrix.SwapOnVSync(canvas)