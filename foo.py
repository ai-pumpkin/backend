import cv2
import time
window_name = "wind22ow"
# cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN) 
import numpy as np
def main():
    # cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)

    while True:
        frame = np.zeros((128,128))
        print("show?")
        cv2.imshow(window_name, frame)
        cv2.waitKey(0) 
    time.sleep(60)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()