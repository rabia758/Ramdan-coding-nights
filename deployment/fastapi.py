
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello_world():
    return {"message": "Hello World"}

