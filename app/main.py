from typing import Optional

from fastapi import FastAPI

import logging
from logging.config import dictConfig
from .config import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("hello-fastapi")


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/bags/{bag_id}")
def get_bag(bag_id: int):
    logger.info("Got a bag.")
    return {"bag_id": bag_id}
