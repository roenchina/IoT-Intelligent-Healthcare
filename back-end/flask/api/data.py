from flask import Blueprint, request
from datetime import datetime

from database.models import User, Facility, Data, Own
from api.format import error_response, bad_request, common_response
from database.extension import db

data_bp = Blueprint("data_bp", __name__, url_prefix='/data')

@data_bp.route('getBasicStatic', methods=["GET"])
def getBasicStatic():
    facCnt = Facility.query.count()
    dataCnt = Data.query.count()
    patCnt = User.query.filter_by(role='patient').count()
    wardCnt = db.session.query(Facility.wardID).distinct().count()
    data = {
        'facNum': facCnt,
        'dataNum': dataCnt,
        'patientNum': patCnt,
        'wardNum': wardCnt
    }
    return common_response(data)


@data_bp.route('getAllData', methods=["POST"])
def getAllData():
    data = []
    request_json = request.get_json()
    limit = 200
    sort = ""
    if( 'limit' in request_json.keys()):
        limit = request_json['limit']
    if( 'sort' in request_json.keys()):
        sort = request_json['sort']

    result = Data.query.order_by(Data.time.desc()).limit(limit) if sort=="recent" else Data.query.limit(limit)
    for res in result:
        fac = Facility.query.get(res.facID)
        item = {
            '_ID': res.id,
            # 'time': res.time,
            # 'time': datetime.strptime(str(res.time), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S"),
            'time': res.time.strftime("%Y-%m-%d %H:%M:%S"),
            'facID': res.facID,
            'location': "(" + str(res.location_lat) + ", " + str(res.location_lng) + ")",
            'location_lat': float(res.location_lat),
            'location_lng': float(res.location_lng),
            'type': res.type,
            'amount': float(res.amount),
            'unit': fac.unit if fac else "",
            'facType': fac.type if fac else ""
        }
        data.append(item)
    
    return common_response(data)


@data_bp.route('deleteData', methods=["DELETE"])
def deleteData():
    data = {}
    request_json = request.get_json()
    if ("_ID" not in request_json.keys()):
        # 用户没有提供ID
        data = {
            'ifTrue': False,
            'message': '_ID undefined'
        }
    else:
        target_id = request_json['_ID']
        target = Data.query.get(target_id)
        if (target):
            # 删除
            db.session.delete(target)
            db.session.commit()
            data = {
                'ifTrue': True,
                'message': 'delete success'
            }
        else:
            # 不存在
            data = {
                'ifTrue': False,
                'message': '_ID not exists'
            }

    return common_response(data)
