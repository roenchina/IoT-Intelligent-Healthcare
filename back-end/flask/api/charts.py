'''
0. 
1. 初始化charts蓝图
2. 使用charts蓝图注册路由url
    @charts_blu.route('/charts/getDataPie')
    def getDataPie():
        pass

'''
from flask import Blueprint

charts_bp = Blueprint("charts_bp", __name__, url_prefix='/charts')


@charts_bp.route('/getFacPie', methods=["GET"])
def getFacPie():
    return 'api: getFacPie'


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
