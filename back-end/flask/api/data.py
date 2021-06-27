from flask import Blueprint

data_bp = Blueprint("data_bp", __name__, url_prefix='/data')

@data_bp.route('getBasicStatic', methods=["GET"])
def getBasicStatic():
    return 'api: getBasicStatic'


@data_bp.route('getAllData', methods=["POST"])
def getAllData():
    return 'api: getAllData'


@data_bp.route('deleteData', methods=["DELETE"])
def deleteData():
    return 'api: deleteData'
