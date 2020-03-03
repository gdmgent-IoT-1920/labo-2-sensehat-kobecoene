from sense_hat import SenseHat
import sys

sense = SenseHat()
sense.set_imu_config(False,False,False)

def main():
    while True:
        sense.show_message('HALLO SERMIN')


try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit(0)