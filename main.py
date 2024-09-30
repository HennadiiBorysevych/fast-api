from datetime import datetime, timedelta, time
from enum import Enum
from uuid import UUID

from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing_extensions import Optional, Literal

from typing import Union

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


# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300,
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: float | None = None
#     tags: set[str] = set()
#     image: list[Image] | None = None
#
#
# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]
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
#
#
# @app.post("/offers")
# def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer
#
#
# @app.post("/images/multiple")
# def create_multiple_images(images: list[Image] = Body(..., embed=True)):
#     return images


"""
Part 10 Body - Extra Data Types
"""

# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300,
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: float | None = None
#     tags: set[str] = set()
#     image: list[Image] | None = None
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2,
#             }
#         }
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
Part 11 - Extra Data Types
"""

#
# @app.put("/items/{item_id}")
# def read_items(
#         item_id: UUID,
#         start_date: datetime | None = Body(None),
#         end_date: datetime | None = Body(None),
#         repeat_at: time | None = Body(None),
#         process_after: timedelta | None = Body(None),
# ):
#     start_process = start_date + process_after
#     duration = end_date - start_process
#     return {
#         "item_id": item_id,
#         "start_date": start_date,
#         "end_date": end_date,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration
#     }


"""
Part 12 - Cookie and Header Parameters
"""


# @app.get("/items")
# def read_items(
#         cookie_id: str | None = Cookie(None),
#         accept_encoding: str | None = Header(None),
#         header_id: str | None = Header(None),
#         x_token: list[str] | None = Header(None),
# ):
#     return {
#         "cookie_id": cookie_id,
#         "accept_encoding": accept_encoding,
#         "header_id": header_id,
#         "x_token": x_token
#     }


"""
Part 13 - Response Model
"""
# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300,
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: float | None = None
#     tags: set[str] = set()
#     image: list[Image] | None = None
#
#
# @app.post(
#     "/items",
#     response_model=Item,
#     summary="Create an item",
#     response_description="The created item",
# )
# def create_item(item: Item):
#     return item
#
#
# class User(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
#
# class UserInDB(User):
#     password: str
#
#
# class UserOut(User):
#     pass
#
#
# @app.post("/user/", response_model=UserOut)
# def create_user(user: User):
#     return user
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []
#
# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }
#
#
# @app.post("/items/", response_model=Item)
# def read_item(item_id: Item):
#     return items
#
#
# @app.get("/items/{item_id}",  response_model=Item, response_model_exclude_unset=True)
# def read_item_defaults(item_id: str):
#     return items[item_id]
#
#
# @app.get("/items/{item_id}/name", response_model=Item, response_model_include={"name", "description"})
# def read_item_name(item_id: str):
#     return items[item_id]
#
#
# @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
# def read_item_public_data(item_id: str):
#     return items[item_id]


"""
Part 13 - Extra Model
"""


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    print(user_in_db.model_dump(), 'DB')
    return user_in_db


@app.post("/user/", response_model=UserOut)
def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


class TrainItem(BaseItem):
    type = "train"
    size: int

items = {
    "item1": {"description": "All my cars", "type": "car"},
    "item2": {"description": "My favorite plane", "type": "plane", "size": 5},
    "item3": {"description": "My favorite train", "type": "train", "size": 10},
}


@app.get("/items/{item_id}", response_model=Union[CarItem, PlaneItem, TrainItem])
def read_item(item_id: Literal["item1", "item2"]):
    return items[item_id]


class ListItem(BaseModel):
    name: str
    description: str | None = None


list_items = {
    "foo": {"name": "Foo"},
    "bar": {"name": "Bar", "description": "The bartenders"},
}


@app.get("/list_items/", response_model=list[ListItem])
def read_list_item():
    return list_items
