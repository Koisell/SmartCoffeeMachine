#!/usr/bin/env python3
# coding: utf-8
from collections import deque
from GPIO.coffee_machine import CoffeeMachine
from time import sleep
from threading import Thread
from socket import socket


class Command():
    def __init__(self, volume, intensity):
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

    def make_coffees(self):
        while True:
            if self.is_command():
                command = self.pop()
                self.make_coffee(*command.get_param())


class ThreadedServer():
    def __init__(self, host, port, waiter):
        self.waiter = waiter
        self.host = host
        self.port = port
        self.sock = socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)  # Max 5 clients. We only need 2 (webserver and recog interface) + debug
        Thread(target=self.waiter.make_coffees)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            Thread(target=self.coffee_commands, args=(client, address)).start()

    def coffee_commands(self, client, address):
        size = 1024  # Max lengh in bytes
        while True:
            try:
                data = client.recv(size)
                if data:
                    msg = data.decode("utf-8")
                    if msg[0] == "C":
                        volume, intensity = data[2:].split(",")
                        self.waiter.appendleft(Command(volume, intensity))
                        response = "OK"
                    elif msg == "N":
                        while not self.waiter.coffee_machine.is_new_cup():
                            sleep(1)
                        volume = self.waiter.coffee_machine.get_position_volume()
                        intensity = self.waiter.coffee_machine.get_position_intensity()
                        response = "{},{}".format(volume, intensity)

                    response = response.encode("utf-8")  # reponse is bytes
                    client.send(response)
                else:
                    raise Exception('Client disconnected')
            except Exception:
                client.close()
                return False


def main():
    raise NotImplementedError()


if __name__ == '__main__':
    main()
