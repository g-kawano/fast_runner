import boto3
from app.lib.db.models.items import get_item_by_id
from app.setting import settings
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class ResponseItem(BaseModel):
    """
    レスポンススキーマ
    """

    id: str
    name: str
    age: int


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{id}", response_model=ResponseItem)
def get_item(id: str):
    """
    アイテムを取得する
    """
    item = get_item_by_id(id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item
