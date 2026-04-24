# F-01: First Steps

## What you will learn / 学習内容

**English:**
This chapter covers the absolute basics of FastAPI:
- Creating a `FastAPI` app instance
- Defining path operation decorators (`@app.get`, `@app.post`, etc.)
- Writing path operation functions (`async def` vs `def`)
- Returning JSON responses automatically
- Exploring auto-generated OpenAPI docs at `/docs` and `/redoc`
- Understanding the relationship between Python type hints and OpenAPI schema generation

**日本語：**
この章では FastAPI の基礎中の基礎を学びます：
- `FastAPI` アプリインスタンスの作成
- path operation デコレーター（`@app.get`, `@app.post` など）の定義
- path operation 関数（`async def` vs `def`）の書き方
- JSON レスポンスの自動返却
- `/docs` と `/redoc` で自動生成された OpenAPI ドキュメントを確認
- 型ヒントと OpenAPI スキーマ生成の関係を理解する

## Key Concepts / 重要概念

| Concept | Description |
|---|---|
| `app = FastAPI()` | Application entry point / アプリの起点 |
| `@app.get("/")` | Path operation decorator / パス操作デコレーター |
| `async def` | For I/O-bound handlers / I/O待ちの処理向け |
| `def` | For CPU-bound or sync handlers / CPU処理・同期処理向け |
| `/docs` | Swagger UI (auto-generated) / 自動生成Swagger |
| `/redoc` | ReDoc UI (auto-generated) / 自動生成ReDoc |
| `/openapi.json` | Raw OpenAPI schema / 生のOpenAPIスキーマ |

## Interview Tips / 面接対策

- 💡 **"Why does FastAPI auto-generate OpenAPI docs?"**
  → FastAPI reads Python type hints at runtime and converts them into JSON Schema, which powers both `/docs` and `/redoc`.
- 💡 **"When should you use `async def` vs `def`?"**
  → Use `async def` when calling async libraries (e.g., `asyncpg`, `httpx`). Using `def` with blocking I/O blocks the entire event loop.

## Files / ファイル構成

```
01_first-steps/
├── main.py     # Exercise file (fill in the TODOs)
└── README.md   # This file
```
