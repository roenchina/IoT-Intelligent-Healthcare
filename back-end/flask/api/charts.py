from flask import Blueprint, request, jsonify
from database.extension import db
from database.models import User, Facility, Data, Own
from api.format import error_response, bad_request, common_response


charts_bp = Blueprint("charts_bp", __name__, url_prefix='/charts')


@charts_bp.route('/getFacPie', methods=["GET"])
def getFacPie():
    return_data = []
    for type in ['online', 'offline', 'error']:
        count = Facility.query.filter_by(status=type).count()
        item = {
            'name': type,
            'value': count
        }
        return_data.append(item)
    
    return common_response(return_data)


@charts_bp.route('/getDataPie', methods=["GET"])
def getDataPie():
    return 'api: getDataPie'


@charts_bp.route('/getAllLine', methods=["GET"])
def getAllLine():
    return 'api: getAllLine'


@charts_bp.route('/getAllMarkers', methods=["GET"])
def getAllMarkers():
    return 'api: getAllMarkers'


@charts_bp.route('/getAllPolyline', methods=["GET"])
def getAllPolyline():
    return 'api: getAllPolyline'
