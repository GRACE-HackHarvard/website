from flask import Flask, render_template, Response, jsonify
from flask_socketio import SocketIO
import cv2

app = Flask(__name__)

app.config['SECRET_KEY'] = 'grace'
socketio = SocketIO(app)

class VideoCamera(object):
    def __init__(self): 
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()        

    def get_frame(self):
        ret, frame = self.video.read()

        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV

        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()



video_stream = VideoCamera()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/_get_camera_data")
def get_camera():
    camera_data = camera.get_frame()
    return camera_data

def gen(camera):
    while True:
        camera_data = camera.get_frame()
        yield camera_data

@app.route('/video_feed')
def video_feed():
     return Response(gen(video_stream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', debug=True,port="5000")
