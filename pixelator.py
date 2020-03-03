from sense_hat import SenseHat
import sys
from time import sleep
import random

sense = SenseHat()
sense.set_imu_config(False,False,False)

count1 = 0
count2 = 0

def random_color():
    number = random.randint(0,255)
    return number

def main():
    while True:
        for count1 in range(8):
            for count2 in range(8):
                sense.set_pixel(count1, count2, random_color(), random_color(), random_color())
                sleep(0.1)
                
        sense.clear()
            
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit(0)