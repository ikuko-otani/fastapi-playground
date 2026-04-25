# schemas.py — Pydantic models for F-06: Response Model
# Ref: https://fastapi.tiangolo.com/tutorial/response-model/
#
# All models must use type hints — this is what FastAPI uses for validation and OpenAPI generation.
# 日本語訳：全モデルで型ヒント必須 — FastAPIはこれをバリデーションとOpenAPI生成に使用します

from pydantic import BaseModel, EmailStr

# ---------------------------------------------------------------------------
# Section 1: Basic Item model
# ---------------------------------------------------------------------------
# TODO: Define Item model with fields: name, description, price, tax, tags
# 日本語訳：Itemモデルを定義してください（フィールド: name, description, price, tax, tags）


# ---------------------------------------------------------------------------
# Section 2: User models — Input / Output separation (security pattern)
# ---------------------------------------------------------------------------
# TODO: Define UserIn (with password) and UserOut (without password)
# NOTE: This is the core security pattern for payment-ledger-api!
# 日本語訳：UserIn（パスワードあり）とUserOut（パスワードなし）を定義してください
# 注意：payment-ledger-api の中核セキュリティパターンです！


# ---------------------------------------------------------------------------
# Section 3: Model inheritance pattern (preferred over response_model param)
# ---------------------------------------------------------------------------
# TODO: Define BaseUser -> UserIn (add password field)
# 日本語訳：BaseUser -> UserIn（passwordフィールド追加）の継承パターンを定義してください
