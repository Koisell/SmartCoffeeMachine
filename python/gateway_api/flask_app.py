#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

from flask import jsonify, request,send_file, Response, stream_with_context
import requests
from requests.exceptions import ConnectionError, Timeout

RECOGNITIONSERVICE_URL = 'http://localhost:5001'
COFFEMACHINE_URL = 'http://localhost:4242'


def forward_request(method, route, request):
    try:
        response = method(route, params=request.args)
    except ConnectionError:
        return "Service unevailable", 503
    except Timeout:
        return "Gateway timeout", 504

    if response.status_code >= 500:
        return "Bad gateway", 501

    return Response(response.text, status=response.status_code, content_type=response.headers['content-type'])


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
        return forward_request(requests.get, COFFEMACHINE_URL + '/coffee', request)

    # To upload file through flask :
    # enctype : multipart/form-data
    @app.route('/recognition', methods=["POST"])
    def recognize_faceimage():
        if 'image' not in request.files:
            print('No file part')
            return "Bad Request", 400
        file = request.files['image']
        try :
            requests.post(RECOGNITIONSERVICE_URL+'/recognition',files = [('image',(file.filename,file))])
        except ConnectionError:
            return "Could not connect to Recognition Service", 421
        return "ok", 200
        # resquests.post(RECOGNITIONSERVICE_URL+'/recognition',data=file)
        # TO BE IMPLEMENTED
        # ASK COFFE MACHINE TO MAKE COFFE
