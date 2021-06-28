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
    facCnt = Facility.query.count()
    dataCnt = Data.query.count()
    patCnt = User.query.filter_by(role='patient').count()
    wardCnt = db.session.query(Facility.wardID).distinct().count()

    for i in range(7):
        item = {
            '0': random.randint(5, 12),
            '1': random.randint(3*i, 3*i+3),
            '2': random.randint(1, 3),
            '3': random.randint(3, 5),
            'time': '6-2' + str(i)
        }
        data.append(item)

    item = {
        '0': facCnt,
        '1': dataCnt,
        '2': patCnt,
        '3': wardCnt,
        'time': '6-2' + str(7)
    }
    data.append(item)
    return common_response(data)


@charts_bp.route('/getAllMarkers', methods=["GET"])
def getAllMarkers():
    data = []
    result = Data.query.order_by(Data.time).all()
    for res in result:
        info = "设备号:" + res.facID + "; 数据ID:" + res.id + "; 时间:" + res.time.strftime(
            "%Y-%m-%d %H:%M:%S") + "; 数值:" + str(res.amount)
        item = {
            'position': {
                'lat': float(res.location_lat),
                'lng': float(res.location_lng),
            },
            'facID': res.facID,
            'icon': NORMAL_ICON if (res.type == 'normal') else WARNING_ICON,
            'info': info,
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
        # print(fac.id)
        item = {
            'facID': fac.id,
            'path': [],
            "geodesic": True,
            "strokeColor": "#9D2D23",
            "strokeOpacity": 0.8,
            "strokeWeight": 4,
        }
        for res in fac.alldata:
            # print(res.id)
            marker = {
                'lng': float(res.location_lng),
                'lat': float(res.location_lat),
            }
            item['path'].append(marker)
        if(item['path']):
            data.append(item)

    return common_response(data)
