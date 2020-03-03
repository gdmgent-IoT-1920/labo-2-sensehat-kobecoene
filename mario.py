from sense_hat import SenseHat
from time import sleep
import sys

sense = SenseHat()
sense.set_imu_config(False,False,False)
sense.set_rotation(270)

R = [248,0,75]  # Red
W = [248,234,226]  # White
H = [166,80,53]  # Hair
S = [248,198,165]  # Skin
Y = [248,248,38]  # Yellow
B = [40,168,248]  # Blue
O = [248,159,0]  # Orange
P = [123,36,81]  # Purple
N = [0,0,0]  # Nothing
        
image = [
N, N, N, R, R, R, W, N,
N, N, N, R, R, R, R, R,
N, N, H, S, H, N, S, N,
N, N, H, S, S, H, H, S,
N, N, N, H, S, S, S, N,
N, R, R, Y, B, B, O, N,
W, N, B, B, B, B, N, P,
N, N, H, N, N, N, P, N
]
        
image_jump = [
N, N, H, S, H, N, S, N,
N, N, H, S, S, H, H, S,
N, N, N, H, S, S, S, N,
N, R, R, Y, B, B, O, N,
W, N, B, B, B, B, N, P,
N, N, H, N, N, N, P, N,
N, N, N, N, N, N, N, N,
N, N, N, N, N, N, N, N
]
        
        
sense.set_pixels(image)

def main():
    while True:
        sense.flip_h(image)
        sleep(2)
        
        for event in sense.stick.get_events():
            sense.set_pixels(image_jump)
            sleep(0.5)
            sense.set_pixels(image)

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit(0)