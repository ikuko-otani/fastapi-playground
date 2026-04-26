# schemas.py — Pydantic models for F-06: Response Model
# Ref: https://fastapi.tiangolo.com/tutorial/response-model/
#
# All models must use type hints — this is what FastAPI uses for validation and OpenAPI generation.
# 全モデルで型ヒント必須 — FastAPIはこれをバリデーションとOpenAPI生成に使用します

from pydantic import BaseModel, EmailStr

# ---------------------------------------------------------------------------
# Section 1: Basic Item model
# ---------------------------------------------------------------------------
# TODO: Define Item model with fields: name, description, price, tax, tags
# Itemモデルを定義してください（フィールド: name, description, price, tax, tags）

# Item model with optional fields and default values
# オプションフィールドとデフォルト値を持つ Item モデル
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


# ---------------------------------------------------------------------------
# Section 2: User models — Input / Output separation (security pattern)
# ---------------------------------------------------------------------------
# TODO: Define UserIn (with password) and UserOut (without password)
# NOTE: This is the core security pattern for payment-ledger-api!
# UserIn（パスワードあり）とUserOut（パスワードなし）を定義してください
# 注意：payment-ledger-api の中核セキュリティパターンです！

# UserIn includes plaintext password — NEVER return this model directly!
# UserIn は平文パスワードを含む — 絶対にそのまま返さないこと！
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

# UserOut excludes password — safe to return in response
# UserOut はパスワードを除外 — レスポンスとして安全に返せる
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


# ---------------------------------------------------------------------------
# Section 3: Model inheritance pattern (preferred over response_model param)
# ---------------------------------------------------------------------------
# TODO: Define BaseUser -> UserIn (add password field)
# BaseUser -> UserIn（passwordフィールド追加）の継承パターンを定義してください

# BaseUser holds the common safe fields
# BaseUser は共通の安全なフィールドを持つ
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

# UserInV2 inherits BaseUser and adds password
# UserInV2 は BaseUser を継承してパスワードを追加する
class UserInV2(BaseUser):
    password: str
