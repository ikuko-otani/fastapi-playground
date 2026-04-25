# Chapter F-05: Query Params & String Validations
# Ref: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

# TODO: Import FastAPI, Query, Annotated, and AfterValidator as you progress through the steps
# 各ステップに進みながら FastAPI, Query, Annotated, AfterValidator をインポート
from typing import Annotated
from fastapi import FastAPI, Query

# Create FastAPI instance
# FastAPI インスタンスを生成
app = FastAPI()

# TODO: Step 1 — Basic optional query parameter (no validation)
# Step 1 — バリデーションなしのオプションクエリパラメーター
# @app.get("/items/")
# async def read_items(q: str | None = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# TODO: Step 2 — Add Query() with min_length / max_length / pattern
# Step 2 — Query() に min_length / max_length / pattern を追加する
@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            min_length=3,
            max_length=50,
            pattern="^[a-z]+$",  # lowercase letters only
            title="Search query",
            description="Filter items by keyword (lowercase letters, 3-50 chars)"
        ),
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# TODO: Step 3 — Required query parameter & list query parameter
# Step 3 — 必須クエリパラメーターとリスト型クエリパラメーター
@app.get("/items/required")
async def read_items_required(
    q: Annotated[str, Query(min_length=3)]
    # No default value = required parameter
    # デフォルト値なし = 必須パラメーター
):
    return {"q": q}


@app.get("/items/multi")
async def read_items_multi(
    q: Annotated[list[str] | None, Query()] = None
    # list[str] must be wrapped in Query() or FastAPI treats it as request body
    # list[str] は Query() でラップ必須。ないとリクエストボディと解釈される
):
    return {"q": q}


# TODO: Step 4 — alias, deprecated, include_in_schema=False
# Step 4 — alias（別名）、deprecated（非推奨）、include_in_schema=False
@app.get("/items/aliased")
async def read_items_aliased(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            # URL uses "item-query", Python uses "q"
            # URL では "item-query"、Python 変数名は "q"
            deprecated=True,
            # shown as deprecated in /docs
            # /docs 上で非推奨として表示
        ),
    ] = None,
):
    return {"item_query": q}


@app.get("/items/hidden")
async def read_items_hidden(
    internal_flag: Annotated[
        str | None,
        Query(include_in_schema=False)
        # hidden from OpenAPI / Swagger UI
        # OpenAPI・Swagger UI から非表示
    ] = None,
):
    return {"flag": internal_flag}


# TODO: Step 5 — Custom validation with AfterValidator (Pydantic v2)
# Step 5 — AfterValidator を使ったカスタムバリデーション（Pydantic v2）
