import cv2

class Camera:
    def __init__(self, camera_id=0):
        self.camera = cv2.VideoCapture(camera_id)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.show_vid_flag = False
      
    def read(self):
        return self.camera.read()
    
