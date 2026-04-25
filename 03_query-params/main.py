# Chapter F-03: Query Parameters
# Ref: https://fastapi.tiangolo.com/tutorial/query-params/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

# TODO: Add your imports below (copy-paste OK)
from fastapi import FastAPI
# from typing import Optional

app = FastAPI()

# Fake in-memory DB for demonstration
# デモ用のインメモリ疑似DB
fake_item_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Basic query parameters with default values
# デフォルト値付きクエリパラメータの基本
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    # skip and limit are query params; inferred from type hints
    # skip・limitはURLパスにないので自動的にクエリパラメータと認識
    return fake_item_db[skip : skip + limit]
