import time_check_flask
from flask import Flask, render_template, request
# from waitress import serve

app = Flask(__name__)

convert_name = 0
    
#need to get what shift to display, then call do_time_check(shift)
#return a string to be put into the html index
@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        
        send_data = request.form.get("fname")
        convert_name = time_check_flask.get_shift_name(send_data)
        
        if convert_name == -1:
            return render_template("index.html", error="Invalid input")
        
        total_data = generate(send_data)
        
        time_data = total_data[0]
        percentage = total_data[1]
        
        get_time = time_check_flask.get_time()
        
        return render_template("return.html", shiftname=convert_name, shift_info=time_data, curr_time=get_time, percentage=percentage)
    return render_template("index.html", error="")

def generate(send_data):
    result = {}
    result = time_check_flask.do_time_check(send_data)
    return result

if __name__ == "__main__":
    app.run(port = 5000)
    # serve(app, host='0.0.0.0', port=5000)