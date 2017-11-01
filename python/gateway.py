#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

from os import getenv
from socket import gethostname
from flask import Flask
from flask_cors import CORS
from gateway_api import add_route, add_doc

PATH_TO_DOC = "../doc"


def main():
    app = Flask(__name__)
    CORS(app)
    add_route(app)
    add_doc(app, PATH_TO_DOC)

    port = getenv('PORT', '5000')
    app.run(host=gethostname(), port=int(port))


if __name__ == '__main__':
    main()
