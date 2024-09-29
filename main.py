from enum import Enum
from urllib.request import Request

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def predict():
    return {"prediction": "prediction"}


@app.get("/predict")
def predict():
    return {"prediction": "prediction"}


@app.get("/predict/{item_id}")
def predict(item_id: int):
    return {"prediction": item_id}


@app.get("/users/{item_id}")
def predict(item_id: str):
    return {"name": item_id}


@app.get("/users/me")
def user():
    return {"name": "<NAME>"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    veggies = "veggies"
    dairy = "dairy"


@app.get("/foods/{food_name}")
def get_food(food_name: FoodEnum):
    print(food_name)
    if food_name == FoodEnum.fruits:
        return {"food_name": FoodEnum[food_name], "message": "you are healthy"}
    if food_name == FoodEnum.veggies:
        return {"food_name": FoodEnum[food_name], "message": "you are healthy"}
    if food_name == FoodEnum.dairy:
        return {"food_name": FoodEnum[food_name], "message": "you are health"}
    else:
        return {"food_name": food_name, "message": "you are not healthy"}
