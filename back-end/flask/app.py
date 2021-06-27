from flask import Flask, request
import json

# import blueprint
from api.charts import charts_bp
from api.data import data_bp
from api.facility import facility_bp
from api.user import user_bp


'''
1. 从api中import蓝图 xxx_blu
2. 定义app后，把蓝图注册到app上
	app.register_blueprint(xxx_blu)
'''

app = Flask(__name__)

app.register_blueprint(charts_bp)
app.register_blueprint(data_bp)
app.register_blueprint(facility_bp)
app.register_blueprint(user_bp)


@app.route("/testapi", methods=["POST"])
def check():
	return_dict = {
		'statusCode': '200', 
		'message': 'successful!', 
		'data': False
	}

	if request.get_data() is None:
		return_dict['statusCode'] = '5004'
		return_dict['message'] = '请求为空'
		return json.dumps(return_dict, ensure_ascii=False)

	get_data = json.loads(request.get_data())

	name = get_data.get('name')
	age = get_data.get('age')

	return_dict['data'] = "%s今年%s岁" % (name, age)
	return json.dumps(return_dict, ensure_ascii=False)


if __name__ == "__main__":
	app.run(debug=True)