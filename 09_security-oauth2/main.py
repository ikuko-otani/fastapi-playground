# Chapter F-09: Security: OAuth2 with Password Bearer（触りのみ）
# セキュリティ：OAuth2 パスワードベアラー（入門のみ）
# Ref: https://fastapi.tiangolo.com/tutorial/security/first-steps/
#
# Run: uvicorn main:app --reload
# uvicorn main:app --reload で起動
# Docs: http://localhost:8000/docs

# TODO Step 1: Import OAuth2PasswordBearer and Depends
# OAuth2PasswordBearer と Depends をインポートする

from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

# TODO Step 2: Create FastAPI app instance
# FastAPI アプリインスタンスを作成する

app = FastAPI()

# TODO Step 3: Create OAuth2PasswordBearer instance with tokenUrl="token"
# tokenUrl="token" を指定して OAuth2PasswordBearer インスタンスを作成する
# Create OAuth2 scheme — tokenUrl is the endpoint clients POST credentials to
# OAuth2スキームを作成 — tokenUrl はクライアントが資格情報を POST するエンドポイント

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO Step 4: Define /items/ endpoint that depends on oauth2_scheme
# oauth2_scheme を依存関係として持つ /items/ エンドポイントを定義する

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    # token is automatically extracted from the Authorization: Bearer <token> header
    # トークンは Authorization: Bearer <token> ヘッダーから自動的に抽出される
    return {"token": token}
