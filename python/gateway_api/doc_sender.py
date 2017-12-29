#!/usr/bin/env python3
# coding: utf-8

from flask import send_from_directory


def add_doc(app, path_to_doc):
    @app.route("/doc/coffee_machine")
    def send_coffee_machine_doc():
        return send_from_directory(path_to_doc, "CoffeeService.yaml", as_attachment=True)

    @app.route("/doc/gateway")
    def send_gateway_doc():
        return send_from_directory(path_to_doc, "Gateway.yaml", as_attachment=True)

    @app.route("/doc/recognition")
    def send_recognition_doc():
        return send_from_directory(path_to_doc, "Recognition.yaml", as_attachment=True)

    @app.route("/help")
    def send_help():
        return send_from_directory(path_to_doc, "Gateway.yaml", as_attachment=True)
