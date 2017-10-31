from os import getenv
from socket import gethostname
from flask import Flask
from recognitionService_api import add_route


def main():
    app = Flask(__name__)
    add_route(app)

    port = getenv('PORT', '5000')
    app.run(host=gethostname(), port=int(port))


if __name__ == '__main__':
    main()
