from matrix import consts, initialise
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
import time

from PIL import Image
import string # Added By CBA
from datetime import datetime # Added by CBA
import zoneinfo # Added by CBA
# Clears matrix
def clearScreen():
    initialise.rgbMatrix.Clear()

# Displays given text to the matrix
def dispText(text, posx, posy, colour, font=consts.smallFont):
    initialise.canvas.Clear()
    graphics.DrawText(initialise.canvas, font, posx, posy, colour, text)
    initialise.canvas = initialise.rgbMatrix.SwapOnVSync(initialise.canvas)

def displayCurrentTime():
    currentText = ''
    text_color = consts.GREEN
	# Pulls the exact local timezone configuration from the OS
	local_tz = zoneinfo.ZoneInfo("localtime") 
	
	# Fetch the time using that specific timezone
	now = datetime.now(local_tz)
    currentText = now.strftime("%H:%M:%S")
    dispText(currentText, 64-len(currentText)*5, 32+6, text_color, font=consts.largeFont)

def dispLogo():
    image = Image.open('logo.png')
    image.thumbnail((50, 50), Image.ANTIALIAS)
    initialise.rgbMatrix.SetImage(image.convert('RGB'),37,5) # rgbMatrix is not global its only created inside initialise.py 
# Code By CBA
def revtext(text): # Reveal Text
	temp = ''
	for ch in text:
		for i in string.printable:
			if i == ch or ch == '':
				time.sleep(0.009)
				new_text = temp+i
				dispText(new_text,5,20,consts.GREEN)
				temp = temp + ch
				break
			else:
				time.sleep(0.009)
				new_text = temp + i
				dispText(new_text,5,20,consts.GREEN)
			time.sleep(0.03)
			
	time.sleep(1)
# End of Code By CBA

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
