from sense_hat import SenseHat
import sys
from time import sleep
import random

sense = SenseHat()
sense.set_imu_config(False,False,False)
sense.set_rotation(270)


def random_txt():
    number = random.randint(0,255)
    return number

def random_back():
    number = random.randint(0,100)
    return number

def main():
    while True:
        sense.show_message('Hello! We are New Media Development :)', text_colour=[random_txt(), random_txt(), random_txt()], back_colour=[random_back(), random_back(), random_back()])


try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit(0)