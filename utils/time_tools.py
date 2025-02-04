import time
import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countDown(countTime):
    while countTime>0:
        clearScreen()
        print(secToMin(countTime))
        countTime-=1
        time.sleep(1)
    print("FINISHED")

def secToMin(timeSec):
    countSec = str(timeSec % 60)
    countMin = str(timeSec // 60)
    
    if int(countSec) < 10:
        countSec = "0" + countSec
    return countMin + ':' + countSec
