#!/usr/bin/env python3
# coding utf-8

import RPi.GPIO as GPIO
from time import sleep


def main():
    GPIO.setmode(GPIO.BOARD)
    chan_list = [40]

    GPIO.setup(chan_list, GPIO.IN)
    GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)

    try:
        while True:
            GPIO.output(38, GPIO.HIGH)
            sleep(.1)
            print(GPIO.input(40))
            GPIO.output(38, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nclean up")


if __name__ == '__main__':
    main()
