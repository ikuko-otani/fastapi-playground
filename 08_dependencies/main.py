# Chapter F-08: Dependencies — First Steps
# Ref: https://fastapi.tiangolo.com/tutorial/dependencies/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

from fastapi import FastAPI, Depends
# FastAPI本体とDependsをインポート

from typing import Annotated
# Annotatedパターン（推奨）のためにインポート

from dependencies import common_parameters
# 共通依存関数をdependencies.pyからインポート

app = FastAPI()
# FastAPIアプリケーションインスタンスを生成


# TODO: Step 1 — implement /items/ endpoint using Depends()
# Step1 — Depends()を使った /items/ エンドポイントを実装する

@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


# TODO: Step 2 — implement /users/ endpoint reusing the same dependency
# Step2 — 同じ依存関数を再利用した /users/ エンドポイントを実装する

@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


# TODO: Step 3 — refactor using Annotated type alias (CommonsDep)
# Step3 — Annotated型エイリアス（CommonsDep）でリファクタリングする

from dependencies import common_parameters, CommonsDep, sync_dep

@app.get("/items/")
async def read_items(commons: CommonsDep):
    return commons

@app.get("/users/")
async def read_users(commons: CommonsDep):
    return commons

@app.get("/check-sync")
async def check_sync(info: dict = Depends(sync_dep)):
    return info
