import time_check_flask
from flask import Flask, jsonify

app = Flask(__name__)

# def get_shift():
#     print('What shift do you want to see?\nType:\n')
#     print('1 - for first\n2 - for second\n3 - for third\n')
#     return input()

# def main():
#     print()
#     time_check_flask.do_time_check(shift)

# if __name__ == "__main__":
#     shift = get_shift()
#     main()
    
app.route('/', methods=['GET'])
def generate():
    result = {}
    result
    return "<p>Blah</p>"

if __name__ == "__main__":
    app.run("localhost", port = 5000)