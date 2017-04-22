#!/usr/bin/env python3
# coding utf-8

import RPi.GPIO as GPIO
from time import sleep


def main():
    try:
        GPIO.setmode(GPIO.BOARD)
        chan_list = [7]

        GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)

        GPIO.output(7, GPIO.HIGH)
        sleep(1)
        GPIO.output(7, GPIO.LOW)

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nclean up")


if __name__ == '__main__':
    main()
