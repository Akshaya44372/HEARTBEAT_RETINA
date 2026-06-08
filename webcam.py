import cv2
import numpy as np
import time

class Webcam(object):
    def __init__(self):
        #print("WebcamEngine.Init")
        self.dirname = "" #for nothing, just to make 2 inputs the same
        self.cap = None
        self.valid = False
        
    def start(self):
        print("[INFO] Start webcam")
        time.sleep(1) # wait for camera to be ready
        self.cap = cv2.VideoCapture(0)
        self.valid = True
        
    def get_frame(self):
        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return frame
        return None
        
    def stop(self):
        if self.cap is not None:
            self.cap.release()
            self.valid = False
