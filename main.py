from urllib.request import Request

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def predict():
    return {"prediction": "prediction"}