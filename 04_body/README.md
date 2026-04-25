# F-04: Request Body (Pydantic)

**Tutorial:** https://fastapi.tiangolo.com/tutorial/body/

## What you learn / 学習内容

| Topic (EN) | トピック (JP) |
|---|---|
| Define Pydantic `BaseModel` | Pydantic `BaseModel` でデータモデルを定義する |
| Required vs optional fields | 必須フィールドとオプションフィールドの違い |
| `POST /items/` — body-only endpoint | ボディのみのPOSTエンドポイント |
| `item.model_dump()` (Pydantic v2) | `model_dump()` でdictに変換 |
| Body + path parameter (`PUT /items/{id}`) | ボディ＋パスパラメータの組み合わせ |
| Body + path + query parameter | ボディ＋パス＋クエリの全部乗せ |
| OpenAPI / Swagger UI auto-generation | 型ヒントから自動生成されるSwagger UI |

## Why this matters for Berlin interviews / ベルリン面接での重要性

- Pydantic v2 is the **de facto standard** for input validation in Python APIs in European scale-ups.
- Being able to explain the difference between **Pydantic v1 (`.dict()`)** and **v2 (`.model_dump()`)** signals real-world experience.
- Understanding how FastAPI **infers parameter location** (path / query / body) from type hints demonstrates deep framework knowledge.
- `payment-ledger-api` uses these exact patterns for `JournalEntryCreate`, `TransactionCreate`, etc.

## Files / ファイル構成

```
04_body/
├── main.py     # ✍️ Complete the TODOs step by step
└── README.md   # This file
```

## Quick start / クイックスタート

```bash
# From the 04_body/ directory
uvicorn main:app --reload
# Open: http://localhost:8000/docs
```

## Flagship connection / payment-ledger-api への応用

`JournalEntryCreate`, `AccountCreate` などのスキーマはすべてここで学ぶ
`BaseModel` パターンを使っています。`model_dump()` は SQLAlchemy への
データ渡しでも活用されます。
