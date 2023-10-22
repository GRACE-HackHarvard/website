from flask import Flask, render_template, Response, jsonify, session
from flask_socketio import SocketIO, emit
import cv2
from PIL import Image
import base64
from ai import detect_light_capture, calibrate_capture
import time
from io import BytesIO
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('ADS_API_KEY')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'grace'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('calibration')
def calibration_call(data):
    b64data = base64.b64decode(data["data"][23:])
    image = Image.open(BytesIO(b64data))
    suc, vals = calibrate_capture(np.array(image))
    print(suc, vals)
    if not suc: return
    R, G, B = vals
    session["vals"] = (B, G, R)

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


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', debug=True,port="5002")
