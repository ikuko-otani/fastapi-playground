# Chapter F-07: Handling Errors
# Ref: https://fastapi.tiangolo.com/tutorial/handling-errors/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

# ============================================================
# IMPORTS — copy-paste OK
# 日本語訳：インポート文はコピペOK
# ============================================================
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel

app = FastAPI()

# ============================================================
# STEP 1: Basic HTTPException — ✍️ write this yourself
# 日本語訳：Step 1 HTTPException の基本 — 自分で入力
# ============================================================
# TODO: Add a fake items DB (dict) and a GET /items/{item_id} endpoint
# that raises HTTPException(404) when item_id is not found.
# 日本語訳：items辞書を作り、存在しないIDで404を raise するGETエンドポイントを作成


# ============================================================
# STEP 2: Custom headers on HTTPException — ✍️ write this yourself
# 日本語訳：Step 2 カスタムヘッダー付きエラー — 自分で入力
# ============================================================
# TODO: Add GET /items-header/{item_id} that raises HTTPException
# with headers={"X-Error": "..."}.
# 日本語訳：headersパラメータ付き HTTPException を発生させるエンドポイントを作成


# ============================================================
# STEP 3: Custom Exception class + @app.exception_handler — ✍️ write this yourself
# 日本語訳：Step 3 カスタム例外クラスとハンドラ — 自分で入力
# ============================================================
# TODO: Define PaymentException(Exception) with amount: float attribute.
# Register @app.exception_handler(PaymentException) returning JSON 422.
# Add GET /pay/{amount} that raises it when amount <= 0.
# 日本語訳：PaymentException クラスを定義し、ハンドラを登録する


# ============================================================
# STEP 4: Override RequestValidationError handler — ✍️ write this yourself
# 日本語訳：Step 4 バリデーションエラーハンドラの上書き — 自分で入力
# ============================================================
# TODO: Override @app.exception_handler(RequestValidationError)
# to return JSON with {"detail": exc.errors(), "body": exc.body}.
# Add POST /payments/ with a Pydantic model (amount: float, currency: str).
# 日本語訳：RequestValidationError ハンドラを上書き。Pydanticモデル付きPOSTエンドポイントを追加


# ============================================================
# STEP 5 (optional): Reuse default handlers with extra logging
# 日本語訳：Step 5（任意）：デフォルトハンドラを再利用しながら追加ログを出力
# ============================================================
# TODO: Combine custom logging (print) + await http_exception_handler(...)
# 日本語訳：カスタムログとデフォルトハンドラを組み合わせる
