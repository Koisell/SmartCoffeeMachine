#!/usr/bin/env python3
# coding utf-8

import RPi.GPIO as GPIO
from time import sleep

sleep_time = 0.1


def main():
    GPIO.setmode(GPIO.BOARD)
    chan_list = [7, 11]

    GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)

    GPIO.output(7, GPIO.HIGH)
    sleep(sleep_time * .5)
    GPIO.output(11, GPIO.HIGH)
    sleep(sleep_time * .5)
    GPIO.output(7, GPIO.LOW)
    sleep(sleep_time * .5)
    GPIO.output(11, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    main()
