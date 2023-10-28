from fastapi import FastAPI, BackgroundTasks
import asyncio
from camera import Camera
import cv2
from logic import Logic
from oac import MyOAC
from pt_model import Model
from text2speech import SaySomething
import uvicorn
import time
from video import Video
app = FastAPI()

# camera
camera = Camera(0)
logic = Logic(model=Model())
DELTA_T_SECS = 0.3

video = Video()

async def play_sounds():
    while True:
        logic(camera.read()[1])
        await asyncio.sleep(DELTA_T_SECS)

async def play_video():
    while True:
        video.run()
        await asyncio.sleep(0.01)

@app.on_event("startup")
# @app.get("/start-video")
async def start_video(background_tasks: BackgroundTasks):
    # This will start the video in a background thread
    background_tasks.add_task(play_video)
    return {"message": "Video started"}

@app.on_event("startup")
# @app.get("/start-other-task")
async def start_play_sounds(background_tasks: BackgroundTasks):
    background_tasks.add_task(play_sounds)
    return {"message": "Sound task started"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
