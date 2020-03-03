from sense_hat import SenseHat
import sys
from time import sleep
import random

sense = SenseHat()
sense.set_imu_config(False,False,False)

def random_color():
    number = random.randint(0,255)
    return number

def main():
    while True:
        sense.set_rotation(270)
        sense.show_letter("N", (random_color(), random_color(), random_color()))
        sleep(1)
        sense.show_letter("M", (random_color(), random_color(), random_color()))
        sleep(1)
        sense.show_letter("D", (random_color(), random_color(), random_color()))
        sleep(1)
        sense.clear()
        sleep(3)
        


try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit(0)