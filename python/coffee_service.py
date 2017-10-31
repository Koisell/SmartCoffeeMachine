#!/usr/bin/env python3
# coding: utf-8
from os import getenv
from socket import gethostname
from collections import deque
from time import sleep
from threading import Thread, Condition
from flask import Flask, request
from GPIO.coffee_machine import CoffeeMachine


class Command():
    def __init__(self, volume, intensity):
        self.volume = volume
        self.intensity = intensity

    def get_param(self):
        return self.volume, self.intensity

    def __str__(self):
        return "Command(%s,%s)" % self.get_param()


class CoffeeWaiter(Thread):
    def __init__(self, condition, coffee_machine=CoffeeMachine()):
        Thread.__init__(self)
        self.commands = deque(maxlen=5)  # No more than 5 coffee in queue
        self.coffee_machine = coffee_machine
        self.condition = condition

    def is_command(self):
        return bool(len(self.commands))

    def make_coffee(self, volume, intensity):
        print("make coffee")
        self.coffee_machine.make_coffee(volume, intensity)
        sleep(20)  # We wait 20 secs before the next coffee

    def run(self):
        print("Waiting for coffees")
        while True:
            self.condition.acquire()
            while True:
                if self.is_command():
                    command = self.commands.pop()
                    print("new command:", command)
                    self.coffee_machine.make_coffee(*command.get_param())
                    sleep(20)  # Waiting 20 s to get the coffee done.
                    break
                self.condition.wait()
            self.condition.release()


def main():
    app = Flask(__name__)
    condition = Condition()  # Used to notify CoffeeWaiter thread to wake up and process coffee.
    coffee_waiter = CoffeeWaiter(condition)
    coffee_waiter.start()

    @app.route('/coffee', methods=["GET"])
    def make_coffee():
        try:
            volume, intensity = map(int, [request.args[v] for v in ("volume", "intensity")])
        except (KeyError, ValueError):
            return "Incorect body", 400

        if volume < 0 or intensity < 0 or volume > 4 or intensity > 3:
            return "Incorect body", 400

        condition.acquire()
        coffee_waiter.commands.appendleft(Command(volume, intensity))
        condition.notify()
        condition.release()
        return "Your coffee just condition you :)", 200

    port = getenv('PORT', '4242')

    app.run(host=gethostname(), port=int(port))


if __name__ == '__main__':
    main()
