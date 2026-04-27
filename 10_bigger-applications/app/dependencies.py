# Shared dependencies used across multiple routers
# 複数のルーターで共有される依存関係

from typing import Annotated
from fastapi import Header, HTTPException


# TODO: Implement get_token_header dependency
# get_token_header 依存関数を実装する
async def get_token_header(x_token: Annotated[str, Header()]) -> None:
    # Validate the X-Token header
    # X-Token ヘッダーを検証する
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


# TODO: Implement get_query_token dependency
# get_query_token 依存関数を実装する
async def get_query_token(token: str) -> None:
    # Validate the query parameter token
    # クエリパラメータ token を検証する
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
