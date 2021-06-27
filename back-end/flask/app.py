from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy

import json


app = Flask(__name__)
app.config.from_pyfile("configs.py")


# import blueprint
from api.charts import charts_bp
from api.data import data_bp
from api.facility import facility_bp
from api.user import user_bp
app.register_blueprint(charts_bp)
app.register_blueprint(data_bp)
app.register_blueprint(facility_bp)
app.register_blueprint(user_bp)


# dbtest
# db = SQLAlchemy(app)

from extension import db
from models import *
db.init_app(app)
db.create_all(app=app)

# Model
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     money = db.Column(db.Integer)
#     def __init__(self, name, thrust):
#         self.name = name
#         self.thrust = thrust
#     def __repr__(self):
#         return '<User %r>' % self.name
#     def __str__(self):
#         return '<User %s>' % self.name



# route
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