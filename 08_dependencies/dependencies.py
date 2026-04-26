# F-08: Dependency functions
# Japanese: 依存性関数を定義するファイル

from typing import Annotated
# Japanese: Annotatedパターンで型エイリアスを定義するために使用

from fastapi import Depends
# Japanese: Dependsをインポート（型エイリアス内で使用）


# TODO: Step 1 — define common_parameters(q, skip, limit)
# Japanese: Step1 — common_parameters(q, skip, limit) 依存関数を定義する
# Hint:
#   def common_parameters(
#       q: str | None = None,
#       skip: int = 0,
#       limit: int = 100,
#   ) -> dict:
#       return {"q": q, "skip": skip, "limit": limit}


# TODO: Step 3 — define CommonsDep as Annotated type alias
# Japanese: Step3 — Annotated型エイリアス CommonsDep を定義する
# Hint: CommonsDep = Annotated[dict, Depends(common_parameters)]
