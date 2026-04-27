# Admin router - internal/shared admin path operations
# 管理ルーター - 内部/共有の管理パスオペレーション

from fastapi import APIRouter

# TODO: Create APIRouter WITHOUT prefix (prefix added at include time in main.py)
# prefix なしで APIRouter を作成する（prefixは main.py の include 時に付与）

router = APIRouter()

# TODO: Add POST / endpoint
# POST / エンドポイントを追加する

@router.post("/")
async def update_admin():
    # Admin action: returns a confirmation message
    # 管理アクション：確認メッセージを返す
    return {"message": "Admin getting schwifty"}
