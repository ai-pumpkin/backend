import cv2

class Camera:
    def __init__(self, camera_id=0):
        self.camera = cv2.VideoCapture(camera_id)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.show_vid_flag = False
        
    def get_camera_id(self):
        return self.camera_id
    
    def read(self):
        return self.camera.read()
    
    def show_img(self, t=1000):
        cv2.imshow("Face", self.camera.read()[1])
        # cv2.waitKey(t)

    def show_vid(self):
        self.show_vid_flag = True
        while self.show_vid_flag:
            cv2.imshow("Face", self.camera.read()[1])
        cv2.destroyAllWindows()

    def stop_vid(self):
        self.show_vid_flag = False

    def __del__(self):
        self.camera.release()
        cv2.destroyAllWindows()
