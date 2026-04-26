# schemas.py — Pydantic models for F-07: Handling Errors
# F-07「エラーハンドリング」用 Pydantic モデル定義
#
# Type hints are REQUIRED — FastAPI uses them for validation & OpenAPI docs.
# 型ヒントは必須 — FastAPI はバリデーションと OpenAPI ドキュメント生成に使用する

from pydantic import BaseModel, Field


class PaymentRequest(BaseModel):
    # Amount to pay (must be > 0)
    # 支払い金額（0より大きい必要がある）
    amount: float = Field(..., gt=0, description="Payment amount, must be positive")

    # ISO 4217 currency code, e.g. "EUR", "USD"
    # ISO 4217 通貨コード（例："EUR"、"USD"）
    currency: str = Field(..., min_length=3, max_length=3, description="3-letter currency code")


class ErrorDetail(BaseModel):
    # Structured error response model
    # 構造化されたエラーレスポンスモデル
    code: str
    message: str
    field: str | None = None  # Optional: which field caused the error
    # どのフィールドがエラーを起こしたか（任意）
