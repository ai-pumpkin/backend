from fastapi import FastAPI
import asyncio
from camera import Camera
import cv2
from logic import Logic
from oac import MyOAC
from pt_model import Model
from text2speech import SaySomething
import uvicorn

app = FastAPI()

# camera
camera = Camera(0)
logic = Logic(model=Model())
DELTA_T_SECS = 0.3


async def show_face():
    while True:
        logic(camera.read()[1])
        while True:
            # video player
            file_name = "zombie.mp4"
            window_name = "window"
            interframe_wait_ms = 30

            cap = cv2.VideoCapture(file_name)
            cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(
                window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
            )
            ret, frame = cap.read()
            if not ret:
                print("Reached end of video, exiting.")
                break

        cv2.imshow(window_name, frame)
        if cv2.waitKey(interframe_wait_ms) & 0x7F == ord("q"):
            print("Exit requested.")
            break

        cap.release()
        cv2.destroyAllWindows()
        await asyncio.sleep(DELTA_T_SECS)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(show_face())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
