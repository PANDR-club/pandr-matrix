from matrix import consts, matrixSetup
from rgbmatrix import graphics
import argparse

# Flags
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', required=True)
parser.add_argument('-x', '--posX', required=True)
parser.add_argument('-y', '--posY', required=True)

args = parser.parse_args()

# Displays given text to the matrix
def dispText(text, posx, posy, colour, font=consts.largeFont):
    matrixSetup.canvas.Clear()
    graphics.DrawText(matrixSetup.canvas, font, posx, posy, colour, text)
    matrixSetup.canvas = matrixSetup.rgbMatrix.SwapOnVSync(matrixSetup.canvas)

if __name__ == "__main__":
    try:
        while True:
            dispText(args.text, int(args.posX), int(args.posY), consts.RED)

    except KeyboardInterrupt:
        matrixSetup.rgbMatrix.Clear()