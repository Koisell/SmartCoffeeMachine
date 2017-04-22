#!/usr/bin/env python3
# coding: utf-8
# You should ALWAYS only use one and only one Instance of CoffeeMachine class

import RPi.GPIO as GPIO
from time import sleep
from functools import partial


class CoffeeMachine():
    standart_time = 0.1

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.pin_single_coffee_button = 7
        self.pin_right_volume = 15
        self.pin_left_volume = 16
        self.pin_intensity = 11

        self.actuator_pin_list = [self.pin_single_coffee_button, self.pin_right_volume, self.pin_left_volume, self.pin_intensity]

        self.pin_intensity_captor = 17
        self.pin_volume_captor = 18
        self.pin_water = 5
        self.volume_captor = None  # to do: implement class
        self.intensity_captor = None

        self.pin_sonar1 = 13
        self.pin_sonar2 = 14
        self.captor_pin_list = [self.pin_intensity_captor, self.pin_volume_captor, self.pin_water]

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

    @staticmethod
    def push_button(pin, standart_time):
        GPIO.output(pin, GPIO.HIGH)
        sleep(standart_time)
        GPIO.output(pin, GPIO.LOW)

    def make_coffee(self, volume, intensity):
        self.set_volume(volume)
        self.set_intensity(intensity)

        # Waiting to refull water tank
        while not self.tank_is_full():
            pass

        CoffeeMachine.push_button(self.pin_single_coffee_button, self.standart_time)

    # f selection is the fonction to change leds position
    @staticmethod
    def set_preference(choice, f_selection, light_captor, nb_choices):
        if choice >= nb_choices:
            raise ValueError("choise must be between 0 and nb_choices")
        position = CoffeeMachine.get_position(f_selection, light_captor, nb_choices)
        nb_pulse = (choice - position) % nb_choices
        for i in range(nb_pulse):
            f_selection()

    def set_intensity(self, intensity):
        f = partial(self.push_button, self.pin_intensity)
        return CoffeeMachine.set_preference(intensity, f, self.intensity_captor, 5)

    def set_volume(self, volume):
        f = partial(self.rotate_volume_button, "r")
        return CoffeeMachine.set_preference(volume, f, self.volume_captor, 6)

    def rotate_volume_button(self, direction):
        if direction.lower() == "r":
            CoffeeMachine.rotate(self.pin_right_volume, self.pin_left_volume, self.standart_time)
        elif direction.lower() == "l":
            CoffeeMachine.rotate(self.pin_left_volume, self.pin_right_volume, self.standart_time)
        else:
            raise ValueError("direction must be equal to r or l")

    def intensity_button(self):
        CoffeeMachine.push_button(self.pin_intensity)

    @staticmethod
    def detection(capteur_lumiere):
        raise NotImplementedError()

    # f selection is the fonction to change leds position
    @staticmethod
    def get_position(f_selection, light_captor, nb_choices):
        position = -1
        machine_used = True

        for i in range(nb_choices):
            if CoffeeMachine.detection(light_captor):
                machine_used = False
                position = i

            f_selection()

        if not machine_used:
            return nb_choices - position - 1
        else:
            return -1

    def get_position_volume(self):
        f = partial(self.rotate_volume_button, "r")
        return CoffeeMachine.get_position(f, self.volume_captor, 6)

    def get_position_intensite(self):
        f = partial(self.push_button, self.pin_intensity)
        return CoffeeMachine.get_position(f, self.intensity_captor, 5)

    # You should ALWAYS only use one and only one Instance of this class
    def clear_pin(self):
        GPIO.output(self.actuator_pin_list, GPIO.LOW)
        GPIO.cleanup()

    def __del__(self):
        self.__clear_pin()

    def __exit__(self):
        self.__clear_pin()
