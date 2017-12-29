#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

import os
from flask import jsonify, request, send_file, Response, stream_with_context
import requests
from requests.exceptions import ConnectionError, Timeout

RECOGNITIONSERVICE_URL = os.environ.get('RECOGNITIONSERVICE_URL', 'http://localhost:5001')
COFFEMACHINE_URL = os.environ.get('COFFEMACHINE_URL', 'http://localhost:4242')


def forward_request(method, route, request):
    try:
        print(request.data)
        response = method(route, params=request.args, data=request.data, headers=request.headers)
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
        return forward_request(requests.get, RECOGNITIONSERVICE_URL + '/users/' + str(id), request)

    @app.route('/users', methods=["POST"])
    def new_user():
        return forward_request(requests.post, RECOGNITIONSERVICE_URL + '/users', request)

    @app.route('/users/<id>', methods=["PUT"])
    def modify_user(id):
        return forward_request(requests.put, RECOGNITIONSERVICE_URL + '/users/' + str(id), request)

    @app.route('/users/<id>', methods=["DELETE"])
    def delete_user(id):
        return forward_request(requests.delete, RECOGNITIONSERVICE_URL + '/users/' + str(id), request)

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
