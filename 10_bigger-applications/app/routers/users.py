# Users router - path operations for /users endpoints
# ユーザールーター - /users エンドポイントのパスオペレーション

from fastapi import APIRouter

# TODO: Create APIRouter instance
# APIRouter インスタンスを作成する

router = APIRouter()

# TODO: Add path operations for GET /users/, GET /users/me, GET /users/{username}
# GET /users/, GET /users/me, GET /users/{username} のパスオペレーションを追加する

@router.get("/users/", tags={"users"})
async def read_users():
    # Return a list of users
    # ユーザー一覧を返す
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/users/me", tags={"users"})
async def read_user_me():
    # Return the current user (fake data)
    # 現在のユーザーを返す（フェイクデータ）
    return {"username": "fakecurrentuser"}

@router.get("/users/{username}}", tags={"users"})
async def read_user(username: str):
    # Return the current user (fake data)
    # ユーザー名で特定のユーザーを返す
    return {"username": username}
