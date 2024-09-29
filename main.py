from enum import Enum

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl
from typing_extensions import Optional


app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.post("/")
# def predict():
#     return {"prediction": "prediction"}
#
#
# @app.get("/predict")
# def predict():
#     return {"prediction": "prediction"}
#
#
# @app.get("/predict/{item_id}")
# def predict(item_id: int):
#     return {"prediction": item_id}
#
#
# @app.get("/users/{item_id}")
# def predict(item_id: str):
#     return {"name": item_id}
#
#
# @app.get("/users/me")
# def user():
#     return {"name": "<NAME>"}
#
#
# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     veggies = "veggies"
#     dairy = "dairy"
#
#
# @app.get("/foods/{food_name}")
# def get_food(food_name: FoodEnum):
#     print(food_name)
#     if food_name == FoodEnum.fruits:
#         return {"food_name": FoodEnum[food_name], "message": "you are healthy"}
#     if food_name == FoodEnum.veggies:
#         return {"food_name": FoodEnum[food_name], "message": "you are healthy"}
#     if food_name == FoodEnum.dairy:
#         return {"food_name": FoodEnum[food_name], "message": "you are health"}
#     else:
#         return {"food_name": food_name, "message": "you are not healthy"}
#
#
# fake_items_db = [
#     {
#         "item_id": "1",
#     },
#     {
#         "item_id": "2",
#     },
#     {
#         "item_id": "3",
#     }
# ]
#
#
# @app.get("/items")
# def items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]
#
#
# @app.get("/items/{item_id}")
# def get_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "This is the first item",
#             }
#         )
#     return item
#
#
# @app.get("/users/{user_id}/items/{item_id}")
# def get_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"user_id": user_id, "item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "This is the second item",
#             }
#         )
#     return item
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# @app.post("/items")
# def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
#
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result
#
#
# @app.get("/items")
# def read_items(q: str | None = Query(None, min_length=3, max_length=10)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
#
# @app.get("/items_hidden")
# def hidden_query_param(hidden_query: str | None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     else:
#         return {"hidden_query": "Not provided"}
#
#
# @app.get("/items_validation/{item_id}")
# def read_items(
#         item_id: int = Path(..., title="The ID of the item to get", gt=10, le=100),
#         q: str | None = Query(None, alias="item-query"),
#         size: float = Query(..., gt=0, lt=10.5)
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


"""
Part 7 Body - Multiple Parameters
"""


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#
#
# @app.put("/items/{item_id}")
# def update_item(
#         *,
#         item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
#         q: str | None = None,
#         item:  Item = Body(..., embed=True),
#         user: User,
#
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     return results


"""
Part 8 Body - Fields
"""


# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300,
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: float | None = None
#
#
# @app.put("/items/{item_id}")
# def update_item(
#         *,
#         item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
#         q: str | None = None,
#         item: Item = Body(..., embed=True),
#
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results


"""
Part 9 Body - Nested Models
"""


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300,
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: float | None = None
    tags: set[str] = set()
    image: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
def update_item(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
        q: str | None = None,
        item: Item = Body(..., embed=True),

):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@app.post("/offers")
def create_offer(offer: Offer = Body(..., embed=True)):
    return offer


@app.post("/images/multiple")
def create_multiple_images(images: list[Image] = Body(..., embed=True)):
    return images
