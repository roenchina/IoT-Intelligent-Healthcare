from flask import Flask, request
import json


app = Flask(__name__)
app.config.from_pyfile("configs.py")


from database.extension import db
from database.models import *
db.init_app(app)
db.create_all(app=app)


from api.charts import charts_bp
from api.data import data_bp
from api.facility import facility_bp
from api.user import user_bp
app.register_blueprint(charts_bp)
app.register_blueprint(data_bp)
app.register_blueprint(facility_bp)
app.register_blueprint(user_bp)


# route
@app.route("/")
def hello_world():
	return "Hello, Flask!"


if __name__ == "__main__":
	app.run(debug=True)