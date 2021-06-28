from flask import Blueprint, request
import random

from database.models import User, Facility, Data, Own
from api.format import error_response, bad_request, common_response
from database.extension import db

facility_bp = Blueprint("facility_bp", __name__, url_prefix='/facility')

NULL_NAME = '_null'


@facility_bp.route('/getAllFacility', methods=["GET"])
def getAllFacility():
    data = []
    result = Facility.query.filter(Facility.name!=NULL_NAME).all()
    for res in result:
        item = {
            'facID': res.id,
            'name': res.name,
            'type': res.type,
            'status': res.status,
            'unit': res.unit,
            'step': float(res.step),
            'wardID': res.wardID,
            'bedID': res.bedID
        }
        data.append(item)

    return common_response(data)


@facility_bp.route('/removeFacility', methods=["POST"])
def removeFacility():
    data = {}
    request_json = request.get_json()
    if ("facID" not in request_json.keys()):
        data = {
            'ifTrue': False,
            'message': 'facID undefined'
        }
    else:
        target_id = request_json['facID']
        target = Facility.query.get(target_id)
        if (target):
            target.name = NULL_NAME
            db.session.commit()
            data = {
                'ifTrue': True,
                'message': 'remove success'
            }
        else:
            data = {
                'ifTrue': False,
                'message': 'facID not exists'
            }

    return common_response(data)


@facility_bp.route('/updateFacility', methods=["POST"])
def updateFacility():
    data = {}
    request_json = request.get_json()
    if ("facID" not in request_json.keys()):
        data = {
            'ifTrue': False,
            'message': 'facID undefined'
        }
    else:
        target_id = request_json['facID']
        target = Facility.query.get(target_id)
        if (target):
            if ('name' in request_json.keys()):
                target.name = request_json['name']
            if ('type' in request_json.keys()):
                if (request_json['type'] in ['temp', 'humi', 'bodyt', 'rate']):
                    target.type = request_json['type']
            if ('status' in request_json.keys()):
                if (request_json['status'] in ['online', 'offline', 'error']):
                    target.status = request_json['status']
            if ('unit' in request_json.keys()):
                target.unit = request_json['unit']
            if ('step' in request_json.keys()):
                target.step = request_json['step']
            if ('wardID' in request_json.keys()):
                target.wardID = request_json['wardID']
            if ('bedID' in request_json.keys()):
                target.bedID = request_json['bedID']
            db.session.commit()
            data = {
                'ifTrue': True,
                'message': 'update success'
            }
        else:
            data = {
                'ifTrue': False,
                'message': 'facID not exists'
            }

    return common_response(data)


@facility_bp.route('/addFacility', methods=["POST"])
def addFacility():
    data = {}
    request_json = request.get_json()
    if ('name' not in request_json.keys()
            or 'type' not in request_json.keys()
            or 'status' not in request_json.keys()
            or 'unit' not in request_json.keys()
            or 'step' not in request_json.keys()
            or 'wardID' not in request_json.keys()
            or 'bedID' not in request_json.keys()
            ):
        data = {
            'ifTrue': False,
            'message': 'info not enough'
        }
    else:
        test_exist = True
        while (test_exist):
            newid = str(random.randint(10000, 99999))
            test_exist = Facility.query.get(newid)

        newtype = request_json['type'] if request_json['type'] in ['temp', 'humi', 'bodyt', 'rate'] else 'temp'
        newstatus = request_json['status'] if request_json['status'] in ['online', 'offline', 'error'] else 'online'
        newfacility = Facility(id=newid,
                               name=request_json['name'],
                               type=newtype,
                               status=newstatus,
                               unit=request_json['unit'],
                               step=request_json['step'],
                               wardID=request_json['wardID'],
                               bedID=request_json['bedID']
                               )
        db.session.add(newfacility)
        db.session.commit()
        data = {
            'ifTrue': True,
            'info': {
                'facID': newid
            },
            'message': 'add success'
        }

    return common_response(data)
