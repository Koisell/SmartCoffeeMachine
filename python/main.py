#!/usr/bin/env python3
# coding: utf-8
from collections import deque
from GPIO.coffee_machine import CoffeeMachine
from time import sleep


class Command():
    def __init__(self, name, volume, intensity):
        self.name = name
        self.volume = volume
        self.intensity = intensity

    def get_param(self):
        return self.volume, self.intensity


class WaitingCoffee(deque):
    def __init__(self, coffee_machine=CoffeeMachine()):
        super().__init__(maxlen=5)  # No more than 5 coffee in queue
        self.coffee_machine = coffee_machine

    def is_command(self):
        return bool(len(self))

    def make_coffee(self, volume, intensity):
        self.coffee_machine.make_coffee(volume, intensity)
        sleep(20)  # We wait 20 secs before the next coffee


def main():
    waiter = WaitingCoffee()
    while True:
        if waiter.is_command():
            command = waiter.pop()
            waiter.make_coffee(*command.get_param())


if __name__ == '__main__':
    main()
