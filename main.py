from flask import Flask, render_template, Response, jsonify
from flask_socketio import SocketIO
import cv2
from ai import detect_light_capture
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('ADS_API_KEY')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'grace'
socketio = SocketIO(app)

thread = None                                                                   

class VideoCamera(object):
    def __init__(self): 
        self.video = cv2.VideoCapture(0)
        self.past = None
        self.pastvel = None

    def __del__(self):
        self.video.release()        

    def get_frame(self):
        ret, frame = self.video.read()
        cur = detect_light_capture(ret, frame)

        past = self.past
        self.past = cur

        if past == None:
            self.pastvel = (0, 0)
            return (0, 0)
        if cur == None:
            return (self.pastvel[0] / 1.5, self.pastvel[1] / 1.5)
        else:
            return (cur[0] - past[0], cur[1] - past[1])


video_stream = VideoCamera()


def background_thread():
    oldval = None                                                   
    while True:                                                                 
        newval = video_stream.get_frame() 
        if newval != oldval:
            oldval = newval
            # print(newval)
            socketio.emit('message', {'velocity': newval})                                        
        time.sleep(0.033)                                                           

@socketio.on('connect')                                                         
def connect():                                                                  
    global thread                                                               
    if thread is None:                                                          
        thread = socketio.start_background_task(target=background_thread)       

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/map') 
def map(): 
	return render_template('map.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_stream), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', debug=True,port="5001")
