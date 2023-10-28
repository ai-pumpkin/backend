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

camera = Camera(0)
logic = Logic(model=Model())
DELTA_T_SECS = 0.3

async def show_face():
    while True:
        logic(camera.read()[1])
        await asyncio.sleep(DELTA_T_SECS)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(show_face())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
