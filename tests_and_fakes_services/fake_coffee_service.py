#!/usr/bin/env python3
# coding: utf-8
from os import getenv
from flask import Flask


def main():
    app = Flask(__name__)

    @app.route('/coffee', methods=["GET"])
    def make_coffee():
        return "Your coffee just waiting you :)", 200

    port = getenv('PORT', '4242')

    app.run(host="localhost", port=int(port))


if __name__ == '__main__':
    main()
