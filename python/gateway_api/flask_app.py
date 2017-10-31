#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

from flask import jsonify, request
import requests

RECOGNITIONSERVICE_URL = 'http://localhost:5001'
COFFEMACHINE_URL = 'http://localhost:4242'

def add_route(app):
    ''' Add routes to a flask app Class. See API swagger doc'''
    @app.route('/users/<id>', methods=['GET'])
    def get_user(id):
        try:
            id = int(id)
        except ValueError:
            return "Invalid id", 400
        print(id)

        try:
            # Do request on  RECOGNITION SERVICE USER(id)
            user = requests.get(RECOGNITIONSERVICE_URL+'/users/'+str(id)).content
        except ConnectionError:
            return "Could not connect to Recognition Service", 421
        return user, 200

    @app.route('/users', methods=["POST"])
    def new_user():
        body = request.get_json()
        try:
            username, intensity, volume = [body[k] for k in ("username", "intensity", "volume")]
        except KeyError:
            return "Incorrect body", 400

        try:
            r= requests.post(RECOGNITIONSERVICE_URL+'/users',json = body).content
        except ConnectionError:
            return "Could not connect to Recognition Service", 421
        return r, 200



    @app.route('/users/<id>', methods=["PUT"])
    def modify_user(id):
        try:
            id = int(id)
        except ValueError:
            return "Invalid id", 400
        body = request.get_json()
        try:
            username, intensity, volume = [body[k] for k in ("username", "intensity", "volume")]
        except KeyError:
            return "Incorrect body", 400

        try:
            r= requests.put(RECOGNITIONSERVICE_URL+'/users/'+str(id),json = body).content
        except ConnectionError:
            return "Could not connect to Recognition Service", 421
        return r, 200

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
