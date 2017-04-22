#!/usr/bin/env python3
# coding utf-8

import RPi.GPIO as GPIO


def main():
    try:
        GPIO.setmode(GPIO.BOARD)
        chan_list = [7]

        GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)

        GPIO.output(7, GPIO.HIGH)
        while True:
            pass
    except KeyboardInterrupt:
        GPIO.output(7, GPIO.LOW)
        GPIO.cleanup()
        print("\nclean up")


if __name__ == '__main__':
    main()
