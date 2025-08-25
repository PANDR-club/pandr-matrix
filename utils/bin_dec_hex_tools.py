# A collection of functions/tools to do with Binary, Hexadecimal and Decimal 8-bit integers

# Here we import the 'randint' function from the 'random' library. Libraries are files that contain
# functions written by other people. In this case, writing a function that returns a random integer
# between two values could be hard and time consuming to code. In such a case, we can use somebody 
# else's code (the 'randint' function) to serve our purpose. Examples on when we might do this is 
# for generating random things and handling time.
from random import choice
from random import randint

# hexChars is a list of all the hex characters in order
hexChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# This is where we declare our function -> 'def' is a python keyword, telling it that the next bit
# of code will be the function name
def randBin():
    # Here we declare an output variable, which we will return. We want to return a string, and so
    # we set the output to initially be an empty string
    output = '' # we have this outside the loop because we don't want to set it to empty every time the loop is run

    # Now we want to create an 8 character long binary number, so we loop 8 times (add 8 random characters to 'output')
    for _ in range(8):
        # Here we use the 'randint' function that we imported at the top of our file. This will
        # generate a random integer from 0 to 1 (i.e. a random binary digit)
        randomDigit = randint(0, 1) # We assign this to a variable, to keep track of it

        # As we want to output a string, we must convert our randomDigit into a string format (otherwise
        # python will try to mathematically add our integer to a string which is not possible (words can't be used in addition))
        randomDigit = str(randomDigit)

        # We can now add this digit onto the end of our output string. This is called concatination
        # Because we have both data types as strings, python will interpret this '+' to do this
        output = output + randomDigit
    
    # Here we simple return our 'output' variable once the loop has finished.
    return output

def randDec():
    return randint(0, 255)

def randHex():
    output = ''

    for _ in range(2):
        randomHex = hexChars[randint(0,15)]
        output = output + randomHex

    return output

# Converts any hex integers to binary equivlents intuitively
def hexToBin(hexStr):
    hexList = [i for i in hexStr] # This is a list comprehension. It saves me from having to run a 'for' loop in order to get each element from our string to put into a list

    result = ''
    for nibble in hexList:
        result += decToBin(hexChars.index(nibble), True) # The index will be the decimal equivlent as the list is ordered

    return result

# Can convert 4 or 8 bit decimal integers to binary intuitively. Defaults to 8 bit mode unless fourBitMode is specified as true
def decToBin(dec, fourBitMode=False): # We assume 8 bit mode unless explicitly stated
    if fourBitMode:
        comparisonNum = 8
    else:
        comparisonNum = 128

    result = ''
    while True:
        if comparisonNum <= dec:
            result += '1'
            dec -= comparisonNum
        else:
            result += '0'

        comparisonNum /= 2
        if comparisonNum < 1:
            break

    return result

def binToDec(binStr):
    comparisonNum = 128
    total = 0
    for char in binStr:
        if char == "1":
            total += comparisonNum
        else:
            total += 0
        comparisonNum /= 2
        if comparisonNum < 1:
            break
    return total

names = ['james', 'jack', 'john']
def rand_name(names):
    print(choice(names))

