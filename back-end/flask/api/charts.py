from flask import Blueprint, request, jsonify
import json
import random
from database.extension import db
from database.models import User, Facility, Data, Own
from api.format import error_response, bad_request, common_response


charts_bp = Blueprint("charts_bp", __name__, url_prefix='/charts')

NORMAL_ICON = 'https://img.icons8.com/color/36/000000/marker--v1.png'
WARNING_ICON = 'https://img.icons8.com/color/36/000000/error--v1.png'

@charts_bp.route('/getFacPie', methods=["GET"])
def getFacPie():
    data = []
    for sta in ['online', 'offline', 'error']:
        count = Facility.query.filter_by(status=sta).count()
        item = {
            'name': sta,
            'value': count
        }
        data.append(item)
    
    return common_response(data)


@charts_bp.route('/getDataPie', methods=["GET"])
def getDataPie():
    data = []
    for sta in ['normal', 'warning']:
        count = Data.query.filter_by(type=sta).count()
        item = {
            'name': sta,
            'value': count
        }
        data.append(item)
    
    return common_response(data)


@charts_bp.route('/getAllLine', methods=["GET"])
def getAllLine():
    data = []
    for i in range(7):
        item = {
            '2015': random.randint(0, 9),
            '2016': random.randint(0, 9),
            '2017': random.randint(0, 9),
            '2018': random.randint(0, 9),
            'time': '6-2' + str(i)
        }
        data.append((item))
    return common_response(data)


@charts_bp.route('/getAllMarkers', methods=["GET"])
def getAllMarkers():
    data = []
    result = Data.query.order_by(Data.time).all()
    for res in result:
        item = {
            'position': {
                'lat': float(res.location_lat),
                'lng': float(res.location_lng),
            },
            'facID': res.facID,
            'icon': NORMAL_ICON if (res.type == 'normal') else WARNING_ICON,
            'info': 'test info',
            'label': '',
            'zIndex': result.index(res)
        }
        data.append(item)

    return common_response(data)


@charts_bp.route('/getAllPolyline', methods=["GET"])
def getAllPolyline():
    data = []
    allFacID = Facility.query.all()
    for fac in allFacID:
        print(fac.id)
        item = {
            'facID': fac.id,
            'path': [],
            "geodesic": True,
            "strokeColor": "#9D2D23",
            "strokeOpacity": 0.8,
            "strokeWeight": 4,
        }
        for res in fac.alldata:
            print(res.id)
            marker = {
                'lat': float(res.location_lat),
                'lng': float(res.location_lng),
            }
            item['path'].append(marker)
        if(item['path']):
            data.append(item)

    return common_response(data)
