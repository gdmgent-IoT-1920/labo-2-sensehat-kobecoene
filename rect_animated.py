from sense_hat import SenseHat
from time import sleep
import random
import sys

sense = SenseHat()
sense.set_imu_config(False,False,False)
sense.set_rotation(270)

def random_color():
    number = random.randint(0,255)
    return number

def R():
    color = [random_color(), random_color(), random_color()]
    return color

N = [0,0,0]

image = [
N, N, N, N, N, N, N, N,
N, N, N, N, N, N, N, N,
N, N, N, N, N, N, N, N,
N, N, N, R(), R(), N, N, N,
N, N, N, R(), R(), N, N, N,
N, N, N, N, N, N, N, N,
N, N, N, N, N, N, N, N,
N, N, N, N, N, N, N, N
]
image1 = [
N, N, N, N, N, N, N, N,
N, N, N, N, N, N, N, N,
N, N, R(), R(), R(), R(), N, N,
N, N, R(), N, N, R(), N, N,
N, N, R(), N, N, R(), N, N,
N, N, R(), R(), R(), R(), N, N,
N, N, N, N, N, N, N, N,
N, N, N, N, N, N, N, N
]
image2 = [
N, N, N, N, N, N, N, N,
N, R(), R(), R(), R(), R(), R(), N,
N, R(), N, N, N, N, R(), N,
N, R(), N, N, N, N, R(), N,
N, R(), N, N, N, N, R(), N,
N, R(), N, N, N, N, R(), N,
N, R(), R(), R(), R(), R(), R(), N,
N, N, N, N, N, N, N, N
]
image3 = [
R(), R(), R(), R(), R(), R(), R(), R(),
R(), N, N, N, N, N, N, R(),
R(), N, N, N, N, N, N, R(),
R(), N, N, N, N, N, N, R(),
R(), N, N, N, N, N, N, R(),
R(), N, N, N, N, N, N, R(),
R(), N, N, N, N, N, N, R(),
R(), R(), R(), R(), R(), R(), R(), R()
]

def main():
    while True:
        sense.set_pixels(image)
        sleep(1)
        sense.set_pixels(image1)
        sleep(1)
        sense.set_pixels(image2)
        sleep(1)
        sense.set_pixels(image3)
        sleep(1)
        sense.set_pixels(image2)
        sleep(1)
        sense.set_pixels(image1)
        sleep(1)
        

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit(0)