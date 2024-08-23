from flask import Flask, jsonify

from flask_cors import CORS
import os



app = Flask(__name__)
CORS(app)



@app.route('/')
def hello():
    try:
        with open('/hello/hello.txt', 'r') as file:
           content = file.read()
        return jsonify(content)
    except Exception as e:
        return jsonify("Hello world")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)