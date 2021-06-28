from flask import jsonify, make_response
from werkzeug.http import HTTP_STATUS_CODES
from database.extension import db


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    return error_response(400, message)


def common_response(data):
    json_data = jsonify({
        'data': data,
    })
    response = make_response(json_data)
    response.sattus = '200'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'content-type'
    return response
