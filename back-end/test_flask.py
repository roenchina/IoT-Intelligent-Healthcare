from flask import Flask, request 
import json

app = Flask(__name__)


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