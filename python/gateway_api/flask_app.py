#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

from flask import jsonify, request,send_file
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
            response= requests.post(RECOGNITIONSERVICE_URL+'/users',json = body).content
        except ConnectionError:
            return "Could not connect to Recognition Service", 421
        return response, 200

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
            response= requests.put(RECOGNITIONSERVICE_URL+'/users/'+str(id),json = body).content
        except ConnectionError:
            return "Could not connect to Recognition Service", 421
        return response, 200

    @app.route('/users/<id>', methods=["DELETE"])
    def delete_user(id):
        try:
            id = int(id)
        except ValueError:
            return "Invalid id", 400
        try:
            response = requests.delete(RECOGNITIONSERVICE_URL+'/users/'+str(id)).content
        except ConnectionError:
            return "Could not connect to Recognition Service", 421
        return response, 200

    @app.route('/coffee', methods=["GET"])
    def make_coffee():
        print(request.values)
        # TO BE IMPLEMENTED
        # ASK COFFE MACHINE TO MAKE COFFE
        raise NotImplementedError()

    # To upload file through flask :
    # enctype : multipart/form-data
    @app.route('/recognition', methods=["POST"])
    def recognize_faceimage():
        if 'image' not in request.files:
            print('No file part')
            return "Bad Request", 400
        file = request.files['image']
        try :
            r = requests.post(RECOGNITIONSERVICE_URL+'/recognition',files = [('image',(file.filename,file))])
        except ConnectionError:
            return "Could not connect to Recognition Service", 421
        return "ok", 200
        # resquests.post(RECOGNITIONSERVICE_URL+'/recognition',data=file)
        # TO BE IMPLEMENTED
        # ASK COFFE MACHINE TO MAKE COFFE
