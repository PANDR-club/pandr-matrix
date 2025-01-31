from rgbmatrix import RGBMatrix, RGBMatrixOptions

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