# F-08: Dependency functions
# 依存性関数を定義するファイル

from typing import Annotated
# Annotatedパターンで型エイリアスを定義するために使用

from fastapi import Depends
# Dependsをインポート（型エイリアス内で使用）


# TODO: Step 1 — define common_parameters(q, skip, limit)
# Step1 — common_parameters(q, skip, limit) 依存関数を定義する

def common_parameters(
    q: str | None = None,
    skip: int = 0,
    limit: int = 100,
) -> dict:
    return {"q": q, "skip": skip, "limit": limit}


# TODO: Step 3 — define CommonsDep as Annotated type alias
# Step3 — Annotated型エイリアス CommonsDep を定義する

CommonsDep = Annotated[dict, Depends(common_parameters)]

def sync_dep() -> dict:
    # Sync dependency — FastAPI handles it correctly even in async routes
    # 同期依存関数 — 非同期ルートでも FastAPI が正しく処理する
    return {"source": "sync_dep"}
