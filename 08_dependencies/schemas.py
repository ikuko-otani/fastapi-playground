# F-08: Pydantic schemas (if needed for response models)
# Japanese: レスポンスモデルなどに使うPydanticスキーマ（必要に応じて）

from pydantic import BaseModel
# Japanese: BaseModelをインポート


# TODO (optional): define Item or User model if you want typed responses
# Japanese: 型付きレスポンスが必要な場合はItemやUserモデルを定義する
# Example:
#   class Item(BaseModel):
#       name: str
#       description: str | None = None
#       price: float
