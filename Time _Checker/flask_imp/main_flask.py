import time_check_flask
from flask import Flask, jsonify

app = Flask(__name__)
    
app.route('/', methods=['GET'])
def generate():
    result = {}
    result = 'hi'
    return jsonify(result)

if __name__ == "__main__":
    app.run()