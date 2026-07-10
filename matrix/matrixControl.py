from matrix import utils, consts
import sys

import threading

def checkInput():
	global mode
	while True:
        	mode = input()

inputChecker = threading.Thread(target=checkInput, daemon=True)

inputChecker.start()

mode = ""

try:
	while True:
		if mode == 'clock':
			utils.displayCurrentTime()
		elif mode == 'screensaver':
			utils.screenSaver()
		elif 'disptext' in mode:
			localText = mode.removeprefix('disptext ')
			 # if localText.startswith()
			utils.dispText(localText, 5, 20, consts.GREEN, font=consts.largeFont)
		elif mode == 'logo':
			utils.dispLogo()
		elif 'revtext' in mode: #Added By CBA
			localText = mode.removeprefix('revtext ')
			utils.revtext(localText)
		else:
			utils.clearScreen()

except KeyboardInterrupt:
	utils.clearScreen()
	sys.exit()
