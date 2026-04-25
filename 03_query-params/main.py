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

# Optional query parameter and bool type conversion
# Optionalクエリパラメータとbool型変換
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    # item_id is a path param; q and short are query params
    # item_idはパスパラメータ、q・shortはクエリパラメータ
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item with a long description"})
    return item

# Multiple path params + query params (detection by name, not order)
# 複数パスパラメータ＋クエリパラメータの混在（名前で自動識別）
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Long description here"})
    return item
