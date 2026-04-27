# Main FastAPI application entry point
# FastAPIメインアプリケーションのエントリーポイント
#
# Run: uvicorn app.main:app --reload  (from 10_bigger-applications/ directory)
# Docs: http://localhost:8000/docs

from fastapi import Depends, FastAPI

# TODO: Import routers and dependencies here
# ここにルーターと依存関係をインポートする

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

# TODO: Create FastAPI app instance with global dependency
# グローバル依存関係を持つ FastAPI インスタンスを作成する

app = FastAPI(dependencies=[Depends(get_query_token)])

# TODO: Include routers
# ルーターをインクルードする

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags={"admin"},
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

# TODO: Add root endpoint
# ルートエンドポイントを追加する

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
