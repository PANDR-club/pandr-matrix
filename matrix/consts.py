# Contains consts useful for programming the matrix

from rgbmatrix import graphics

smallFont = graphics.Font()
smallFont.LoadFont("matrix/fonts/6x10.bdf") # 21 char horizontal limit

medFont = graphics.Font()
medFont.LoadFont('matrix/fonts/8x13.bdf') # 16 char horizontal limit

largeFont = graphics.Font()
largeFont.LoadFont("matrix/fonts/10x20.bdf") # 13 char horizontal limit

RED = graphics.Color(255, 0, 0)
GREEN = graphics.Color(0, 255, 0)
BLUE = graphics.Color(0, 0, 255)
TURQUOISE = graphics.Color(0, 255, 255)
YELLOW = graphics.Color(255, 255, 0)
PURPLE = graphics.Color(128, 0, 128)
ORANGE = graphics.Color(255, 165, 0)
PINK = graphics.Color(255, 192, 203)
WHITE = graphics.Color(255, 255, 255)
GRAY = graphics.Color(128, 128, 128)
CYAN = graphics.Color(0, 255, 255)
MAGENTA = graphics.Color(255, 0, 255)
BROWN = graphics.Color(165, 42, 42)
LIME = graphics.Color(0, 255, 0)
NAVY = graphics.Color(0, 0, 128)
MAROON = graphics.Color(128, 0, 0)
OLIVE = graphics.Color(128, 128, 0)
TEAL = graphics.Color(0, 128, 128)
