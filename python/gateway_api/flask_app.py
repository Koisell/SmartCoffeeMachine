#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

from flask import jsonify, request

def add_route(app):
    ''' Add routes to a flask app Class. See API swagger doc'''
    @app.route('/users/<id>', methods=['GET'])
    def get_user(id):
        try:
            id = int(id)
        except ValueError:
            return "Invalid id", 400
        print(id)
        # TO BE IMPLEMENTED
        # ASK RECOGNITION SERVICE FOR USER(id)
        raise NotImplementedError()
        if result:
            return jsonify(dict(result.items()))
        else:
            return "User not found", 404

    @app.route('/users', methods=["POST"])
    def new_user():
        body = request.get_json()
        try:
            username, intensity, volume = [body[k] for k in ("username", "intensity", "volume")]
        except KeyError:
            return "Incorrect body", 400
        # TO BE IMPLEMENTED
        # ASK RECOGNITION SERVICE TO CREATE USER
        raise NotImplementedError()

    @app.route('/users/<id>', methods=["PUT"])
    def modify_user(id):
        try:
            id = int(id)
        except ValueError:
            return "Invalid id", 400
        # TO BE IMPLEMENTED
        # ASK RECOGNITION SERVICE TO MODIY USER

        raise NotImplementedError()

    @app.route('/users/<id>', methods=["DELETE"])
    def delete_user(id):
        try:
            id = int(id)
        except ValueError:
            return "Invalid id", 400

        # TO BE IMPLEMENTED
        # ASK RECOGNITION SERVICE TO DELETE USER
        raise NotImplementedError()

    @app.route('/coffee', methods=["GET"])
    def make_coffee():
        print(request.values)
        # TO BE IMPLEMENTED
        # ASK COFFE MACHINE TO MAKE COFFE
        raise NotImplementedError()
