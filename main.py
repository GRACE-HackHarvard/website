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

app = Flask(__name__)

app.config['SECRET_KEY'] = 'grace'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('calibration')
def calibration_call(data):
    b64data = base64.b64decode(data["data"][23:])
    image = Image.open(BytesIO(b64data))
    suc, vals = calibrate_capture(np.array(image))
    print(suc, vals)
    if not suc:
        print("hold on!")
        emit("hold on!", {})
        return
    if "vals" not in session:
        session["vals_tmp"] = [[],[],[],[]]
    session["vals_tmp"][data["id"]].append((B, G, R))

@socketio.on('done_calibration')
def complete_calibration(data):
    A, B, C, D = session["vals_tmp"]
    session["vals"] = (
    (sum([a[0] for a in A])/len(A), sum([a[1] for a in A])/len(A)),
    (sum([a[0] for a in D])/len(A), sum([a[1] for a in D])/len(A)),
    (sum([a[0] for a in B])/len(A), sum([a[1] for a in B])/len(A))
        )

@socketio.on('reset_calibration')
def complete_calibration(data):
    session.remove("vals_tmp")
    session.remove("vals")

@socketio.on('lightcapture')
def calibration_call(data):

    if "vals" not in session:
        emit("redirect_calibrate", {})
        return


    b64data = base64.b64decode(data["data"][23:])
    image = Image.open(BytesIO(b64data))
    suc, x, y = detect_light_capture(np.array(image))

    if not suc: return

    print(session)
    print(session["vals"])

    R, G, B = session["vals"]
    newcoords = convert_coords((x, y), (sub(R, B), sub(G, B)))
    emit("lightcoords", {"coords":newcoords})

def sub(A, B):
    return (A[0] - B[0], A[1] - B[1])

def convert_coords(exact, vals):
    if "vals" not in session:
        return None

    # vec_new = np.linalg.inv(np.column_stack((w1, w2, w3))).dot(vec_old)

    return np.linalg.solve(mp.array(vals), np.array(exact)) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calibration')
def calibrate():
     return render_template("calibration.html")

@app.route('/map')
def map_route():
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
