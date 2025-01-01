from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
import fonts

# Options (the flags that we used in the examples)
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.gpio_slowdown = 4
options.pwm_bits = 8

matrix = RGBMatrix(options=options)


def dispText(text, font, posx, posy, colour):
    canvas.Clear()
    graphics.DrawText(canvas, font, posx, posy, colour, text)

canvas = matrix.CreateFrameCanvas()

currentText = ''
text_color = graphics.Color(0, 255, 0)

try:
    while True:
        currentText = time.strftime("%H:%M:%S", time.gmtime())

        dispText(currentText, fonts.largeFont, 64-len(currentText)*5, 32+6, text_color)

        canvas = matrix.SwapOnVSync(canvas)
except KeyboardInterrupt:
    matrix.Clear()

