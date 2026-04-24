# Chapter F-01: First Steps
# Ref: https://fastapi.tiangolo.com/tutorial/first-steps/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

# TODO: Step 1 — Import FastAPI and create app instance
# FastAPI をインポートし、app インスタンスを作成する
from fastapi import FastAPI

# Create the FastAPI application instance
# FastAPI アプリケーションのインスタンスを作成する
app = FastAPI()

# TODO: Step 2 — Define root endpoint GET /
# ルートエンドポイント GET / を定義する
@app.get("/")
async def root():
    return {"message": "Hello World"}

# TODO: Step 3 — Add GET /health endpoint
# ヘルスチェック用エンドポイント GET /health を追加する

# TODO: Step 4 — Add async GET /items/{item_id} endpoint
# 非同期版エンドポイント GET /items/{item_id} を追加する

# TODO: Step 5 — Add sync def GET /ping endpoint (compare with async)
# 同期版エンドポイント GET /ping を追加して async def と比較する
