# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="DevOps API REST")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


@app.route('/')
def devops():
    return jsonify(message="DevOps API REST")