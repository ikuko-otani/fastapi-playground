# F-02: Path Parameters

**Tutorial:** https://fastapi.tiangolo.com/tutorial/path-params/

## What you learn / 学習内容

### English
- Declare path parameters with `{param}` syntax in the URL template
- Use Python type hints to enable automatic parsing and Pydantic validation
- Understand route evaluation order (fixed routes before parameterized ones)
- Restrict path parameter values using `str, Enum` subclasses
- Handle path-containing path parameters with `:path` converter

### 日本語
- `{param}` 構文でパスパラメータを宣言する方法
- 型ヒントで自動パース＆Pydanticバリデーションを有効化する
- ルート評価順序（固定パスをパラメータ付きより先に定義する重要性）
- `str, Enum` 継承クラスで許容値を制限する
- `:path` コンバーターでパスを含むパラメータを扱う

## Key interview topics / 面接で聞かれるポイント

- Type hints → automatic OpenAPI schema generation
- Pydantic validates under the hood → 422 Unprocessable Entity on mismatch
- Route order matters: `/users/me` must precede `/users/{user_id}`
- `str, Enum` for constrained parameters (e.g., account types, currencies)

## Flagship connection / payment-ledger-api への応用

- `GET /accounts/{account_id}` pattern
- `GET /transactions/{transaction_id}` with UUID type (see Extra Data Types)
- Enum for account types / currency codes

## Files

- `main.py` — main exercise file

## Related Advanced Guide

- Path Parameters and Numeric Validations: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
- Extra Data Types (UUID etc.): https://fastapi.tiangolo.com/tutorial/extra-data-types/
