from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
from matrix import consts

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


# Displays given text to the matrix
def dispText(text, posx, posy, colour, font=consts.medFont):
    global canvas

    canvas.Clear()
    graphics.DrawText(canvas, font, posx, posy, colour, text)
    canvas = rgbMatrix.SwapOnVSync(canvas)

def displayCurrentTime():
    currentText = ''
    text_color = consts.GREEN

    while True:
        currentText = time.strftime("%H:%M:%S", time.gmtime())
        dispText(currentText, 64-len(currentText)*5, 32+6, text_color, font=consts.largeFont)
        canvas = rgbMatrix.SwapOnVSync(canvas)
        time.sleep(0.2) # Helps reduce flickering
