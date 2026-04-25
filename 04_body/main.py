# Chapter F-04: Request Body (Pydantic)
# Ref: https://fastapi.tiangolo.com/tutorial/body/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

# --- Imports (copy-paste OK) ---
# 日本語訳：インポート文（コピペOK）
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# --- App instance (copy-paste OK) ---
# 日本語訳：FastAPIアプリインスタンス（コピペOK）
app = FastAPI()

# ============================================================
# STEP 1: Define a Pydantic model  ✍️ Type this yourself
# 日本語訳：Pydanticモデルを定義する（自分で入力）
# ============================================================
# TODO: Define class Item(BaseModel) with fields:
#   name: str
#   description: str | None = None
#   price: float
#   tax: float | None = None
# 日本語訳：上記フィールドを持つItemクラスを定義してください


# ============================================================
# STEP 2: POST endpoint – body only  ✍️ Type this yourself
# 日本語訳：POSTエンドポイント（ボディのみ）
# ============================================================
# TODO: @app.post("/items/") -> return item
# 日本語訳：Itemを受け取ってそのまま返すエンドポイントを作成


# ============================================================
# STEP 3: POST endpoint – use model methods  ✍️ Type this yourself
# 日本語訳：モデルのメソッドを活用するエンドポイント
# ============================================================
# TODO: @app.post("/items/with-tax") -> return item.model_dump() + price_with_tax
# 💡 Interview tip: model_dump() is Pydantic v2; .dict() is v1 (deprecated)
# 日本語訳：model_dump()はPydantic v2。面接でv1/v2の違いを聞かれることがある


# ============================================================
# STEP 4: PUT endpoint – body + path parameter  ✍️ Type this yourself
# 日本語訳：ボディ＋パスパラメータの組み合わせ
# ============================================================
# TODO: @app.put("/items/{item_id}") with item_id: int, item: Item
# 💡 FastAPI auto-detects: path param from path, Pydantic model from body
# 日本語訳：FastAPIはパスパラメータとボディを型ヒントで自動判別する


# ============================================================
# STEP 5: PUT endpoint – body + path + query  ✍️ Type this yourself
# 日本語訳：ボディ＋パス＋クエリの全部乗せ
# ============================================================
# TODO: @app.put("/items/{item_id}/full") add optional query param q: str | None = None
# 日本語訳：クエリパラメータqも加えた完全版エンドポイント
