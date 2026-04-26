# F-06: Response Model

## What You Learn / 学習内容

### English
This chapter covers how FastAPI uses **return type annotations** and the `response_model` parameter
to validate, filter, and document API responses.

Key concepts:
- Declare response shape via return type annotation or `response_model=` parameter
- **Security pattern**: separate `UserIn` (has password) from `UserOut` (no password) — critical for payment APIs
- Model inheritance (`BaseUser` → `UserIn`) for cleaner type-safe filtering
- `response_model_exclude_unset=True` — omit fields not explicitly set (useful for sparse PATCH payloads)
- `response_model_include` / `response_model_exclude` for ad-hoc field control
- Returning `Response` / `JSONResponse` / `RedirectResponse` directly

### 日本語
この章では、FastAPI が **戻り値の型アノテーション** と `response_model` パラメーターを使って、
APIレスポンスのバリデーション・フィルタリング・ドキュメント生成を行う仕組みを学びます。

主要概念：
- 戻り値の型アノテーション or `response_model=` でレスポンスの形を宣言する
- **セキュリティパターン**：`UserIn`（パスワードあり）と `UserOut`（パスワードなし）を分離 — 決済APIに必須
- モデル継承（`BaseUser` → `UserIn`）による型安全なフィルタリング
- `response_model_exclude_unset=True` — 明示的に設定されたフィールドのみ返す（PATCH API に有効）
- `response_model_include` / `response_model_exclude` でフィールドをアドホックに制御
- `Response` / `JSONResponse` / `RedirectResponse` を直接返すパターン

## Flagship Connection / payment-ledger-api での活用

- `TransactionOut` (no internal fields like `hashed_password`, internal IDs)
- `response_model_exclude_unset=True` on PATCH `/transactions/{id}`
- `UserOut` schema to never leak `hashed_password` in any response

## Run

```bash
cd 06_response-model
uvicorn main:app --reload
# Open: http://localhost:8000/docs
```

## Reference
- Tutorial: https://fastapi.tiangolo.com/tutorial/response-model/
- Advanced (Response directly): https://fastapi.tiangolo.com/advanced/response-directly/
- Advanced (Custom Response): https://fastapi.tiangolo.com/advanced/custom-response/
