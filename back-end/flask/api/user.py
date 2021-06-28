from flask import Blueprint, request
from database.models import User, Facility, Data, Own
from api.format import error_response, bad_request, common_response
from database.extension import db

user_bp = Blueprint("user_bp", __name__, url_prefix='/user')


@user_bp.route('/userRegister', methods=["POST"])
def userRegister():
    data = {}
    request_json = request.get_json()
    res = User.query.get(request_json['userID'])
    if(res):
        data = {
            'ifTrue': False,
            'message': 'userID already exists'
        }
    else:
        newuser = User(id=request_json['userID'],
                       name=request_json['name'],
                       email=request_json['email'],
                       passwd=request_json['passwd'],
                       role=request_json['role'])
        db.session.add(newuser)
        db.session.commit()
        data = {
            'ifTrue': True,
            'message': 'add newuser success'
        }
    return common_response(data)


@user_bp.route('/userVerify', methods=["POST"])
def userVerify():
    data = {}
    request_json = request.get_json()
    # print(request_json)
    res = User.query.get(request_json['userID'])
    if (res):
        if (res.passwd == request_json['passwd']):
            data = {
                'ifTrue': True,
                'userInfo': {
                    'name': res.name,
                    'email': res.email,
                    'role': res.role
                },
                'message': 'success'
            }
        else:
            data = {
                'ifTrue': False,
                'message': 'wrong passwd'
            }
    else:
        data = {
            'ifTrue': False,
            'message': 'userID not exists'
        }

    return common_response(data)
