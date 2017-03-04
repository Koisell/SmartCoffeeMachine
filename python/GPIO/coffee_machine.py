#!/usr/bin/env python3
# coding: utf-8

import RPi.GPIO as GPIO
from time import sleep


class CoffeeMachine():
    standart_time = 0.1

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.pin_single_coffee_button = 7
        self.pin_right_volume = 15
        self.pin_left_volume = 16
        self.pin_intensity = 11

        self.actuator_pin_list = [self.pin_single_coffee_button, self.pin_right_volume, self.pin_left_volume, self.pin_intensity]
        self.actuator_name_list = ["single coffee", "right pin volume", "left pin volume", "intensity"]
        self.actuator_dict = dict(zip(self.actuator_pin_list, self.actuator_name_list))

        self.captor_pin_list = []
        self.captor_name_list = []
        self.captor_dict = dict(zip(self.captor_pin_list, self.captor_name_list))

        GPIO.setup(self.actuator_pin_list, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.captor_pin_list, GPIO.IN)

    @staticmethod
    def rotate(pin1, pin2, standart_time):
        GPIO.output(pin1, GPIO.HIGH)
        sleep(standart_time * .5)
        GPIO.output(pin2, GPIO.HIGH)
        sleep(standart_time * .5)
        GPIO.output(pin1, GPIO.LOW)
        sleep(standart_time * .5)
        GPIO.output(pin2, GPIO.LOW)

    def make_coffee(self):
        GPIO.output(7, GPIO.HIGH)
        sleep(self.standart_time)
        GPIO.output(7, GPIO.LOW)

    def rotate_volume_button(self, direction):
        if direction.lower() == "r":
            CoffeeMachine.rotate(self.pin_right_volume, self.pin_left_volume, self.standart_time)
        elif direction.lower() == "l":
            CoffeeMachine.rotate(self.pin_left_volume, self.pin_right_volume, self.standart_time)
        else:
            raise ValueError("direction must be equal to r or l")

    def __clear_pin(self):
        GPIO.cleanup()

    def __del__(self):
        self.__clear_pin()

    def __exit__(self):
        self.__clear_pin()
