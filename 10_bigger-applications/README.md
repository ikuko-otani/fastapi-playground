# F-10: Bigger Applications — Router Splitting

## What You Learn / 学習内容

This unit covers how to scale a FastAPI application by splitting path operations into multiple files using `APIRouter`.

このユニットでは、`APIRouter` を使ってパスオペレーションを複数ファイルに分割し、FastAPIアプリケーションをスケールする方法を学びます。

## Key Concepts / 主要コンセプト

| Concept | Description |
|---|---|
| `APIRouter` | A "mini FastAPI" for grouping related endpoints / 関連エンドポイントをグループ化する「ミニFastAPI」 |
| `prefix` | Auto-prepend a path prefix to all routes in a router / ルーター内の全ルートにパスプレフィックスを自動付与 |
| `tags` | Group endpoints in the OpenAPI docs / OpenAPI ドキュメントでエンドポイントをグループ化 |
| `dependencies` | Apply shared `Depends()` to every route in the router / ルーター内の全ルートに共有 `Depends()` を適用 |
| `responses` | Declare shared response schemas for all routes / 全ルートの共有レスポンススキーマを宣言 |
| `app.include_router()` | Mount an APIRouter into the main FastAPI app / APIRouter をメイン FastAPI アプリにマウント |
| Relative imports (`..`) | Navigate Python package structure / Pythonパッケージ構造をナビゲート |
| `__init__.py` | Makes a directory a Python package / ディレクトリをPythonパッケージにする |

## File Structure / ファイル構成

```
10_bigger-applications/
└── app/
    ├── __init__.py
    ├── main.py              # Entry point / エントリーポイント
    ├── dependencies.py      # Shared dependencies / 共有依存関係
    ├── routers/
    │   ├── __init__.py
    │   ├── users.py         # /users endpoints
    │   └── items.py         # /items endpoints
    └── internal/
        ├── __init__.py
        └── admin.py         # /admin endpoints
```

## Run / 実行方法

```bash
# From the 10_bigger-applications/ directory:
cd 10_bigger-applications
uvicorn app.main:app --reload
```

Open: http://localhost:8000/docs

## Reference / 参考

- Tutorial: https://fastapi.tiangolo.com/tutorial/bigger-applications/
- Advanced - Router Testing: https://fastapi.tiangolo.com/advanced/testing-dependencies/
- Advanced - Custom Response: https://fastapi.tiangolo.com/advanced/custom-response/
