# F-07: Handling Errors

**Tutorial:** https://fastapi.tiangolo.com/tutorial/handling-errors/

## What You Learn / 学習内容

This chapter covers how to return meaningful error responses in FastAPI APIs.

この章では、FastAPI API で意味のあるエラーレスポンスを返す方法を学びます。

## Topics Covered / カバーするトピック

| Topic | Class / Decorator | Importance |
|---|---|---|
| Basic error response | `HTTPException` | ⭐⭐⭐ Essential |
| Custom error headers | `HTTPException(headers=...)` | ⭐⭐ Useful |
| Custom exception class | `class MyError(Exception)` | ⭐⭐⭐ Essential |
| Global exception handler | `@app.exception_handler()` | ⭐⭐⭐ Essential |
| Override validation errors | `RequestValidationError` | ⭐⭐⭐ Berlin interview |
| Override HTTP error handler | `StarletteHTTPException` | ⭐⭐ Advanced |
| Reuse default handlers | `fastapi.exception_handlers` | ⭐⭐ Advanced |
| Access request body in errors | `exc.body` | ⭐⭐ Debugging |

## Relevance to payment-ledger-api / Flagship への応用

- `PaymentException` — domain-specific error for invalid payment amounts
  ／不正な支払い金額に対するドメイン固有エラー
- `RequestValidationError` override — structured JSON errors for API consumers
  ／API利用者向けの構造化JSONエラー
- Custom headers — `X-Request-ID` tracing in payment operations
  ／支払い処理での `X-Request-ID` トレーシング

## File Structure / ファイル構成

```
handling-errors/
├── main.py       # All endpoints and exception handlers (✍️ fill in during study)
├── schemas.py    # Pydantic models (scaffold provided)
└── README.md     # This file
```

## How to Run / 実行方法

```bash
cd handling-errors
uvicorn main:app --reload
# Open: http://localhost:8000/docs
```

## Key Interview Points / 面接頻出ポイント

1. **`raise` not `return`** — HTTPException is always raised, not returned.
   ／HTTPException は `return` ではなく `raise` する。
2. **FastAPI vs Starlette HTTPException** — handlers should target `StarletteHTTPException`.
   ／ハンドラ登録は `StarletteHTTPException` を対象にする。
3. **`RequestValidationError`** — triggered automatically by Pydantic on invalid input.
   ／不正な入力に対して Pydantic が自動的にトリガーする。
4. **`detail` can be any JSON-serializable value** — dict, list, not just str.
   ／`detail` は str だけでなく dict・list など JSON 化できる値なら何でも可。
