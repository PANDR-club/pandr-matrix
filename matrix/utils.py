from matrix import consts, initialise
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
import json
import time
import threading # added by cba
from urllib.error import URLError
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageFont
import string # Added By CBA
from datetime import datetime # added by CBA
import zoneinfo	#added by CBA

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# Clears matrix
def clearScreen():
    initialise.rgbMatrix.Clear()

# Displays given text to the matrix
def dispText(text, posx, posy, colour, font=consts.smallFont):
    initialise.canvas.Clear()
    graphics.DrawText(initialise.canvas, font, posx, posy, colour, text)
    initialise.canvas = initialise.rgbMatrix.SwapOnVSync(initialise.canvas)

def dispText_without_clear(text, posx, posy, colour, font=consts.smallFont):	# added by cba
    initialise.canvas.Clear()
    graphics.DrawText(initialise.canvas, font, posx, posy, colour, text)
    initialise.canvas = initialise.rgbMatrix.SwapOnVSync(initialise.canvas)

def _matrix_size():
    width = getattr(initialise.rgbMatrix, "width", SCREEN_WIDTH)
    height = getattr(initialise.rgbMatrix, "height", SCREEN_HEIGHT)
    return width, height


def _draw_cloud(draw, left, top, scale=1):
    r = scale
    draw.ellipse((left + 6 * r, top + 2 * r, left + 16 * r, top + 12 * r), fill="white")
    draw.ellipse((left + 12 * r, top, left + 24 * r, top + 12 * r), fill="white")
    draw.ellipse((left + 18 * r, top + 4 * r, left + 30 * r, top + 14 * r), fill="white")
    draw.rectangle((left + 8 * r, top + 8 * r, left + 26 * r, top + 16 * r), fill="white")


def _draw_wind(draw, left, top, scale=1):
    r = scale
    draw.arc((left, top, left + 26 * r, top + 10 * r), start=10, end=180, fill=(120, 220, 255), width=max(1, r))
    draw.arc((left + 4 * r, top + 8 * r, left + 30 * r, top + 18 * r), start=10, end=180, fill=(120, 220, 255), width=max(1, r))


def _draw_rain(draw, left, top, scale=1):
    r = scale
    _draw_cloud(draw, left, top, scale)
    for offset in (8, 14, 20):
        draw.line((left + offset * r, top + 18 * r, left + offset * r - 2 * r, top + 26 * r), fill=(90, 160, 255), width=max(1, r))


def _draw_computer(draw, left, top, scale=1):
    r = scale
    draw.rounded_rectangle((left, top + 2 * r, left + 26 * r, top + 18 * r), radius=2 * r, outline=(180, 220, 255), width=max(1, r))
    draw.rectangle((left + 4 * r, top + 5 * r, left + 22 * r, top + 14 * r), fill=(20, 40, 60))
    draw.rectangle((left + 9 * r, top + 18 * r, left + 17 * r, top + 22 * r), fill=(180, 220, 255))
    draw.rectangle((left + 6 * r, top + 22 * r, left + 20 * r, top + 24 * r), fill=(180, 220, 255))


def _weather_icon_from_code(weather_code, wind_speed_kph):
    if wind_speed_kph is not None and wind_speed_kph >= 28:
        return "wind"
    if weather_code in (51, 53, 55, 61, 63, 65, 66, 67, 80, 81, 82, 95, 96, 99):
        return "rain"
    return "cloud"


def _weather_label(weather_code, wind_speed_kph):
    if wind_speed_kph is not None and wind_speed_kph >= 28:
        return f"Wind {wind_speed_kph:.0f}kph"
    if weather_code in (51, 53, 55):
        return "Drizzle"
    if weather_code in (61, 63, 65, 80, 81, 82):
        return "Rain"
    if weather_code in (95, 96, 99):
        return "Storm"
    if weather_code in (45, 48):
        return "Fog"
    if weather_code in (1, 2, 3):
        return "Cloud"
    return "Clear"


def _fetch_dorchester_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=50.7112&longitude=-2.4384"
        "&current_weather=true&timezone=auto"
    )
    try:
        with urlopen(url, timeout=5) as response:
            payload = json.loads(response.read().decode("utf-8"))
        current = payload.get("current_weather", {})
        temperature_c = current.get("temperature")
        weather_code = current.get("weathercode", 2)
        wind_speed_kph = current.get("windspeed")
        return temperature_c, weather_code, wind_speed_kph
    except (URLError, TimeoutError, ValueError, KeyError, TypeError):
        return None, None, None


# new screen saver festure	by cba
def screenSaver():
    width, height = _matrix_size()
    local_tz = zoneinfo.ZoneInfo("localtime")
    now = datetime.now(local_tz)
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%a %d %b")
    temperature_c, weather_code, wind_speed_kph = _fetch_dorchester_weather()
    weather_state = _weather_icon_from_code(weather_code, wind_speed_kph)
    weather_label = _weather_label(weather_code, wind_speed_kph)
    temperature_text = "--" if temperature_c is None else f"{temperature_c:.0f}"

    image = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    text_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

    draw.text((2, 1), current_time, fill=(0, 255, 0), font=text_font)
    draw.text((2, 12), f"Dorchester {temperature_text}C", fill=(255, 255, 255), font=small_font)
    draw.text((2, 22), current_date, fill=(120, 200, 255), font=small_font)
    draw.text((width - 42, 20), weather_label, fill=(255, 255, 255), font=small_font)

    logo = Image.open('logo.png')
    logo.thumbnail((28, 28), Image.ANTIALIAS)
    image.paste(logo.convert('RGB'), (2, height - logo.height - 2))

    icons_left = width - 42
    icons_top = 2
    if weather_state == "rain":
        _draw_rain(draw, icons_left, icons_top, scale=1)
    elif weather_state == "wind":
        _draw_wind(draw, icons_left, icons_top + 2, scale=1)
    else:
        _draw_cloud(draw, icons_left, icons_top, scale=1)

    _draw_computer(draw, width - 30, height - 28, scale=1)

    initialise.rgbMatrix.SetImage(image.convert("RGB"), 0, 0)

def displayCurrentTime():
    currentText = ''
    text_color = consts.GREEN
    local_tz = zoneinfo.ZoneInfo("localtime")
    now = datetime.now(local_tz)
    currentText = now.strftime("%H:%M:%S")
    ###currentText = time.strftime("%H:%M:%S", time.gmtime())
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
