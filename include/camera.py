import cv2

class AnyCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture('http://wmccpinetop.axiscam.net/mjpg/video.mjpg')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()