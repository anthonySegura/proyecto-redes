from time import time
import numpy as np
import cv2

class Camera():
    def get_frame(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            yield cv2.imencode('.jpg', frame)[1].tobytes()