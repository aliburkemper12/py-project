import time_check_flask
from flask import Flask, render_template, request, jsonify
# from waitress import serve
# fake data

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
        
        #curr_time = get_time() and change the header in return.html
        
        return render_template("return.html", shiftname=convert_name, shift_info=time_data, curr_time=get_time, percentage=percentage)
    return render_template("index.html", error="")
    
@app.route('/displays')
def displays():
    total_data = generate("1")
        
    time_data_1 = total_data[0]
    percentage_1 = total_data[1]
    
    total_data = generate("2")
        
    time_data_2 = total_data[0]
    percentage_2 = total_data[1]
    
    total_data = generate("3")
        
    time_data_3 = total_data[0]
    percentage_3 = total_data[1]
        
    get_time = time_check_flask.get_time()
        
    return render_template("displays.html", shift_info_1=time_data_1, curr_time=get_time, percentage_1=percentage_1,
            shift_info_2=time_data_2, percentage_2=percentage_2, shift_info_3=time_data_3, percentage_3=percentage_3)

def generate(send_data):
    result = {}
    result = time_check_flask.do_time_check(send_data)
    return result

@app.route('/ajax_displays')
def ajax_request():
    total_data = generate("1")
        
    time_data_1 = total_data[0]
    percentage_1 = total_data[1]
    
    total_data = generate("2")
        
    time_data_2 = total_data[0]
    percentage_2 = total_data[1]
    
    total_data = generate("3")
        
    time_data_3 = total_data[0]
    percentage_3 = total_data[1]
        
    get_time = time_check_flask.get_time()
    return jsonify( shift_info_1=time_data_1, curr_time=get_time, percentage_1=percentage_1,
            shift_info_2=time_data_2, percentage_2=percentage_2, shift_info_3=time_data_3, percentage_3=percentage_3)

@app.route('/ajax_return')
def ajax_return():
    send_data = request.form.get("fname")
    convert_name = time_check_flask.get_shift_name(send_data)
        
    total_data = generate(send_data)
        
    time_data = total_data[0]
    percentage = total_data[1]
        
    get_time = time_check_flask.get_time()
    
    return jsonify(shiftname=convert_name, shift_info=time_data, curr_time=get_time, percentage=percentage)

if __name__ == "__main__":
    app.run(port = 5000)