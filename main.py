# from fastapi import FastAPI, BackgroundTasks
# import asyncio
# from camera import Camera
# import cv2
# from logic import Logic
# from oac import MyOAC
# from pt_model import Model
# from text2speech import SaySomething
# import uvicorn
# import time
# from video import Video
# app = FastAPI()

# # camera
# camera = Camera(0)
# logic = Logic(model=Model())
# DELTA_T_SECS = 0.3

# video = Video()

# async def play_sounds():
#     while True:
#         logic(camera.read()[1])
#         print(logic.tags)
#         await asyncio.sleep(DELTA_T_SECS)

# async def play_video():
#     while True:
#         video.run()
#         print('video played')
#         await asyncio.sleep(0.01)

# # @app.on_event("startup")
# @app.get("/start-video")
# async def start_video(background_tasks: BackgroundTasks):
#     # This will start the video in a background thread
#     background_tasks.add_task(play_video)
#     return {"message": "Video started"}

# @app.get("/start-play-sounds")
# async def start_play_sounds(background_tasks: BackgroundTasks):
#     background_tasks.add_task(play_sounds)
#     return {"message": "Sound task started"}

# @app.on_event("startup")
# async def startup_event():
#     app.get("/start-play-sounds")
#     app.get("/start-video")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)


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
background_tasks = BackgroundTasks()
worker_threads = []
from threading import Thread


import websockets
import asyncio


should_play = False

def play_sounds():
    global should_play
    print('play sounds')
    while True:
        if logic(camera.read()[1]):
            should_play = True
            # play video
            ...
        time.sleep(DELTA_T_SECS)

def play_video():
    print('play video')
    video.run()
    print('video played')
    # await asyncio.sleep(0.01)

# @app.on_event("startup")
def startup_event():
    # Instantiate the background task handler
    print('startup')
    tasks = [play_sounds]
    for fn in tasks:
        th = Thread(target=fn, daemon=True)
        th.start()
        worker_threads.append(th)
        
    
import asyncio
import websockets

async def send_message(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(response)

async def echo(websocket, path):
    global should_play
    # Register the new client
    while True:
        await asyncio.sleep(1/30)  # send a message every second
        if not should_play:
            continue
        
        # Sending the message to all connected clients
        if not websocket.open:
            continue
        try:
            await websocket.send("play it")
            should_play = False
        except:
            print("oops")
            return
def ws_main():
    print()

def run_server():
    server = websockets.serve(echo, "localhost", 8765)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(server)
    loop.run_forever()
    
if __name__ == "__main__":
    startup_event()
    run_server()
    print('done')
    
    # ws_thread=  Thread(target=ws_main, daemon=True)
    # ws_thread.start()
    # ws_thread.join()
    
# @app.get("/start-video")
# async def start_video(background_tasks: BackgroundTasks):
#     # This can still start the video in a background thread manually if needed
#     background_tasks.add_task(play_video)
#     return {"message": "Video started"}

# @app.get("/start-play-sounds")
# async def start_play_sounds(background_tasks: BackgroundTasks):
#     # This can still start the sound in a background thread manually if needed
#     background_tasks.add_task(play_sounds)
#     return {"message": "Sound task started"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
