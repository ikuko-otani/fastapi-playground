# Chapter F-04: Request Body (Pydantic)
# Ref: https://fastapi.tiangolo.com/tutorial/body/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

# --- Imports ---
# インポート文
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# --- App instance ---
# FastAPIアプリインスタンス
app = FastAPI()

# ============================================================
# STEP 1: Define a Pydantic model
# Pydanticモデルを定義する
# ============================================================
# TODO: Define class Item(BaseModel) with fields:
#   name: str
#   description: str | None = None
#   price: float
#   tax: float | None = None
# 上記フィールドを持つItemクラスを定義
class Item(BaseModel):
    name: str
    # description is optional — defaults to None
    # descriptionはオプション。デフォルトはNone
    description: str | None = None
    price: float

    # tax is optional
    # taxもオプション
    tax: float | None = None


# ============================================================
# STEP 2: POST endpoint – body only
# POSTエンドポイント（ボディのみ）
# ============================================================
# TODO: @app.post("/items/") -> return item
# Itemを受け取ってそのまま返すエンドポイント
@app.post("/items/")
async def create_item(item: Item):
    return item


# ============================================================
# STEP 3: POST endpoint – use model methods
# モデルのメソッドを活用するエンドポイント
# ============================================================
# TODO: @app.post("/items/with-tax") -> return item.model_dump() + price_with_tax
# 💡 Interview tip: model_dump() is Pydantic v2; .dict() is v1 (deprecated)
# model_dump()はPydantic v2。面接でv1/v2の違いを聞かれることがある


# ============================================================
# STEP 4: PUT endpoint – body + path parameter
# ボディ＋パスパラメータの組み合わせ
# ============================================================
# TODO: @app.put("/items/{item_id}") with item_id: int, item: Item
# 💡 FastAPI auto-detects: path param from path, Pydantic model from body
# FastAPIはパスパラメータとボディを型ヒントで自動判別する


# ============================================================
# STEP 5: PUT endpoint – body + path + query
# ボディ＋パス＋クエリの全部乗せ
# ============================================================
# TODO: @app.put("/items/{item_id}/full") add optional query param q: str | None = None
# クエリパラメータqも加えた完全版エンドポイント
