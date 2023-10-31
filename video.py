import cv2
import time

class Video:
    
    def __init__(self):
        self.window_name = "window"
        cv2.namedWindow(self.window_name, cv2.WND_PROP_FULLSCREEN)

    def run(self):
        interframe_wait_ms = 30
        file_name = "zombie.mp4"  # Replace with your video file path

        cap = cv2.VideoCapture(file_name)
        if not cap.isOpened():
            print("Error: Could not open video.")
            exit()

        
        # cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # Read and display frames from the video
        ret, frame = cap.read()
        if ret:
            start_time = time.time()
            while time.time() - start_time < 3:  # Display the first frame for 3 seconds
                cv2.imshow(self.window_name, frame)
                if cv2.waitKey(1) & 0x7F == ord('q'):  # Exit if 'q' is pressed
                    break

            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Reached end of video, exiting.")
                    break

                cv2.imshow(self.window_name, frame)
                if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
                    print("Exit requested.")
                    break

        cap.release()
        cv2.destroyAllWindows()
    