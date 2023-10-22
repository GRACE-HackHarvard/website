from flask import Flask, render_template, Response, jsonify, session, request
from flask_socketio import SocketIO, emit
import cv2
from PIL import Image
import base64
from ai import detect_light_capture, calibrate_capture
import time
from io import BytesIO
import numpy as np
import ads_api
import os
from flask_session import Session
from flask_cors import CORS
import redis

app = Flask(__name__)
app.secret_key="anystringhere"


app.config['SECRET_KEY'] = 'grace'
app.secret_key="anystringhere"


app.config.update(SECRET_KEY=os.urandom(24))
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)
app.config['SECRET_KEY'] = 'grace'
app.secret_key="anystringhere"


CORS(app)
app.config['SECRET_KEY'] = 'grace'
app.config['SECRET_KEY'] = 'grace'
app.secret_key="anystringhere"


app.config.update(SECRET_KEY=os.urandom(24))
app.config['SECRET_KEY'] = 'grace'
app.secret_key="anystringhere"



socketio = SocketIO(app, cors_allowed_origins="*", manage_sessions=False)
app.config['SECRET_KEY'] = 'grace'
app.secret_key="anystringhere"
Session().init_app(app)



@socketio.on('calibration')
def calibration_call(data):
    b64data = base64.b64decode(data["data"][23:])
    image = Image.open(BytesIO(b64data))
    suc, vals = calibrate_capture(np.array(image))
    if not suc:
        emit("hold on!", {})
        return
    if "vals_tmp" not in session or session["vals_tmp"] == None:
        session["vals_tmp"] = [[],[],[],[]]#(tuple([tuple()]), tuple([tuple()]), tuple([tuple()]), tuple([tuple()]))
    session["vals_tmp"][data["id"] - 1].append(vals)
    session["vals_tmp"][data["id"] - 1] = session["vals_tmp"][data["id"] - 1].copy()
    session.modified = True


@socketio.on('done_calibration')    
def complete_calibration(data):
    A, B, C, D = session["vals_tmp"]
    session["vals"] = (
    (sum([a[0] for a in A])/len(A), sum([a[1] for a in A])/len(A)),
    (sum([a[0] for a in D])/len(A), sum([a[1] for a in D])/len(A)),
    (sum([a[0] for a in B])/len(A), sum([a[1] for a in B])/len(A))
        )
    B, D, A = session["vals"]
    try:
        np.linalg.inv(np.array((sub(B, A), sub(D, A))))
        emit("leave", {"vals":session["vals"]})
    except: 
        emit("die and cry", {})
        reset_calibration()


@app.route("/_store_session", methods=["POST"])
def store_session():
    session["vals"] = request.json["vals"]
    return "god help me please"

@socketio.on('reset_calibration')
def reset_calibration(data):
    session.remove("vals_tmp")
    session.remove("vals")

@socketio.on('lightcapture')
def calibration_call(data):
    if "vals" not in session or session["vals"] == None:
        try:
            print("Hello world!")
        except Exception as e:
            pass          
        emit("redirect_calibrate", {})
        return


    b64data = base64.b64decode(data["data"][23:])
    image = Image.open(BytesIO(b64data))
    suc, x, y = detect_light_capture(np.array(image))

    if not suc: return

    R, G, B = session["vals"]
    newcoords = convert_coords(sub((x, y), B), (sub(R, B), sub(G, B)))
    emit("lightcoords", {"coords":newcoords})

def sub(A, B):
    return (A[0] - B[0], A[1] - B[1])

def convert_coords(exact, vals):
    if "vals" not in session:
        return None

    # vec_new = np.linalg.inv(np.column_stack((w1, w2, w3))).dot(vec_old)

    return tuple(np.linalg.solve(np.array(vals), np.array(exact)))

@app.route('/')
def index():
    session['x'] = 'y'
    return render_template('index.html')

@app.route('/calibration')
def calibrate():
    session['x'] = 'y'
    return render_template("calibration.html")

@app.route('/map')
def map_route():
    session['x'] = 'y'
    return render_template("map.html")

@app.route('/api/data', methods=['GET'])
def get_data():
    # Your API logic here
    return jsonify(ads_api.get_abstracts_of_query())

@app.route('/api_call', methods=['POST'])
def api_call():
    data = request.get_json()
    search_query = data.get('search_query')
    # Process the user_input and make an API call if needed
    # Replace this with your API call logic
    api_response = f"API response for {search_query}"
    return jsonify({'api_response': api_response})

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', debug=True,port="5002")
