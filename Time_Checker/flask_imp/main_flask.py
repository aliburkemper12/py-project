# import time_check_flask
from flask import Flask, jsonify, render_template

app = Flask(__name__)
    
app.route("/")
def index():
    return render_template("index.html")

# def generate():
#     result = {}
#     result = 'hi'
#     return jsonify(result)

if __name__ == "__main__":
    app.run()