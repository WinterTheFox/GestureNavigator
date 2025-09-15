# Program to stream video using cv2
import cv2

class Camera:
    def __init__(self, cam_index=0):
        self.cap = cv2.VideoCapture(cam_index)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        frame = cv2.flip(frame, 1)              # espejo
        return frame

    def release(self):
        self.cap.release()
