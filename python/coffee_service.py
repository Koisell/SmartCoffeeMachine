#!/usr/bin/env python3
# coding: utf-8
from os import getenv
from socket import gethostname
from collections import deque
from time import sleep
from threading import Thread, Condition
from flask import Flask, request
from GPIO.coffee_machine import CoffeeMachine

def main():
    app = Flask(__name__)
    coffee_machine=CoffeeMachine()

    @app.route('/coffee', methods=["GET"])
    def make_coffee():
        try:
            volume, intensity = map(int, [request.args[v] for v in ("volume", "intensity")])
        except KeyError:
            return "Incorect query: missing parameters", 400
        except ValueError:
            return "Incorect query: invalid parameter type, must be positiv integer", 400

        if volume < 0 or intensity < 0 or volume > 4 or intensity > 5:
            return "Incorect query: parameters must be in ranges given in doc", 400
        coffee_machine.make_coffee(volume, intensity)
        return "Your coffee just condition you :)", 200
    port = getenv('PORT', '4242')
    app.run("0.0.0.0", port=int(port))


if __name__ == '__main__':
    main()
