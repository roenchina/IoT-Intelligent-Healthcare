from flask import Blueprint

user_bp = Blueprint("user_bp", __name__, url_prefix='/user')


@user_bp.route('/userRegister', methods=["POST"])
def userRegister():
    return 'api: userRegister'


@user_bp.route('/userVerify', methods=["POST"])
def userVerify():
    return 'api: userVerify'

