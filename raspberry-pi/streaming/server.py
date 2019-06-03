from flask import Flask, Response
from camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
    while True:
        return video_feed()

def gen(camera):
    video_stream = camera.get_frame()
    while True:
        frame = next(video_stream)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)