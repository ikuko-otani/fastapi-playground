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

# POST endpoint using model_dump()
# model_dump()を使って辞書に変換・加工してから返すエンドポイント
@app.post("/item/with-tax")
async def create_item_with_tax(item: Item):
    # model_dump() is Pydantic v2. Do NOT use .dict() in new code.
    # model_dump()はPydantic v2の書き方。.dict()は非推奨
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# ============================================================
# STEP 4: PUT endpoint – body + path parameter
# ボディ＋パスパラメータの組み合わせ
# ============================================================
# TODO: @app.put("/items/{item_id}") with item_id: int, item: Item
# 💡 FastAPI auto-detects: path param from path, Pydantic model from body
# FastAPIはパスパラメータとボディを型ヒントで自動判別する

# PUT endpoint — body + path parameter
# ボディとパスパラメータを組み合わせたPUTエンドポイント
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # FastAPI knows: item_id comes from path, item comes from body
    # FastAPIが型ヒントから自動判別：item_idはパス、itemはボディ
    return {"item_id": item_id, **item.model_dump()}


# ============================================================
# STEP 5: PUT endpoint – body + path + query
# ボディ＋パス＋クエリの全部乗せ
# ============================================================
# TODO: @app.put("/items/{item_id}/full") add optional query param q: str | None = None
# クエリパラメータqも加えた完全版エンドポイント

# PUT endpoint — body + path + query
# ボディ＋パス＋クエリの全部乗せエンドポイント
@app.put("/items/{item_id}/full")
async def update_item_full(item_id: int, item: Item, q: str | None = None):
    # q is a query parameter because it's a singular type with a default
    # qはsingular型＋デフォルト値なのでクエリパラメータと判別される
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
