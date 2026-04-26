# Chapter F-06: Response Model
# Ref: https://fastapi.tiangolo.com/tutorial/response-model/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs
#
# Topics covered in this chapter:
#   1. Return type annotation as response model
#   2. response_model parameter in path operation decorator
#   3. Input/Output model separation (security: password filtering)
#   4. Model inheritance for data filtering
#   5. response_model_exclude_unset / _exclude_defaults / _exclude_none
#   6. response_model_include / response_model_exclude
#   7. Returning Response directly (JSONResponse, RedirectResponse)
#   8. response_model=None to disable validation

from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from typing import Any
from schemas import Item, UserIn, UserOut, BaseUser, UserInV2

# Type hints are mandatory in FastAPI — they drive validation, serialization, and OpenAPI docs
# 型ヒントはFastAPIの必須要件 — バリデーション・シリアライズ・OpenAPI生成に直結します

app = FastAPI()

# --- Section 1: Return type annotation (basic) ---
# FastAPI validates, serializes, and generates OpenAPI schema from return type
# 戻り値の型から自動でバリデーション・シリアライズ・OpenAPI生成
@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Ledger Entry", price=100.0),
        Item(name="Transfer Fee", price=1.5),
    ]


# --- Section 2: response_model separates input/output (security pattern) ---
# response_model=UserOut filters out 'password' even though we return UserIn
# response_model=UserO
@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
    # password is filtered by FastAPI automatically


# --- Section 3: Inheritance pattern — better editor support ---
# Return type BaseUser + FastAPI filtering = type-safe AND data-filtered
# 戻り値型 BaseUser + FastAPI フィルタリング = 型安全 + データ除外
@app.post("/user/v2")
async def create_user_v2(user: UserInV2) -> BaseUser:
    return user


# --- Section 4: response_model_exclude_unset ---
# Only return fields that were explicitly set (great for PATCH in payment-ledger-api)
# 明示的にセットされたフィールドのみ返す（PATCH API に最適）
items_db = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighter", "price": 62.0, "tax": 20.2},
}


@app.get(
    "/items/{item_id}",
    response_model=Item,
    response_model_exclude_unset=True,
)
async def read_item(item_id: str):
    return items_db[item_id]


# --- Section 5: response_model_include / response_model_exclude ---
# Include only specific fields in response
# レスポンスに含めるフィールドを限定する
@app.get(
    "/items/{item_id}/public",
    response_model=Item,
    response_model_exclude={"tax"},
)
async def read_item_public(item_id: str):
    return items_db[item_id]


# --- Section 6: Return Response directly ---
# When returning Response/JSONResponse/RedirectResponse, FastAPI handles it automatically
# Response 系を直接返す場合、FastAPI が自動的に処理する
@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> JSONResponse | RedirectResponse:
    if teleport:
        return RedirectResponse(url="https://fastapi.tiangolo.com")
    return JSONResponse(content={"message": "Welcome to the API portal."})


# --- Section 7: Disable response model with response_model=None ---
# Use when return type annotation is non-Pydantic union
# Pydantic 非対応のユニオン型を使う場合に response_model を無効化する
@app.get("/portal/v2", response_model=None)
async def get_portal_v2(teleport: bool = False) -> JSONResponse | dict:
    if teleport:
        return RedirectResponse(url="https://fastapi.tiangolo.com")
    return {"message": "Portal v2 without response model validation."}
