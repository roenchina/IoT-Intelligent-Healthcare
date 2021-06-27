from flask import Blueprint

facility_bp = Blueprint("facility_bp", __name__, url_prefix='/facility')


@facility_bp.route('/getAllFacility', methods=["GET"])
def getAllFacility():
    return 'api: getAllFacility'


@facility_bp.route('/removeFacility', methods=["POST"])
def removeFacility():
    return 'api: removeFacility'


@facility_bp.route('/updateFacility', methods=["POST"])
def updateFacility():
    return 'api: updateFacility'


@facility_bp.route('/addFacility', methods=["POST"])
def addFacility():
    return 'api: addFacility'
