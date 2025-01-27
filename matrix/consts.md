# Consts

consts.py contains different variables which are useful when programming the matrix. They should only be used for the matrix (i.e. **not** for the UI)

## Fonts:
There are three different fonts (thus far):
 - smallFont - You can fit `21` characters horizontally. To center horizontally, use `64-len(currentText)*3` as the x value - note this is 1 pixel off (to the left) perfectly centered.
 - medFont - You can fit `16` characters horizontally. To center horizontally, use `64-len(currentText)*4` as the x value
 - largeFont - You can fit `13` characters horizontally. To center horizontally, use `64-len(currentText)*5` as the x value