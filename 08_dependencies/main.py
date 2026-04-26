# Chapter F-08: Dependencies — First Steps
# Ref: https://fastapi.tiangolo.com/tutorial/dependencies/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

from fastapi import FastAPI, Depends
# Japanese: FastAPI本体とDependsをインポート

from typing import Annotated
# Japanese: Annotatedパターン（推奨）のためにインポート

from dependencies import common_parameters
# Japanese: 共通依存関数をdependencies.pyからインポート

app = FastAPI()
# Japanese: FastAPIアプリケーションインスタンスを生成


# TODO: Step 1 — implement /items/ endpoint using Depends()
# Japanese: Step1 — Depends()を使った /items/ エンドポイントを実装する
# Hint:
#   @app.get("/items/")
#   async def read_items(commons: dict = Depends(common_parameters)):
#       return commons


# TODO: Step 2 — implement /users/ endpoint reusing the same dependency
# Japanese: Step2 — 同じ依存関数を再利用した /users/ エンドポイントを実装する
# Hint:
#   @app.get("/users/")
#   async def read_users(commons: dict = Depends(common_parameters)):
#       return commons


# TODO: Step 3 — refactor using Annotated type alias (CommonsDep)
# Japanese: Step3 — Annotated型エイリアス（CommonsDep）でリファクタリングする
# Hint: from dependencies import CommonsDep
#   @app.get("/items/")
#   async def read_items(commons: CommonsDep):
#       return commons
