# F-03: Query Parameters

## What you will learn / 何を学ぶか

### English
In this exercise, you will learn how FastAPI handles **query parameters** — the key-value pairs
that appear after `?` in a URL (e.g., `/items/?skip=0&limit=10`).

Key concepts covered:
- Declaring query parameters with type hints (auto parsing + validation)
- Default values and optional parameters (`None` default)
- `bool` type conversion (`true`, `1`, `on`, `yes` all map to `True`)
- Mixing path parameters and query parameters
- Required query parameters (no default value = required)
- How type hints automatically generate OpenAPI docs at `/docs`

### 日本語
FastAPIでクエリパラメータ（URLの `?` 以降のキー・バリューペア）を扱う方法を学びます。

主なテーマ：
- 型ヒントによるクエリパラメータの宣言（自動変換・バリデーション）
- デフォルト値と任意パラメータ（`None` デフォルト）
- `bool` 型変換（`true`, `1`, `on`, `yes` はすべて `True` に変換）
- パスパラメータとクエリパラメータの混在
- 必須クエリパラメータ（デフォルト値なし＊必須）
- 型ヒントが OpenAPI ドキュメント（`/docs`）に自動反映される仕組み

## Connection to Flagship / Flagshipとの接続

In `payment-ledger-api`, query parameters will be used for:
- Pagination: `GET /entries?skip=0&limit=50`
- Filtering: `GET /entries?account_id=xxx&date_from=2026-01-01`
- Feature flags: `GET /entries?include_voided=true`

## Tutorial
https://fastapi.tiangolo.com/tutorial/query-params/

## Related Advanced Docs
- [Query Parameter Models](https://fastapi.tiangolo.com/tutorial/query-param-models/)
- [Additional Validation with Query()](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
