from matrix import consts, initialise
from rgbmatrix import graphics
import time

# Clears matrix
def clearScreen():
    initialise.rgbMatrix.Clear()

# Displays given text to the matrix
def dispText(text, posx, posy, colour, font=consts.largeFont):
    initialise.canvas.Clear()
    graphics.DrawText(initialise.canvas, font, posx, posy, colour, text)
    initialise.canvas = initialise.rgbMatrix.SwapOnVSync(initialise.canvas)

def displayCurrentTime():
    currentText = ''
    text_color = consts.GREEN

    currentText = time.strftime("%H:%M:%S", time.gmtime())
    dispText(currentText, 64-len(currentText)*5, 32+6, text_color)


# if __name__ == "__main__":
#     # Flags
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-t', '--text', required=True)
#     parser.add_argument('-x', '--posX', required=True)
#     parser.add_argument('-y', '--posY', required=True)

#     args = parser.parse_args()

#     try:
#         while True:
#             dispText(args.text, int(args.posX), int(args.posY), consts.RED)
#             consts.james = 99999

#     except KeyboardInterrupt:
#         initialise.rgbMatrix.Clear()