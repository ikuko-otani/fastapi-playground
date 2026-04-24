# Chapter F-02: Path Parameters
# Ref: https://fastapi.tiangolo.com/tutorial/path-params/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

# TODO: Implement the following steps
#
# Step 1: Basic path parameter (no type hint)
# Step 2: Path parameter with int type hint -> auto parsing & validation
# Step 3: Order matters -> /users/me before /users/{user_id}
# Step 4: Enum-based predefined values (str, Enum)
# Step 5: Path containing path -> /files/{file_path:path}

from enum import Enum
from fastapi import FastAPI

app = FastAPI()

# Step 1-A: Basic path parameter WITHOUT type hints
# 型ヒントなしの基本パスパラメータ
@app.get("/items/{item_id}")
async def read_item_basic(item_id):
    return  {"item_id": item_id}

# Step 1-B: Path parameter WITH int type hint -> auto parsing + validation
# int型ヒント付き -> 自動パース＋バリデーション
@app.get("/items/typed/{item_id}")
async def read_item_typed(item_id: int):
    return {"item_id": item_id}

# Step 2: Route evaluation order — FIXED path must come BEFORE parameterized
# 固定パスは必ずパラメータ付きパスより先に定義する（順番重要）
@app.get("/user/me")
async def read_user_me():
    # Return the current user
    # 現在のユーザー情報を返す
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    # Returns a specific user by ID
    # IDで指定されたユーザーを返す
    return {"user_id": user_id}
