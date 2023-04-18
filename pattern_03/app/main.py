import boto3
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


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{id}", response_model=ResponseItem)
def get_item(id: str):
    """
    アイテムを取得する
    """
    pass
