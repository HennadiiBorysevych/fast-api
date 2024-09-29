from enum import Enum
from fastapi import FastAPI
from typing_extensions import Optional

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


fake_items_db = [
    {
        "item_id": "1",
    },
    {
        "item_id": "2",
    },
    {
        "item_id": "3",
    }
]


@app.get("/items")
def items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
def get_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "This is the first item",
            }
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
def get_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"user_id": user_id, "item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "This is the second item",
            }
        )
    return item