from fastapi import FastAPI
import asyncio

app = FastAPI()

async def my_task():
    while True:
        # Replace this with your task logic
        print("Running the task every second")
        await asyncio.sleep(1)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(my_task())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
