from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
	return jsonify(message='Hello from Quickr')


if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=5000)