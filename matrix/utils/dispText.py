from matrix import matrix, consts
from rgbmatrix import graphics

# Displays given text to the matrix
def dispText(text, posx, posy, colour, font=consts.largeFont):
    matrix.canvas.Clear()
    graphics.DrawText(matrix.canvas, font, posx, posy, colour, text)
    matrix.canvas = matrix.rgbMatrix.SwapOnVSync(matrix.canvas)

if __name__ == "__main__":
    try:
        while True:
            dispText(matrix.args.text, int(matrix.args.posX), int(matrix.args.posY), consts.RED)

    except KeyboardInterrupt:
        matrix.rgbMatrix.Clear()